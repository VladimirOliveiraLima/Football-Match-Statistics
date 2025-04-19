import matplotlib.pyplot as plt
import seaborn as sns

def plot_goals_per_team(df):
    team_goals = {}

    for _, row in df.iterrows():
        team_goals[row["Time_Mandante"]] = team_goals.get(row["Time_Mandante"], 0) + row["Gols_Mandante"]
        team_goals[row["Time_Visitante"]] = team_goals.get(row["Time_Visitante"], 0) + row["Gols_Visitante"]

    teams = list(team_goals.keys())
    goals = list(team_goals.values())

    plt.figure(figsize=(12, 6))
    sns.barplot(x=teams, y=goals)
    plt.title("Gols por Time no Campeonato")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
