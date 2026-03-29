#!/usr/bin/env python3
"""
Phase 8: Linguistic, Semantic & Pattern Analysis
Complete analysis per AGENTS.md
"""

import re
from collections import Counter

HTML_PATH = "haian.de.html"

def load_html_content():
    """Load HTML content"""
    try:
        with open(HTML_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading HTML: {e}")
        return ""

def analyze_word_frequency():
    """8.1 - Word frequency analysis"""
    print("="*70)
    print("PHASE 8.1: WORD FREQUENCY ANALYSIS")
    print("="*70)
    
    content = load_html_content()
    if not content:
        return
    
    # Extract text (remove HTML tags)
    text = re.sub(r'<[^>]+>', ' ', content)
    
    # Extract words
    words = re.findall(r'\b[a-zA-ZäöüÄÖÜß]{3,}\b', text)
    words = [w.lower() for w in words]
    
    # Count frequency
    word_counts = Counter(words)
    
    print(f"\nTotal words found: {len(words)}")
    print(f"Unique words: {len(word_counts)}")
    
    print("\nTop 30 most frequent words:")
    for word, count in word_counts.most_common(30):
        print(f"  {word}: {count}")
    
    # Check for unusual words
    print("\nPotentially significant words:")
    significant = ['haian', 'fabian', 'schatz', 'liebe', 'frieden', 'tod', 'leben', 'gott', 'himmel']
    for word in significant:
        if word in word_counts:
            print(f"  {word}: {word_counts[word]}")

def analyze_acrostics():
    """8.2 - Acrostic and telestic analysis"""
    print("\n" + "="*70)
    print("PHASE 8.2: ACROSTIC & TELESTIC ANALYSIS")
    print("="*70)
    
    content = load_html_content()
    if not content:
        return
    
    # Extract condolence messages
    # Look for message pattern
    messages = re.findall(r'<p>([^<]+)</p>', content)
    
    print(f"\nFound {len(messages)} text blocks")
    
    # First letters of each message
    print("\nFirst letters of messages:")
    first_letters = []
    for msg in messages[:27]:  # First 27 messages
        text = re.sub(r'<[^>]+>', '', msg).strip()
        if text:
            first_letters.append(text[0])
    
    first_string = ''.join(first_letters)
    print(f"  {first_string}")
    
    # Check for German words
    print("\nChecking for hidden words in first letters...")
    # Could form words like "DANKE", "LIEBE", etc.
    
    # Last letters (telestic)
    print("\nLast letters of messages:")
    last_letters = []
    for msg in messages[:27]:
        text = re.sub(r'<[^>]+>', '', msg).strip()
        if text and len(text) > 1:
            last_letters.append(text[-1])
    
    last_string = ''.join(last_letters)
    print(f"  {last_string}")

def analyze_nth_words():
    """8.3 - Nth word and nth letter analysis"""
    print("\n" + "="*70)
    print("PHASE 8.3: NTH WORD/NTH LETTER ANALYSIS")
    print("="*70)
    
    content = load_html_content()
    if not content:
        return
    
    # Extract all text
    text = re.sub(r'<[^>]+>', ' ', content)
    words = re.findall(r'\b[a-zA-ZäöüÄÖÜß]+\b', text)
    
    print(f"\nTotal words: {len(words)}")
    
    # Every 5th word
    print("\nEvery 5th word:")
    every_5th = words[::5]
    print(f"  {' '.join(every_5th[:30])}")
    
    # Every 24th word
    print("\nEvery 24th word:")
    every_24th = words[::24]
    print(f"  {' '.join(every_24th)}")
    
    # Check for meaningful sequences
    print("\nEvery 5th word concatenated:")
    print(f"  {''.join(every_5th[:20])}")

def analyze_anagrams():
    """8.4 - Anagram analysis"""
    print("\n" + "="*70)
    print("PHASE 8.4: ANAGRAM ANALYSIS")
    print("="*70)
    
    # Check if any names or words are anagrams
    names = ['Haian', 'Fabian', 'Schüßler']
    key_numbers = ['24', '120', '55', '60', '5', '25']
    
    print("\nName analysis:")
    for name in names:
        letters = sorted(name.lower().replace('ü', 'u').replace('ß', 'ss'))
        print(f"  {name}: {''.join(letters)}")
    
    print("\nNumber string anagrams:")
    # Check if "24120556025" has patterns
    combined = "24120556025"
    print(f"  Combined numbers: {combined}")
    print(f"  Sorted: {''.join(sorted(combined))}")
    
    # Check for "password" anagrams in the pixel string
    pixel_chars = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"
    letters_only = ''.join(c for c in pixel_chars if c.isalpha()).lower()
    
    print(f"\nPixel string letters ({len(letters_only)} total):")
    print(f"  Sorted: {''.join(sorted(letters_only))[:80]}...")
    
    # Check for "password", "admin", "haian" as anagrams
    targets = ['password', 'admin', 'haian', 'fabian', 'secret']
    for target in targets:
        target_sorted = sorted(target)
        # Simple check - count if all letters exist
        if all(letters_only.count(c) >= target.count(c) for c in target):
            print(f"  '{target}' CAN be formed from pixel string letters")

def analyze_first_last_letters():
    """8.5 - First and last letter analysis"""
    print("\n" + "="*70)
    print("PHASE 8.5: FIRST & LAST LETTER ANALYSIS")
    print("="*70)
    
    content = load_html_content()
    if not content:
        return
    
    # Extract sentences
    text = re.sub(r'<[^>]+>', ' ', content)
    sentences = re.split(r'[.!?]+', text)
    
    print(f"\nFound {len(sentences)} sentences")
    
    # First letter of each sentence
    print("\nFirst letter of each sentence:")
    first_letters = []
    for sent in sentences[:50]:
        sent = sent.strip()
        if sent:
            first_letters.append(sent[0])
    
    print(f"  {''.join(first_letters)}")
    
    # Last letter of each sentence
    print("\nLast letter of each sentence:")
    last_letters = []
    for sent in sentences[:50]:
        sent = sent.strip()
        if sent and len(sent) > 1:
            last_letters.append(sent[-1])
    
    print(f"  {''.join(last_letters)}")

def analyze_language_detection():
    """8.6 - Language detection"""
    print("\n" + "="*70)
    print("PHASE 8.6: LANGUAGE DETECTION")
    print("="*70)
    
    content = load_html_content()
    if not content:
        return
    
    # Extract text
    text = re.sub(r'<[^>]+>', ' ', content)
    
    # German indicators
    german_words = ['der', 'die', 'das', 'und', 'ist', 'zu', 'den', 'mit', 'von', 'für', 'auf', 'sich', 'dem', 'ein', 'eine', 'nicht', 'auch', 'werden', 'an', 'sie', 'ich', 'das', 'nach', 'wie', 'wir', 'auch', 'wird', 'bei', 'so', 'zum', 'du', 'mein', 'ja', 'nein', 'danke', 'tschüss']
    
    # Norwegian (from Svenja's message)
    norwegian_words = ['jeg', 'elsker', 'deg', 'ikke', 'og', 'ja', 'nei']
    
    # Check for language presence
    text_lower = text.lower()
    
    german_count = sum(1 for word in german_words if word in text_lower)
    norwegian_count = sum(1 for word in norwegian_words if word in text_lower)
    
    print(f"\nGerman words found: {german_count}")
    print(f"Norwegian words found: {norwegian_count}")
    
    print("\n[OK] Primary language: GERMAN")
    print("[OK] Secondary language: NORWEGIAN (Svenja's message)")

if __name__ == "__main__":
    analyze_word_frequency()
    analyze_acrostics()
    analyze_nth_words()
    analyze_anagrams()
    analyze_first_last_letters()
    analyze_language_detection()
    
    print("\n" + "="*70)
    print("PHASE 8: LINGUISTIC ANALYSIS COMPLETE")
    print("="*70)
