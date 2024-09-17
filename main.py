#!/usr/bin/env python
# coding: utf-8


# # Install SwarmaURI SDK
# pip install swarmauri[full]==0.4.1

import os
import gradio as gr
from swarmauri.standard.llms.concrete.GroqModel import GroqModel
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent
from swarmauri.standard.messages.concrete.SystemMessage import SystemMessage
from swarmauri.standard.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation
from config import API_KEY

# Intialize the Groqmodel with the API key to access allowed models
llm = GroqModel(api_key=API_KEY)

# Get the available models from the llm instance
allowed_models = llm.allowed_models

# Initialize a MaxSystemContextConversation instance
conversation = MaxSystemContextConversation()


# Define a function to dynamically change model based on the dropdown input
def load_model(selected_model):
    return GroqModel(api_key = API_KEY, name = selected_model)

# Define the function to interact with the agent
def converse(input_text, history, system_context, model_name):
    print(f"system_context: {system_context}")
    print(f"Selected model: {model_name}")

    # Intialize the model dynamically based on user selection
    llm = load_model(model_name)

    # Initialize the agebt with the new model
    agent = SimpleConversationAgent(llm = llm, conversation = conversation)
    agent.conversation.system_context = SystemMessage(content=system_context)

    # Ensure input_text is a string
    input_text = str(input_text)
    print(conversation.history)

    # Execute the inpir command with the agent
    result = agent.exec(input_text)
    print(result, type(result))

    # Return the result as a string
    return str(result)


# Initial code

# Setting up the Gradio Interface with a dropdown for model selection
# demo = gr.ChatInterface(
#     fn=converse,
#     additional_inputs=[
#         gr.Textbox(label = "System Context"),
#         gr.Dropdown(label = "Model Name", choices = allowed_models, value = allowed_models[0]) # Drop down box

#     ],
#     title = "A system context conversation",
#     description = "Interact with the agent using a selected model and system context."
# )



# Setting up the Gradio Interface with a dropdown for model selection(A reusable code block)
def gradio_interface(converse_function, allowed_models_list):
    """
    Sets up the Gradio interface for interacting with the agent.
    
    Parameters:
    - converse_function: The function to process user input and generate responses.
    - allowed_models_list: List of model names for dropdown selection.
    
    Returns:
    - Gradio Interface object.
    """
    
    # Define the Gradio components
    system_context_input = gr.Textbox(label="System Context", placeholder="Enter system context here...")
    model_selection_dropdown = gr.Dropdown(
        label="Model Name",
        choices=allowed_models_list,
        value=allowed_models_list[0]
    )
    
    # Create the Gradio interface
    interface = gr.ChatInterface(
        fn=converse_function,
        additional_inputs=[system_context_input, model_selection_dropdown],
        title="A System Context Conversation",
        description="Interact with the agent using a selected model and system context."
    )
    
    return interface

# Usage example
demo = gradio_interface(converse, allowed_models)


if __name__ == "__main__":
    demo.launch()





