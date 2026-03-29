#!/usr/bin/env python3
"""
ALTERNATIVE ADMIN ACCESS METHODS
Try different ways to access /admin
"""

import requests

BASE_URL = "https://haian.de"

def try_alternative_methods():
    """Try different ways to access /admin"""
    print("="*70)
    print("ALTERNATIVE /admin ACCESS METHODS")
    print("="*70)
    
    # Try POST instead of GET
    print("\n1. POST request to /admin:")
    try:
        r = requests.post(f"{BASE_URL}/admin", timeout=10)
        print(f"   Status: {r.status_code}")
        if r.status_code != 401:
            print(f"   Response: {r.text[:500]}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Try with different headers
    print("\n2. GET with custom headers:")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
    }
    try:
        r = requests.get(f"{BASE_URL}/admin", headers=headers, timeout=10)
        print(f"   Status: {r.status_code}")
        if r.status_code != 401:
            print(f"   Response: {r.text[:500]}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Try with form data
    print("\n3. POST with form data (password=5):")
    try:
        r = requests.post(f"{BASE_URL}/admin", data={'password': '5'}, timeout=10)
        print(f"   Status: {r.status_code}")
        if r.status_code != 401:
            print(f"   Response: {r.text[:500]}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Try with JSON
    print("\n4. POST with JSON (password=5):")
    try:
        r = requests.post(f"{BASE_URL}/admin", json={'password': '5'}, timeout=10)
        print(f"   Status: {r.status_code}")
        if r.status_code != 401:
            print(f"   Response: {r.text[:500]}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Try query parameters
    print("\n5. GET with query params (?password=5):")
    try:
        r = requests.get(f"{BASE_URL}/admin?password=5", timeout=10)
        print(f"   Status: {r.status_code}")
        if r.status_code != 401:
            print(f"   Response: {r.text[:500]}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Try cookie
    print("\n6. GET with cookie (password=5):")
    try:
        cookies = {'password': '5', 'admin': 'true'}
        r = requests.get(f"{BASE_URL}/admin", cookies=cookies, timeout=10)
        print(f"   Status: {r.status_code}")
        if r.status_code != 401:
            print(f"   Response: {r.text[:500]}")
    except Exception as e:
        print(f"   Error: {e}")

def check_response_headers():
    """Check what headers come back from 401"""
    print("\n" + "="*70)
    print("ANALYZING 401 RESPONSE HEADERS")
    print("="*70)
    
    try:
        r = requests.get(f"{BASE_URL}/admin", timeout=10)
        print(f"\nStatus: {r.status_code}")
        print("\nResponse Headers:")
        for key, value in r.headers.items():
            print(f"  {key}: {value}")
        
        # Check for WWW-Authenticate header
        if 'WWW-Authenticate' in r.headers:
            print(f"\n*** WWW-Authenticate: {r.headers['WWW-Authenticate']}")
            print("This tells us what auth method is required!")
        
        print(f"\nResponse body (first 500 chars):")
        print(r.text[:500])
    except Exception as e:
        print(f"Error: {e}")

def check_other_paths():
    """Check other potential admin-related paths"""
    print("\n" + "="*70)
    print("CHECKING RELATED PATHS")
    print("="*70)
    
    paths = [
        '/login',
        '/wp-admin',
        '/administrator',
        '/admin.php',
        '/admin.html',
        '/manage',
        '/management',
        '/panel',
        '/dashboard',
        '/backend',
        '/console',
    ]
    
    for path in paths:
        try:
            r = requests.get(f"{BASE_URL}{path}", timeout=5, allow_redirects=False)
            if r.status_code != 404:
                print(f"  {path}: {r.status_code}")
        except:
            pass

if __name__ == "__main__":
    try_alternative_methods()
    check_response_headers()
    check_other_paths()
