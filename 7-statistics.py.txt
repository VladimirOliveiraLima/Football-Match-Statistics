def calculate_statistics(df):
    stats = {}
    for index, row in df.iterrows():
        home = row["Time_Mandante"]
        away = row["Time_Visitante"]
        home_goals = row["Gols_Mandante"]
        away_goals = row["Gols_Visitante"]

        for team, goals, opp_goals in [(home, home_goals, away_goals), (away, away_goals, home_goals)]:
            if team not in stats:
                stats[team] = {"jogos": 0, "vitorias": 0, "empates": 0, "derrotas": 0, "gols_pro": 0, "gols_contra": 0}

            stats[team]["jogos"] += 1
            stats[team]["gols_pro"] += goals
            stats[team]["gols_contra"] += opp_goals

            if goals > opp_goals:
                stats[team]["vitorias"] += 1
            elif goals == opp_goals:
                stats[team]["empates"] += 1
            else:
                stats[team]["derrotas"] += 1
    return stats
