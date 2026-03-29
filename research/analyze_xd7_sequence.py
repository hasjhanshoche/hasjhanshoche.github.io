#!/usr/bin/env python3
"""
Analyze the "xd7<" sequence found in ASCII mappings
120='x', 100='d', 55='7', 60='<'
This sequence appeared in our number-to-ASCII analysis
"""

# The sequence x-d-7-< comes from:
# 120 (Skat Ouvert) -> 'x'
# 100 (Sven's 100%) -> 'd'  
# 55 (Thomas) -> '7'
# 60 (Thomas) -> '<'

SEQUENCE_NUMS = [120, 100, 55, 60]
SEQUENCE_CHARS = ['x', 'd', '7', '<']

def analyze_xd7_sequence():
    """Deep analysis of the xd7< sequence"""
    print("="*70)
    print("ANALYSIS OF 'xd7<' SEQUENCE")
    print("="*70)
    
    print(f"\nSequence: {''.join(SEQUENCE_CHARS)}")
    print(f"From numbers: {SEQUENCE_NUMS}")
    print(f"\nSources:")
    print(f"  'x' = ASCII(120) - Skat Grand Ouvert value from Ihno's message")
    print(f"  'd' = ASCII(100) - Sven's '100%' message")
    print(f"  '7' = ASCII(55) - Thomas's '55' years")
    print(f"  '<' = ASCII(60) - Thomas's '60' years")
    
    print("\n" + "-"*70)
    print("MATHEMATICAL ANALYSIS")
    print("-"*70)
    
    # Various combinations
    print(f"\nSum: {sum(SEQUENCE_NUMS)} = {sum(SEQUENCE_NUMS)}")
    print(f"Product: {SEQUENCE_NUMS[0] * SEQUENCE_NUMS[1] * SEQUENCE_NUMS[2] * SEQUENCE_NUMS[3]}")
    
    # Differences
    print(f"\nDifferences from 120:")
    for n in SEQUENCE_NUMS[1:]:
        print(f"  120 - {n} = {120 - n}")
    
    # XOR combinations
    print(f"\nXOR combinations:")
    from itertools import combinations
    for a, b in combinations(SEQUENCE_NUMS, 2):
        result = a ^ b
        char = chr(result) if 32 <= result <= 126 else f"({result})"
        print(f"  {a} XOR {b} = {result} -> {char}")
    
    print("\n" + "-"*70)
    print("POSSIBLE INTERPRETATIONS")
    print("-"*70)
    
    interpretations = [
        ("Password candidate", "xd7< or xd7 or 7< or similar"),
        ("Hex value", "0xD7 = 215 decimal, 0x7< invalid"),
        ("Coordinate", "x=120, d=100, 7=55, <=60 -> (120,100,55,60)"),
        ("HTML/XML", "< could be start of tag"),
        ("Math expression", "x * d * 7 < something?"),
        ("Base64 fragment", "Could be part of larger base64"),
    ]
    
    for title, desc in interpretations:
        print(f"\n{title}:")
        print(f"  {desc}")
    
    print("\n" + "-"*70)
    print("TEST AS PASSWORD")
    print("-"*70)
    
    # Test variations as potential passwords
    variations = [
        'xd7<',
        'xd7',
        'd7<',
        '7<',
        'xD7<',
        'XD7<',
        'xd7<120',
        'xd7<100',
        'xd7<55',
        'xd7<60',
        '1201005560',
        'x-d-7-<',
        'x_d_7_<',
    ]
    
    print("\nPotential password variations:")
    for pwd in variations:
        print(f"  - {pwd}")
    
    print("\n" + "-"*70)
    print("CIPHER/ENCODING CHECKS")
    print("-"*70)
    
    s = 'xd7<'
    
    # ROT13
    rot13 = ''.join(chr((ord(c) - ord('a') + 13) % 26 + ord('a')) if c.isalpha() and c.islower() 
                     else chr((ord(c) - ord('A') + 13) % 26 + ord('A')) if c.isalpha() and c.isupper()
                     else c for c in s)
    print(f"\nROT13: {rot13}")
    
    # Reverse
    print(f"Reversed: {s[::-1]}")
    
    # Base64
    import base64
    try:
        decoded = base64.b64decode(s + '==')
        print(f"Base64 decoded: {decoded}")
    except:
        print(f"Base64: Not valid base64")
    
    # As hex
    hex_str = ''.join(hex(ord(c))[2:] for c in s)
    print(f"As hex string: {hex_str}")
    
    # Check if numbers have meaning
    print("\n" + "-"*70)
    print("NUMERICAL PROPERTIES")
    print("-"*70)
    
    # 120, 100, 55, 60
    print(f"\n120 = 2^3 × 3 × 5 = T_15 (triangular)")
    print(f"100 = 2^2 × 5^2 = 10^2 (perfect square)")
    print(f"55 = 5 × 11 = T_10 (triangular)")
    print(f"60 = 2^2 × 3 × 5 = highly composite")
    
    print(f"\nCommon factors:")
    print(f"  GCD(120,100,55,60) = {gcd(gcd(120,100), gcd(55,60))}")
    print(f"  All divisible by 5: {all(n % 5 == 0 for n in [120,100,55,60])}")
    
    print("\n" + "="*70)
    print("CONCLUSION: 'xd7<' appears to be a meaningful sequence")
    print("combining key puzzle numbers through their ASCII mappings.")
    print("It may be a password fragment or point to a specific cipher.")
    print("="*70)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    analyze_xd7_sequence()
