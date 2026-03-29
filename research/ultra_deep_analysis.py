#!/usr/bin/env python3
"""
ULTRA-DEEP ANALYSIS - BEYOND STANDARD APPROACHES
Think like a codebreaker, cryptographer, pattern hunter
"""

import math
from PIL import Image
import os

print("="*70)
print("ULTRA-DEEP ANALYSIS - BEYOND THE OBVIOUS")
print("="*70)

# 1. P-adic valuations (exponent of prime p in n)
def p_adic_valuation(n, p):
    """Highest power of p dividing n"""
    val = 0
    while n % p == 0:
        n //= p
        val += 1
    return val

print("\n1. P-ADIC VALUATION ANALYSIS")
print("-"*70)

numbers = {
    'birth_month': 10,
    'birth_day': 30,
    'death_month': 10,
    'death_day': 20,
    'age_years': 24,
    'age_days': 20,
    'skat_24': 24,
    'skat_120': 120,
    'thomas_55': 55,
    'thomas_60': 60,
    'image_width': 700,
    'image_height': 1000,
    'image_bytes': 269508,
}

for name, num in numbers.items():
    v2 = p_adic_valuation(num, 2)
    v3 = p_adic_valuation(num, 3)
    v5 = p_adic_valuation(num, 5)
    print(f"{name:15s}: v2={v2} v3={v3} v5={v5} | num={num}")

# 2. Digital root and iterated digit sum
print("\n\n2. DIGITAL ROOT ANALYSIS")
print("-"*70)

def digital_root(n):
    """Iterated digit sum until single digit"""
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

for name, num in numbers.items():
    dr = digital_root(num)
    digit_sum = sum(int(d) for d in str(num))
    print(f"{name:15s}: digit_sum={digit_sum:3d}, digital_root={dr} | num={num}")

# 3. Look for 666-related patterns in image
print("\n\n3. DEEP IMAGE BYTE ANALYSIS")
print("-"*70)

image_path = "images/haian_mit_text_skaliert_rand.jpeg"
if os.path.exists(image_path):
    with open(image_path, 'rb') as f:
        data = f.read()
    
    # Check every byte
    count_6 = data.count(6)
    count_66 = sum(1 for i in range(len(data)-1) if data[i] == 6 and data[i+1] == 6)
    count_102 = data.count(102)  # 102 = 0x66
    
    print(f"\nOccurrences of byte 6: {count_6}")
    print(f"Occurrences of consecutive 6,6: {count_66}")
    print(f"Occurrences of byte 102 (0x66): {count_102}")
    
    # Check at positions related to our numbers
    print("\nBytes at significant positions:")
    for pos in [5, 24, 55, 60, 120, 666, 1024]:
        if pos < len(data):
            print(f"  Position {pos}: {data[pos]} (0x{data[pos]:02x})")

# 4. XOR chain analysis
print("\n\n4. XOR CHAIN ANALYSIS")
print("-"*70)

nums = [5, 24, 55, 60, 120]
print("\nXOR between consecutive numbers:")
for i in range(len(nums)-1):
    x = nums[i] ^ nums[i+1]
    print(f"  {nums[i]} XOR {nums[i+1]} = {x}")

print("\nXOR of all numbers:")
total_xor = 0
for n in nums:
    total_xor ^= n
print(f"  5 ^ 24 ^ 55 ^ 60 ^ 120 = {total_xor}")

# 5. Hamming weight (number of 1 bits)
print("\n\n5. HAMMING WEIGHT ANALYSIS")
print("-"*70)

print("\nPopulation count (number of 1 bits):")
for name, num in numbers.items():
    hw = bin(num).count('1')
    print(f"  {name}: {num} -> {hw} bits set")

# 6. Gray code representation
print("\n\n6. GRAY CODE ANALYSIS")
print("-"*70)

def to_gray(n):
    """Convert to Gray code"""
    return n ^ (n >> 1)

print("\nGray code representations:")
for name, num in numbers.items():
    gray = to_gray(num)
    print(f"  {name}: {num} -> Gray({num}) = {gray}")

# 7. Look for perfect numbers and amicable pairs
print("\n\n7. PERFECT/ABUNDANT/DEFICIENT ANALYSIS")
print("-"*70)

def classify_number(n):
    """Classify as perfect, abundant, or deficient"""
    div_sum = sum(i for i in range(1, n) if n % i == 0)
    if div_sum == n:
        return "PERFECT"
    elif div_sum > n:
        return f"ABUNDANT (+{div_sum - n})"
    else:
        return f"DEFICIENT (-{n - div_sum})"

print("\nClassification:")
for name, num in numbers.items():
    if num <= 10000:
        cls = classify_number(num)
        print(f"  {name}: {num} is {cls}")

# 8. Collatz conjecture paths
print("\n\n8. COLLATZ PATH ANALYSIS")
print("-"*70)

def collatz_steps(n):
    """Count steps to reach 1 in Collatz sequence"""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        steps += 1
    return steps

print("\nCollatz steps to reach 1:")
for name, num in numbers.items():
    if num <= 1000:  # Limit for computation
        steps = collatz_steps(num)
        print(f"  {name}: {num} -> {steps} steps")

# 9. Continued fraction representations
print("\n\n9. CONTINUED FRACTION ANALYSIS")
print("-"*70)

def continued_fraction_sqrt(n, terms=10):
    """Compute continued fraction of sqrt(n)"""
    if int(math.sqrt(n)) ** 2 == n:
        return [int(math.sqrt(n))]
    
    a0 = int(math.sqrt(n))
    m, d, a = 0, 1, a0
    cf = [a0]
    
    for _ in range(terms):
        m = d * a - m
        d = (n - m * m) // d
        if d == 0:
            break
        a = (a0 + m) // d
        cf.append(a)
    
    return cf

print("\nContinued fractions of square roots:")
for name, num in numbers.items():
    if num > 0:
        cf = continued_fraction_sqrt(num, 5)
        print(f"  sqrt({num}): {cf}")

print("\n" + "="*70)
print("ULTRA-DEEP ANALYSIS COMPLETE")
print("="*70)
