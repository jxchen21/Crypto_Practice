print("")
input_1 = input("Enter first hex num: ")
print("")
input_2 = input("Enter second hex num: ")
bytes_1 = bytes.fromhex(input_1)
bytes_2 = bytes.fromhex(input_2)
xor_result = bytes([x ^ y for (x, y) in zip(bytes_1, bytes_2)])
print("")
print("Result: " + xor_result.hex())
print("")