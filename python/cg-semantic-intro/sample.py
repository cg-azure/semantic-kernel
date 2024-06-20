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
    ai_model_id = "gpt-3.5-turbo"  # Example model ID; replace with the actual model ID you intend to use
    kernel.add_service(
        OpenAIChatCompletion(
            service_id=service_id,
            ai_model_id=ai_model_id,
            env_file_path=".env",
        ),
    )


# Add the joke plugin to the kernel
joke_plugin_path = "/Users/cg_mac/Documents/GitHub/semantic-kernel/prompt_template_samples/"
joke_plugin = kernel.add_plugin(parent_directory=joke_plugin_path, plugin_name="FunPlugin")
joke_function = joke_plugin["Joke"]


# Add the chat plugin to the kernel
chat_plugin_path = "/Users/cg_mac/Documents/GitHub/semantic-kernel/prompt_template_samples/"
chat_plugin = kernel.add_plugin(parent_directory=chat_plugin_path, plugin_name="ChatPlugin")
chat_function = chat_plugin["Chat"]

# # Asynchronously invoke the joke function and print the result
# async def get_joke():
#     joke = await kernel.invoke(
#         joke_function,
#         KernelArguments(input="ice cream during summer", style="super silly"),
#     )
#     print(joke)


# # Asynchronously invoke the excuses function and print the result
# async def get_excuses():
#     joke = await kernel.invoke(
#         joke_function,
#         KernelArguments(input="I am late for school", style="humble"),
#     )
#     print(joke)


# Asynchronously invoke the chat function and print the result
async def get_chat():
    chat = await kernel.invoke(
        chat_function,
        KernelArguments(user="Chandan", input="help me find a recipe that I can cook in flat top iron skillet grill", bot="my_ai"),
    )
    print(chat)

# To run the async functions in a script
import asyncio

# # Example to get a joke
# asyncio.run(get_joke())

# # Example to get a joke
# asyncio.run(get_excuses())

# Example to get a joke
asyncio.run(get_chat())