from typing import Optional

from aioowm.const.const import WEATHER_CODES


async def response_handler(response: Optional[dict]) -> dict:
    if response["cod"] != 200:
        return {"error": True, "code": response["cod"]}
    return {
        "error": False,
        "code": response["cod"],
        "default": response,
        "city": {
            "id": response["id"],
            "name": response["name"],
            "country": response["sys"]["country"],
            "timezone": response["timezone"],
            "sunrise": response["sys"]["sunrise"],
            "sunset": response["sys"]["sunset"],
            "coordinates": {
                "longitude": response["coord"]["lon"],
                "latitude": response["coord"]["lat"]
            }
        },
        "weather": {
            "id": response["weather"][0]["id"],
            "main": response["weather"][0]["main"],
            "description": WEATHER_CODES[response["weather"][0]["id"]],
            "clouds": response["clouds"]["all"],
            "rain": response["rain"].get("1h") if "rain" in response else None,
            "snow": response["snow"].get("1h") if "snow" in response else None,
            "humidity": response["main"].get("humidity"),
            "pressure": {
                "sea_level": response["main"].get("sea_level"),
                "ground_level": response["main"].get("grnd_leve,"),
                "value": response["main"].get("pressure")
            },
            "wind": {
                "speed": response["wind"].get("speed"),
                "direction": response["wind"].get("deg"),
                "gust": response["wind"].get("gust")
            },
            "temperature": {
                "now": response["main"].get("temp"),
                "minimal": response["main"].get("temp_min"),
                "maximal": response["main"].get("temp_max"),
                "feels_like": response["main"].get("feels_like")
            }
        }
    }
