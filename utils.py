def format_percent(value, total):
    if total == 0:
        return "0.0%"
    return f"{(value / total * 100):.1f}%"
