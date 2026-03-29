#!/usr/bin/env python3
"""
PIXEL 5 STRING - DEEP KEY ANALYSIS
Treat the string as a potential password/key and analyze all possible interpretations
"""

import base64
import binascii
import math
from collections import Counter

PIXEL5_STRING = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"

print("="*80)
print("PIXEL 5 STRING - COMPREHENSIVE KEY ANALYSIS")
print("="*80)
print(f"\nOriginal string: {PIXEL5_STRING}")
print(f"Length: {len(PIXEL5_STRING)} characters")

# 1. BASIC CHARACTER ANALYSIS
print("\n1. CHARACTER COMPOSITION ANALYSIS")
print("-"*80)

char_counts = Counter(PIXEL5_STRING)
print(f"\nUnique characters: {len(char_counts)}")
print(f"Character frequency:")
for char, count in char_counts.most_common(20):
    print(f"  '{char}': {count} times (ASCII {ord(char)})")

# Check character types
lowercase = sum(1 for c in PIXEL5_STRING if c.islower())
uppercase = sum(1 for c in PIXEL5_STRING if c.isupper())
digits = sum(1 for c in PIXEL5_STRING if c.isdigit())
special = len(PIXEL5_STRING) - lowercase - uppercase - digits

print(f"\nCharacter types:")
print(f"  Lowercase: {lowercase} ({lowercase/len(PIXEL5_STRING)*100:.1f}%)")
print(f"  Uppercase: {uppercase} ({uppercase/len(PIXEL5_STRING)*100:.1f}%)")
print(f"  Digits: {digits} ({digits/len(PIXEL5_STRING)*100:.1f}%)")
print(f"  Special: {special} ({special/len(PIXEL5_STRING)*100:.1f}%)")

# 2. INDEX OF COINCIDENCE
print("\n\n2. INDEX OF COINCIDENCE (Cipher Detection)")
print("-"*80)

def index_of_coincidence(text):
    """Calculate IC - used to detect cipher type"""
    n = len(text)
    if n <= 1:
        return 0
    freq = Counter(text)
    ic = sum(f * (f - 1) for f in freq.values()) / (n * (n - 1))
    return ic

ic = index_of_coincidence(PIXEL5_STRING)
print(f"Index of Coincidence: {ic:.6f}")
print(f"Expected IC for random: ~0.038")
print(f"Expected IC for English: ~0.067")
if ic < 0.045:
    print("  [!] Low IC suggests TRANSPOSITION cipher or polyalphabetic substitution")
elif ic > 0.060:
    print("  [!] High IC suggests simple substitution cipher")
else:
    print("  [!] Medium IC - could be transposition or short text")

# 3. FACTORIZATION OF LENGTH
print("\n\n3. LENGTH FACTORIZATION (Grid Arrangement)")
print("-"*80)

length = len(PIXEL5_STRING)
print(f"String length: {length}")
print(f"Factors:")
for i in range(1, int(math.sqrt(length)) + 1):
    if length % i == 0:
        print(f"  {i} x {length // i}")
        if i != length // i:
            print(f"  {length // i} x {i}")

# Check if 5×23 theory holds
if length == 115:
    print(f"\n[!] 115 = 5 × 23 - matches our key number 5!")

# 4. BASE64 ATTEMPTS
print("\n\n4. BASE64 DECODING ATTEMPTS")
print("-"*80)

# Try direct base64
try:
    decoded = base64.b64decode(PIXEL5_STRING)
    print(f"Direct base64: {decoded}")
except:
    print("Direct base64: FAILED")

# Try with padding
try:
    padded = PIXEL5_STRING + '=' * (4 - len(PIXEL5_STRING) % 4)
    decoded = base64.b64decode(padded)
    print(f"With padding: {decoded}")
except:
    print("With padding: FAILED")

# 5. XOR ANALYSIS
print("\n\n5. XOR ANALYSIS WITH KEY NUMBERS")
print("-"*80)

keys = [5, 24, 55, 60, 120, 25, 52, 115]
for key in keys:
    result = ''.join([chr(ord(c) ^ key) for c in PIXEL5_STRING[:20]])
    readable = sum(1 for c in result if 32 <= ord(c) <= 126)
    print(f"XOR with {key}: {result[:30]}... ({readable}/20 readable)")

