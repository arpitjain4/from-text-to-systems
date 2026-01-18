import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: Text -> Bits (reuse Post 1 logic)
# -----------------------------

def text_to_bits(text):
    bits = []
    for ch in text:
        ascii_val = ord(ch)
        binary = format(ascii_val, '08b')
        bits.extend([int(b) for b in binary])
    return np.array(bits)


# -----------------------------
# STEP 2: Black Box — Bits to "Signal"
# -----------------------------
# We deliberately do NOT explain how this works yet.
# Think of this as: bits → some physical representation → numbers

def black_box_signal_mapper(bits):
    """
    Simple mapping:
    0 -> -1
    1 -> +1

    This is NOT modulation (yet).
    It's just a numeric placeholder for 'signal values'.
    """
    return np.where(bits == 0, -1.0, 1.0)


# -----------------------------
# STEP 3: Noise Models
# -----------------------------

def add_awgn(signal, mean=0.0, std=0.3):
    noise = np.random.normal(mean, std, size=signal.shape)
    return signal + noise


def add_uniform_noise(signal, low=-0.5, high=0.5):
    noise = np.random.uniform(low, high, size=signal.shape)
    return signal + noise


def add_poisson_noise(signal, lam=1.0):
    """
    Poisson noise is non-negative and discrete.
    We shift signal to be positive before applying it,
    then shift back.
    """
    shifted = signal + 2.0
    noise = np.random.poisson(lam, size=signal.shape)
    return shifted + noise - 2.0


# -----------------------------
# STEP 4: Visualization
# -----------------------------

def plot_histograms(clean, awgn, uniform, poisson):
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.hist(clean, bins=20)
    plt.title("Clean Signal (No Noise)")
    plt.xlabel("Value")
    plt.ylabel("Count")

    plt.subplot(2, 2, 2)
    plt.hist(awgn, bins=20)
    plt.title("AWGN (Gaussian Noise)")
    plt.xlabel("Value")

    plt.subplot(2, 2, 3)
    plt.hist(uniform, bins=20)
    plt.title("Uniform Noise")
    plt.xlabel("Value")

    plt.subplot(2, 2, 4)
    plt.hist(poisson, bins=20)
    plt.title("Poisson Noise")
    plt.xlabel("Value")

    plt.tight_layout()
    plt.show()


# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":
    message = "Hey, I am Arpit"

    bits = text_to_bits(message)
    signal = black_box_signal_mapper(bits)

    awgn_signal = add_awgn(signal)
    uniform_signal = add_uniform_noise(signal)
    poisson_signal = add_poisson_noise(signal)

    plot_histograms(signal, awgn_signal, uniform_signal, poisson_signal)
