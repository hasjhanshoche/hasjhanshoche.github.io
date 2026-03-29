#!/usr/bin/env python3
"""
ULTIMATE PUZZLE CRACKER
Deep analysis to find the hidden password/code
"""

import requests
from requests.auth import HTTPBasicAuth
from itertools import permutations

BASE_URL = "https://haian.de"

# The pixel 5 string
PIXEL5 = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"

def try_transposition_ciphers():
    """Try various transposition ciphers on pixel 5 string"""
    print("="*70)
    print("TRANSPOSITION CIPHER ANALYSIS")
    print("="*70)
    
    # Columnar transposition with key 5
    print("\n1. Columnar Transposition (key=5):")
    key = 5
    cols = [''] * key
    for i, c in enumerate(PIXEL5):
        cols[i % key] += c
    result5 = ''.join(cols)
    print(f"   Result: {result5[:80]}...")
    
    # Check if readable
    alpha_count = sum(1 for c in result5 if c.isalpha())
    print(f"   Alpha ratio: {alpha_count/len(result5):.2%}")
    
    # Columnar with key 24
    print("\n2. Columnar Transposition (key=24):")
    key = 24
    cols = [''] * key
    for i, c in enumerate(PIXEL5):
        cols[i % key] += c
    result24 = ''.join(cols)
    print(f"   Result: {result24[:80]}...")
    alpha_count = sum(1 for c in result24 if c.isalpha())
    print(f"   Alpha ratio: {alpha_count/len(result24):.2%}")
    
    # Rail fence cipher
    print("\n3. Rail Fence Cipher (rails=5):")
    rails = 5
    fence = [[''] * len(PIXEL5) for _ in range(rails)]
    rail = 0
    var = 1
    for i, c in enumerate(PIXEL5):
        fence[rail][i] = c
        rail += var
        if rail == rails - 1 or rail == 0:
            var = -var
    rail5 = ''.join(''.join(row) for row in fence)
    print(f"   Result: {rail5[:80]}...")
    
    # Rail fence with 24 rails
    print("\n4. Rail Fence Cipher (rails=24):")
    rails = 24
    fence = [[''] * len(PIXEL5) for _ in range(rails)]
    rail = 0
    var = 1
    for i, c in enumerate(PIXEL5):
        fence[rail][i] = c
        rail += var
        if rail == rails - 1 or rail == 0:
            var = -var
    rail24 = ''.join(''.join(row) for row in fence)
    print(f"   Result: {rail24[:80]}...")
    
    return [result5, result24, rail5, rail24]

def test_passwords_direct(passwords):
    """Test passwords directly against /admin"""
    print("\n" + "="*70)
    print("PASSWORD TESTING AGAINST /admin")
    print("="*70)
    
    url = f"{BASE_URL}/admin"
    usernames = ['admin', 'haian', 'fabian', '5', '24', '']
    
    for pwd in passwords:
        for username in usernames:
            try:
                response = requests.get(url, auth=HTTPBasicAuth(username, pwd), timeout=5)
                if response.status_code == 200:
                    print(f"\n[*** SUCCESS ***] '{username}' / '{pwd}'")
                    print(f"Response: {response.text[:500]}")
                    return (username, pwd)
            except:
                pass
    
    print("\n[*] No direct matches found")
    return None

def extract_clean_password_candidates():
    """Extract clean password candidates from analysis"""
    print("\n" + "="*70)
    print("PASSWORD CANDIDATE GENERATION")
    print("="*70)
    
    candidates = []
    
    # From pixel 5 string
    candidates.append(PIXEL5)  # Full string
    candidates.append(PIXEL5[:25])  # First 25 chars
    candidates.append(PIXEL5[-25:])  # Last 25 chars
    candidates.append(''.join(c for c in PIXEL5 if c.isalnum()))  # Alphanumeric only
    
    # From xd7< sequence
    candidates.extend(['xd7<', 'xd7', 'd7<', '1201005560'])
    
    # Simple numbers
    candidates.extend(['5', '25', '52', '24', '120', '55', '60'])
    
    # Combinations
    candidates.extend(['5xd7<', 'xd7<5', '5pixel5', 'pixel55'])
    
    # XOR results
    candidates.extend(['`', '/', '}', 'O', 'D', 'a', '2', '9'])
    candidates.extend(['OD', 'OS', 'OX', 'DS', 'DX'])
    
    # Image dimensions
    candidates.extend(['700', '1000', '7001000'])
    
    print(f"\nGenerated {len(candidates)} password candidates")
    for c in candidates[:20]:
        print(f"  - {c[:50]}{'...' if len(c) > 50 else ''}")
    
    return candidates

