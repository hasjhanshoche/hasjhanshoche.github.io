#!/usr/bin/env python3
"""
PASSWORD TESTER - Test pixel 5 derived candidates on /admin
"""

import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://haian.de"
PIXEL5_STRING = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"

print("="*80)
print("PASSWORD TESTING - Pixel 5 String Candidates")
print("="*80)

# Extract best candidates
candidates = [
    ("Full string", PIXEL5_STRING),
    ("First 25 chars (age)", PIXEL5_STRING[:25]),
    ("Last 25 chars", PIXEL5_STRING[-25:]),
    ("First 20 chars", PIXEL5_STRING[:20]),
    ("Alphanumeric only", ''.join(c for c in PIXEL5_STRING if c.isalnum())),
    ("Alphanumeric 20", ''.join(c for c in PIXEL5_STRING if c.isalnum())[:20]),
    ("Every 5th char", PIXEL5_STRING[::5]),
    ("Every 23rd char", PIXEL5_STRING[::23]),
    ("First 5 chars", PIXEL5_STRING[:5]),
    ("Last 5 chars", PIXEL5_STRING[-5:]),
    ("Middle 10", PIXEL5_STRING[52:62]),
    ("Numbers only", ''.join(c for c in PIXEL5_STRING if c.isdigit())),
    ("Before 25", PIXEL5_STRING[:17]),  # Up to '25'
    ("After 25", PIXEL5_STRING[19:]),  # After '25'
    ("OrBiD pattern", "OrBiD"),  # From column analysis
    ("DpSzM pattern", "DpSzM"),
    ("REttn pattern", "REttn"),
    ("kRBiD", "kRBiD"),  # Every 23rd
]

print(f"\nGenerated {len(candidates)} password candidates from pixel 5 string")
print("\nCandidates to test:")
for i, (name, pwd) in enumerate(candidates, 1):
    print(f"  {i}. {name}: '{pwd}' (len: {len(pwd)})")

print("\n" + "="*80)
print("TESTING AGAINST /admin")
print("="*80)

# Test each candidate
usernames = ["admin", "haian", "fabian"]

for username in usernames:
    print(f"\nTesting with username: {username}")
    print("-"*80)
    
    for name, password in candidates:
        try:
            response = requests.get(
                f"{BASE_URL}/admin",
                auth=HTTPBasicAuth(username, password),
                timeout=5
            )
            
            if response.status_code == 200:
                print(f"\n[✓] SUCCESS! {username}/{name}: '{password}'")
                print(f"    Access granted!")
                # Save success
                with open("research/password_cracked.txt", "w") as f:
                    f.write(f"Username: {username}\nPassword: {password}\nMethod: {name}\n")
                exit()
            elif response.status_code == 401:
                print(f"[✗] {name}: Failed (401)")
            else:
                print(f"[?] {name}: Status {response.status_code}")
                
        except Exception as e:
            print(f"[!] {name}: Error - {str(e)[:30]}")

print("\n" + "="*80)
print("Standard candidates failed. Trying transposition approaches...")
print("="*80)

# Try transposition-based passwords
print("\nTrying column reads from 6×19 grid (114 = 6×19):")
rows = [PIXEL5_STRING[i:i+19] for i in range(0, 114, 6)]
if len(rows) >= 6:
    for col in range(19):
        if all(len(row) > col for row in rows[:6]):
            column = ''.join([rows[row][col] for row in range(6)])
            if len(column) >= 5:
                print(f"  Col {col+1}: '{column}'")
                # Test column
                try:
                    response = requests.get(
                        f"{BASE_URL}/admin",
                        auth=HTTPBasicAuth("admin", column),
                        timeout=3
                    )
                    if response.status_code == 200:
                        print(f"\n[✓] COLUMN CRACKED! admin/{column}")
                        exit()
                except:
                    pass

print("\n" + "="*80)
print("All pixel 5 candidates tested. Password not found in standard tests.")
print("The string may require additional decoding (transposition cipher).")
print("="*80)
