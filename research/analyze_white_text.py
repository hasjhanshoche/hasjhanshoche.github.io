#!/usr/bin/env python3
"""
Analyze lines and columns overflown by white text in the memorial image
The white text (birth/death dates) appears as high-brightness pixels
Uses only PIL (no numpy required)
"""

from PIL import Image

IMAGE_PATH = "images/haian_mit_text_skaliert_rand.jpeg"

def analyze_white_text_regions():
    """Identify and analyze regions with white text"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("="*70)
    print("WHITE TEXT REGION ANALYSIS")
    print("="*70)
    print(f"Image dimensions: {width}x{height}")
    
    # White text appears as high brightness pixels (close to 255)
    # Find rows and columns with high brightness values
    
    # Threshold for "white" - text is typically 200-255 in grayscale
    white_threshold = 200
    
    # Find rows (lines) that contain white pixels
    white_rows = []
    for row in range(height):
        row_pixels = pixels[row*width:(row+1)*width]
        white_count = sum(1 for p in row_pixels if p > white_threshold)
        if white_count > 10:  # At least 10 white pixels to be text
            white_rows.append((row, white_count))
    
    print(f"\nRows with white pixels (>200, >10 pixels):")
    print(f"Found {len(white_rows)} rows")
    
    # Group consecutive rows into text regions
    text_regions = []
    current_region = []
    for row, count in white_rows:
        if not current_region or row == current_region[-1][0] + 1:
            current_region.append((row, count))
        else:
            if len(current_region) > 0:
                text_regions.append(current_region)
            current_region = [(row, count)]
    if current_region:
        text_regions.append(current_region)
    
    print(f"\nGrouped into {len(text_regions)} text regions:")
    for i, region in enumerate(text_regions):
        start_row = region[0][0]
        end_row = region[-1][0]
        print(f"  Region {i+1}: Rows {start_row}-{end_row} ({len(region)} lines)")
    
    return white_rows

def extract_text_line_data(white_rows):
    """Extract pixel data from lines containing white text"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\n" + "="*70)
    print("TEXT LINE PIXEL DATA EXTRACTION")
    print("="*70)
    
    white_threshold = 200
    
    print(f"Analyzing {len(white_rows)} text-heavy rows:")
    
    # Collect all X positions from white text rows
    all_x_positions = []
    all_pixel_values = []
    
    for idx, (row, count) in enumerate(white_rows[:30]):  # First 30 text rows
        row_data = pixels[row*width:(row+1)*width]
        
        # Get positions of white pixels
        white_positions = [i for i, p in enumerate(row_data) if p > white_threshold]
        white_values = [p for p in row_data if p > white_threshold]
        
        all_x_positions.extend(white_positions)
        all_pixel_values.extend(white_values)
        
        if white_positions:
            # Check if positions map to ASCII
            ascii_chars = []
            for pos in white_positions:
                if 32 <= pos <= 126:
                    ascii_chars.append(chr(pos))
            
            # Check pixel values as ASCII
            pixel_ascii = []
            for val in white_values:
                if 32 <= val <= 126:
                    pixel_ascii.append(chr(val))
            
            if len(ascii_chars) > 0 or len(pixel_ascii) > 0:
                print(f"\nRow {row}:")
                if ascii_chars:
                    print(f"  X positions (ASCII): {''.join(ascii_chars[:40])}")
                if pixel_ascii:
                    print(f"  Pixel values (ASCII): {''.join(pixel_ascii[:40])}")
    
    return all_x_positions, all_pixel_values

