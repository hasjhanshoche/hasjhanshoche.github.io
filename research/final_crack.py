#!/usr/bin/env python3
"""
FINAL COMPREHENSIVE CRACK
Try every possible combination and approach
"""

import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://haian.de"

def final_crack_attempt():
    """Final comprehensive password attempt"""
    print("="*70)
    print("FINAL COMPREHENSIVE CRACK ATTEMPT")
    print("="*70)
    
    # Every possible password candidate we can think of
    passwords = []
    
    # Basic numbers
    passwords.extend(['5', '55', '555', '5555', '55555'])
    passwords.extend(['24', '25', '52', '11', '20'])
    passwords.extend(['120', '240', '24'])
    passwords.extend(['55', '60', '5560', '6055'])
    
    # Combinations
    passwords.extend([
        '524', '5120', '55560', '52411', '5524',
        '525', '552', '255', '522',
        '12055', '12060', '1205',
        '24120', '241205',
        '60120', '55120',
    ])
    
    # With 'haian' or 'fabian'
    passwords.extend(['haian5', 'fabian5', '5haian', '5fabian'])
    passwords.extend(['haian25', 'fabian25', 'haian24', 'fabian24'])
    
    # The pixel 5 string and fragments
    pixel5 = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"
    passwords.append(pixel5)
    passwords.append(pixel5[:25])
    passwords.append(pixel5[-25:])
    passwords.append(''.join(c for c in pixel5 if c.isalnum()))
    
    # Column reads from 5x23 grid
    passwords.extend([
        'kR?h;',
        'OrBiD',
        'DpSzM',
        'REttn',
        'OS5h=',
    ])
    
    # From 23x5 grid columns
    passwords.extend([
        'kI{SRsa44O5sVuiedk@N_MP',
        'O|[Z8Q5p5?28OtluiO@=eAC',
    ])
    
    # Simple/common
    passwords.extend(['password', 'admin', '12345', 'qwerty', 'letmein'])
    passwords.extend(['geheim', 'passwort', 'schlüssel'])
    
    # Image related
    passwords.extend(['700', '1000', '7001000', '269508'])
    
    # Date formats
    passwords.extend(['30101986', '20102011', '301086', '201011'])
    
    # xd7 sequence
    passwords.extend(['xd7<', 'xd7', 'd7<', '1201005560'])
    
    # XOR results
    passwords.extend(['`', '/', '}', 'O', 'D', 'a', '2', '9'])
    passwords.extend(['OD', 'OS', 'OX', 'DS', 'DX', 'ODOS', 'ODOSOX'])
    
    # Every 5th char from pixel string
    passwords.append('I{SRsa44O5sVuiedk@N_MP')
    
    # Try all
    url = f"{BASE_URL}/admin"
    users = ['admin', 'haian', 'fabian', 'user', 'root', '5', '']
    
    total = len(users) * len(passwords)
    print(f"\nTesting {len(users)} users × {len(passwords)} passwords = {total} combinations")
    
    tested = 0
    for user in users:
        for pwd in passwords:
            tested += 1
            if tested % 50 == 0:
                print(f"  Progress: {tested}/{total}")
            
            try:
                r = requests.get(url, auth=HTTPBasicAuth(user, pwd), timeout=5)
                if r.status_code == 200:
                    print(f"\n[*** FOUND ***] User: '{user}' / Password: '{pwd}'")
                    print("\n" + "="*70)
                    print("RESPONSE:")
                    print("="*70)
                    print(r.text[:2000])
                    return (user, pwd, r.text)
            except:
                pass
    
    print(f"\n[*] Exhausted all {tested} combinations")
    return None

def try_post_auth():
    """Try POST authentication"""
    print("\n" + "="*70)
    print("TRYING POST AUTHENTICATION")
    print("="*70)
    
    passwords = ['5', '25', '24', '120', '55', '60', pixel5[:50]]
    
    for pwd in passwords:
        try:
            r = requests.post(f"{BASE_URL}/admin", data={'password': pwd}, timeout=5)
            if r.status_code == 200:
                print(f"[POST SUCCESS] password={pwd}")
                print(r.text[:500])
                return (pwd, r.text)
        except:
            pass
    
    print("[*] POST auth didn't work")
    return None

if __name__ == "__main__":
    result = final_crack_attempt()
    
    if not result:
        result = try_post_auth()
    
    if result:
        print("\n" + "="*70)
        print("PUZZLE SOLVED!")
        print("="*70)
        print(f"Credentials found!")
    else:
        print("\n" + "="*70)
        print("ALL ATTEMPTS FAILED")
        print("="*70)
        print("\nPossible conclusions:")
        print("  1. Password is not in our test set")
        print("  2. Different authentication mechanism required")
        print("  3. Additional puzzle layers need to be solved first")
        print("  4. The /admin endpoint may not be the actual entry point")
