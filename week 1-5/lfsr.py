# Student: [Your Name] - BIT4138

def lfsr(seed, taps, length):
    """
    Linear Feedback Shift Register (LFSR)
    seed  = starting bits e.g. [1, 0, 1, 1]
    taps  = positions used to calculate the next bit
    length = how many bits to generate
    """
    state  = seed[:]   # copy the seed so we don't modify the original
    output = []

    for _ in range(length):
        # Record current first bit as output
        output.append(state[0])

        # Calculate new bit by XORing the tap positions
        new_bit = 0
        for t in taps:
            new_bit ^= state[t]

        # Shift the register: drop the last bit, add new bit at the front
        state = [new_bit] + state[:-1]

    return output

# --- Run the LFSR ---
seed   = [1, 0, 1, 1, 0, 1, 0, 1]   # 8-bit starting seed
taps   = [0, 2, 3, 7]               # feedback tap positions
length = 20                          # generate 20 bits

sequence = lfsr(seed, taps, length)

print("=== LFSR Pseudorandom Generator ===")
print(f"Seed         : {seed}")
print(f"Tap positions: {taps}")
print(f"Bits generated ({length}): {sequence}")
print(f"Number of 0s : {sequence.count(0)}")
print(f"Number of 1s : {sequence.count(1)}")