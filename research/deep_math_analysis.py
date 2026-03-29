#!/usr/bin/env python3
"""
DEEP MATHEMATICAL ANALYSIS - AGENTS.md Phase 3, 6, 8
Following the protocol: cross-correlate every finding across all phases
"""

import math
from collections import Counter
from itertools import combinations

# Our key findings
NUMBERS = {
    'age_days': 9121,
    'age_years': 24,
    'age_months': 11,
    'age_days_partial': 20,
    'almost_25': 25,
    'skat_grand': 24,
    'skat_ouvert': 120,
    'key_number': 5,
    'thomas_55': 55,
    'thomas_60': 60,
    'difference_5': 5,
    'image_width': 700,
    'image_height': 1000,
    'image_size': 269508,
    'message_count': 27,
    'birth_day': 30,
    'birth_month': 10,
    'birth_year': 1986,
    'death_day': 20,
    'death_month': 10,
    'death_year': 2011,
    'isabella_day': 24,
    'isabella_month': 2,
    'isabella_year': 2012,
}

# Pixel 5 string analysis
PIXEL5_STRING = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"

def prime_factorization(n):
    """Return prime factorization of n"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_prime(n):
    """Check if n is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def deep_number_analysis():
    """Phase 3: Deep Number Analysis per AGENTS.md"""
    print("="*70)
    print("PHASE 3: DEEP MATHEMATICAL ANALYSIS")
    print("="*70)
    
    print("\n1. PRIME FACTORIZATIONS")
    print("-"*70)
    
    for name, value in NUMBERS.items():
        if value > 1:
            factors = prime_factorization(value)
            factor_str = ' × '.join(map(str, factors)) if len(factors) > 1 else str(factors[0]) + " (prime)"
            print(f"{name:20s}: {value:6d} = {factor_str}")
    
    print("\n2. MATHEMATICAL RELATIONSHIPS")
    print("-"*70)
    
    # Check all ratios
    print("\nAll ratios between key numbers:")
    key_nums = {k: v for k, v in NUMBERS.items() if k in ['age_days', 'skat_grand', 'skat_ouvert', 'thomas_55', 'thomas_60', 'key_number', 'age_years']}
    
    for (n1, v1), (n2, v2) in combinations(key_nums.items(), 2):
        if v2 != 0:
            ratio = v1 / v2
            if ratio == int(ratio) and ratio > 0:
                print(f"  {n1} / {n2} = {int(ratio)}")
    
    # Check differences
    print("\nAll differences:")
    for (n1, v1), (n2, v2) in combinations(key_nums.items(), 2):
        diff = abs(v1 - v2)
        if diff > 0 and diff < 1000:
            print(f"  |{n1} - {n2}| = {diff}")
    
    print("\n3. BASE CONVERSIONS")
    print("-"*70)
    
    critical_nums = [9121, 24, 120, 5, 55, 60, 25]
    for n in critical_nums:
        print(f"\n{n}:")
        print(f"  Binary:     {bin(n)[2:]}")
        print(f"  Octal:      {oct(n)[2:]}")
        print(f"  Hex:        {hex(n)[2:].upper()}")
        print(f"  Base36:     {to_base36(n)}")
        if 32 <= n <= 126:
            print(f"  ASCII:      '{chr(n)}'")
    
    print("\n4. COORDINATE TRANSFORMATIONS")
    print("-"*70)
    
    # Check if numbers form valid coordinates
    print("\nPotential coordinate pairs:")
    coords = [
        ('age_years', 'skat_grand'),      # 24, 24
        ('key_number', 'age_years'),       # 5, 24
        ('thomas_55', 'thomas_60'),        # 55, 60
        ('almost_25', 'skat_grand'),       # 25, 24
        ('birth_month', 'death_month'),    # 10, 10
    ]
    
    for n1, n2 in coords:
        v1, v2 = NUMBERS[n1], NUMBERS[n2]
        print(f"  ({n1}, {n2}) = ({v1}, {v2}) -> ASCII: ", end="")
        if 32 <= v1 <= 126 and 32 <= v2 <= 126:
            print(f"'{chr(v1)}{chr(v2)}'")
        else:
            print("(not printable)")
    
    print("\n5. ASCII SUM ANALYSIS")
    print("-"*70)
    
    # Sum of ASCII values of "Haian"
    haian_sum = sum(ord(c) for c in "Haian")
    fabian_sum = sum(ord(c) for c in "Fabian")
    print(f"\nASCII sum of 'Haian':  {haian_sum}")
    print(f"ASCII sum of 'Fabian': {fabian_sum}")
    print(f"Factorization of {haian_sum}: {prime_factorization(haian_sum)}")
    print(f"Factorization of {fabian_sum}: {prime_factorization(fabian_sum)}")

