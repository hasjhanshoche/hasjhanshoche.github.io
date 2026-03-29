#!/usr/bin/env python3
"""
Deep Hexdump Analysis - Check for Belphegor's Prime and hidden patterns
"""

import requests
import os

# Belphegor's Prime pattern: 1 followed by zeros, 666, zeros, 1
BELPHEGOR_HEX = "00000000000000666"  # The central part in hex would look like this

def deep_hex_analysis():
    """Deep hexdump analysis of website and image"""
    print("="*70)
    print("DEEP HEXDUMP ANALYSIS")
    print("="*70)
    
    # Check website
    print("\n1. WEBSITE HTML HEX ANALYSIS")
    print("-"*70)
    try:
        r = requests.get("https://haian.de", timeout=10)
        html_bytes = r.content  # Get raw bytes
        
        print(f"Total bytes: {len(html_bytes)}")
        
        # Look for specific hex patterns
        hex_str = html_bytes.hex()
        
        # Check for 666666 (six sixes)
        count_666666 = hex_str.count('666666')
        print(f"Occurrences of '666666' (6 sixes): {count_666666}")
        
        # Check for 000000 pattern (zeros like in Belphegor)
        count_zeros = hex_str.count('000000')
        print(f"Occurrences of '000000' (6 zeros): {count_zeros}")
        
        # Check for specific byte values
        print("\nFirst 100 bytes (hex):")
        first_100 = hex_str[:200]
        print(f"  {first_100}")
        
        # Look for JPEG markers or special sequences
        print("\nLooking for special sequences:")
        
        # Check for 2012 in hex
        if '32303132' in hex_str:  # 2012 in ASCII
            print("  [FOUND] '2012' appears in hex (Pickover naming year)")
        
        # Check for specific numbers
        targets = ['24', '55', '60', '120', '5', '25', '666']
        for t in targets:
            t_hex = t.encode().hex()
            count = hex_str.count(t_hex)
            if count > 0:
                print(f"  '{t}' (hex: {t_hex}): {count} occurrences")
                
    except Exception as e:
        print(f"Error: {e}")
    
    # Check image
    print("\n2. MEMORIAL IMAGE HEX ANALYSIS")
    print("-"*70)
    
    image_path = "images/haian_mit_text_skaliert_rand.jpeg"
    if os.path.exists(image_path):
        try:
            with open(image_path, 'rb') as f:
                img_bytes = f.read()
            
            print(f"Total bytes: {len(img_bytes)}")
            
            hex_str = img_bytes.hex()
            
            # JPEG starts with FFD8 and ends with FFD9
            print("\nJPEG structure:")
            print(f"  Start marker (FFD8): {'ffd8' in hex_str[:10]}")
            print(f"  End marker (FFD9): {'ffd9' in hex_str[-10:]}")
            
            # Look for COM markers (comments)
            print("\nLooking for JPEG comment markers (FFFE)...")
            com_count = hex_str.count('fffe')
            print(f"  COM markers found: {com_count}")
            
            # Look for 666 patterns in detail
            print("\n666 pattern analysis:")
            
            # Check different forms
            patterns = ['666', '0666', '6660', '06660', '6666', '66666', '666666']
            for p in patterns:
                count = hex_str.count(p)
                if count > 0:
                    print(f"  '{p}': {count} occurrences")
            
            # Check for zero runs (Belphegor has 13 zeros)
            print("\nZero run analysis (like Belphegor's 13 zeros):")
            for run_len in [13, 10, 5, 3]:
                pattern = '0' * run_len
                count = hex_str.count(pattern)
                if count > 0:
                    print(f"  Run of {run_len} zeros: {count} occurrences")
            
            # Check file size properties
            size = len(img_bytes)
            print(f"\nFile size analysis ({size} bytes):")
            
            # Check digit sum of file size
            digit_sum = sum(int(d) for d in str(size))
            print(f"  Digit sum of size: {digit_sum}")
            
            # Check for Belphegor-related properties
            if digit_sum == 13:
                print(f"  [!] Digit sum = 13 (Belphegor connection!)")
            if digit_sum == 31:
                print(f"  [!] Digit sum = 31 (Belphegor prime length!)")
            if digit_sum == 6:
                print(f"  [!] Digit sum = 6 (666 related!)")
            
            # Check divisibility
            if size % 666 == 0:
                print(f"  [!] Size divisible by 666!")
            if size % 13 == 0:
                print(f"  [!] Size divisible by 13!")
            
            # Look at specific byte positions
            print("\nAnalyzing specific byte positions:")
            
            # Check bytes at positions related to our numbers
            positions = [5, 24, 55, 60, 120, 666, 1024, 2048]
            for pos in positions:
                if pos < len(img_bytes):
                    byte_val = img_bytes[pos]
                    print(f"  Byte at position {pos}: {byte_val} (hex: {hex(byte_val)[2:]:0>2})")
            
        except Exception as e:
            print(f"Error analyzing image: {e}")
    else:
        print(f"Image not found: {image_path}")

