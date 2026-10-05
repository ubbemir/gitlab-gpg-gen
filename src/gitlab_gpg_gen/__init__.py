import base64
import gitlab
import os
import pgpy

from . import gpg
from . import glab

def base64_key(key: pgpy.PGPKey) -> str:
    bytes = str(key).encode("ascii")
    base64_bytes = base64.b64encode(bytes)
    return base64_bytes.decode("ascii")

def main():
    key = gpg.generate_gpg_key("Bot", "botsson@example.com")
    gl = glab.new_client("https://gitlab.com", os.environ["GLAB_TOKEN"])

    project = gl.projects.get(76850953)

    variable = project.variables.create({
        'key': 'GPG_PRIVATE_KEY',
        'value': base64_key(key),
        'masked': True,
        'protected': True,
        'raw': True
    })

if __name__ == "__main__":
    main()
