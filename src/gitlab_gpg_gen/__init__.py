import os

from . import gpg
from . import glab
from . import constants
from . import config


def main():
    cfg = config.get_config()

    project = glab.new_client(cfg.gitlab_url, cfg.personal_token).projects.get(
        cfg.project_id
    )
    bot_user = glab.new_client(cfg.gitlab_url, cfg.bot_token).user

    (bot_name, bot_email) = (
        glab.get_user_name(bot_user),
        glab.get_user_email(bot_user),
    )
    print(f"Got Bot '{bot_name}' email: {bot_email}")
    key = gpg.generate_gpg_key(bot_name, bot_email)

    print(
        f"Setting CI/CD Variable for GPG Private key on project '{glab.get_project_name(project)}' ..."
    )
    glab.overwrite_or_create_ci_secret(
        project, constants.CI_CD_KEY, gpg.base64_key(key)
    )

    print("Setting bot GPG Public key ...")
    glab.set_gpg_key(bot_user, str(key.pubkey))

    print("Bot GPG Keys:")
    for k in bot_user.gpgkeys.list():
        print(k.asdict())


if __name__ == "__main__":
    main()
