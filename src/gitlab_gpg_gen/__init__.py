import os

from . import gpg
from . import glab

CI_CD_KEY = "GPG_PRIVATE_KEY"
GITLAB_URL = os.environ.get("GLAB_URL", "https://gitlab.com")

def main():
    key = gpg.generate_gpg_key("Bot", "botsson@example.com")
    gl = glab.new_client(GITLAB_URL, os.environ["GLAB_TOKEN"])

    project = gl.projects.get(76850953)

    glab.overwrite_or_create_ci_secret(project, CI_CD_KEY, gpg.base64_key(key))

    gl = glab.new_client(GITLAB_URL, os.environ["GLAB_BOT_TOKEN"])
    bot_user = gl.user

    glab.set_gpg_key(bot_user, str(key.pubkey))

    for k in bot_user.gpgkeys.list():
        print(k)

if __name__ == "__main__":
    main()
