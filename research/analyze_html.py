#!/usr/bin/env python3
"""
HTML source analysis for hidden data, comments, and encoding
"""

import re
import html

def analyze_html_file(filepath):
    """Analyze HTML for hidden patterns"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=" * 60)
    print("HTML SOURCE ANALYSIS")
    print("=" * 60)
    
    # 1. Find HTML comments
    print("\n1. HTML COMMENTS:")
    comments = re.findall(r'<!--(.*?)-->', content, re.DOTALL)
    for i, comment in enumerate(comments):
        print(f"\nComment {i+1}:")
        print(f"  Content: {comment[:200]}...")
        print(f"  Length: {len(comment)} chars")
        
        # Check for hidden content in comment
        if len(comment) > 50:
            print(f"  *** LONG COMMENT - CHECKING FOR HIDDEN DATA ***")
    
    # 2. Check for zero-width characters
    print("\n2. ZERO-WIDTH / INVISIBLE CHARACTERS:")
    zw_chars = {
        '\u200B': 'ZERO WIDTH SPACE',
        '\u200C': 'ZERO WIDTH NON-JOINER',
        '\u200D': 'ZERO WIDTH JOINER',
        '\uFEFF': 'ZERO WIDTH NO-BREAK SPACE (BOM)',
        '\u2060': 'WORD JOINER',
        '\u00AD': 'SOFT HYPHEN',
    }
    
    found_zw = False
    for char, name in zw_chars.items():
        count = content.count(char)
        if count > 0:
            print(f"  Found {count} x {name} (U+{ord(char):04X})")
            found_zw = True
    
    if not found_zw:
        print("  No zero-width characters found")
    
    # 3. Check for unusual whitespace (multiple spaces, tabs)
    print("\n3. WHITESPACE PATTERNS:")
    double_spaces = len(re.findall(r'  ', content))
    triple_spaces = len(re.findall(r'   ', content))
    tabs = content.count('\t')
    
    print(f"  Double spaces: {double_spaces}")
    print(f"  Triple spaces: {triple_spaces}")
    print(f"  Tabs: {tabs}")
    
    # 4. Look for encoded strings
    print("\n4. ENCODED STRING PATTERNS:")
    
    # Base64 patterns
    base64_pattern = r'[A-Za-z0-9+/]{40,}={0,2}'
    base64_matches = re.findall(base64_pattern, content)
    if base64_matches:
        print(f"  Potential Base64 strings: {len(base64_matches)}")
        for m in base64_matches[:5]:
            print(f"    {m[:60]}...")
    else:
        print("  No obvious Base64 patterns")
    
    # Hex patterns
    hex_pattern = r'[0-9a-fA-F]{16,}'
    hex_matches = re.findall(hex_pattern, content)
    if hex_matches:
        print(f"  Potential hex strings: {len(hex_matches)}")
        for m in hex_matches[:5]:
            print(f"    {m}")
    else:
        print("  No obvious hex patterns")
    
    # 5. Check color values for hidden data
    print("\n5. COLOR VALUES ANALYSIS:")
    color_pattern = r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}'
    colors = re.findall(color_pattern, content)
    print(f"  Found {len(colors)} color values: {colors}")
    
    # Convert to RGB and check for patterns
    for color in colors[:10]:
        if len(color) == 7:  # #RRGGBB
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            # Check if values map to ASCII
            chars = []
            for val in [r, g, b]:
                if 32 <= val <= 126:
                    chars.append(chr(val))
                else:
                    chars.append('?')
            print(f"    {color} -> RGB({r},{g},{b}) -> ASCII: {''.join(chars)}")
    
    # 6. Check for hidden URLs or paths
    print("\n6. URL/PATH EXTRACTION:")
    url_pattern = r'(href|src)="([^"]+)"'
    urls = re.findall(url_pattern, content)
    for attr, url in urls:
        print(f"  {attr}={url}")
    
    # 7. Analyze text content between tags
    print("\n7. TEXT CONTENT ANALYSIS:")
    text_pattern = r'>([^<]{10,})<'
    texts = re.findall(text_pattern, content)
    
    # Check for steganography in text (trailing spaces, etc.)
    trailing_spaces = 0
    leading_spaces = 0
    for text in texts:
        if text.endswith(' '):
            trailing_spaces += 1
        if text.startswith(' '):
            leading_spaces += 1
    
    print(f"  Elements with trailing spaces: {trailing_spaces}")
    print(f"  Elements with leading spaces: {leading_spaces}")
    
    # 8. Check for binary data or non-printable chars
    print("\n8. NON-PRINTABLE CHARACTER CHECK:")
    non_printable = []
    for i, char in enumerate(content):
        if ord(char) < 32 and char not in '\n\r\t':
            non_printable.append((i, ord(char)))
    
    if non_printable:
        print(f"  Found {len(non_printable)} non-printable characters")
        for pos, code in non_printable[:10]:
            print(f"    Position {pos}: 0x{code:02X}")
    else:
        print("  No non-printable characters found")
    
    # 9. Save clean text
    print("\n9. SAVING CLEAN TEXT:")
    # Remove HTML tags
    clean_text = re.sub(r'<[^>]+>', ' ', content)
    # Normalize whitespace
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    with open('research/00_target/page_text.txt', 'w', encoding='utf-8') as f:
        f.write(clean_text)
    print("  Clean text saved to research/00_target/page_text.txt")

if __name__ == "__main__":
    analyze_html_file('research/00_target/page_source.html')
    print("\n" + "=" * 60)
    print("HTML analysis complete")
    print("=" * 60)
