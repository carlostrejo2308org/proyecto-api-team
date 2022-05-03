from stats import DeezerUserStats

if __name__ == '__main__':
    user_stats = DeezerUserStats()

    top_tracks = user_stats.get_top_tracks(period="PERIOD_7DAYS", limit=5)
    top_artists = user_stats.get_top_artists(period="PERIOD_7DAYS", limit=5)
    total_time = user_stats.get_total_time_listened(period="PERIOD_7DAYS")

    top_tracks = user_stats.get_top_tracks(period="PERIOD_1MONTH", limit=5)
    top_artists = user_stats.get_top_artists(period="PERIOD_1MONTH", limit=5)
    total_time = user_stats.get_total_time_listened(period="PERIOD_1MONTH")
