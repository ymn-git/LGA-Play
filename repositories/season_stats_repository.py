from entities.season_stats import SeasonStats

class SeasonStatsRepository:
    def __init__(self):
        self.stats = []  # lista de SeasonStats

    def get_stats(self, season_id, player_id):
        for s in self.stats:
            if s.season_id == season_id and s.player_id == player_id:
                return s
        return None

    def create_stats(self, season_id, player_id):
        stats = SeasonStats(season_id, player_id)
        self.stats.append(stats)
        return stats

    def update(self, stats):
        # En memoria no hace nada, porque el objeto ya está modificado
        # Se deja por compatibilidad para cuando migres a BD
        pass

    def get_top_scorers(self, season_id):
        season_list = [
            s for s in self.stats
            if s.season_id == season_id
        ]
        return sorted(season_list, key=lambda s: s.goals, reverse=True)
