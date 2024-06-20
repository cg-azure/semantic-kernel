from semantic_kernel import Kernel
from services import Service
from service_settings import ServiceSettings
from semantic_kernel.functions import KernelArguments

# Import the WeatherPlugin class
from weather_plugin.weather_plugin import WeatherPlugin

# Instantiate the kernel
kernel = Kernel()

# Create an instance of ServiceSettings
service_settings = ServiceSettings()

# Select the OpenAI service to use for this script
selectedService = Service.OpenAI
print(f"Using service type: {selectedService}")

# Remove all services so that this script can be re-run without restarting the kernel
kernel.remove_all_services()

# Initialize service_id
service_id = None

# Add the OpenAI service to the kernel
if selectedService == Service.OpenAI:
    from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

    service_id = "default"
    ai_model_id = "gpt-3.5-turbo"  # Example model ID; replace with the actual model ID you intend to use
    kernel.add_service(
        OpenAIChatCompletion(
            service_id=service_id,
            ai_model_id=ai_model_id,
            env_file_path=".env",
        ),
    )

# Instantiate and register the WeatherPlugin
weather_plugin_instance = WeatherPlugin(api_token="a61fd6ecc2c6cc7765f67accea1897f7")

# Add the weather plugin to the kernel
weather_plugin_path = "/Users/cg_mac/Documents/GitHub/semantic-kernel/python/samples/cg-semantic-intro/weather_check/"
weather_plugin = kernel.add_plugin(weather_plugin_instance, parent_directory=weather_plugin_path, plugin_name="weather_plugin")

# Asynchronously invoke the weather function and print the result
async def get_weather(location: str, type: str):
    weather_function = weather_plugin["WeatherAtPlace"] if type == "current" else weather_plugin["ForecastAtPlace"]
    weather = await kernel.invoke(
        weather_function,
        KernelArguments(location=location),
    )
    print(weather)

# To run the async functions in a script
import asyncio

# Example to get weather information
asyncio.run(get_weather("chicago", "forecast"))
