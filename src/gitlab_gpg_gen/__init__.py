import os

from . import gpg
from . import glab

CI_CD_KEY = "GPG_PRIVATE_KEY"
GITLAB_URL = os.environ.get("GLAB_URL", "https://gitlab.com")

def main():
    gl = glab.new_client(GITLAB_URL, os.environ["GLAB_TOKEN"])
    bot_client = glab.new_client(GITLAB_URL, os.environ["GLAB_BOT_TOKEN"])
    bot_user = bot_client.user


    (bot_name, bot_email) = (glab.get_user_name(bot_user), glab.get_user_email(bot_user))
    print(f"Got Bot '{bot_name}' email: {bot_email}")
    key = gpg.generate_gpg_key(bot_name, bot_email)

    project = gl.projects.get(76850953)

    glab.overwrite_or_create_ci_secret(project, CI_CD_KEY, gpg.base64_key(key))
    glab.set_gpg_key(bot_user, str(key.pubkey))


    print("Bot GPG Keys:")
    for k in bot_user.gpgkeys.list():
        print(k.asdict())

if __name__ == "__main__":
    main()
