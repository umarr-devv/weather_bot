import aiohttp


class WeatherAPIClient:
    url = 'http://api.openweathermap.org/data/2.5/weather'

    @staticmethod
    async def get_response(url: str, params: dict) -> aiohttp.ClientResponse | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    return await response.json()

    @staticmethod
    async def get_weather_by_city(key: str, city: str,
                                  units: str = 'metric', lang: str = 'ru') -> dict | None:
        return await WeatherAPIClient.get_response(WeatherAPIClient.url, params={
            'appId': key, 'q': city, 'units': units, 'lang': lang
        })