def check_pixel_positions():
    """Check if pixel positions themselves form a password"""
    print("\n" + "="*70)
    print("PIXEL POSITION PASSWORD ANALYSIS")
    print("="*70)
    
    from PIL import Image
    
    img = Image.open("images/haian_mit_text_skaliert_rand.jpeg").convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    # Get positions where pixel value = 5
    positions = [(i % width, i // width) for i, p in enumerate(pixels) if p == 5]
    
    print(f"\nFound {len(positions)} pixels with value 5")
    
    # Try extracting passwords from positions
    x_coords = [x for x, y in positions]
    y_coords = [y for x, y in positions]
    
    # Check first N positions as ASCII
    for n in [5, 10, 15, 20, 25]:
        x_str = ''.join(chr(x) for x in x_coords[:n] if 32 <= x <= 126)
        y_str = ''.join(chr(y) for y in y_coords[:n] if 32 <= y <= 126)
        print(f"\nFirst {n} X positions as ASCII: {x_str}")
        print(f"First {n} Y positions as ASCII: {y_str}")
    
    # Check specific positions that might spell something
    # Every 5th position
    every_5th = positions[::5]
    x_5th = ''.join(chr(x) for x, y in every_5th if 32 <= x <= 126)
    print(f"\nEvery 5th position X ASCII: {x_5th}")

def try_permutation_analysis():
    """Try permutations of key elements"""
    print("\n" + "="*70)
    print("PERMUTATION ANALYSIS")
    print("="*70)
    
    # Key elements
    elements = ['5', '24', '120', '55', '60', '25', 'x', 'd', '7', '<', 'O', 'D']
    
    # Try 2-4 element permutations
    for length in [2, 3, 4]:
        print(f"\nTrying {length}-element permutations...")
        count = 0
        for perm in permutations(elements, length):
            candidate = ''.join(perm)
            count += 1
            if count > 1000:  # Limit to avoid spam
                break
        print(f"  Generated {count} candidates of length {length}")

def deep_string_patterns():
    """Look for hidden patterns in the pixel 5 string"""
    print("\n" + "="*70)
    print("DEEP STRING PATTERN ANALYSIS")
    print("="*70)
    
    print(f"\nString length: {len(PIXEL5)}")
    print(f"115 = 5 × 23")
    print(f"115 = 23 × 5")
    
    # Check divisibility
    print(f"\nDivisible by 5: {len(PIXEL5) % 5 == 0}")
    print(f"Divisible by 23: {len(PIXEL5) % 23 == 0}")
    
    # Try splitting into 5 equal parts
    if len(PIXEL5) % 5 == 0:
        part_len = len(PIXEL5) // 5
        print(f"\nSplit into 5 parts of {part_len} chars:")
        for i in range(5):
            part = PIXEL5[i*part_len:(i+1)*part_len]
            print(f"  Part {i+1}: {part}")
    
    # Check for alternating patterns
    even_chars = PIXEL5[::2]
    odd_chars = PIXEL5[1::2]
    print(f"\nEven positions: {even_chars[:50]}")
    print(f"Odd positions: {odd_chars[:50]}")
    
    # Look for specific substrings
    print("\nSearching for meaningful substrings:")
    meaningful = ['key', 'flag', 'pass', 'word', 'admin', 'haian', 'five', 'four', 'open', 'lock']
    for word in meaningful:
        if word in PIXEL5.lower():
            idx = PIXEL5.lower().index(word)
            print(f"  Found '{word}' at position {idx}")

if __name__ == "__main__":
    print("="*70)
    print("ULTIMATE PUZZLE CRACKER - FULL ANALYSIS")
    print("="*70)
    
    # Run all analyses
    trans_results = try_transposition_ciphers()
    
    candidates = extract_clean_password_candidates()
    candidates.extend(trans_results)
    
    print(f"\n[*] Testing {len(candidates)} password candidates...")
    result = test_passwords_direct(candidates[:50])  # Test first 50
    
    if not result:
        check_pixel_positions()
        try_permutation_analysis()
        deep_string_patterns()
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
