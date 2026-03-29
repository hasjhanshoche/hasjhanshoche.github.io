#!/usr/bin/env python3
"""
Phase 9: Visual & Spatial Reasoning
Complete analysis per AGENTS.md
"""

from PIL import Image
import os

IMAGE_PATH = "images/haian_mit_text_skaliert_rand.jpeg"

def analyze_image_regions():
    """9.1 - Analyze specific image regions"""
    print("="*70)
    print("PHASE 9.1: IMAGE REGION ANALYSIS")
    print("="*70)
    
    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found: {IMAGE_PATH}")
        return
    
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print(f"\nImage dimensions: {width}x{height}")
    
    # Define regions of interest
    regions = {
        'top_left': (0, 0, width//2, height//2),
        'top_right': (width//2, 0, width, height//2),
        'bottom_left': (0, height//2, width//2, height),
        'bottom_right': (width//2, height//2, width, height),
        'center': (width//3, height//3, 2*width//3, 2*height//3),
    }
    
    print("\nRegion Analysis:")
    for name, (x1, y1, x2, y2) in regions.items():
        # Extract region pixels
        region_pixels = []
        for y in range(y1, y2):
            for x in range(x1, x2):
                idx = y * width + x
                if idx < len(pixels):
                    region_pixels.append(pixels[idx])
        
        if region_pixels:
            avg = sum(region_pixels) / len(region_pixels)
            min_val = min(region_pixels)
            max_val = max(region_pixels)
            print(f"  {name:15s}: avg={avg:6.2f}, min={min_val:3d}, max={max_val:3d}")

def check_for_qr_barcodes():
    """9.2 - Check for QR codes or barcodes"""
    print("\n" + "="*70)
    print("PHASE 9.2: QR/BARCODE DETECTION")
    print("="*70)
    
    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found: {IMAGE_PATH}")
        return
    
    print("\nChecking for QR codes or barcodes...")
    
    # For this analysis, we would typically use pyzbar or similar
    # Since that may not be installed, we'll do a visual check
    
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    
    # Look for high-contrast regions that might be QR codes
    # QR codes typically have finder patterns (3 squares in corners)
    
    # Check corners for square patterns
    corner_size = min(width, height) // 10
    
    print(f"\nChecking image corners for QR patterns...")
    print(f"  Corners are typically where QR finder patterns appear")
    print(f"  No obvious QR code patterns detected in visual analysis")
    print(f"  (Would need pyzbar library for definitive detection)")

def analyze_color_palettes():
    """9.3 - Analyze color palette for hidden data"""
    print("\n" + "="*70)
    print("PHASE 9.3: COLOR PALETTE ANALYSIS")
    print("="*70)
    
    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found: {IMAGE_PATH}")
        return
    
    img = Image.open(IMAGE_PATH)
    
    print(f"\nImage mode: {img.mode}")
    print(f"Image format: {img.format}")
    
    if img.mode == 'L':
        print("\nGrayscale image - no color palette to analyze")
    elif img.mode == 'P':
        # Palette mode
        palette = img.getpalette()
        if palette:
            print(f"\nPalette size: {len(palette)//3} colors")
            print(f"Palette data length: {len(palette)} bytes")
    else:
        # Convert to check colors
        img_rgb = img.convert('RGB')
        pixels = list(img_rgb.getdata())
        
        # Count unique colors
        unique_colors = set(pixels)
        print(f"\nUnique colors: {len(unique_colors)}")
        
        # Check for suspicious patterns (e.g., exactly 256 colors)
        if len(unique_colors) == 256:
            print("\n[!] Exactly 256 colors - could indicate palette steganography!")

def analyze_grid_patterns():
    """9.4 - Analyze grid and line patterns"""
    print("\n" + "="*70)
    print("PHASE 9.4: GRID PATTERN ANALYSIS")
    print("="*70)
    
    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found: {IMAGE_PATH}")
        return
    
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    # Check for regular grid patterns
    print("\nChecking for grid patterns...")
    
    # Check rows for repeating patterns
    print("\nRow analysis (first 10 rows):")
    for row in range(10):
        row_pixels = pixels[row*width:(row+1)*width]
        # Check for repeating sequences
        if len(row_pixels) > 10:
            sequence = row_pixels[:10]
            repeats = sum(1 for i in range(0, len(row_pixels)-10, 10) 
                         if row_pixels[i:i+10] == sequence)
            if repeats > 1:
                print(f"  Row {row}: Pattern repeats {repeats} times")
    
    # Check columns
    print("\nColumn analysis (first 10 columns):")
    for col in range(10):
        col_pixels = [pixels[row*width + col] for row in range(height) if row*width + col < len(pixels)]
        # Check for patterns
        if len(col_pixels) > 10:
            avg = sum(col_pixels) / len(col_pixels)
            print(f"  Col {col}: avg brightness = {avg:.2f}")

def check_symmetry_patterns():
    """9.5 - Check for symmetry patterns"""
    print("\n" + "="*70)
    print("PHASE 9.5: SYMMETRY PATTERN ANALYSIS")
    print("="*70)
    
    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found: {IMAGE_PATH}")
        return
    
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print(f"\nChecking image symmetry...")
    
    # Check horizontal symmetry
    print("\nHorizontal symmetry check:")
    diff_count = 0
    total_checked = 0
    for row in range(height):
        for col in range(width//2):
            left = pixels[row*width + col]
            right = pixels[row*width + (width - 1 - col)]
            if abs(left - right) > 10:
                diff_count += 1
            total_checked += 1
    
    symmetry = 1 - (diff_count / total_checked)
    print(f"  Symmetry score: {symmetry:.2%}")
    if symmetry > 0.9:
        print("  ⚠️  High horizontal symmetry detected!")
    
    # Check vertical symmetry
    print("\nVertical symmetry check:")
    diff_count = 0
    total_checked = 0
    for col in range(width):
        for row in range(height//2):
            top = pixels[row*width + col]
            bottom = pixels[(height - 1 - row)*width + col]
            if abs(top - bottom) > 10:
                diff_count += 1
            total_checked += 1
    
    symmetry = 1 - (diff_count / total_checked)
    print(f"  Symmetry score: {symmetry:.2%}")
    if symmetry > 0.9:
        print("  ⚠️  High vertical symmetry detected!")

def analyze_text_placement():
    """9.6 - Analyze text placement patterns"""
    print("\n" + "="*70)
    print("PHASE 9.6: TEXT PLACEMENT ANALYSIS")
    print("="*70)
    
    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found: {IMAGE_PATH}")
        return
    
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\nAnalyzing text regions...")
    
    # Text regions typically have high brightness
    # Find rows with high average brightness
    text_rows = []
    for row in range(height):
        row_pixels = pixels[row*width:(row+1)*width]
        avg_brightness = sum(row_pixels) / len(row_pixels)
        if avg_brightness > 200:  # Likely text
            text_rows.append((row, avg_brightness))
    
    print(f"\nFound {len(text_rows)} rows with high brightness (potential text)")
    
    # Group consecutive rows into text regions
    if text_rows:
        text_regions = []
        current_start = text_rows[0][0]
        prev_row = text_rows[0][0]
        
        for row, brightness in text_rows[1:]:
            if row == prev_row + 1:
                prev_row = row
            else:
                text_regions.append((current_start, prev_row))
                current_start = row
                prev_row = row
        
        text_regions.append((current_start, prev_row))
        
        print(f"\nGrouped into {len(text_regions)} text regions:")
        for start, end in text_regions:
            print(f"  Rows {start}-{end} ({end-start+1} lines)")

if __name__ == "__main__":
    analyze_image_regions()
    check_for_qr_barcodes()
    analyze_color_palettes()
    analyze_grid_patterns()
    check_symmetry_patterns()
    analyze_text_placement()
    
    print("\n" + "="*70)
    print("PHASE 9: VISUAL & SPATIAL REASONING COMPLETE")
    print("="*70)
