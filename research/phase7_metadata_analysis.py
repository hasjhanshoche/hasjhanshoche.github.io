#!/usr/bin/env python3
"""
Phase 7: Metadata, Timestamps & Binary Forensics
Complete analysis per AGENTS.md
"""

import os
from datetime import datetime
from PIL import Image
import struct

RESEARCH_DIR = "research"
IMAGE_PATH = "images/haian_mit_text_skaliert_rand.jpeg"
HTML_PATH = "haian.de.html"

def analyze_file_timestamps():
    """7.2 - Analyze file timestamps for patterns"""
    print("="*70)
    print("PHASE 7.2: FILE TIMESTAMP ANALYSIS")
    print("="*70)
    
    files_to_check = [
        IMAGE_PATH,
        HTML_PATH,
        "README.md",
    ]
    
    # Add research directory files
    if os.path.exists(RESEARCH_DIR):
        for f in os.listdir(RESEARCH_DIR):
            if f.endswith('.py') or f.endswith('.md'):
                files_to_check.append(os.path.join(RESEARCH_DIR, f))
    
    print("\nFile Timestamps:")
    print("-"*70)
    print(f"{'File':<40} {'Size (bytes)':<15} {'Modified':<20}")
    print("-"*70)
    
    timestamps = []
    
    for filepath in files_to_check:
        if os.path.exists(filepath):
            try:
                stat = os.stat(filepath)
                size = stat.st_size
                mtime = datetime.fromtimestamp(stat.st_mtime)
                mtime_str = mtime.strftime('%Y-%m-%d %H:%M:%S')
                
                print(f"{filepath:<40} {size:<15} {mtime_str:<20}")
                timestamps.append((filepath, size, mtime))
            except Exception as e:
                print(f"{filepath:<40} ERROR: {e}")
    
    # Analyze image file specifically
    print("\n" + "="*70)
    print("MEMORIAL IMAGE FILE ANALYSIS")
    print("="*70)
    
    if os.path.exists(IMAGE_PATH):
        stat = os.stat(IMAGE_PATH)
        print(f"\nFile: {IMAGE_PATH}")
        print(f"Size: {stat.st_size} bytes")
        print(f"Created: {datetime.fromtimestamp(stat.st_ctime)}")
        print(f"Modified: {datetime.fromtimestamp(stat.st_mtime)}")
        print(f"Accessed: {datetime.fromtimestamp(stat.st_atime)}")
        
        # Check if size has significance
        size = stat.st_size
        print(f"\nSize Analysis ({size}):")
        print(f"  In hex: {hex(size)}")
        print(f"  Modulo 256: {size % 256}")
        if 32 <= size % 256 <= 126:
            print(f"  Mod 256 as ASCII: '{chr(size % 256)}'")
        
        # Check for common encoding patterns in size
        print(f"  Divisible by 5: {size % 5 == 0}")
        print(f"  Divisible by 24: {size % 24 == 0}")
        print(f"  Divisible by 120: {size % 120 == 0}")
        print(f"  Divisible by 55: {size % 55 == 0}")
        print(f"  Divisible by 60: {size % 60 == 0}")
    
    print("\n" + "="*70)
    print("TIMESTAMP PATTERN ANALYSIS")
    print("="*70)
    
    if len(timestamps) > 1:
        # Sort by modification time
        timestamps.sort(key=lambda x: x[2])
        
        print("\nFiles ordered by modification time:")
        for i, (path, size, mtime) in enumerate(timestamps):
            print(f"  {i+1}. {os.path.basename(path):<30} {mtime}")
        
        # Check for patterns in modification times
        print("\nTime differences between files:")
        for i in range(len(timestamps)-1):
            diff = (timestamps[i+1][2] - timestamps[i][2]).total_seconds()
            print(f"  {os.path.basename(timestamps[i][0])} -> {os.path.basename(timestamps[i+1][0])}: {diff:.0f} seconds")

def analyze_binary_strings():
    """7.3 - Extract printable strings from binary files"""
    print("\n" + "="*70)
    print("PHASE 7.3: BINARY STRINGS ANALYSIS")
    print("="*70)
    
    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found: {IMAGE_PATH}")
        return
    
    print(f"\nExtracting strings from {IMAGE_PATH}...")
    
    # Read binary file
    with open(IMAGE_PATH, 'rb') as f:
        data = f.read()
    
    # Extract printable strings (4+ chars)
    strings_found = []
    current_string = ""
    
    for byte in data:
        if 32 <= byte <= 126:  # Printable ASCII
            current_string += chr(byte)
        else:
            if len(current_string) >= 4:
                strings_found.append(current_string)
            current_string = ""
    
    # Check last string
    if len(current_string) >= 4:
        strings_found.append(current_string)
    
    print(f"\nFound {len(strings_found)} strings (4+ chars)")
    
    # Look for interesting patterns
    interesting = []
    for s in strings_found:
        # Look for keywords
        if any(keyword in s.lower() for keyword in ['password', 'pass', 'key', 'flag', 'admin', 'secret', 'haian', 'fabian', '5', '24', '120']):
            interesting.append(s)
    
    if interesting:
        print("\nPotentially interesting strings:")
        for s in interesting[:20]:
            print(f"  - {s}")
    else:
        print("\nNo obviously interesting strings found.")
    
    # Check for base64-like strings
    import re
    b64_pattern = re.compile(r'[A-Za-z0-9+/]{20,}={0,2}')
    b64_candidates = b64_pattern.findall(' '.join(strings_found))
    
    if b64_candidates:
        print(f"\nBase64-like strings found: {len(b64_candidates)}")
        for b in b64_candidates[:5]:
            print(f"  - {b[:50]}")

