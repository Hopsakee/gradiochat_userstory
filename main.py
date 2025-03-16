import gradio as gr
from gradiochat.config import ModelConfig, ChatAppConfig
from gradiochat.gradio_themes import themeWDODelta
from gradiochat.ui import create_chat_app
from dotenv import load_dotenv

load_dotenv()

with open("system.md", "r", encoding="utf-8") as f:
        system_prompt = f.read()

modelconfig = ModelConfig(
    model_name="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    provider="togetherai",
    api_key_env_var="TG_API_KEY"
)

user_story_config = ChatAppConfig(
    app_name="Hulp bij het schrijven van een user story",
    description="Een chat applicatie die je helpt bij het schrijven van een user story.",
    system_prompt=system_prompt,
    model=modelconfig,
    theme=themeWDODelta,
    logo_path="wdod_logo.svg"
)

def main():
    app = create_chat_app(user_story_config)
    app.build_interface().launch(pwa=True, favicon_path="wdod_logo.svg")

if __name__ == "__main__":
    main()