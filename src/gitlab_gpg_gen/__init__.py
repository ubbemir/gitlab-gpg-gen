import os

from . import gpg
from . import glab

CI_CD_KEY = "GPG_PRIVATE_KEY"

def main():
    key = gpg.generate_gpg_key("Bot", "botsson@example.com")
    gl = glab.new_client("https://gitlab.com", os.environ["GLAB_TOKEN"])

    project = gl.projects.get(76850953)

    for var in project.variables.list():
        if var.asdict()["key"] == CI_CD_KEY:
            var.delete()

    variable = project.variables.create({
        'key': CI_CD_KEY,
        'value': gpg.base64_key(key),
        'masked': True,
        'protected': True,
        'raw': True
    })

    gl = glab.new_client("https://gitlab.com", os.environ["GLAB_BOT_TOKEN"])
    gl.auth()

    for k in gl.user.gpgkeys.list():
        k.delete()

    gl.user.gpgkeys.create({'key': str(key.pubkey)})

    for k in gl.user.gpgkeys.list():
        print(k)

if __name__ == "__main__":
    main()