def analyze_trailing_data():
    """7.4 - Check for trailing data after image"""
    print("\n" + "="*70)
    print("PHASE 7.4: TRAILING DATA ANALYSIS")
    print("="*70)
    
    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found: {IMAGE_PATH}")
        return
    
    # Read image
    with open(IMAGE_PATH, 'rb') as f:
        data = f.read()
    
    # JPEG ends with FFD9
    if data[:2] == b'\xff\xd8':  # JPEG start
        # Find JPEG end marker
        end_marker = data.rfind(b'\xff\xd9')
        if end_marker != -1:
            end_pos = end_marker + 2
            trailing = data[end_pos:]
            
            print(f"\nJPEG ends at position: {end_pos}")
            print(f"File size: {len(data)}")
            print(f"Trailing data: {len(trailing)} bytes")
            
            if trailing:
                print(f"\nTrailing data (hex): {trailing[:100].hex()}")
                print(f"Trailing data (ascii): {trailing[:100]}")
                
                # Check if trailing data is meaningful
                printable = all(32 <= b <= 126 or b in (9, 10, 13) for b in trailing[:50])
                print(f"\nIs printable: {printable}")
            else:
                print("\nNo trailing data found - image is clean.")

def check_icc_profile():
    """7.5 - Check ICC color profile data"""
    print("\n" + "="*70)
    print("PHASE 7.5: ICC COLOR PROFILE ANALYSIS")
    print("="*70)
    
    try:
        img = Image.open(IMAGE_PATH)
        
        print(f"\nImage mode: {img.mode}")
        print(f"Image format: {img.format}")
        print(f"Image size: {img.size}")
        
        # Check for ICC profile
        if 'icc_profile' in img.info:
            icc = img.info['icc_profile']
            print(f"\nICC Profile present: {len(icc)} bytes")
            print(f"ICC Profile (hex): {icc[:50].hex()}")
            
            # Check for embedded data
            if len(icc) > 1000:  # Suspiciously large
                print("\n⚠️  ICC profile unusually large - may contain hidden data!")
        else:
            print("\nNo ICC profile found.")
        
        # Check other metadata
        print("\nImage info:")
        for key, value in img.info.items():
            if key != 'icc_profile':
                print(f"  {key}: {value}")
                
    except Exception as e:
        print(f"Error analyzing image: {e}")

def check_jpeg_structure():
    """7.6 - Deep JPEG structure analysis"""
    print("\n" + "="*70)
    print("PHASE 7.6: JPEG STRUCTURE ANALYSIS")
    print("="*70)
    
    if not os.path.exists(IMAGE_PATH):
        return
    
    with open(IMAGE_PATH, 'rb') as f:
        data = f.read()
    
    print(f"\nFile size: {len(data)} bytes")
    
    # Find all JPEG markers
    markers = []
    i = 0
    while i < len(data) - 1:
        if data[i] == 0xFF and data[i+1] != 0x00 and data[i+1] != 0xFF:
            marker = data[i+1]
            markers.append((i, marker))
            i += 2
        else:
            i += 1
    
    print(f"\nFound {len(markers)} JPEG markers")
    print("\nMarker positions:")
    
    marker_names = {
        0xD8: 'SOI (Start of Image)',
        0xD9: 'EOI (End of Image)',
        0xE0: 'APP0 (JFIF)',
        0xE1: 'APP1 (EXIF/XMP)',
        0xE2: 'APP2',
        0xED: 'APP13 (Photoshop)',
        0xEE: 'APP14 (Adobe)',
        0xFE: 'COM (Comment)',
        0xDB: 'DQT (Define Quantization Table)',
        0xC0: 'SOF0 (Start of Frame)',
        0xC4: 'DHT (Define Huffman Table)',
        0xDA: 'SOS (Start of Scan)',
    }
    
    for pos, marker in markers[:20]:  # Show first 20
        name = marker_names.get(marker, f'0x{marker:02X}')
        print(f"  Position {pos:8d}: {name}")
    
    # Check for COM (comment) markers
    com_markers = [m for m in markers if m[1] == 0xFE]
    if com_markers:
        print(f"\n⚠️  Found {len(com_markers)} COMMENT markers - potential hidden data!")
        for pos, _ in com_markers:
            # Read comment length
            length = struct.unpack('>H', data[pos+2:pos+4])[0]
            comment = data[pos+4:pos+2+length]
            print(f"  Comment at {pos}: {comment[:50]}")

if __name__ == "__main__":
    analyze_file_timestamps()
    analyze_binary_strings()
    analyze_trailing_data()
    check_icc_profile()
    check_jpeg_structure()
    
    print("\n" + "="*70)
    print("PHASE 7: METADATA ANALYSIS COMPLETE")
    print("="*70)
