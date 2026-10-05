import os
from dataclasses import dataclass


@dataclass
class Config:
    gitlab_url: str
    personal_token: str
    bot_token: str
    project_id: int


class ConfigException(Exception):
    pass


def get_config() -> Config:
    try:
        return Config(
            gitlab_url=os.environ.get("GLAB_URL", "https://gitlab.com"),
            personal_token=os.environ["GLAB_TOKEN"],
            bot_token=os.environ["GLAB_BOT_TOKEN"],
            project_id=os.environ["GLAB_PROJECT_ID"],
        )
    except KeyError as e:
        raise ConfigException(f"Failed to get app config. Missing env var: {e}")
