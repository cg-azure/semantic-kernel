import asyncio
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


# Add the intent plugin to the kernel
intent_plugin_path = "/Users/cg_mac/Documents/GitHub/semantic-kernel/prompt_template_samples/"
intent_plugin = kernel.add_plugin(parent_directory=intent_plugin_path, plugin_name="IntentDetectionPlugin")
intent_function = intent_plugin["AssistantIntent"]


# Asynchronously invoke the intent function and print the result
async def get_intent(input_text):

    
    chat = await kernel.invoke(
        intent_function,
        KernelArguments(input=input_text),
    )
    return chat

# # To run the async functions in a script
# import asyncio

# # Example to get a joke
# asyncio.run(get_intent())

# Main function to accept user question as input and process it
async def process_user_input(input_text):
    if not input_text:
        return "No input text provided."

    response = await get_intent(input_text)
    print(response)

# # # Example usage
# input_text = "what is the weather today at chicago"
# response = asyncio.run(process_user_input(input_text))
