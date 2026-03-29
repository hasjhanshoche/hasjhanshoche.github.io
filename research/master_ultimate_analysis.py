#!/usr/bin/env python3
"""
MASTER DEEP RESEARCH - ULTIMATE ANALYSIS
Combines all approaches: mathematical, cryptographic, steganographic, linguistic
"""

import math
from PIL import Image
import os
import requests

# All key numbers
KEY_NUMBERS = {
    'birth_year': 1986, 'birth_month': 10, 'birth_day': 30,
    'death_year': 2011, 'death_month': 10, 'death_day': 20,
    'age_years': 24, 'age_months': 11, 'age_days': 20,
    'days_lived': 9121,
    'skat_24': 24, 'skat_120': 120,
    'thomas_55': 55, 'thomas_60': 60,
    'key_number': 5,
    'image_width': 700, 'image_height': 1000,
    'image_bytes': 269508,
}

print("="*80)
print("MASTER ULTIMATE ANALYSIS - HAIAN.DE PUZZLE")
print("="*80)

# 1. ADVANCED NUMBER THEORY
print("\n1. ADVANCED NUMBER THEORY ANALYSIS")
print("-"*80)

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1: factors.append(n)
    return factors

def digit_sum(n):
    return sum(int(d) for d in str(n))

# Check all numbers for hidden patterns
print("\nDeep factorization with exponent analysis:")
for name, num in KEY_NUMBERS.items():
    factors = prime_factors(num)
    if len(factors) == 1 and factors[0] == num:
        print(f"  {name:15s}: {num:8d} = PRIME")
    else:
        # Count exponents
        from collections import Counter
        fac_counts = Counter(factors)
        fac_str = ' x '.join([f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(fac_counts.items())])
        print(f"  {name:15s}: {num:8d} = {fac_str}")

# 2. PYTHAGOREAN ANALYSIS
print("\n\n2. PYTHAGOREAN TRIPLES ANALYSIS")
print("-"*80)

numbers = list(KEY_NUMBERS.values())
print("\nSearching for Pythagorean triples...")
for i, a in enumerate(numbers):
    for j, b in enumerate(numbers):
        if i < j:
            c_squared = a*a + b*b
            c = int(math.sqrt(c_squared))
            if c*c == c_squared:
                print(f"  [!] {a}^2 + {b}^2 = {c}^2  ->  {a**2} + {b**2} = {c_squared}")

# Check for near-misses
print("\nNear-miss Pythagorean triples (within 5):")
for i, a in enumerate(numbers):
    for j, b in enumerate(numbers):
        if i < j and a < 1000 and b < 1000:
            c_squared = a*a + b*b
            c = int(math.sqrt(c_squared))
            diff = abs(c*c - c_squared)
            if diff <= 5 and diff > 0:
                print(f"  {a}^2 + {b}^2 ~ {c}^2 (diff: {diff})")

# 3. GOLDEN RATIO ANALYSIS
print("\n\n3. GOLDEN RATIO (PHI) ANALYSIS")
print("-"*80)

phi = (1 + math.sqrt(5)) / 2
print(f"\nphi = {phi:.10f}")
print(f"\nChecking which numbers relate to phi:")
for name, num in KEY_NUMBERS.items():
    if num > 0:
        ratio_to_phi = num / phi
        phi_to_ratio = phi / num if num != 0 else 0
        print(f"  {name}: {num}")
        print(f"  {num}/phi = {ratio_to_phi:.4f}")
        print(f"    phi/{num} = {phi_to_ratio:.6f}")
        # Check if close to integer
        nearest_int = round(ratio_to_phi)
        if abs(ratio_to_phi - nearest_int) < 0.1:
            print(f"    [!] Close to integer: {nearest_int}")

# 4. EGYPTIAN FRACTIONS
print("\n\n4. EGYPTIAN FRACTION ANALYSIS")
print("-"*80)

def egyptian_fraction(n, d, max_terms=10):
    """Convert n/d to Egyptian fraction"""
    if n == 0: return []
    fractions = []
    while n != 0 and len(fractions) < max_terms:
        x = math.ceil(d / n)
        fractions.append(x)
        n = n*x - d
        d = d*x
    return fractions

print("\nKey ratios as Egyptian fractions:")
ratios = [
    (24, 120, "24/120"),
    (55, 60, "55/60"),
    (5, 24, "5/24"),
    (55, 120, "55/120"),
]

for num, den, name in ratios:
    ef = egyptian_fraction(num, den)
    if ef:
        ef_str = " + ".join([f"1/{x}" for x in ef])
        print(f"  {name} = {num/den:.4f} = {ef_str}")

# 5. SACRED GEOMETRY
print("\n\n5. SACRED GEOMETRY ANALYSIS")
print("-"*80)

print("\nImage dimensions as sacred geometry:")
w, h = 700, 1000
print(f"  Width: {w}, Height: {h}")
print(f"  Aspect ratio: {w/h:.4f} = {w}/{h}")
print(f"  Simplified: {w//100}:{h//100} = 7:10")

# Check for vesica piscis
print(f"\nVesica Piscis check (sqrt(3) ratio):")
print(f"  {h * math.sqrt(3)/2:.2f} vs {w}")

