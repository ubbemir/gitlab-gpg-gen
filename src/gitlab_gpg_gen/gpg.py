import pgpy
from pgpy.constants import PubKeyAlgorithm

def generate_gpg_key(name: str, email: str) -> pgpy.PGPKey:
    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
    uid = pgpy.PGPUID.new(name, email=email)
    key.add_uid(uid)
    return key
