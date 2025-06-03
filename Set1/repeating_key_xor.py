def encrypt(plaintext, key):
    # Note: .encode converts text to bytes
    text_hex = plaintext.encode()
    key_hex = key.encode()
    out = bytes([c ^ key_hex[x % len(key_hex)] for x, c in enumerate(text_hex)])
    return out.hex()

def main():
    print("")
    in_text = input("Enter text to be encrypted: ")
    print(encrypt(in_text,"ICE"))
    print("")


if __name__=="__main__":
    main()