#!/usr/bin/env python3
"""
FINAL ATTEMPT - PIXEL COORDINATE ANALYSIS
Look at pixel value 5 positions as direct password source
"""

from PIL import Image

IMAGE_PATH = "images/haian_mit_text_skaliert_rand.jpeg"

def analyze_pixel5_positions():
    """Deep analysis of where pixel value 5 appears"""
    print("="*70)
    print("PIXEL VALUE 5 POSITION ANALYSIS")
    print("="*70)
    
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    # Get all positions where pixel value = 5
    positions = [(i % width, i // width) for i, p in enumerate(pixels) if p == 5]
    
    print(f"\nTotal pixels with value 5: {len(positions)}")
    print(f"Image dimensions: {width} x {height}")
    
    # Check if positions spell something
    print("\n" + "-"*70)
    print("X COORDINATES AS ASCII (all positions):")
    print("-"*70)
    
    x_ascii = ''.join(chr(x) for x, y in positions if 32 <= x <= 126)
    print(f"\nAll X as ASCII: {x_ascii}")
    
    # Try different groupings
    print("\n" + "-"*70)
    print("Y COORDINATES AS ASCII:")
    print("-"*70)
    
    y_ascii = ''.join(chr(y) for x, y in positions if 32 <= y <= 126)
    print(f"\nAll Y as ASCII: {y_ascii}")
    
    # Check if alternating X,Y gives something
    print("\n" + "-"*70)
    print("ALTERNATING X,Y AS MESSAGE:")
    print("-"*70)
    
    alt_msg = ''
    for i, (x, y) in enumerate(positions):
        if 32 <= x <= 126:
            alt_msg += chr(x)
        if 32 <= y <= 126:
            alt_msg += chr(y)
    print(f"\nAlternating X,Y: {alt_msg[:100]}")
    
    # Check specific ranges
    print("\n" + "-"*70)
    print("FIRST 20 PIXEL POSITIONS:")
    print("-"*70)
    
    for i, (x, y) in enumerate(positions[:20]):
        x_char = chr(x) if 32 <= x <= 126 else f"({x})"
        y_char = chr(y) if 32 <= y <= 126 else f"({y})"
        print(f"  {i:2d}: X={x:3d}({x_char}), Y={y:3d}({y_char})")
    
    # Check if positions form a pattern
    print("\n" + "-"*70)
    print("POSITION PATTERNS:")
    print("-"*70)
    
    # Check consecutive positions
    x_coords = [x for x, y in positions]
    y_coords = [y for x, y in positions]
    
    print(f"\nX range: {min(x_coords)} to {max(x_coords)}")
    print(f"Y range: {min(y_coords)} to {max(y_coords)}")
    
    # Check if X positions have meaning
    x_unique = sorted(set(x_coords))
    print(f"\nUnique X values: {len(x_unique)}")
    if len(x_unique) < 50:
        print(f"X values: {x_unique}")
    
    # Try reading X coordinates as password
    print("\n" + "-"*70)
    print("X COORDINATES AS POTENTIAL PASSWORD:")
    print("-"*70)
    
    # Different ways to interpret X coords
    x_str = ''.join(str(x) for x in x_coords[:10])  # First 10
    print(f"First 10 X concatenated: {x_str}")
    
    # Check if there's a simple pattern
    diffs = [positions[i+1][0] - positions[i][0] for i in range(len(positions)-1)]
    print(f"\nX differences (first 20): {diffs[:20]}")
    
    # Check if diffs spell something
    diff_ascii = ''.join(chr(d+64) for d in diffs if 1 <= d <= 26)
    if diff_ascii:
        print(f"Differences as letters (A=1): {diff_ascii}")

def test_extracted_passwords():
    """Test passwords extracted from pixel analysis"""
    print("\n" + "="*70)
    print("TESTING EXTRACTED PASSWORD CANDIDATES")
    print("="*70)
    
    import requests
    from requests.auth import HTTPBasicAuth
    
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    positions = [(i % width, i // width) for i, p in enumerate(pixels) if p == 5]
    
    # Extract password candidates from positions
    candidates = []
    
    # X coordinates as string
    x_str = ''.join(chr(x) for x, y in positions[:20] if 32 <= x <= 126)
    candidates.append(x_str)
    
    # First 5 X values concatenated
    x_nums = ''.join(str(x) for x, y in positions[:5])
    candidates.append(x_nums)
    
    # Every 5th position
    every_5th = ''.join(chr(x) for x, y in positions[::5] if 32 <= x <= 126)
    candidates.append(every_5th)
    
    url = "https://haian.de/admin"
    users = ['admin', 'haian', 'fabian', '5', '']
    
    print(f"\nTesting {len(candidates)} extracted candidates...")
    
    for pwd in candidates:
        for user in users:
            try:
                r = requests.get(url, auth=HTTPBasicAuth(user, pwd), timeout=5)
                if r.status_code == 200:
                    print(f"\n[FOUND] '{user}' / '{pwd}'")
                    return (user, pwd)
            except:
                pass
    
    print("\n[*] No match from extracted candidates")
    return None

if __name__ == "__main__":
    analyze_pixel5_positions()
    test_extracted_passwords()
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
