# matura-tracker

Mały serwer pokazujący postęp przygotowań do matury (matematyka + fizyka) jako JSON, do podpięcia pod widżet na telefonie.

## Uruchomienie

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

`GET /status` zwraca:

```json
{
  "days_to_matura": 522,
  "phase": {"label": "...", "math": "...", "physics": "..."},
  "next_checkpoint": {"date": "...", "label": "..."},
  "progress_pct": 0
}
```

## Dostęp z telefonu

Zainstaluj [Tailscale](https://tailscale.com) na tym komputerze i na telefonie — serwer będzie dostępny pod adresem Tailscale, bez przekierowań portów.

## Widżet (Android, KWGT)

W KWGT dodaj moduł "Web" wskazujący na `http://<tailscale-ip>:8000/status`, wyciągnij pola `phase.label`, `days_to_matura`, `next_checkpoint.label`, `progress_pct`.

## Odhaczanie checkpointów

Na razie ręcznie w `data.json` (`"done": true`). Endpoint do odhaczania przez widżet — do zrobienia, jeśli się okaże potrzebny.