def check_creative_connections():
    """Check for creative mathematical connections"""
    print("\n" + "="*70)
    print("CREATIVE CONNECTIONS ANALYSIS")
    print("="*70)
    
    # Our key numbers
    numbers = {
        'age_days': 9121,
        'skat_24': 24,
        'skat_120': 120,
        'thomas_55': 55,
        'thomas_60': 60,
        'image_width': 700,
        'image_height': 1000,
        'image_size': 269508,
    }
    
    print("\n1. Belphegor Prime Digit Pattern Check")
    print("-"*70)
    
    # Belphegor: 1 0000000000000 666 0000000000000 1
    # Structure: 1 (13 zeros) 666 (13 zeros) 1
    
    for name, num in numbers.items():
        s = str(num)
        
        # Check for 666 substring
        if '666' in s:
            print(f"  [!] {name} ({num}) contains '666'")
        
        # Check for 1 at start and end (like Belphegor)
        if s[0] == '1' and s[-1] == '1':
            print(f"  [!] {name} ({num}) starts AND ends with 1 (Belphegor-like)")
        
        # Check if palindrome
        if s == s[::-1]:
            print(f"  [!] {name} ({num}) is palindrome (Pickover interest)")
    
    print("\n2. Pickover's Mathematical Curiosities")
    print("-"*70)
    
    # Pickover is interested in:
    # - Palindromic primes
    # - Beast numbers
    # - Unusual digit patterns
    
    # Check if 55 and 60 have special relationship
    print(f"\n55 and 60 analysis:")
    print(f"  55 = 5 × 11")
    print(f"  60 = 5 × 12")
    print(f"  Difference: 60 - 55 = 5 (our key number)")
    print(f"  55 is palindrome: {str(55) == str(55)[::-1]}")
    
    # Check 120 (Skat value)
    print(f"\n120 analysis:")
    print(f"  120 = 5! (5 factorial) = 5 × 4 × 3 × 2 × 1")
    print(f"  This connects to our key number 5!")
    
    # Check 24
    print(f"\n24 analysis:")
    print(f"  24 = 4! (4 factorial)")
    print(f"  120 / 24 = 5 (our key number)")
    
    print("\n3. Image Dimension Analysis")
    print("-"*70)
    
    # Image is 700 × 1000
    print(f"Image: 700 × 1000 = {700 * 1000} pixels")
    print(f"700 = 7 × 100 = 7 × 10²")
    print(f"1000 = 10³")
    print(f"700 contains '7' (Thomas's lucky number reference)")
    print(f"1000 contains 3 zeros (not quite 13, but zeros are significant)")
    
    # Check if 700 or 1000 relates to Belphegor
    for dim in [700, 1000]:
        s = str(dim)
        digit_sum = sum(int(d) for d in s)
        print(f"\n{dim}: digit sum = {digit_sum}")
        if digit_sum == 13:
            print(f"  [!] Digit sum = 13 (Belphegor!)")

if __name__ == "__main__":
    deep_hex_analysis()
    check_creative_connections()
    
    print("\n" + "="*70)
    print("DEEP ANALYSIS COMPLETE")
    print("="*70)
