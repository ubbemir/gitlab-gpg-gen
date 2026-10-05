import base64

import pgpy
from pgpy.constants import PubKeyAlgorithm


def generate_gpg_key(name: str, email: str) -> pgpy.PGPKey:
    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
    uid = pgpy.PGPUID.new(name, email=email)
    key.add_uid(uid)
    return key


def base64_key(key: pgpy.PGPKey) -> str:
    bytes = str(key).encode("ascii")
    base64_bytes = base64.b64encode(bytes)
    return base64_bytes.decode("ascii")
