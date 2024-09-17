from fastapi import FastAPI
import gradio as gr
from main import gradio_interface, allowed_models, converse

# Create the FastAPI app
app = FastAPI()

# Create the Gradio interface by calling the gradio_interface function
gradio_app = gradio_interface(converse, allowed_models)

# Mount the Gradio app to FastAPI
app = gr.mount_gradio_app(app, gradio_app, path="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)
