from datetime import datetime
from zoneinfo import ZoneInfo

import ntplib
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Bienvenido a la API de hora oficial de Chile. Usa /time para ver la hora."
    }


@app.get("/time")
def get_time():
    try:
        client = ntplib.NTPClient()
        response = client.request("cl.pool.ntp.org")
        now = datetime.fromtimestamp(response.tx_time)
        return {
            "time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "source": "hora obtenida desde servidor NTP cl.pool.ntp.org",
        }
    except Exception:
        now = datetime.now(ZoneInfo("America/Santiago"))
        return {
            "time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "source": "hora obtenida desde zona horaria local America/Santiago (fallback)",
        }