def to_base36(n):
    """Convert number to base36"""
    if n == 0:
        return '0'
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    while n > 0:
        n, r = divmod(n, 36)
        result = digits[r] + result
    return result

def xor_analysis():
    """XOR analysis between key numbers"""
    print("\n6. XOR ANALYSIS")
    print("-"*70)
    
    key_vals = [9121, 24, 120, 5, 55, 60, 25, 269508]
    names = ['days', 'skat24', 'skat120', 'key5', 'thomas55', 'thomas60', 'almost25', 'filesize']
    
    print("\nXOR results:")
    for i, (n1, name1) in enumerate(zip(key_vals, names)):
        for n2, name2 in zip(key_vals[i+1:], names[i+1:]):
            result = n1 ^ n2
            print(f"  {name1} XOR {name2} = {result}")
            if 32 <= result <= 126:
                print(f"    -> ASCII: '{chr(result)}'")
            if result in NUMBERS.values():
                print(f"    -> MATCHES a known number!")

def analyze_pixel5_string():
    """Phase 6: Deep cipher analysis of pixel 5 string"""
    print("\n" + "="*70)
    print("PHASE 6: CIPHER ANALYSIS - PIXEL 5 STRING")
    print("="*70)
    
    print(f"\nOriginal string ({len(PIXEL5_STRING)} chars):")
    print(PIXEL5_STRING)
    
    # Character frequency
    freq = Counter(PIXEL5_STRING)
    print("\n1. CHARACTER FREQUENCY ANALYSIS")
    print("-"*70)
    for char, count in freq.most_common(15):
        print(f"  '{char}': {count} ({100*count/len(PIXEL5_STRING):.1f}%)")
    
    # Check for Index of Coincidence (IC)
    print("\n2. INDEX OF COINCIDENCE (IC)")
    print("-"*70)
    ic = calculate_ic(PIXEL5_STRING)
    print(f"  IC = {ic:.4f}")
    print(f"  English plaintext IC ~ 0.065")
    print(f"  Random text IC ~ 0.038")
    if ic > 0.06:
        print(f"  -> Pattern suggests SUBSTITUTION cipher")
    elif ic < 0.05:
        print(f"  -> Pattern suggests TRANSPOSITION or polyalphabetic")
    
    # Try Vigenère with key "5" or "25"
    print("\n3. VIGENERE DECRYPTION ATTEMPTS")
    print("-"*70)
    
    for key in ['5', '25', '24', '120', '5', 'haian', 'fabian']:
        decrypted = vigenere_decrypt(PIXEL5_STRING, key)
        readable = sum(1 for c in decrypted if c.isalnum() or c.isspace())
        ratio = readable / len(decrypted) if decrypted else 0
        print(f"\n  Key '{key}':")
        print(f"    Result: {decrypted[:60]}")
        print(f"    Readable ratio: {ratio:.2%}")
        if ratio > 0.8:
            print(f"    *** HIGH READABILITY ***")
    
    # Try XOR with key bytes
    print("\n4. XOR DECRYPTION ATTEMPTS")
    print("-"*70)
    
    for key_val in [5, 25, 24, 120, 55, 60]:
        xored = ''.join(chr(ord(c) ^ key_val) for c in PIXEL5_STRING[:50])
        readable = sum(1 for c in xored if 32 <= ord(c) <= 126)
        print(f"\n  XOR with {key_val}:")
        print(f"    Result: {xored[:50]}")
        print(f"    Printable: {readable}/50")
    
    # Atbash cipher
    print("\n5. ATBASH CIPHER")
    print("-"*70)
    atbash_result = atbash(PIXEL5_STRING)
    print(f"  Result: {atbash_result[:80]}")

