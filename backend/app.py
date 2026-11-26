from datetime import date
from pathlib import Path
import json

from fastapi import FastAPI

DATA = json.loads(Path(__file__).with_name("data.json").read_text())
app = FastAPI()


@app.get("/status")
def status():
    today = date.today().isoformat()
    matura = date.fromisoformat(DATA["matura_date"])

    phase = next((p for p in DATA["phases"] if p["start"] <= today <= p["end"]), None)
    upcoming = [c for c in DATA["checkpoints"] if not c["done"] and c["date"] >= today]
    next_checkpoint = min(upcoming, key=lambda c: c["date"]) if upcoming else None
    done_count = sum(1 for c in DATA["checkpoints"] if c["done"])

    return {
        "days_to_matura": (matura - date.today()).days,
        "phase": phase,
        "next_checkpoint": next_checkpoint,
        "progress_pct": round(100 * done_count / len(DATA["checkpoints"])),
    }

