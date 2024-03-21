import os

Numbers = [
    47, 82, 8, 13, 74, 91, 65, 104, 55, 81, 20, 19, 49, 92, 50, 66, 21, 55, 25, 10,
    18, 38, 67, 75, 75, 82, 33, 90, 87, 31, 33, 37, 61, 27, 26, 53, 43, 47, 103, 25,
    49, 71, 26, 60, 103, 22, 25, 98, 104, 59, 26, 48, 85, 104, 69, 103, 60, 8, 100,
    21, 61, 67, 47, 88, 77, 28, 76, 66, 95, 19, 38, 50, 89, 30, 29, 101, 79, 7, 6,
    97, 30, 38, 41, 11, 31, 19, 42, 38, 105, 8, 35, 6, 36, 36, 91, 97, 66, 91, 86, 43
]

def encrypt_data(data, length):
    assert length == 24
    
    for i in range(length):
        data[i] ^= Numbers[i % len(Numbers)] ^ (0x0000000000000A72 + 0x0000000000000739 + 0x0000000000000D39 - 0x00000000000019AB) % 256

def calculate_file_size(file):
    return os.path.getsize(file.name)

def main(argc, argv):
    output = "/home/salimabd/Desktop/SparkCTF/Write_ups/Reverse_Engeneering/TopSecret/challenge/output" 
    if not os.path.isfile(output):
        print("File not found!")
        return -(0x0000000000000002 + 0x0000000000000201 + 0x0000000000000801 - 0x0000000000000A03)
    
    output_file_path = os.path.join("output", os.path.basename(output))
    with open(output, "rb") as file:
        data = bytearray(file.read())
        encrypt_data(data, len(data))
        
        with open(output, "wb") as output_file:
            output_file.write(data)
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(len(sys.argv), sys.argv))

