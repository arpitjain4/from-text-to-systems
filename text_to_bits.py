
# text_to_bits.py
# Base file for communication system simulations


# Why ASCII = American Standard Code for Information Interchange
# 7-bit originally (128 characters)
# Deterministic, Fixed-length (1 byte), Easy to visualize and debug
# Most modern systems use UTF-8, but ASCII is still the backbone
# — UTF-8 is backward compatible with ASCII.
def text_to_ascii_bits(text):
    result = []

    for ch in text:
        # converting a character into its numeric code
        # This is the moment where meaning is lost and representation beginss
        ascii_val = ord(ch)
        # 08b :Memory, files, and communication systems work in bytes,
        #       not random-length binaries.
        # 0: Pad with leading zeros
        # 8: Force 8 bits (1 byte)
        # b: Convert number to binary
        binary_val = format(ascii_val, '08b')
        result.append((ch, ascii_val, binary_val))

    return result


def save_bits_to_file(bitstream, filename="stored_bits.txt"):
    with open(filename, "w") as f:
        for ch, ascii_val, binary_val in bitstream:
            f.write(f"{ch}\t{ascii_val}\t{binary_val}\n")


if __name__ == "__main__":
    text = input("Enter your message: ")

    bitstream = text_to_ascii_bits(text)

    print("\nCharacter | ASCII | Binary")
    print("----------------------------")
    for ch, ascii_val, binary_val in bitstream:
        print(f"{repr(ch):>9} | {ascii_val:>5} | {binary_val}")

    save_bits_to_file(bitstream)

    print("\nMessage converted to bits and saved locally.")
    print(bitstream)
