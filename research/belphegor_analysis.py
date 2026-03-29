#!/usr/bin/env python3
"""
Belphegor's Prime & Pickover Analysis
Check for patterns related to Belphegor's Prime in haian.de data
"""

import requests
from PIL import Image
import os

# Belphegor's Prime: 1000000000000066600000000000001
# 31 digits: 1 + 13 zeros + 666 + 13 zeros + 1
BELPHEGOR_PRIME = "1000000000000066600000000000001"

def check_hexdump_patterns():
    """Check hexdump of website and image for Belphegor patterns"""
    print("="*70)
    print("BELPHEGOR'S PRIME & PICKOVER ANALYSIS")
    print("="*70)
    print(f"\nBelphegor's Prime: {BELPHEGOR_PRIME}")
    print(f"Length: {len(BELPHEGOR_PRIME)} digits")
    print(f"Structure: 1 + 13 zeros + 666 + 13 zeros + 1")
    
    # Check website HTML
    print("\n" + "="*70)
    print("HEXDUMP ANALYSIS: haian.de website")
    print("="*70)
    
    try:
        r = requests.get("https://haian.de", timeout=10)
        html_content = r.text
        
        # Look for 666 patterns
        print(f"\nHTML content length: {len(html_content)} bytes")
        
        # Check for '666' in HTML
        count_666 = html_content.count('666')
        print(f"Occurrences of '666' in HTML: {count_666}")
        
        # Look for the number 13 patterns
        print("\nLooking for 13-related patterns...")
        
        # Check file size for Belphegor-like structure
        size = len(html_content)
        print(f"HTML size: {size} bytes")
        
        # Check if size has 13-related properties
        if size % 13 == 0:
            print(f"  ⚠️ Size divisible by 13: {size} / 13 = {size // 13}")
        if size % 31 == 0:  # 31 is length of Belphegor's prime
            print(f"  ⚠️ Size divisible by 31: {size} / 31 = {size // 31}")
        
        # Check for palindromic patterns in hex
        print("\nChecking for palindromic byte sequences...")
        
    except Exception as e:
        print(f"Error fetching website: {e}")
    
    # Check image
    print("\n" + "="*70)
    print("HEXDUMP ANALYSIS: Memorial Image")
    print("="*70)
    
    image_path = "images/haian_mit_text_skaliert_rand.jpeg"
    if os.path.exists(image_path):
        try:
            with open(image_path, 'rb') as f:
                img_data = f.read()
            
            print(f"\nImage size: {len(img_data)} bytes")
            
            # Check for 666 patterns in bytes
            hex_data = img_data.hex()
            count_666_hex = hex_data.count('666')
            count_0666 = hex_data.count('0666')
            
            print(f"Occurrences of '666' in hex: {count_666_hex}")
            print(f"Occurrences of '0666' in hex: {count_0666}")
            
            # Check file size
            size = len(img_data)
            if size % 13 == 0:
                print(f"  ⚠️ Size divisible by 13: {size} / 13 = {size // 13}")
            if size % 31 == 0:
                print(f"  ⚠️ Size divisible by 31: {size} / 31 = {size // 31}")
            if size % 666 == 0:
                print(f"  ⚠️ Size divisible by 666: {size} / 666 = {size // 666}")
            
            # Look for specific byte patterns
            print("\nChecking for specific byte patterns...")
            
            # Look for 0x00 patterns (zeros like in Belphegor's prime)
            zero_runs = []
            current_run = 0
            for byte in img_data[:1000]:  # First 1000 bytes
                if byte == 0:
                    current_run += 1
                else:
                    if current_run > 0:
                        zero_runs.append(current_run)
                        current_run = 0
            
            if zero_runs:
                print(f"Zero runs found (first 1000 bytes): {zero_runs[:10]}")
                if 13 in zero_runs:
                    print("  ⚠️ Found run of 13 zeros!")
            
        except Exception as e:
            print(f"Error analyzing image: {e}")
    else:
        print(f"Image not found: {image_path}")

def check_pickover_connections():
    """Check for Clifford A. Pickover related patterns"""
    print("\n" + "="*70)
    print("CLIFFORD A. PICKOVER CONNECTIONS")
    print("="*70)
    
    # Pickover is known for:
    # 1. Naming Belphegor's Prime (2012)
    # 2. Mathematical curiosities and puzzles
    # 3. Books on mathematics, chaos, fractals
    
    print("\nPickover's known interests:")
    print("  - Palindromic primes")
    print("  - Beast number (666) patterns")
    print("  - Mathematical curiosities")
    print("  - Fractals and chaos theory")
    
    print("\nChecking haian.de for Pickover-like patterns...")
    
    # Check for date 2012 (when Pickover named Belphegor's prime)
    print("\nDates in messages:")
    print("  - 2012 is when Pickover named Belphegor's prime")
    print("  - Messages span 2011-2012")
    print("  - Isabella's message: 24.02.2012")
    
    # Check if 2012 or related numbers appear
    print("\nLooking for Pickover-relevant numbers...")
    print("  - 666: Number of the beast")
    print("  - 13: Unlucky number / Belphegor structure")
    print("  - 31: Length of Belphegor's prime (13 reversed)")
    print("  - 2012: Year Belphegor's prime was named")

def analyze_number_666():
    """Special analysis of 666 connections"""
    print("\n" + "="*70)
    print("SPECIAL ANALYSIS: THE BEAST NUMBER (666)")
    print("="*70)
    
    # Check our key numbers for 666 connections
    key_numbers = [5, 24, 55, 60, 120, 700, 1000, 9121, 269508]
    
    print("\nChecking key numbers for 666 relationships:")
    for num in key_numbers:
        # Check divisibility
        if num % 6 == 0:
            print(f"  {num}: divisible by 6 ({num // 6})")
        # Check sums of digits
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum == 6:
            print(f"  {num}: digit sum = 6")
        if digit_sum == 13:
            print(f"  {num}: digit sum = 13 (Belphegor connection!)")
    
    # 666 divisibility
    print("\n666 divisibility check:")
    for num in key_numbers:
        if 666 % num == 0:
            print(f"  666 / {num} = {666 // num}")

def check_palindromes():
    """Check for palindromic patterns (Pickover's interest)"""
    print("\n" + "="*70)
    print("PALINDROME ANALYSIS (Pickover's Interest)")
    print("="*70)
    
    # Check if any of our key numbers are palindromes
    key_numbers = [5, 24, 55, 60, 120, 700, 1000, 269508, 9121]
    
    print("\nChecking key numbers for palindromes:")
    for num in key_numbers:
        s = str(num)
        if s == s[::-1]:
            print(f"  [!] {num} is a palindrome!")
    
    # 55 is a palindrome!
    print("\n55 = '55' is a palindrome (reads same forwards/backwards)")
    print("This connects to Belphegor's prime being palindromic")
    
    # Check pixel string for palindromes
    pixel5 = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"
    
    print("\nChecking pixel 5 string for palindromic substrings...")
    # Check first/last chars
    if pixel5[0].lower() == pixel5[-1].lower():
        print(f"  First and last chars match: '{pixel5[0]}' / '{pixel5[-1]}'")
    else:
        print(f"  First: '{pixel5[0]}', Last: '{pixel5[-1]}'")
    
    # Check for specific patterns
    print(f"\nString length: {len(pixel5)} (not a palindrome length)")

if __name__ == "__main__":
    check_hexdump_patterns()
    check_pickover_connections()
    analyze_number_666()
    check_palindromes()
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
