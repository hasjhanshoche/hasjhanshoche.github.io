#!/usr/bin/env python3
"""
Advanced image analysis - DCT steganography for JPEG (without numpy)
"""

from PIL import Image
import struct

IMAGE_PATH = "research/01_assets/images/haian_mit_text_skaliert_rand.jpeg"

def analyze_jpeg_structure():
    """Analyze JPEG marker structure"""
    with open(IMAGE_PATH, 'rb') as f:
        data = f.read()
    
    print("="*60)
    print("JPEG STRUCTURE ANALYSIS")
    print("="*60)
    
    # Find all JPEG markers
    markers = []
    i = 0
    while i < len(data) - 1:
        if data[i] == 0xFF and data[i+1] != 0x00 and data[i+1] != 0xFF:
            marker = data[i+1]
            markers.append((i, hex(marker)))
            # Skip marker segment
            if marker not in [0xD8, 0xD9, 0x01]:  # SOI, EOI, TEM don't have length
                if i + 3 < len(data):
                    length = struct.unpack('>H', data[i+2:i+4])[0]
                    i += 2 + length
                    continue
        i += 1
    
    print(f"Found {len(markers)} markers:")
    for pos, marker in markers[:20]:
        print(f"  Position {pos}: {marker}")
    
    # Look for APP segments (can contain hidden data)
    print("\nAPP segments analysis:")
    for i in range(len(data) - 1):
        if data[i] == 0xFF:
            if 0xE0 <= data[i+1] <= 0xEF:  # APP0-APP15
                app_num = data[i+1] - 0xE0
                if i + 3 < len(data):
                    length = struct.unpack('>H', data[i+2:i+4])[0]
                    content = data[i+4:i+2+length]
                    print(f"  APP{app_num} at {i}: length={length}")
                    if length < 100:
                        print(f"    Content: {content[:50]}")

def extract_dct_coefficients():
    """Extract DCT coefficients (advanced)"""
    print("\n" + "="*60)
    print("DCT COEFFICIENT EXTRACTION")
    print("="*60)
    print("This requires specialized JPEG parsing libraries.")
    print("Trying basic statistical analysis...")
    
    try:
        from PIL import Image
        img = Image.open(IMAGE_PATH)
        
        # Convert to YCbCr and analyze each channel
        if img.mode != 'YCbCr':
            img_ycbcr = img.convert('YCbCr')
        else:
            img_ycbcr = img
        
        y, cb, cr = img_ycbcr.split()
        
        print("\nChannel statistics:")
        for name, channel in [('Y', y), ('Cb', cb), ('Cr', cr)]:
            data = list(channel.getdata())
            print(f"  {name}: min={min(data)}, max={max(data)}, avg={sum(data)/len(data):.2f}")
            
            # Check LSB distribution
            lsb_counts = [0, 0]
            for val in data:
                lsb_counts[val & 1] += 1
            print(f"    LSB distribution: 0s={lsb_counts[0]}, 1s={lsb_counts[1]}")
    
    except Exception as e:
        print(f"Error: {e}")

def check_commented_sections():
    """Check for data in comment segments (COM = 0xFFFE)"""
    with open(IMAGE_PATH, 'rb') as f:
        data = f.read()
    
    print("\n" + "="*60)
    print("COMMENT SEGMENTS (COM)")
    print("="*60)
    
    i = 0
    found = False
    while i < len(data) - 3:
        if data[i] == 0xFF and data[i+1] == 0xFE:
            found = True
            length = struct.unpack('>H', data[i+2:i+4])[0]
            content = data[i+4:i+2+length]
            print(f"COM segment at {i}: length={length}")
            print(f"  Content: {content[:100]}")
            print(f"  As text: {content[:100].decode('utf-8', errors='ignore')}")
        i += 1
    
    if not found:
        print("No comment segments found")

def find_hidden_strings():
    """Search for hidden strings in JPEG"""
    with open(IMAGE_PATH, 'rb') as f:
        data = f.read()
    
    print("\n" + "="*60)
    print("HIDDEN STRING SEARCH")
    print("="*60)
    
    # Search for interesting strings
    patterns = [
        b'flag', b'key', b'password', b'secret', b'hidden',
        b'<?php', b'<?=', b'<script', b'<!--',
        b'http', b'https', b'ftp://',
        b'PK\x03\x04',  # ZIP signature
        b'%PDF', b'<?xml',
    ]
    
    for pattern in patterns:
        pos = data.find(pattern)
        if pos != -1:
            print(f"Found '{pattern}' at position {pos}")
            context = data[max(0, pos-50):min(len(data), pos+100)]
            print(f"  Context: {context}")

if __name__ == "__main__":
    analyze_jpeg_structure()
    extract_dct_coefficients()
    check_commented_sections()
    find_hidden_strings()
