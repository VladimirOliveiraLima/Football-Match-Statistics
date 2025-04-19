from src.brasileirao.data_loader import load_csv_data
from src.brasileirao.statistics import calculate_statistics
from src.brasileirao.visualizer import plot_goals_per_team

def main():
    data = load_csv_data("data/sample_matches.csv")
    stats = calculate_statistics(data)
    print("\nResumo Estatístico do Campeonato Brasileiro:")
    for team, team_stats in stats.items():
        print(f"{team}: {team_stats}")
    
    plot_goals_per_team(data)

if __name__ == "__main__":
    main()
