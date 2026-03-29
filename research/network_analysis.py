#!/usr/bin/env python3
"""
Phase 1.5: DNS and Certificate Analysis
Check DNS records and TLS certificate for hidden data
"""

import subprocess
import ssl
import socket

TARGET = "haian.de"

def check_dns():
    """Check DNS records"""
    print("="*70)
    print("DNS ANALYSIS (Phase 1.5)")
    print("="*70)
    print(f"\nTarget: {TARGET}")
    
    # Try to get IP address
    try:
        ip = socket.gethostbyname(TARGET)
        print(f"\nA Record: {ip}")
        
        # Check if IP has significance
        ip_parts = ip.split('.')
        print(f"IP parts: {ip_parts}")
        
        # Check if any part maps to ASCII
        ascii_parts = []
        for part in ip_parts:
            num = int(part)
            if 32 <= num <= 126:
                ascii_parts.append(chr(num))
        if ascii_parts:
            print(f"IP as ASCII: {''.join(ascii_parts)}")
    except Exception as e:
        print(f"\nCould not resolve DNS: {e}")
    
    # Note: Full DNS record checks require dig/nslookup which may not be available
    print("\n[Note] Full DNS TXT/MX/NS records require 'dig' or 'nslookup' tools")
    print("       which are typically not available in standard Python environments.")

def check_certificate():
    """Check TLS certificate"""
    print("\n" + "="*70)
    print("TLS CERTIFICATE ANALYSIS (Phase 1.5)")
    print("="*70)
    
    try:
        context = ssl.create_default_context()
        with socket.create_connection((TARGET, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=TARGET) as ssock:
                cert = ssock.getpeercert()
                
                print(f"\nSSL/TLS connection established to {TARGET}:443")
                print(f"Cipher: {ssock.cipher()}")
                print(f"Version: {ssock.version()}")
                
                if cert:
                    print("\nCertificate Info:")
                    
                    # Subject
                    subject = cert.get('subject', [])
                    print(f"  Subject: {subject}")
                    
                    # Issuer
                    issuer = cert.get('issuer', [])
                    print(f"  Issuer: {issuer}")
                    
                    # Dates
                    not_before = cert.get('notBefore', 'N/A')
                    not_after = cert.get('notAfter', 'N/A')
                    print(f"  Not Before: {not_before}")
                    print(f"  Not After: {not_after}")
                    
                    # Subject Alternative Names
                    san = cert.get('subjectAltName', [])
                    if san:
                        print(f"  SANs: {[name for _, name in san[:5]]}")
                    
                    # Serial number
                    serial = cert.get('serialNumber', 'N/A')
                    print(f"  Serial Number: {serial}")
                    
                    # Check for suspicious data in fields
                    print("\nChecking for encoded data in certificate fields...")
                    for field in ['subject', 'issuer', 'serialNumber']:
                        value = str(cert.get(field, ''))
                        # Check for base64-like strings
                        import re
                        b64_pattern = re.compile(r'[A-Za-z0-9+/]{20,}={0,2}')
                        matches = b64_pattern.findall(value)
                        if matches:
                            print(f"  [Found potential base64 in {field}: {matches[:2]}]")
                else:
                    print("No certificate obtained")
                    
    except socket.timeout:
        print(f"\n[Connection timeout to {TARGET}:443]")
    except ConnectionRefusedError:
        print(f"\n[Connection refused to {TARGET}:443 - no HTTPS service]")
    except Exception as e:
        print(f"\n[Error checking certificate: {e}]")

def check_wayback():
    """Check for historical snapshots"""
    print("\n" + "="*70)
    print("HISTORICAL SNAPSHOTS (Phase 1.6)")
    print("="*70)
    print(f"\nTarget: https://{TARGET}")
    print(f"\nWayback Machine URL:")
    print(f"  https://web.archive.org/web/*/{TARGET}")
    print(f"\n[Note] Manual check required - visit the Wayback Machine URL above")
    print("       to see historical versions of the memorial page.")
    
    # Check if we can access it programmatically
    try:
        import urllib.request
        wayback_url = f"https://web.archive.org/web/20110101000000*/{TARGET}"
        print(f"\nTrying: {wayback_url}")
        
        req = urllib.request.Request(
            wayback_url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        
        with urllib.request.urlopen(req, timeout=10) as response:
            # Just check if it exists
            print(f"  Status: {response.status}")
            if response.status == 200:
                print("  [Historical snapshots may be available]")
    except Exception as e:
        print(f"  [Could not query Wayback: {e}]")

if __name__ == "__main__":
    check_dns()
    check_certificate()
    check_wayback()
    
    print("\n" + "="*70)
    print("NETWORK ANALYSIS COMPLETE")
    print("="*70)
    print("\nNote: Some network checks may require external tools")
    print("      or may be blocked by firewall/security settings.")
