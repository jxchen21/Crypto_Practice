
def score_english(text):
    # Thanks Chat for the frequency table
    frequency = {
        'a': .065, 'b': .012, 'c': .022, 'd': .032, 'e': .103, 'f': .02,
        'g': .016, 'h': .047, 'i': .057, 'j': .001, 'k': .005, 'l': .033,
        'm': .02, 'n': .057, 'o': .062, 'p': .015, 'q': .001, 'r': .049,
        's': .053, 't': .075, 'u': .023, 'v': .008, 'w': .017, 'x': .001,
        'y': .014, 'z': .001, ' ': .13
    }
    return sum(frequency.get(chr(byte).lower(), 0) for byte in text)

def break_single_byte_xor(in_hex):
    in_bytes = bytes.fromhex(in_hex)
    high = 0
    best_result = {}
    for i in range(128):
        # Note for future; You can straight up xor with a decimal number, you don't have to convert or anything
        out = bytes([x ^ i for x in in_bytes])
        score = score_english(out)
        if (score_english(out) > high):
            best_result = {
                "key": chr(i),
                "plaintext": out.decode(),
                "score": score
            }
            high = score
    return best_result


def main():
    print("")
    in_hex = input("Enter hex string: ")

    best_result = break_single_byte_xor(in_hex)

    print("")
    print("Most likely plaintext: " + best_result['plaintext'])
    print("Key used: " + best_result['key'])
    print("")

if __name__=="__main__":
    main()