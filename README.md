# gitlab-gpg-gen

Generate a GPG key for a GitLab bot and store the private key as a masked/protected CI/CD variable on a project.

## What it does
- creates a GPG key
- uploads the private key to the target project as a CI/CD Variable
- replaces any existing key with the same name
- adds the matching public key to the bot user on GitLab

## Required environment variables
```bash
export GLAB_URL="https://gitlab.com"   # optional
export GLAB_TOKEN="<personal-token>"
export GLAB_BOT_TOKEN="<bot-user-token>"
export GLAB_PROJECT_ID="123"
```

## Run
```bash
uv run gitlab-gpg-gen
```
