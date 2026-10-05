import gitlab
import requests


def new_client(host: str, token: str) -> gitlab.Gitlab:
    session = requests.Session()
    gl = gitlab.Gitlab(url=host, private_token=token, session=session)
    return gl

