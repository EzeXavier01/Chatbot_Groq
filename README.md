# Chatbot_Groq
## Chatbot with FastAPI, Gradio, and SwarmaURI SDK

This project implements a chatbot using FastAPI as the backend, Gradio for the frontend interface, and the SwarmaURI SDK to interact with different models for natural language processing tasks.

## Project Structure

- `main.py`: Contains the core logic, including the setup for the Gradio interface and functions to handle conversation using SwarmaURI's `GroqModel`.
- `config.py`: Stores configuration settings like the API key, retrieved from environment variables.
- `run.py`: Runs the FastAPI app and mounts the Gradio interface on the FastAPI route.

## Key Components

### `main.py`
- **Gradio Interface**: A chat-based interface where users can select a model from a dropdown and provide a system context to converse with.
- **Model Selection**: Users can dynamically select an available model from SwarmaURI's list of allowed models.
- **Conversation Handling**: Uses SwarmaURI's `SimpleConversationAgent` to interact with the chosen model and process the conversation history.

### `config.py`
- **API Key**: Stores the API key required to interact with SwarmaURI models, fetched from environment variables (`GROQ_API_KEY`).

### `run.py`
- **FastAPI App**: Defines the FastAPI app and mounts the Gradio interface on the `/gradio` route.
- **Mounting Gradio**: The `gr.mount_gradio_app` method is used to integrate the Gradio interface into FastAPI.



This project is licensed under the MIT License.

Here’s a breakdown of each import and their typical uses:

### `from swarmauri.standard.llms.concrete.GroqModel import GroqModel`
- **GroqModel**: This class provides an interface to a specific machine learning model. It is likely associated with Groq's machine learning technology or API. It's used to interact with Groq's models for tasks such as generating predictions, embeddings, or other model-based functionalities.

### `from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent`
- **SimpleConversationAgent**: This class represents a simple conversational agent or chatbot. It manages and processes interactions in a conversation, handling user input, managing dialogue states, and generating appropriate responses. It’s used to create agents capable of engaging in structured conversations.

### `from swarmauri.standard.messages.concrete.SystemMessage import SystemMessage`
- **SystemMessage**: This module manages system messages within a conversational system. These messages convey information about the system’s state or configuration, such as initialization messages, status updates, or non-user messages providing operational feedback in the conversation.

### `from swarmauri.standard.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation`
- **MaxSystemContextConversation**: This class deals with conversations that incorporate the maximum amount of system context. It manages conversations requiring extensive contextual information about the system’s state or the conversation’s history. This is used for more sophisticated conversation systems that need a high level of contextual awareness for coherent and relevant interactions.

## Summary of Uses:
- **GroqModel**: Interfaces with machine learning models, likely for prediction tasks.
- **SimpleConversationAgent**: Manages and processes conversational interactions.
- **SystemMessage**: Handles system-specific messages and notifications.
- **MaxSystemContextConversation**: Manages conversations with high system context awareness.

Each of these components contributes to the construction and management of advanced conversational systems, particularly those with machine learning integration, conversation management, and system context handling requirements.
