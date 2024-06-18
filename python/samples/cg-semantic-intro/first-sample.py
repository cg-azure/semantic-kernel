from semantic_kernel import Kernel
from services import Service
from service_settings import ServiceSettings
from semantic_kernel.functions import KernelArguments

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
    ai_model_id = "text-davinci-003"  # Example model ID; replace with the actual model ID you intend to use
    kernel.add_service(
        OpenAIChatCompletion(
            service_id=service_id,
            ai_model_id=ai_model_id,
            env_file_path=".env",
        ),
    )

# Add a plugin to the kernel
plugin = kernel.add_plugin(parent_directory="/Users/cg_mac/Documents/GitHub/semantic-kernel/prompt_template_samples/", plugin_name="FunPlugin")

# Access the "Joke" function from the plugin
joke_function = plugin["Joke"]

# Asynchronously invoke the joke function and print the result
async def get_joke():
    joke = await kernel.invoke(
        joke_function,
        KernelArguments(input="time travel to dinosaur age", style="super silly"),
    )
    print(joke)

# To run the async function in a script
import asyncio
asyncio.run(get_joke())