def analyze_text_columns():
    """Analyze columns that contain white text pixels"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\n" + "="*70)
    print("TEXT COLUMN ANALYSIS")
    print("="*70)
    
    white_threshold = 200
    
    # Find columns with white pixels
    text_columns = []
    for col in range(width):
        col_pixels = [pixels[row*width + col] for row in range(height)]
        white_count = sum(1 for p in col_pixels if p > white_threshold)
        if white_count > 5:  # Some white pixels in this column
            text_columns.append((col, white_count))
    
    print(f"Found {len(text_columns)} columns with white pixels")
    
    # Group into regions
    col_regions = []
    current = []
    for col, count in text_columns:
        if not current or col == current[-1][0] + 1:
            current.append((col, count))
        else:
            if len(current) > 0:
                col_regions.append(current)
            current = [(col, count)]
    if current:
        col_regions.append(current)
    
    print(f"Grouped into {len(col_regions)} column regions:")
    for i, region in enumerate(col_regions[:15]):  # Show first 15
        start = region[0][0]
        end = region[-1][0]
        print(f"  Region {i+1}: Columns {start}-{end} ({end-start+1} cols)")
    
    return text_columns

def extract_text_coordinates(white_rows):
    """Extract coordinates where white text appears and check for encoding"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\n" + "="*70)
    print("WHITE TEXT COORDINATE ENCODING")
    print("="*70)
    
    white_threshold = 200
    
    # Get all coordinates of white pixels from text rows
    white_coords = []
    for row, count in white_rows:
        row_data = pixels[row*width:(row+1)*width]
        for col, val in enumerate(row_data):
            if val > white_threshold:
                white_coords.append((col, row))  # (x, y)
    
    print(f"Total white pixels in text rows: {len(white_coords)}")
    
    # Check if X coordinates (columns) encode ASCII
    x_coords = [x for x, y in white_coords]
    x_ascii = [chr(x) for x in x_coords if 32 <= x <= 126]
    
    # Check if Y coordinates (rows) encode ASCII  
    y_coords = [y for x, y in white_coords]
    y_ascii = [chr(y) for x, y in white_coords if 32 <= y <= 126]
    
    print(f"\nX coordinates as ASCII ({len(x_ascii)} chars):")
    print(''.join(x_ascii[:150]))
    
    print(f"\nY coordinates as ASCII ({len(y_ascii)} chars):")
    print(''.join(y_ascii[:150]))
    
    return white_coords

def analyze_text_specific_values(all_pixel_values):
    """Analyze specific pixel values in white text regions"""
    
    print("\n" + "="*70)
    print("WHITE TEXT PIXEL VALUE ANALYSIS")
    print("="*70)
    
    print(f"Total white pixel values collected: {len(all_pixel_values)}")
    
    # Check for specific values
    unique_values = sorted(set(all_pixel_values))
    print(f"\nUnique white pixel values ({len(unique_values)}):")
    print(unique_values[:50])  # First 50
    
    # Check if any map to our target numbers
    target_nums = [5, 24, 55, 60, 120, 25, 52, 100]
    print(f"\nChecking for target values {target_nums}:")
    for target in target_nums:
        count = all_pixel_values.count(target)
        if count > 0:
            print(f"  Value {target}: {count} occurrences")
    
    # Check ASCII mapping of white values
    ascii_from_values = [chr(int(v)) for v in all_pixel_values if 32 <= v <= 126]
    print(f"\nWhite values as ASCII ({len(ascii_from_values)} chars):")
    print(''.join(ascii_from_values[:100]))

def analyze_text_rows_deep(white_rows):
    """Deep analysis of text rows - check for hidden messages"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\n" + "="*70)
    print("DEEP TEXT ROW ANALYSIS")
    print("="*70)
    
    white_threshold = 200
    
    # Get all X positions from white text rows
    all_x_positions = []
    for row, count in white_rows:
        row_data = pixels[row*width:(row+1)*width]
        white_positions = [i for i, p in enumerate(row_data) if p > white_threshold]
        all_x_positions.extend(white_positions)
    
    print(f"Collected {len(all_x_positions)} X positions from white text")
    
    # Check for patterns in X positions
    # Try every nth position
    for n in [2, 3, 4, 5, 6, 7, 8]:
        nth_positions = all_x_positions[::n]
        nth_ascii = [chr(x) for x in nth_positions if 32 <= x <= 126]
        if len(nth_ascii) > 5:
            print(f"\nEvery {n}th X position as ASCII: {''.join(nth_ascii[:50])}")
    
    # Check differences between consecutive positions
    diffs = [all_x_positions[i+1] - all_x_positions[i] for i in range(len(all_x_positions)-1)]
    diff_ascii = [chr(d + 64) if 32 <= (d + 64) <= 126 else '?' for d in diffs if d < 64]
    if diff_ascii:
        print(f"\nDifferences as ASCII: {''.join(diff_ascii[:50])}")

if __name__ == "__main__":
    white_rows = analyze_white_text_regions()
    x_positions, pixel_values = extract_text_line_data(white_rows)
    text_columns = analyze_text_columns()
    white_coords = extract_text_coordinates(white_rows)
    analyze_text_specific_values(pixel_values)
    analyze_text_rows_deep(white_rows)
