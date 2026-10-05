import gitlab
import requests


def new_client(host: str, token: str) -> gitlab.Gitlab:
    session = requests.Session()
    gl = gitlab.Gitlab(url=host, private_token=token, session=session)
    gl.auth()
    return gl

def delete_ci_var(key: str, target):
    for var in target.variables.list():
            if var.asdict()["key"] == key:
                var.delete()

def overwrite_or_create_ci_secret(target, key: str, value: str):
    delete_ci_var(key, target)

    return target.variables.create({
        'key': key,
        'value': value,
        'masked_and_hidden': True,
        'protected': True,
        'raw': True
    })

def set_gpg_key(user, key: str):
    for k in user.gpgkeys.list():
        k.delete()
     
    user.gpgkeys.create({'key': str(key)})

def get_user_email(user) -> str:
    return user.emails.list()[0].asdict()["email"]
