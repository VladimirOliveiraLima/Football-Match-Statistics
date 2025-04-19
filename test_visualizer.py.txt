from src.brasileirao.visualizer import plot_goals_per_team
import pandas as pd

def test_plot(monkeypatch):
    # Simula plt.show() para testes
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    df = pd.DataFrame({
        "Time_Mandante": ["A"],
        "Gols_Mandante": [2],
        "Time_Visitante": ["B"],
        "Gols_Visitante": [1]
    })

    plot_goals_per_team(df)