def calculate_ic(text):
    """Calculate Index of Coincidence"""
    text = ''.join(c for c in text if c.isalpha())
    if not text:
        return 0
    
    n = len(text)
    freq = Counter(text.upper())
    
    ic = sum(f * (f - 1) for f in freq.values()) / (n * (n - 1)) if n > 1 else 0
    return ic

def vigenere_decrypt(ciphertext, key):
    """Decrypt Vigenère cipher"""
    result = []
    key = key.upper()
    key_len = len(key)
    
    for i, c in enumerate(ciphertext):
        if c.isalpha():
            shift = ord(key[i % key_len]) - ord('A')
            if c.isupper():
                result.append(chr((ord(c) - ord('A') - shift) % 26 + ord('A')))
            else:
                result.append(chr((ord(c) - ord('a') - shift) % 26 + ord('a')))
        else:
            result.append(c)
    
    return ''.join(result)

def atbash(text):
    """Apply Atbash cipher"""
    result = []
    for c in text:
        if c.isupper():
            result.append(chr(ord('Z') - (ord(c) - ord('A'))))
        elif c.islower():
            result.append(chr(ord('z') - (ord(c) - ord('a'))))
        else:
            result.append(c)
    return ''.join(result)

def deep_linguistic_analysis():
    """Phase 8: Deep linguistic patterns"""
    print("\n" + "="*70)
    print("PHASE 8: DEEP LINGUISTIC ANALYSIS")
    print("="*70)
    
    # Check pixel 5 string for word patterns
    print("\n1. SUBSTRING ANALYSIS")
    print("-"*70)
    
    # Look for common English words
    test_words = ['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 
                  'had', 'her', 'was', 'one', 'our', 'out', 'key', 'flag', 'pass',
                  'word', 'haian', 'fabian', 'five', 'four', 'nine', 'love', 'hope']
    
    lower_string = PIXEL5_STRING.lower()
    found_words = []
    for word in test_words:
        if word in lower_string:
            found_words.append(word)
    
    if found_words:
        print(f"\n  Found words: {found_words}")
    else:
        print("\n  No common English words found in pixel 5 string")
    
    # Check for 2-letter and 3-letter combinations
    print("\n2. N-GRAM ANALYSIS")
    print("-"*70)
    
    # Bigrams
    bigrams = [PIXEL5_STRING[i:i+2] for i in range(len(PIXEL5_STRING)-1)]
    bigram_freq = Counter(bigrams)
    print("\n  Most common 2-char sequences:")
    for bg, count in bigram_freq.most_common(10):
        print(f"    '{bg}': {count}")
    
    # Check if string is readable when reversed
    print("\n3. REVERSAL ANALYSIS")
    print("-"*70)
    reversed_str = PIXEL5_STRING[::-1]
    print(f"\n  Reversed: {reversed_str[:80]}")
    
    # Check for anagrams
    print("\n4. ANAGRAM CHECK")
    print("-"*70)
    
    # Check if any section is an anagram of "haian" or "fabian"
    for name in ['haian', 'fabian']:
        sorted_name = ''.join(sorted(name))
        for i in range(len(PIXEL5_STRING) - len(name) + 1):
            substring = PIXEL5_STRING[i:i+len(name)].lower()
            if ''.join(sorted(substring)) == sorted_name:
                print(f"  Found anagram of '{name}': '{substring}' at position {i}")

