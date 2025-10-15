import asyncio
from typing import Optional, Dict, Any
from contextlib import asynccontextmanager
import aiohttp
import config

IP_API = getattr(
    config,
    "IP_API",
    "http://ip-api.com/json/?fields=status,message,city,regionName,country,lat,lon,timezone,query",
)


@asynccontextmanager
async def _maybe_session(session: Optional[aiohttp.ClientSession] = None):
    if session is not None:
        yield session
    else:
        async with aiohttp.ClientSession() as s:
            yield s


async def detect_city_via_ip_async(
    session: Optional[aiohttp.ClientSession] = None,
) -> Optional[Dict[str, Any]]:
    try:
        async with _maybe_session(session) as sess:
            async with sess.get(IP_API, timeout=10) as resp:
                data = await resp.json()
        if data.get("status") != "success":
            return None
        city = data.get("city")
        country = data.get("country")
        region = data.get("regionName")
        lat = data.get("lat")
        lon = data.get("lon")
        tz = data.get("timezone")
        label = ", ".join([p for p in [city, country] if p])
        return {
            "city": city,
            "region": region,
            "country": country,
            "latitude": lat,
            "longitude": lon,
            "timezone": tz,
            "ip": data.get("query"),
            "label": label,
        }
    except Exception:
        return None


def detect_city_via_ip() -> Optional[Dict[str, Any]]:
    return asyncio.run(detect_city_via_ip_async())
