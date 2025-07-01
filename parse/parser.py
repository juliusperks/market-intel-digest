from dataclasses import dataclass
import datetime

@dataclass
class MarketEntry:
    ticker: str
    date: datetime.date
    open: float
    high: float
    low: float
    close: float
    volume: int

def parse_line(line: str) -> MarketEntry:
    parts = line.strip().split(',')
    return MarketEntry(
        ticker=parts[0],
        date=datetime.datetime.strptime(parts[1], "%d %b %Y").date(),
        open=float(parts[2]),
        high=float(parts[3]),
        low=float(parts[4]),
        close=float(parts[5]),
        volume=int(parts[6])
    )

def parse_file(filepath: str):
    with open(filepath, "r") as f:
        return [parse_line(line) for line in f if line.strip()]
