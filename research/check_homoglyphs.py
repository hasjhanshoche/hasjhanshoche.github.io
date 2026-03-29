#!/usr/bin/env python3
"""
Phase 4.3: Homoglyph Substitution Analysis
Check for characters that look like ASCII but are different Unicode codepoints
"""

import unicodedata

# Read the haian.de.html file
HTML_PATH = "haian.de.html"

def analyze_homoglyphs():
    """Check for Cyrillic/Homoglyph substitutions in text"""
    print("="*70)
    print("HOMOGLYPH SUBSTITUTION ANALYSIS (Phase 4.3)")
    print("="*70)
    
    try:
        with open(HTML_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Known homoglyph mappings
    homoglyphs = {
        'а': ('a', 'CYRILLIC SMALL LETTER A'),
        'е': ('e', 'CYRILLIC SMALL LETTER IE'),
        'о': ('o', 'CYRILLIC SMALL LETTER O'),
        'с': ('c', 'CYRILLIC SMALL LETTER ES'),
        'р': ('p', 'CYRILLIC SMALL LETTER ER'),
        'х': ('x', 'CYRILLIC SMALL LETTER HA'),
        'А': ('A', 'CYRILLIC CAPITAL LETTER A'),
        'Е': ('E', 'CYRILLIC CAPITAL LETTER IE'),
        'О': ('O', 'CYRILLIC CAPITAL LETTER O'),
        'С': ('C', 'CYRILLIC CAPITAL LETTER ES'),
        'Р': ('P', 'CYRILLIC CAPITAL LETTER ER'),
        'Η': ('H', 'GREEK CAPITAL LETTER ETA'),
        'ο': ('o', 'GREEK SMALL LETTER OMICRON'),
    }
    
    found_homoglyphs = []
    
    for i, char in enumerate(content):
        if char in homoglyphs:
            latin_equiv, unicode_name = homoglyphs[char]
            found_homoglyphs.append({
                'position': i,
                'char': char,
                'looks_like': latin_equiv,
                'unicode': f"U+{ord(char):04X}",
                'name': unicode_name
            })
    
    print(f"\nFile: {HTML_PATH}")
    print(f"Total characters: {len(content)}")
    
    if found_homoglyphs:
        print("\n*** FOUND " + str(len(found_homoglyphs)) + " HOMOGLYPHS ***")
        print("\nPosition | Char | Looks Like | Unicode  | Unicode Name")
        print("-"*70)
        for h in found_homoglyphs[:20]:  # Show first 20
            print(f"{h['position']:8d} | {h['char']:4s} | {h['looks_like']:10s} | {h['unicode']:8s} | {h['name']}")
        
        # Extract message from homoglyphs
        message = ''.join(h['looks_like'] for h in found_homoglyphs)
        print(f"\n\nMessage from homoglyphs: {message}")
    else:
        print("\n[OK] No homoglyph substitutions found")
        print("  All characters are standard Latin/ASCII")
    
    # Also check for other non-ASCII characters
    print("\n" + "="*70)
    print("NON-ASCII CHARACTER INVENTORY")
    print("="*70)
    
    non_ascii = []
    for i, char in enumerate(content):
        codepoint = ord(char)
        if codepoint > 127:
            try:
                name = unicodedata.name(char, 'UNKNOWN')
                category = unicodedata.category(char)
                non_ascii.append({
                    'pos': i,
                    'char': char,
                    'codepoint': f"U+{codepoint:04X}",
                    'name': name,
                    'category': category
                })
            except:
                pass
    
    if non_ascii:
        print(f"\nFound {len(non_ascii)} non-ASCII characters:")
        print("\nPosition | Char | Codepoint | Category | Name")
        print("-"*70)
        seen = set()
        for item in non_ascii[:30]:  # Show first 30 unique
            key = (item['char'], item['codepoint'])
            if key not in seen:
                seen.add(key)
                print(f"{item['pos']:8d} | {item['char']:4s} | {item['codepoint']:9s} | {item['category']:8s} | {item['name']}")
        
        if len(non_ascii) > 30:
            print(f"\n... and {len(non_ascii) - 30} more")
    else:
        print("\n[OK] No non-ASCII characters found")

if __name__ == "__main__":
    analyze_homoglyphs()
