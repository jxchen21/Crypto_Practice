import base64
print("")
input = input("Enter hex: ")
byte_data = bytes.fromhex(input)
out_64 = base64.b64encode(byte_data).decode('utf-8')
print("Out: " + out_64)
print("")