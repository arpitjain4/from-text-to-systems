# ASCII cannot represent emojis, Hindi, Chinese, etc.
# Unicode is not an encoding. A universal numbering system for every character in the world
# Properties:
# Variable-length (1 to 4 bytes)
# Backward compatible with ASCII
# Dominates: WhatsApp, Web, Linux, Android,iOS
# 'A'  → 1 byte → 01000001
# '🙂' → 4 bytes → 11110000 10011111 10011001 10000010
# UTF-16

def text_to_utf8_bits(text):
    utf8_bytes = text.encode('utf-8')
    bitstream = []

    for byte in utf8_bytes:
        bitstream.append(format(byte, '08b'))

    return utf8_bytes, bitstream


text = "Hey 🙂"
bytes_data, bits = text_to_utf8_bits(text)

print("Bytes:", list(bytes_data))
print("Bits:")
for b in bits:
    print(b)