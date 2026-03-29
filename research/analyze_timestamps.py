#!/usr/bin/env python3
"""
Phase 7.2: File Timestamp Analysis
Check file modification times for patterns
"""

import os
from datetime import datetime

RESEARCH_DIR = "research"
IMAGE_PATH = "images/haian_mit_text_skaliert_rand.jpeg"
HTML_PATH = "haian.de.html"

def analyze_timestamps():
    """Analyze file timestamps for patterns"""
    print("="*70)
    print("FILE TIMESTAMP ANALYSIS (Phase 7.2)")
    print("="*70)
    
    files_to_check = [
        IMAGE_PATH,
        HTML_PATH,
        "README.md",
    ]
    
    # Add research directory files
    if os.path.exists(RESEARCH_DIR):
        for f in os.listdir(RESEARCH_DIR):
            if f.endswith('.py'):
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

if __name__ == "__main__":
    analyze_timestamps()
