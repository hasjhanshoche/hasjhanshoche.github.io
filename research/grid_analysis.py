#!/usr/bin/env python3
"""
GRID READING ANALYSIS - Find password in column patterns
"""

PIXEL5 = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"

def analyze_grid_readings():
    """Try different grid reading patterns"""
    print("="*70)
    print("GRID READING ANALYSIS")
    print("="*70)
    
    # 5 rows × 23 columns
    rows_5 = [PIXEL5[i*23:(i+1)*23] for i in range(5)]
    
    print("\nReading COLUMNS in different patterns:")
    print("-"*70)
    
    # Read columns left-to-right
    cols_lr = [''.join(rows_5[r][c] for r in range(5)) for c in range(23)]
    print("\nColumns left-to-right:")
    for i, col in enumerate(cols_lr):
        alpha = sum(1 for c in col if c.isalpha())
        if alpha >= 3:
            print(f"  Col {i+1:2d}: {col} ({alpha}/5 letters)")
    
    # Read columns right-to-left
    print("\nColumns right-to-left:")
    for i in range(22, -1, -1):
        col = cols_lr[i]
        alpha = sum(1 for c in col if c.isalpha())
        if alpha >= 3:
            print(f"  Col {i+1:2d}: {col} ({alpha}/5 letters)")
    
    # Read in zigzag pattern
    print("\nZigzag column reading:")
    zigzag = []
    for i in range(23):
        if i % 2 == 0:
            col = ''.join(rows_5[r][i] for r in range(5))
        else:
            col = ''.join(rows_5[r][i] for r in range(4, -1, -1))
        zigzag.append(col)
        print(f"  {col}")
    
    # Concatenate high-letter columns
    print("\n" + "-"*70)
    print("HIGH-LETTER COLUMNS CONCATENATED:")
    print("-"*70)
    
    high_letter_cols = []
    for i, col in enumerate(cols_lr):
        alpha = sum(1 for c in col if c.isalpha())
        if alpha >= 4:
            high_letter_cols.append((i+1, col))
    
    print(f"\nFound {len(high_letter_cols)} columns with 4+ letters:")
    for num, col in high_letter_cols:
        print(f"  Col {num}: {col}")
    
    # Try combining them
    if high_letter_cols:
        combined = ''.join(col for _, col in high_letter_cols)
        print(f"\nCombined: {combined}")
        
        # Also try first letter of each
        first_letters = ''.join(col[0] for _, col in high_letter_cols)
        print(f"First letters: {first_letters}")
        
        # Try last letter of each
        last_letters = ''.join(col[-1] for _, col in high_letter_cols)
        print(f"Last letters: {last_letters}")

def test_column_passwords():
    """Test column-based passwords"""
    import requests
    from requests.auth import HTTPBasicAuth
    
    print("\n" + "="*70)
    print("TESTING COLUMN-BASED PASSWORDS")
    print("="*70)
    
    # Generate passwords from columns
    rows_5 = [PIXEL5[i*23:(i+1)*23] for i in range(5)]
    cols = [''.join(rows_5[r][c] for r in range(5)) for c in range(23)]
    
    passwords = []
    
    # Individual columns with high letter count
    for col in cols:
        alpha = sum(1 for c in col if c.isalpha())
        if alpha >= 4:
            passwords.append(col)
    
    # Combinations
    passwords.append('OrBiD')  # Column 2
    passwords.append('DpSzM')  # Column 14
    passwords.append('REttn')  # Column 21
    passwords.append('OrBiDREttn')
    passwords.append('OrBiDDpSzM')
    
    url = "https://haian.de/admin"
    users = ['admin', 'haian', 'fabian', '5', '']
    
    print(f"\nTesting {len(passwords)} column-based passwords...")
    
    for pwd in passwords:
        for user in users:
            try:
                r = requests.get(url, auth=HTTPBasicAuth(user, pwd), timeout=5)
                if r.status_code == 200:
                    print(f"\n[FOUND] '{user}' / '{pwd}'")
                    return (user, pwd)
            except:
                pass
    
    print("\n[*] No column passwords worked")
    return None

def spiral_reading():
    """Try spiral reading patterns"""
    print("\n" + "="*70)
    print("SPIRAL READING PATTERNS")
    print("="*70)
    
    # Arrange as 5x23 grid
    grid = []
    for i in range(5):
        row = list(PIXEL5[i*23:(i+1)*23])
        grid.append(row)
    
    # Spiral from outside in
    spiral = []
    top, bottom = 0, 4
    left, right = 0, 22
    
    while top <= bottom and left <= right:
        # Top row
        for i in range(left, right + 1):
            spiral.append(grid[top][i])
        top += 1
        
        # Right column
        for i in range(top, bottom + 1):
            spiral.append(grid[i][right])
        right -= 1
        
        # Bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral.append(grid[bottom][i])
            bottom -= 1
        
        # Left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral.append(grid[i][left])
            left += 1
    
    spiral_str = ''.join(spiral)
    print(f"\nSpiral reading: {spiral_str[:80]}...")
    
    # Check if spiral reveals words
    alpha = sum(1 for c in spiral_str if c.isalpha())
    print(f"Alpha ratio: {alpha/len(spiral_str):.2%}")

if __name__ == "__main__":
    analyze_grid_readings()
    spiral_reading()
    test_column_passwords()
