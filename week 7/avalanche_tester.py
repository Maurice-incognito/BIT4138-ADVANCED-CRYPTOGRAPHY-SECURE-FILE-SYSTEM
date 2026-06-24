# Student: [Your Name] - BIT4138
import hashlib

def sha256_bits(text):
    h = hashlib.sha256(text.encode()).digest()
    return ''.join(f'{byte:08b}' for byte in h)

def flip_bit(text, bit_position):
    # Convert text to bits, flip one bit, convert back
    byte_pos = bit_position // 8
    bit_pos  = bit_position % 8
    data     = bytearray(text.encode())
    if byte_pos < len(data):
        data[byte_pos] ^= (1 << (7 - bit_pos))
    return data.decode(errors='replace')

def count_diff(bits1, bits2):
    return sum(b1 != b2 for b1, b2 in zip(bits1, bits2))

original = "BIT4138Cryptography"

print("=== Avalanche Effect Tester ===")
print(f"Original input: '{original}'")
print()
print(f"{'Bit Flipped':<15} {'Changed Bits':<15} {'Avalanche %':<15} {'Rating'}")
print("-" * 60)

orig_bits = sha256_bits(original)
results   = []

for bit in range(0, min(40, len(original) * 8), 5):
    modified  = flip_bit(original, bit)
    mod_bits  = sha256_bits(modified)
    diff      = count_diff(orig_bits, mod_bits)
    pct       = (diff / 256) * 100
    rating    = "Excellent" if pct >= 45 else "Good" if pct >= 35 else "Weak"
    results.append(pct)
    print(f"{bit:<15} {diff:<15} {pct:<15.1f} {rating}")

avg = sum(results) / len(results)
print()
print(f"Average avalanche effect: {avg:.1f}%")
print(f"Ideal target            : ~50%")
print()
if avg >= 45:
    print("Result: STRONG avalanche effect — cipher behaves securely!")
else:
    print("Result: WEAK avalanche effect — cipher may be vulnerable!")