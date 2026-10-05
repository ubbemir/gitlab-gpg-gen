import os

from dataclasses import dataclass

@dataclass
class Config:
    gitlab_url: str
    personal_token: str
    bot_token: str
    project_id: int


def get_config() -> Config:
    return Config(
        gitlab_url=os.environ.get("GLAB_URL", "https://gitlab.com"),
        personal_token=os.environ["GLAB_TOKEN"],
        bot_token=os.environ["GLAB_BOT_TOKEN"],
        project_id = os.environ["GLAB_PROJECT_ID"],
    )