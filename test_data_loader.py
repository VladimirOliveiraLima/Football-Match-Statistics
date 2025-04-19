from src.brasileirao.data_loader import load_csv_data

def test_load_csv_data():
    df = load_csv_data("data/sample_matches.csv")
    assert not df.empty
