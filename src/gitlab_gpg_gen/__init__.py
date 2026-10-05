import pgpy
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm

def generate_gpg_key(name: str, email: str) -> pgpy.PGPKey:
    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
    uid = pgpy.PGPUID.new(name, comment='Honest Abe', email=email)
    key.add_uid(uid, usage={KeyFlags.Sign}, hashes=[HashAlgorithm.SHA512, HashAlgorithm.SHA256],
            ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.Camellia256],
            compression=[CompressionAlgorithm.BZ2, CompressionAlgorithm.Uncompressed])
    return key

def main():
    print("Hello from gitlab-gpg-gen!")
    key = generate_gpg_key("Abraham Lincoln", "abraham.lincoln@whitehouse.gov")
    print("Generated GPG Key:")
    print(key)
    print("public key:")
    print(key.pubkey)

if __name__ == "__main__":
    main()
