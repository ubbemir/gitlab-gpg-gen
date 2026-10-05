import os

from . import gpg
from . import glab



def main():
    key = gpg.generate_gpg_key("Bot", "botsson@example.com")
    gl = glab.new_client("https://gitlab.com", os.environ["GLAB_TOKEN"])

    project = gl.projects.get(76850953)

    variable = project.variables.create({
        'key': 'GPG_PRIVATE_KEY',
        'value': gpg.base64_key(key),
        'masked': True,
        'protected': True,
        'raw': True
    })

if __name__ == "__main__":
    main()
