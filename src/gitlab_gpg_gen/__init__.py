from . import gpg

def main():
    key = gpg.generate_gpg_key("Abraham Lincoln", "abraham.lincoln@whitehouse.gov")
    print(key)
    print(key.pubkey)

if __name__ == "__main__":
    main()