# Check for root rectangles
print(f"\nRoot rectangle check:")
for root in [2, 3, 5]:
    expected = h * math.sqrt(root)
    print(f"    sqrt({root}) x {h} = {expected:.2f} vs {w}")

# 6. RUNE/GEMATRIA ANALYSIS
print("\n\n6. ALPHANUMERIC GEMATRIA ANALYSIS")
print("-"*80)

names = ["Fabian", "Haian", "Schuessler", "Thomas", "Ihno", "Isabella", "Svenja"]
print("\nGematria values (A=1, B=2, ..., Z=26):")

def gematria(s):
    return sum(ord(c.upper()) - ord('A') + 1 for c in s if c.isalpha())

def simple_gematria(s):
    return sum(int(c) for c in s if c.isdigit())

for name in names:
    g = gematria(name)
    print(f"  {name:15s}: {g}")
    # Check if matches any key numbers
    for kn, kv in KEY_NUMBERS.items():
        if g == kv:
            print(f"    [!] Matches {kn}!")

# 7. ADVANCED XOR ANALYSIS
print("\n\n7. ADVANCED XOR CRYPTOGRAPHY")
print("-"*80)

key_nums = [5, 24, 55, 60, 120]
print("\nXOR chain analysis:")
for i, a in enumerate(key_nums):
    for j, b in enumerate(key_nums):
        if i < j:
            x = a ^ b
            ascii_char = chr(x) if 32 <= x <= 126 else '?'
            print(f"  {a:3d} XOR {b:3d} = {x:3d} (0x{x:02x}) = '{ascii_char}'")

# XOR with image dimensions
print("\nXOR with image dimensions:")
for num in key_nums:
    x_w = num ^ 700
    x_h = num ^ 1000
    print(f"  {num} XOR 700 = {x_w} (0x{x_w:x}), XOR 1000 = {x_h} (0x{x_h:x})")

# 8. JULIAN DAY CALCULATIONS
print("\n\n8. ASTRONOMICAL DATE ANALYSIS")
print("-"*80)

def gregorian_to_julian(year, month, day):
    if month <= 2:
        year -= 1
        month += 12
    A = int(year / 100)
    B = 2 - A + int(A / 4)
    JD = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + B - 1524.5
    return JD

print("\nJulian Day Numbers:")
dates = [
    ("Birth", 1986, 10, 30),
    ("Death", 2011, 10, 20),
    ("Isabella msg", 2012, 2, 24),
]

julian_days = {}
for name, y, m, d in dates:
    jd = gregorian_to_julian(y, m, d)
    julian_days[name] = jd
    print(f"  {name:15s}: JD {jd:.1f}")

# Calculate differences
print("\nJulian Day differences:")
life_span = julian_days["Death"] - julian_days["Birth"]
print(f"  Life span: {life_span:.0f} days")
to_isabella = julian_days["Isabella msg"] - julian_days["Death"]
print(f"  To Isabella: {to_isabella:.0f} days")

# 9. CHECKSUM ANALYSIS
print("\n\n9. CHECKSUM & HASH ANALYSIS")
print("-"*80)

# Checksums of key numbers
def luhn_checksum(n):
    """Luhn algorithm checksum"""
    digits = [int(d) for d in str(n)]
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2*d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10

print("\nLuhn checksums:")
for name, num in KEY_NUMBERS.items():
    if num < 1000000:
        cs = luhn_checksum(num)
        print(f"  {name}: {num} -> Luhn checksum: {cs}")

# 10. NUMBER BASE CONVERSIONS
print("\n\n10. EXOTIC BASE CONVERSIONS")
print("-"*80)

def to_base(n, base):
    if n == 0: return "0"
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return ''.join(str(d) if d < 10 else chr(ord('A') + d - 10) for d in reversed(digits))

print("\nKey numbers in different bases:")
targets = [5, 24, 55, 60, 120, 700, 1000]
bases = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 16]

for num in targets:
    print(f"\n  {num}:")
    for base in bases:
        converted = to_base(num, base)
        print(f"    Base {base:2d}: {converted}")
        # Check if palindrome
        if converted == converted[::-1]:
            print(f"      [!] PALINDROME in base {base}!")

# 11. COMPLEX NUMBER ANALYSIS
print("\n\n11. COMPLEX NUMBER PATTERNS")
print("-"*80)

print("\nPolar representations:")
for name, num in KEY_NUMBERS.items():
    if num > 0:
        # Treat as magnitude with angle = number
        angle_rad = num * math.pi / 180
        real = num * math.cos(angle_rad)
        imag = num * math.sin(angle_rad)
        magnitude = abs(complex(real, imag))
        print(f"  {num} at {num} degrees = {real:.2f} + {imag:.2f}i")

# 12. FINAL SYNTHESIS
print("\n\n12. SYNTHESIS - ALL CONNECTIONS")
print("-"*80)

print("\nNumber 5 appears in:")
print("  - 120/24 = 5 (Skat)")
print("  - 60-55 = 5 (Thomas)")
print("  - sigma(24) = 60 (divisor sum)")
print("  - 5 = F_5 (Fibonacci)")
print("  - Image 1000 = 10³ (10-5=5)")
print("  - 55 = 5 × 11")
print("  - 120 = 5! (factorial)")

print("\n" + "="*80)
print("MASTER ANALYSIS COMPLETE")
print("="*80)
