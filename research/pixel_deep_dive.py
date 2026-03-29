#!/usr/bin/env python3
"""
PIXEL STRING PATTERN DEEP DIVE
Find the hidden pattern in the pixel 5 string
"""

PIXEL5 = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"

def deep_pattern_analysis():
    print("="*70)
    print("PIXEL 5 STRING - DEEP PATTERN ANALYSIS")
    print("="*70)
    print(f"\nString: {PIXEL5}")
    print(f"Length: {len(PIXEL5)}")
    
    # Key insight: 115 = 5 × 23
    print(f"\n115 = 5 × 23")
    print(f"This suggests a 5×23 or 23×5 grid arrangement!")
    
    # Try reading as 5 rows of 23
    print("\n" + "-"*70)
    print("GRID ARRANGEMENT: 5 rows × 23 columns")
    print("-"*70)
    
    rows_5 = []
    for i in range(5):
        row = PIXEL5[i*23:(i+1)*23]
        rows_5.append(row)
        print(f"Row {i+1}: {row}")
    
    # Try reading columns
    print("\nReading by COLUMNS (top-to-bottom):")
    cols = []
    for col in range(23):
        column = ''.join(rows_5[row][col] for row in range(5))
        cols.append(column)
        if col < 10:  # Show first 10
            print(f"  Col {col+1}: {column}")
    
    # Check if columns spell something
    print("\n" + "-"*70)
    print("COLUMN ANALYSIS")
    print("-"*70)
    
    for i, col in enumerate(cols):
        # Check if column is readable
        alpha = sum(1 for c in col if c.isalpha())
        if alpha >= 3:  # Mostly letters
            print(f"  Column {i+1}: {col} ({alpha}/5 letters)")
    
    # Try 23 rows of 5
    print("\n" + "-"*70)
    print("GRID ARRANGEMENT: 23 rows × 5 columns")
    print("-"*70)
    
    rows_23 = []
    for i in range(23):
        row = PIXEL5[i*5:(i+1)*5]
        rows_23.append(row)
        if i < 10:  # Show first 10
            print(f"Row {i+1}: {row}")
    
    # Read columns
    print("\nReading columns (23×5 grid):")
    for col in range(5):
        column = ''.join(rows_23[row][col] for row in range(23))
        print(f"  Column {col+1}: {column}")
    
    # Check for readable words in columns
    print("\n" + "-"*70)
    print("EXTRACTING READABLE PATTERNS")
    print("-"*70)
    
    # Extract all positions that are letters
    letters_only = ''.join(c for c in PIXEL5 if c.isalpha())
    print(f"\nLetters only: {letters_only}")
    print(f"Length: {len(letters_only)}")
    
    # Check every nth character
    for n in [2, 3, 4, 5, 6, 7, 8, 10, 15, 20]:
        subset = PIXEL5[::n]
        alpha_ratio = sum(1 for c in subset if c.isalpha()) / len(subset)
        if alpha_ratio > 0.5:
            print(f"\nEvery {n}th char (alpha={alpha_ratio:.0%}): {subset[:40]}")

def find_hidden_words():
    print("\n" + "="*70)
    print("SEARCHING FOR HIDDEN WORDS")
    print("="*70)
    
    # Common password words
    password_words = [
        'admin', 'password', 'pass', 'key', 'flag', 'secret', 'code',
        'haian', 'fabian', 'satoshi', 'bitcoin', 'crypto',
        'five', 'four', 'nine', 'love', 'hope', 'peace',
        'open', 'enter', 'access', 'login', 'user', 'root',
        'skat', 'poker', 'game', 'play', 'win',
        'german', 'deutsch', 'berlin', 'hamburg',
    ]
    
    lower_pixel = PIXEL5.lower()
    
    print("\nSearching for password-related words:")
    for word in password_words:
        if word in lower_pixel:
            idx = lower_pixel.index(word)
            print(f"  FOUND '{word}' at position {idx}: {PIXEL5[idx:idx+len(word)]}")
    
    # Check for reversed words
    reversed_pixel = PIXEL5[::-1].lower()
    print("\nSearching in REVERSED string:")
    for word in password_words:
        if word in reversed_pixel:
            idx = reversed_pixel.index(word)
            original_idx = len(PIXEL5) - idx - len(word)
            print(f"  FOUND '{word}' (reversed) at original position {original_idx}")

def extract_every_position():
    print("\n" + "="*70)
    print("POSITION-BASED EXTRACTION")
    print("="*70)
    
    # Every position that equals 5, 24, etc.
    targets = [5, 24, 25, 55, 60, 120]
    
    for target in targets:
        if target < len(PIXEL5):
            char = PIXEL5[target]
            print(f"\nPosition {target}: '{char}'")
            if target > 0:
                context = PIXEL5[target-2:target+3]
                print(f"  Context: ...{context}...")
    
    # Extract characters at prime positions
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    prime_chars = ''.join(PIXEL5[p] for p in primes if p < len(PIXEL5))
    print(f"\nCharacters at PRIME positions: {prime_chars}")
    
    # Extract characters at position 5, 10, 15, 20... (multiples of 5)
    mult5 = ''.join(PIXEL5[i] for i in range(5, len(PIXEL5), 5))
    print(f"Characters at multiples of 5: {mult5}")
    
    # Extract characters at position 24, 48, 72, 96 (multiples of 24)
    mult24 = ''.join(PIXEL5[i] for i in range(24, len(PIXEL5), 24))
    print(f"Characters at multiples of 24: {mult24}")

def check_numeric_sequences():
    print("\n" + "="*70)
    print("NUMERIC SEQUENCE ANALYSIS")
    print("="*70)
    
    # Find all digit sequences
    import re
    digits = re.findall(r'\d+', PIXEL5)
    print(f"\nAll digit sequences found: {digits}")
    
    # Check if they have meaning
    for d in digits:
        num = int(d)
        print(f"  {d}: ", end="")
        if num == 25:
            print("AGE-1 ✓")
        elif num == 45:
            print("45")
        elif num == 52:
            print("REVERSED 25 ✓")
        elif num == 8:
            print("8")
        elif num == 9:
            print("9")
        else:
            print(num)
    
    # Check positions of numbers
    for d in ['25', '52', '45', '8']:
        idx = PIXEL5.find(d)
        if idx != -1:
            print(f"\n'{d}' found at position {idx}")

if __name__ == "__main__":
    deep_pattern_analysis()
    find_hidden_words()
    extract_every_position()
    check_numeric_sequences()
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
