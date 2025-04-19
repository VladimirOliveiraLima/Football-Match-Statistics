import pandas as pd
from src.brasileirao.statistics import calculate_statistics

def test_statistics():
    data = pd.DataFrame({
        "Time_Mandante": ["A", "B"],
        "Gols_Mandante": [1, 2],
        "Time_Visitante": ["B", "A"],
        "Gols_Visitante": [0, 1]
    })
    stats = calculate_statistics(data)
    assert "A" in stats and "B" in stats
    assert stats["A"]["vitorias"] == 1
