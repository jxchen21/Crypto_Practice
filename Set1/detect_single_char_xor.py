from single_byte_xor import score_english, break_single_byte_xor

def get_strings(filepath):
    infile = open(filepath, "r")
    return infile.readlines();

def get_highscore(strings):
    high = 0
    best = {}
    for i in strings:
        crack_string = break_single_byte_xor(i.strip())
        if(crack_string['score'] > high):
            best = crack_string
            best["ciphertext"] = i.strip();
            high = crack_string['score']
    return best

def main():
    filepath = "C:/Users/jxche/Documents/Crypto_Practice/Set1/chal4.txt"
    strings_to_try = get_strings(filepath)
    best_fit = get_highscore(strings_to_try)
    print("Located encrypted string: ")
    print(best_fit)

if __name__=="__main__":
    main()