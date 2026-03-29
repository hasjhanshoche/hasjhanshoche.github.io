#!/usr/bin/env python3
"""
AROUND-THE-CORNER THINKING
Unconventional approaches, lateral thinking, hidden dimensions
"""

import math
from PIL import Image
import os

KEY_NUMBERS = [5, 24, 55, 60, 120, 700, 1000, 9121, 269508]

print("="*70)
print("AROUND-THE-CORNER EXPERIMENTAL ANALYSIS")
print("="*70)

# 1. GEOMETRIC INTERPRETATIONS
print("\n1. GEOMETRIC/SPATIAL INTERPRETATIONS")
print("-"*70)

print("\nImage dimensions as geometric shapes:")
print(f"  700 × 1000 could be:")
print(f"    - Aspect ratio: 7:10 (simplified)")
print(f"    - Diagonal: {math.sqrt(700**2 + 1000**2):.2f}")
print(f"    - Area: {700*1000} pixels")
print(f"    - Perimeter: {2*(700+1000)} pixels")

# Golden ratio check
phi = (1 + math.sqrt(5)) / 2
print(f"\nGolden ratio phi = {phi:.6f}")
print(f"  700 x phi = {700 * phi:.2f} (close to 1000? {abs(700*phi - 1000) < 50})")
print(f"  1000 / phi = {1000 / phi:.2f} (close to 700? {abs(1000/phi - 700) < 50})")

# 2. MUSICAL/FREQUENCY INTERPRETATIONS
print("\n\n2. MUSICAL INTERPRETATIONS")
print("-"*70)

print("\nNumbers as frequencies (Hz):")
a4 = 440  # Standard pitch
for num in [24, 55, 60, 120]:
    # Check if it's a musical interval from A4
    ratio = num / a4
    # Semitone ratio is 2^(1/12)
    semitones = 12 * math.log2(ratio) if ratio > 0 else 0
    print(f"  {num} Hz: {semitones:.2f} semitones from A4")

# 3. CHEMISTRY/PHYSICS CONNECTIONS
print("\n\n3. SCIENTIFIC CONSTANTS CHECK")
print("-"*70)

# Atomic numbers
elements = {
    5: "Boron (B)",
    6: "Carbon (C)",
    24: "Chromium (Cr)",
    55: "Cesium (Cs)",
    60: "Neodymium (Nd)",
}

print("\nAtomic number connections:")
for num in KEY_NUMBERS:
    if num in elements:
        print(f"  [!] {num} = {elements[num]}")

# 4. TIME/SPACE COORDINATES
print("\n\n4. TEMPORAL COORDINATE ANALYSIS")
print("-"*70)

print("\nBirth date: 30.10.1986")
print("Death date: 20.10.2011")
print("Isabella message: 24.02.2012")

# Check Julian day numbers
def date_to_julian(year, month, day):
    # Simplified Julian day calculation
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12*a - 3
    return day + (153*m + 2)//5 + 365*y + y//4 - y//100 + y//400 - 32045

birth_jd = date_to_julian(1986, 10, 30)
death_jd = date_to_julian(2011, 10, 20)
isabella_jd = date_to_julian(2012, 2, 24)

print(f"\nJulian Day Numbers:")
print(f"  Birth: {birth_jd}")
print(f"  Death: {death_jd}")
print(f"  Isabella msg: {isabella_jd}")
print(f"  Difference (life): {death_jd - birth_jd} days")
print(f"  Difference (to Isabella): {isabella_jd - death_jd} days")

# 5. CIPHER SQUARE ANALYSIS
print("\n\n5. CIPHER SQUARE/MAGIC SQUARE CHECK")
print("-"*70)

def is_magic_square_partial(nums):
    """Check if numbers can form partial magic square"""
    if len(nums) >= 4:
        # Check if any 4 form magic properties
        for a in nums:
            for b in nums:
                if b != a:
                    for c in nums:
                        if c not in [a, b]:
                            for d in nums:
                                if d not in [a, b, c]:
                                    # 2x2 magic: all rows/cols/diags sum to same
                                    row1 = a + b
                                    row2 = c + d
                                    col1 = a + c
                                    col2 = b + d
                                    diag1 = a + d
                                    diag2 = b + c
                                    if row1 == row2 == col1 == col2 == diag1 == diag2:
                                        return (a, b, c, d, row1)
    return None

result = is_magic_square_partial([24, 55, 60, 120])
if result:
    print(f"[!] Magic square found: {result[0]}, {result[1]}, {result[2]}, {result[3]} = {result[4]}")
else:
    print("  No simple magic square arrangement found")

# 6. ANGLE/DEGREE INTERPRETATIONS
print("\n\n6. ANGLE INTERPRETATIONS")
print("-"*70)

print(f"\nNumbers as degrees:")
print(f"  24 degrees = 24 degrees (normalized)")
print(f"  55 degrees = 55 degrees (normalized)")
print(f"  60 degrees = 60 degrees (normalized)")
print(f"    [!] Significant angle: 60 degrees")
print(f"  120 degrees = 120 degrees (normalized)")
print(f"    [!] Significant angle: 120 degrees")

# 7. BOOK CIPHER POTENTIAL
print("\n\n7. BOOK CIPHER ANALYSIS")
print("-"*70)

print("\nNumbers could be:")
print(f"  24.02.2012 -> Page 24, Line 02, Word 2012 (or combinations)")
print(f"  55-60 -> Pages 55-60")
print(f"  24, 120 -> Pages/paragraphs")

# 8. ASCII ART / VISUAL PATTERNS
print("\n\n8. VISUAL PATTERN ANALYSIS")
print("-"*70)

pixel5 = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"

print("\nVisual pattern in pixel 5 string:")
print("  First 20 chars: ", pixel5[:20])
print("  Last 20 chars:  ", pixel5[-20:])

# Check for mirror patterns
first_half = pixel5[:len(pixel5)//2]
second_half = pixel5[len(pixel5)//2:]
print(f"\n  Length: {len(pixel5)} (middle at {len(pixel5)//2})")
print(f"  First half ends with: ...{first_half[-5:]}")
print(f"  Second half starts with: {second_half[:5]}...")

# Check for symmetry
if first_half == second_half[::-1]:
    print("  [!] String is palindromic!")
else:
    print("  String is NOT palindromic")
    # Check partial symmetry
    matches = sum(1 for a, b in zip(first_half, second_half[::-1]) if a == b)
    print(f"  Partial symmetry: {matches}/{len(first_half)} characters match")

# 9. QUANTUM/PHYSICS NUMBERS
print("\n\n9. PHYSICS CONSTANT PROXIMITY")
print("-"*70)

# Fine structure constant
alpha = 1/137.036
print(f"\nFine structure constant alpha ~ 1/137 ~ {alpha:.6f}")
print(f"  1/24 = {1/24:.6f} (not close)")
print(f"  1/55 = {1/55:.6f} (not close)")

# Speed of light
print(f"\nSpeed of light c ~ 299,792,458 m/s")
print(f"  299792458 / 24 = {299792458 // 24} remainder {299792458 % 24}")
print(f"  299792458 / 120 = {299792458 // 120} remainder {299792458 % 120}")

print("\n" + "="*70)
print("AROUND-THE-CORNER ANALYSIS COMPLETE")
print("="*70)
