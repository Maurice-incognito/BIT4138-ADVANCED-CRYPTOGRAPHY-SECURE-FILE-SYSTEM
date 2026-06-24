# Student: [Your Name] - BIT4138
import time, random

def lfsr(seed, taps, length):
    state, output = seed[:], []
    for _ in range(length):
        output.append(state[0])
        new_bit = sum(state[t] for t in taps) % 2
        state = [new_bit] + state[:-1]
    return output

def rc4_keystream(key, length):
    key_bytes = [ord(c) for c in key]
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key_bytes[i % len(key_bytes)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    out = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(S[(S[i] + S[j]) % 256])
    return out

N = 10000

start = time.time()
lfsr([1,0,1,1,0,1,0,1], [0,2,3,7], N)
lfsr_time = (time.time() - start) * 1000

start = time.time()
rc4_keystream("SECRETKEY", N)
rc4_time = (time.time() - start) * 1000

print("=== Performance Comparison (10,000 bits) ===")
print(f"LFSR Time : {lfsr_time:.4f} ms")
print(f"RC4  Time : {rc4_time:.4f} ms")
print()
if lfsr_time < rc4_time:
    print("LFSR is faster for raw bit generation.")
else:
    print("RC4 is faster — better suited for encryption tasks.")