def cross_correlation():
    """Phase 10: Cross-correlation matrix per AGENTS.md"""
    print("\n" + "="*70)
    print("PHASE 10: CROSS-CORRELATION MATRIX")
    print("="*70)
    
    print("\nFinding Interconnections:")
    print("-"*70)
    
    findings = [
        ("F-001", "Number 5 derived from 120/24", ["F-002", "F-003"]),
        ("F-002", "Number 5 from 60-55", ["F-001", "F-004"]),
        ("F-003", "Pixel value 5 string", ["F-001", "F-006"]),
        ("F-004", "Thomas message (55-60)", ["F-002", "F-007"]),
        ("F-005", "Isabella date 24", ["F-006", "F-008"]),
        ("F-006", "Skat 24/120", ["F-003", "F-005", "F-001"]),
        ("F-007", "Admin endpoint 401", ["F-004"]),
        ("F-008", "Age 24 years", ["F-005", "F-006"]),
    ]
    
    print("\n| ID  | Finding                    | Connects To      | Confidence |")
    print("|-----|----------------------------|------------------|------------|")
    for fid, desc, connects in findings:
        conf = "HIGH" if len(connects) >= 2 else "MEDIUM"
        print(f"| {fid} | {desc:26s} | {', '.join(connects):16s} | {conf:10s} |")
    
    print("\n\nCRITICAL PATH HYPOTHESIS:")
    print("-"*70)
    print("""
    The evidence suggests a chain:
    
    1. Thomas's message "55 - 60 jahren" -> difference = 5
    2. Ihno's Skat message 24/120 -> 120/24 = 5
    3. These converge on the NUMBER 5 as the KEY
    4. Pixel value 5 in the image contains encoded data
    5. The /admin endpoint requires authentication
    
    CONCLUSION: The password for /admin is encoded in the pixel 5 string.
               The string itself or its decoded form is the credential.
    """)

def advanced_math_patterns():
    """Advanced mathematical patterns per AGENTS.md 3.4-3.7"""
    print("\n" + "="*70)
    print("ADVANCED MATHEMATICAL PATTERNS")
    print("="*70)
    
    print("\n1. MIRROR & FLIP OPERATIONS")
    print("-"*70)
    
    critical = [24, 120, 5, 55, 60, 25, 9121]
    for n in critical:
        # Reverse digits
        reversed_num = int(str(n)[::-1])
        print(f"\n  {n}:")
        print(f"    Reversed: {reversed_num}")
        if is_prime(reversed_num):
            print(f"    -> Reversed is PRIME!")
        if 32 <= reversed_num <= 126:
            print(f"    -> ASCII: '{chr(reversed_num)}'")
        
        # Upside-down (7-segment style)
        upside_map = {'0': '0', '1': '1', '2': '2', '5': '5', '6': '9', '8': '8', '9': '6'}
        upside = ''.join(upside_map.get(c, c) for c in str(n))
        print(f"    Upside-down: {upside}")
    
    print("\n2. Pythagorean Triples Check")
    print("-"*70)
    
    # Check if any numbers form Pythagorean triples
    for a in [5, 24, 55, 60, 25]:
        for b in [5, 24, 55, 60, 25]:
            c_sq = a*a + b*b
            c = int(math.sqrt(c_sq))
            if c*c == c_sq:
                print(f"  {a}² + {b}² = {c}²  -> Triple found!")
    
    print("\n3. TRIANGULAR, SQUARE, CUBE NUMBERS")
    print("-"*70)
    
    for n in critical:
        # Check if triangular: n = k(k+1)/2
        k = int((math.sqrt(8*n + 1) - 1) / 2)
        if k*(k+1)//2 == n:
            print(f"  {n} is triangular (T_{k})")
        
        # Check if square
        root = int(math.sqrt(n))
        if root*root == n:
            print(f"  {n} is square ({root}²)")
        
        # Check if cube
        cbrt = int(round(n**(1/3)))
        if cbrt**3 == n:
            print(f"  {n} is cube ({cbrt}³)")
    
    print("\n4. DATE ENCODINGS")
    print("-"*70)
    
    # Birth and death dates as single numbers
    birth_num = 30101986  # DDMMYYYY
    death_num = 20102011
    
    print(f"\n  Birth (DDMMYYYY): {birth_num}")
    print(f"    Factors: {prime_factorization(birth_num)}")
    print(f"  Death (DDMMYYYY): {death_num}")
    print(f"    Factors: {prime_factorization(death_num)}")
    
    # Difference
    diff = abs(death_num - birth_num)
    print(f"\n  Difference: {diff}")
    print(f"    Factors: {prime_factorization(diff)}")

if __name__ == "__main__":
    deep_number_analysis()
    xor_analysis()
    analyze_pixel5_string()
    deep_linguistic_analysis()
    cross_correlation()
    advanced_math_patterns()
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE - See above for deep mathematical findings")
    print("="*70)
