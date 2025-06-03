from single_byte_xor import score_english, break_single_byte_xor

def get_strings(filepath):
    infile = open(filepath, "r")
    return infile.readlines();

def main():
    filepath = "chal4.txt"
    strings_to_try = get_strings(filepath)
    print(strings_to_try)

if __name__=="__main__":
    main()