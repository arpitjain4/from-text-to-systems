import random
from text_to_bits import text_to_ascii_bits


def extract_bits(bitstream):
    """
    Converts (char, ascii, binary) tuples
    into a flat list of bits.
    """
    bits = []
    for _, _, binary_val in bitstream:
        bits.extend([int(b) for b in binary_val])
    return bits

"""
A Binary Symmetric Channel (BSC) is the simplest model of a faulty channel:
Input: bits (0 or 1), Output: bits (0 or 1)
Each bit has: Probability p of flipping, Probability 1 − p of staying the same
“Symmetric” means: 0 → 1 and 1 → 0 are equally likely
This is not a real physical channel, It’s a conceptual tool.
Errors are probabilistic, not deterministic.
Even with the same input, Output can differ every run

Other channel models to explore:
- Binary Erasure Channel (bit lost, replaced by '?')
- Burst Error Channel (errors occur in clusters)
- AWGN Channel (noise added to signal, not bits)
We start with BSC because it isolates one idea:
random, independent bit corruption.
"""
def binary_symmetric_channel(bits, flip_probability):
    """
    Each bit flips independently with probability p.
    """
    noisy_bits = []

    for bit in bits:
        if random.random() < flip_probability:
            noisy_bits.append(1 - bit)
        else:
            noisy_bits.append(bit)

    return noisy_bits

"""
bit error occurs when: transmitted_bit != received_bit
Bit Error Rate (BER) = errors / total_bits
Out of all transmitted bits, what fraction got corrupted?”
8 errors in 1000 bits => BER = 0.008
"""
def bit_error_rate(tx_bits, rx_bits):
    errors = sum(t != r for t, r in zip(tx_bits, rx_bits))
    return errors, errors / len(tx_bits)


if __name__ == "__main__":

    message = input("Enter your message: ")
    flip_probability = float(input("Enter the flip probability: "))
    """
    | Flip Probability (p) | What happens            |
    | -------------------- | ----------------------- |
    | 0.0                  | Perfect channel         |
    | 0.001                | Rare errors             |
    | 0.01                 | Noticeable corruption   |
    | 0.05                 | Message starts breaking |
    | 0.1                  | Many bits wrong         |
    | 0.5                  | Random noise            |
    """
    
    # Source encoding (Post 1)
    bitstream = text_to_ascii_bits(message)
    tx_bits = extract_bits(bitstream)

    # Channel (Post 2)
    rx_bits = binary_symmetric_channel(tx_bits, flip_probability)

    # Metrics
    errors, ber = bit_error_rate(tx_bits, rx_bits)
    error_positions = [i for i, (t, r) in enumerate(zip(tx_bits, rx_bits)) if t != r]

    # A single flipped bit can change the entire character
    # because characters are groups of bits, not independent unit

    print("Original message :", message)
    print("Total bits       :", len(tx_bits))
    print("Flip probability :", flip_probability)
    print("Bit errors       :", errors)
    print("Bit Error Rate   :", ber)

    print("\nFirst 64 transmitted bits:")
    print(tx_bits[:64])

    print("\nFirst 64 received bits:")
    print(rx_bits[:64])

    print("\nError positions (first 20):", error_positions[:20])