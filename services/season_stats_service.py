from repositories.season_stats_repository import SeasonStatsRepository

repo = SeasonStatsRepository()

def add_goal(season, player_id):
    stats = repo.get_stats(season, player_id)
    if not stats:
        stats = repo.create_stats(season, player_id)
    stats.goals += 1
    repo.update(stats)

def add_yellow_card(season, player_id):
    stats = repo.get_stats(season, player_id)
    if not stats:
        stats = repo.create_stats(season, player_id)
    stats.yellow_cards += 1
    repo.update(stats)

def add_red_card(season, player_id):
    stats = repo.get_stats(season, player_id)
    if not stats:
        stats = repo.create_stats(season, player_id)
    stats.red_cards += 1
    repo.update(stats)

def get_top_scorers(season):
    return repo.get_top_scorers(season)



