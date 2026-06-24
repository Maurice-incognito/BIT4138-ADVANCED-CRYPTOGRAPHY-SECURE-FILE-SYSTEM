# Student: [Your Name] - BIT4138

def lfsr(seed, taps, length):
    state  = seed[:]
    output = []
    for _ in range(length):
        output.append(state[0])
        new_bit = 0
        for t in taps:
            new_bit ^= state[t]
        state = [new_bit] + state[:-1]
    return output

seed     = [1, 0, 1, 1, 0, 1, 0, 1]
taps     = [0, 2, 3, 7]
sequence = lfsr(seed, taps, 100)

print("=== LFSR Output: 100-bit Pseudorandom Sequence ===")
print()

# Print bits in rows of 20 so it fits nicely on screen
print("Bit sequence (20 bits per row):")
for i in range(0, 100, 20):
    row = sequence[i:i+20]
    print(f"  Bits {i+1:>3}-{i+20:<3}: {' '.join(str(b) for b in row)}")

print()
print(f"Total bits generated : 100")
print(f"Total 0s             : {sequence.count(0)}")
print(f"Total 1s             : {sequence.count(1)}")
print(f"Ratio (1s/total)     : {sequence.count(1)/100:.2f}  (ideal = 0.50)")