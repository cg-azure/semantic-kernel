from pyowm import OWM
from datetime import datetime, timedelta
from semantic_kernel.functions.kernel_function_decorator import kernel_function

class WeatherPlugin:
    def __init__(self, api_token: str) -> None:
        self.mgr = OWM(api_token).weather_manager()

    @kernel_function(
        description="Get current weather information for a given location",
        name="WeatherAtPlace"
    )
    def weather_at_place(self, location: str) -> str:
        observation = self.mgr.weather_at_place(location)
        w = observation.weather
        ret = {
            'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'detailed_status': w.detailed_status,
            'wind': w.wind(),
            'humidity': w.humidity,
            'temperature': w.temperature('celsius'),
            'rain': w.rain,
            'heat_index': w.heat_index,
            'clouds': w.clouds
        }
        return str(ret)

    @kernel_function(
        description="Get weather forecast information for a given location",
        name="ForecastAtPlace"
    )
    def get_weather_forecast(self, location: str) -> str:
        forecast = self.mgr.forecast_at_place(location, '3h')
        target_time = datetime.now() + timedelta(hours=6)
        weather_at_target_time = forecast.get_weather_at(target_time)
        ret = {
            'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'forecast_time': target_time.strftime('%Y-%m-%d %H:%M:%S'),
            'temperature': weather_at_target_time.temperature('celsius'),
            'status': weather_at_target_time.detailed_status,
            'rain': weather_at_target_time.rain,
            'humidity': weather_at_target_time.humidity
        }
        return str(ret)