# 6. CAESAR/ROT SHIFTS
print("\n\n6. CAESAR CIPHER (ROT) ANALYSIS")
print("-"*80)

def caesar(text, shift):
    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)
    return ''.join(result)

# Try shifts that might reveal German words
print("Trying shifts that might reveal German words...")
for shift in [5, 24, 55 % 26, 60 % 26, 120 % 26, 25, 11]:
    result = caesar(PIXEL5_STRING, shift)
    # Check for common German patterns
    if 'die' in result.lower() or 'der' in result.lower() or 'und' in result.lower():
        print(f"ROT{shift}: {result[:50]}... [!] Contains German words!")
    else:
        print(f"ROT{shift}: {result[:50]}...")

# 7. REVERSE AND MIRROR
print("\n\n7. REVERSE AND MIRROR PATTERNS")
print("-"*80)

print(f"Reversed: {PIXEL5_STRING[::-1]}")
print(f"First 25: {PIXEL5_STRING[:25]}")
print(f"Last 25: {PIXEL5_STRING[-25:]}")

# Check for partial palindrome
half = len(PIXEL5_STRING) // 2
first_half = PIXEL5_STRING[:half]
second_half = PIXEL5_STRING[half:]
matches = sum(1 for a, b in zip(first_half, second_half[::-1]) if a == b)
print(f"Partial symmetry: {matches}/{half} characters match between halves")

# 8. EXTRACT NUMBERS FROM STRING
print("\n\n8. NUMBERS EMBEDDED IN STRING")
print("-"*80)

import re
numbers = re.findall(r'\d+', PIXEL5_STRING)
print(f"Numbers found: {numbers}")
print(f"Sum: {sum(int(n) for n in numbers)}")
print(f"Concatenated: {''.join(numbers)}")

# 9. EVERY NTH CHARACTER
print("\n\n9. EVERY NTH CHARACTER ANALYSIS")
print("-"*80)

for n in [5, 23, 10, 20, 25]:
    every_nth = PIXEL5_STRING[::n]
    print(f"Every {n}th: {every_nth}")
    # Check if readable
    readable = sum(1 for c in every_nth if c.isalnum())
    print(f"  Readable ratio: {readable}/{len(every_nth)}")

# 10. ALPHANUMERIC ONLY
print("\n\n10. ALPHANUMERIC EXTRACTION")
print("-"*80)

alphanumeric = ''.join(c for c in PIXEL5_STRING if c.isalnum())
print(f"Alphanumeric only: {alphanumeric}")
print(f"Length: {len(alphanumeric)}")

# 11. ASCII VALUE ANALYSIS
print("\n\n11. ASCII VALUE PATTERNS")
print("-"*80)

ascii_vals = [ord(c) for c in PIXEL5_STRING]
print(f"ASCII values: {ascii_vals[:30]}...")
print(f"Min: {min(ascii_vals)}, Max: {max(ascii_vals)}")
print(f"Range: {max(ascii_vals) - min(ascii_vals)}")
print(f"Average: {sum(ascii_vals)/len(ascii_vals):.1f}")

# Check for printable ASCII
non_printable = sum(1 for v in ascii_vals if v < 32 or v > 126)
print(f"Non-printable characters: {non_printable}")

# 12. VIGENERE CIPHER ATTEMPTS
print("\n\n12. VIGENERE CIPHER ATTEMPTS")
print("-"*80)

def vigenere_decrypt(text, key):
    result = []
    key_len = len(key)
    for i, c in enumerate(text):
        if c.isalpha():
            shift = ord(key[i % key_len].lower()) - ord('a')
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base - shift) % 26 + base))
        else:
            result.append(c)
    return ''.join(result)

# Try with common keys
keys_to_try = ['five', 'haian', 'fabian', 'admin', 'skat', 'key', 'password']
for key in keys_to_try:
    result = vigenere_decrypt(PIXEL5_STRING[:30], key)
    print(f"Key '{key}': {result}")

# 13. ATBASH CIPHER
print("\n\n13. ATBASH CIPHER (Reverse Alphabet)")
print("-"*80)

