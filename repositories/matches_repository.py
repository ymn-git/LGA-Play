from sqlalchemy import func, or_
from sqlalchemy.orm import Session
from entities.match import Match
from entities.goal import Goal
from entities.card import Card
from entities.playoff import Playoff

class MatchesRepository:

    def __init__(self, db: Session):
        self.db = db

    def _load_extras(self, match):

        goals = (
            self.db.query(Goal)
            .filter(Goal.id_match == match.id_match)
            .all()
        )

        cards = (
            self.db.query(Card)
            .filter(Card.id_match == match.id_match)
            .all()
        )

        match.scorers = [
            {
                "team_id": goal.id_team,
                "player_id": goal.id_player,
                "own_goal": goal.own_goal
            }
            for goal in goals
        ]

        match.yellow_cards = [
            card.id_player
            for card in cards
            if card.type == "yellow"
        ]

        match.red_cards = [
            card.id_player
            for card in cards
            if card.type == "red"
        ]

        return match

    def get_match_by_id(self, match_id):

        match = (
            self.db.query(Match)
            .filter(Match.id_match == match_id)
            .first()
        )

        if match is None:
            raise ValueError("Match not found")

        return self._load_extras(match)

    def get_matches_by_matchday(self, matchday, season):

        matches = (
            self.db.query(Match)
            .filter(
                Match.matchday == matchday,
                Match.season == season
            )
            .order_by(Match.id_match)
            .all()
        )

        return [
            self._load_extras(match)
            for match in matches
        ]

    def get_played_matches_by_season(self, season, include_playoffs=True):
        q = self.db.query(Match).filter(
            Match.season == season,
            Match.jugado.is_(True)
        )

        if not include_playoffs:
            q = q.filter(Match.id_match.notin_(self._playoff_ids()))
        return [self._load_extras(m) for m in q.all()]

    def get_played_matches_by_team(
        self,
        team_id,
        season,
        limit=None
    ):

        query = (
            self.db.query(Match)
            .filter(
                Match.season == season,
                Match.jugado.is_(True),
                or_(
                    Match.teamA_id == team_id,
                    Match.teamB_id == team_id
                )
            )
            .order_by(Match.matchday.desc())
        )

        if limit:
            query = query.limit(limit)

        matches = query.all()

        return [
            self._load_extras(match)
            for match in matches
        ]

    def update_match(self, match: Match):

        db_match = (
            self.db.query(Match)
            .filter(Match.id_match == match.id_match)
            .first()
        )
        if db_match is None:
            raise ValueError("Match not found")

        db_match.goalsA = match.goalsA
        db_match.goalsB = match.goalsB
        db_match.jugado = match.jugado

        self.db.query(Goal).filter(
            Goal.id_match == match.id_match
        ).delete()

        for goal in match.scorers:
            self.db.add(
                Goal(
                    id_match=match.id_match,
                    id_team=goal["team_id"],
                    id_player=goal["player_id"],
                    own_goal=goal["own_goal"]
                )
            )

        self.db.query(Card).filter(
            Card.id_match == match.id_match
        ).delete()

        for player_id in match.yellow_cards:
            self.db.add(
                Card(
                    id_match=match.id_match,
                    id_player=player_id,
                    type="yellow"
                )
            )

        for player_id in match.red_cards:
            self.db.add(
                Card(
                    id_match=match.id_match,
                    id_player=player_id,
                    type="red"
                )
            )

        self.db.commit()

        self.db.refresh(db_match)

        return self.get_match_by_id(
            match.id_match
        )

    def mark_match_as_played(self, match_id):

        match = self.get_match_by_id(match_id)

        match.jugado = True

        self.db.commit()
        self.db.refresh(match)

        return match

    def get_next_matchday(self, season):

        row = (
            self.db.query(
                func.min(Match.matchday)
            )
            .filter(
                Match.season == season,
                Match.jugado.is_(False),
                Match.id_match.notin_(self._playoff_ids())
            )
            .scalar()
        )

        return row

    def add(self, team_a_id, team_b_id, matchday, season, full_date):
        match = Match(teamA_id=team_a_id, teamB_id=team_b_id, matchday=matchday,
                      season=season, full_date=full_date,
                      goalsA=0, goalsB=0, jugado=False)
        self.db.add(match)
        self.db.flush()
        return match

    def _playoff_ids(self):
        return self.db.query(Playoff.match_id)