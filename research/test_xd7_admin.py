#!/usr/bin/env python3
"""
Test the xd7< sequence as password for /admin
"""

import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://haian.de"

def test_xd7_passwords():
    """Test xd7 sequence variations as passwords"""
    print("="*70)
    print("TESTING 'xd7<' AS /admin PASSWORD")
    print("="*70)
    
    # Variations of the xd7 sequence
    passwords = [
        'xd7<',
        'xd7',
        'd7<',
        '7<',
        'xD7<',
        'XD7<',
        '1201005560',
        'xd7<5',  # Adding the key number
        '5xd7<',
        'xd7<24',
        'xd7<120',
        'xd7<55',
        'xd7<60',
    ]
    
    usernames = ['admin', 'haian', 'fabian', 'user', 'root', '5', '24', '']
    
    url = f"{BASE_URL}/admin"
    
    print(f"\nTesting {len(usernames)} usernames × {len(passwords)} passwords = {len(usernames) * len(passwords)} combinations")
    print(f"Target: {url}")
    
    found = False
    for username in usernames:
        for password in passwords:
            try:
                response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=5)
                if response.status_code == 200:
                    print(f"\n[*** SUCCESS ***] Username: '{username}', Password: '{password}'")
                    print(f"Response length: {len(response.text)}")
                    print(f"First 500 chars:\n{response.text[:500]}")
                    found = True
                    return (username, password)
                elif response.status_code == 401:
                    pass  # Wrong credentials
                else:
                    print(f"[{response.status_code}] {username}/{password}")
            except Exception as e:
                pass  # Silently skip errors
    
    if not found:
        print("\n[*] No valid credentials found with xd7 sequence variations")
        print("\n[*] This suggests:")
        print("    1. xd7< is not the direct password")
        print("    2. It may be a key to decode something else")
        print("    3. It may need transformation (ROT, XOR, etc.)")
    
    return None

def test_ascii_combo():
    """Test ASCII from XOR combinations"""
    print("\n" + "="*70)
    print("TESTING XOR ASCII COMBINATIONS")
    print("="*70)
    
    # From our XOR analysis:
    # 120 XOR 55 = 79 -> 'O'
    # 120 XOR 60 = 68 -> 'D'
    # 100 XOR 55 = 83 -> 'S'
    # 100 XOR 60 = 88 -> 'X'
    
    xor_results = [
        ('OD', 79, 68),    # 120 XOR 55, 120 XOR 60
        ('OS', 79, 83),    # 120 XOR 55, 100 XOR 55
        ('OX', 79, 88),    # 120 XOR 55, 100 XOR 60
        ('DS', 68, 83),    # 120 XOR 60, 100 XOR 55
        ('DX', 68, 88),    # 120 XOR 60, 100 XOR 60
        ('SX', 83, 88),    # 100 XOR 55, 100 XOR 60
    ]
    
    usernames = ['admin', 'haian', 'fabian', '']
    url = f"{BASE_URL}/admin"
    
    print("\nTesting XOR result combinations...")
    
    for combo, _, _ in xor_results:
        for username in usernames:
            try:
                response = requests.get(url, auth=HTTPBasicAuth(username, combo), timeout=5)
                if response.status_code == 200:
                    print(f"\n[*** SUCCESS ***] '{username}' / '{combo}'")
                    return (username, combo)
            except:
                pass
    
    print("\n[*] No XOR ASCII combinations worked")
    return None

if __name__ == "__main__":
    test_xd7_passwords()
    test_ascii_combo()