def atbash(text):
    result = []
    for c in text:
        if c.isupper():
            result.append(chr(ord('Z') - (ord(c) - ord('A'))))
        elif c.islower():
            result.append(chr(ord('z') - (ord(c) - ord('a'))))
        else:
            result.append(c)
    return ''.join(result)

print(f"Atbash: {atbash(PIXEL5_STRING)}")

# 14. PASSWORD CANDIDATE EXTRACTION
print("\n\n14. PASSWORD CANDIDATES FROM STRING")
print("-"*80)

candidates = []

# Various segmentations
for length in [5, 10, 15, 20, 25]:
    candidates.append(PIXEL5_STRING[:length])
    candidates.append(PIXEL5_STRING[-length:])

# Every other character
candidates.append(PIXEL5_STRING[::2])
candidates.append(PIXEL5_STRING[1::2])

# Middle section
mid = len(PIXEL5_STRING) // 2
candidates.append(PIXEL5_STRING[mid-10:mid+10])

# Alphanumeric only
candidates.append(alphanumeric)
candidates.append(alphanumeric[:20])

# Numbers only
candidates.append(''.join(numbers))

# Print unique candidates
unique_candidates = list(set(candidates))
print("Extracted password candidates:")
for i, cand in enumerate(unique_candidates[:15], 1):
    print(f"  {i}. '{cand}' (length: {len(cand)})")

# 15. ENTROPY CALCULATION
print("\n\n15. ENTROPY ANALYSIS")
print("-"*80)

def calculate_entropy(text):
    """Calculate Shannon entropy"""
    freq = Counter(text)
    length = len(text)
    entropy = -sum((count/length) * math.log2(count/length) for count in freq.values())
    return entropy

entropy = calculate_entropy(PIXEL5_STRING)
print(f"Shannon entropy: {entropy:.4f} bits per character")
print(f"Max possible for this charset: {math.log2(len(set(PIXEL5_STRING))):.4f}")
if entropy > 5.0:
    print("  [!] High entropy - likely encrypted or random")
elif entropy < 3.0:
    print("  [!] Low entropy - likely structured/patterned")
else:
    print("  [!] Medium entropy - mixed content")

# 16. FINAL SYNTHESIS
print("\n\n16. KEY SYNTHESIS")
print("-"*80)

print("\nBest password candidates:")
print(f"  1. Full string (length {len(PIXEL5_STRING)}): {PIXEL5_STRING[:30]}...")
print(f"  2. First 25 chars (age): {PIXEL5_STRING[:25]}")
print(f"  3. Last 25 chars: {PIXEL5_STRING[-25:]}")
print(f"  4. Alphanumeric only: {alphanumeric[:30]}...")
print(f"  5. Numbers: {''.join(numbers)}")
print(f"  6. Every 5th char: {PIXEL5_STRING[::5]}")
print(f"  7. Every 23rd char: {PIXEL5_STRING[::23]}")

# 17. SPECIFIC PATTERN: 25 AND 52
print("\n\n17. '25' AND '52' PATTERN ANALYSIS")
print("-"*80)

if '25' in PIXEL5_STRING:
    idx = PIXEL5_STRING.index('25')
    print(f"'25' found at position {idx}")
    print(f"Context: ...{PIXEL5_STRING[max(0,idx-5):idx+7]}...")

if '52' in PIXEL5_STRING:
    idx = PIXEL5_STRING.index('52')
    print(f"'52' found at position {idx}")
    print(f"Context: ...{PIXEL5_STRING[max(0,idx-5):idx+7]}...")

# 18. GRID ARRANGEMENT (5x23)
print("\n\n18. 5×23 GRID ARRANGEMENT")
print("-"*80)

if len(PIXEL5_STRING) == 115:
    print("Grid read as 5 rows x 23 columns:")
    grid = [PIXEL5_STRING[i:i+23] for i in range(0, 115, 23)]
    for i, row in enumerate(grid):
        print(f"  Row {i+1}: {row}")
    
    print("\nColumn reads (each column 5 characters):")
    for col in range(23):
        column = ''.join([grid[row][col] for row in range(5)])
        print(f"  Col {col+1:2d}: {column}")
        if column.isalpha() and len(column) == 5:
            print(f"    [!] 5-letter word candidate: {column}")

print("\n" + "="*80)
print("PIXEL 5 STRING ANALYSIS COMPLETE")
print("="*80)
