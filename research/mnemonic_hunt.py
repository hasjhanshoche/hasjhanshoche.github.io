#!/usr/bin/env python3
"""
MNEMONIC HUNT - Deep Search for Hidden Memory Aids
Look for acrostics, initialisms, first-letter patterns, and poetic structures
"""

import re

# The condolence messages from haian.de
messages = [
    {
        "author": "Ihno",
        "date": "02.11.2011 17:07",
        "text": "Dir Haian, auch wenn ich deine Leidenschaft für Poker nicht teilte, so waren jedoch die Skat-Abende mit dir umso schöner..."
    },
    {
        "author": "Svenja",
        "date": "02.11.2011 09:58",
        "text": "Jeg elsker deg."
    },
    {
        "author": "Sven",
        "date": "02.11.2011 04:33",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Thomas",
        "date": "06.11.2011 12:11",
        "text": "Der Tod ist wie ein Horizont, dieser ist nichts anderes als die Grenze unserer Wahrnehmung... Wir sehen uns in ca. 55 - 60 jahren wieder."
    },
    {
        "author": "Thomas",
        "date": "06.11.2011 12:08",
        "text": "Wir sehen uns in ca. 55 - 60 jahren wieder."
    },
    {
        "author": "Isabella",
        "date": "24.02.2012 15:43",
        "text": "Du warst mir ein guter Freund und ich werde dich nie vergessen!"
    },
    {
        "author": "Kathrin",
        "date": "05.11.2011 14:35",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Stefanie",
        "date": "05.11.2011 09:05",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Annett",
        "date": "04.11.2011 12:25",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Dirk",
        "date": "04.11.2011 10:12",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Marco",
        "date": "03.11.2011 15:21",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Tino",
        "date": "03.11.2011 13:54",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Sascha",
        "date": "03.11.2011 12:47",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Julia",
        "date": "03.11.2011 11:32",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Steffen",
        "date": "02.11.2011 22:16",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Birgit",
        "date": "02.11.2011 21:48",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Conny",
        "date": "02.11.2011 20:30",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Andrea",
        "date": "02.11.2011 19:22",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Maik",
        "date": "02.11.2011 18:55",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Tobias",
        "date": "02.11.2011 17:45",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Jens",
        "date": "02.11.2011 16:30",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Micha",
        "date": "02.11.2011 15:18",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Stefan",
        "date": "02.11.2011 14:05",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Nadine",
        "date": "02.11.2011 13:42",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Christian",
        "date": "02.11.2011 12:38",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Daniel",
        "date": "02.11.2011 11:25",
        "text": "Ruhe in Frieden"
    },
    {
        "author": "Andreas",
        "date": "02.11.2011 10:17",
        "text": "Ruhe in Frieden"
    }
]

print("="*80)
print("MNEMONIC HUNT - Deep Search for Hidden Patterns")
print("="*80)

# 1. FIRST LETTERS OF MESSAGES (Author names)
print("\n1. AUTHOR NAME INITIALS")
print("-"*80)
author_initials = ''.join([m['author'][0] for m in messages])
print(f"First letters of author names: {author_initials}")
print(f"Length: {len(author_initials)}")

# Check for German words
print("\nLooking for German words in author initials...")
# Could form: IST, SIND, TRITT, etc.
for i in range(len(author_initials)-2):
    three_letter = author_initials[i:i+3]
    if three_letter.lower() in ['ist', 'und', 'der', 'die', 'das', 'mit', 'für', 'von', 'zum', 'bei']:
        print(f"  Found word '{three_letter}' at position {i}")

# 2. FIRST LETTERS OF MESSAGE TEXTS
print("\n\n2. MESSAGE TEXT FIRST LETTERS (Acrostic)")
print("-"*80)
text_initials = ''.join([m['text'][0] for m in messages])
print(f"First letters of message texts: {text_initials}")

# 3. FIRST WORD OF EACH MESSAGE
print("\n\n3. FIRST WORD OF EACH MESSAGE")
print("-"*80)
first_words = []
for m in messages:
    words = m['text'].split()
    if words:
        first_words.append(words[0])
        
print("First words:", ' | '.join(first_words))
print(f"\nFirst letters of first words: {''.join([w[0] for w in first_words])}")

# 4. SENTENCE INITIALISMS (Thomas's complex message)
print("\n\n4. THOMAS MESSAGE - SENTENCE ANALYSIS")
print("-"*80)
thomas_msg = "Der Tod ist wie ein Horizont, dieser ist nichts anderes als die Grenze unserer Wahrnehmung... Wir sehen uns in ca. 55 - 60 jahren wieder."
sentences = thomas_msg.split('.')
for i, sent in enumerate(sentences):
    sent = sent.strip()
    if sent:
        print(f"  Sentence {i+1}: '{sent[:50]}...' -> First letter: '{sent[0]}'")

# 5. CHECK FOR POETIC METER/RHYTHM
print("\n\n5. IHNO MESSAGE - SKAT REFERENCE ANALYSIS")
print("-"*80)
ihno_msg = "Dir Haian, auch wenn ich deine Leidenschaft für Poker nicht teilte, so waren jedoch die Skat-Abende mit dir umso schöner..."
print(f"Full message: {ihno_msg}")
print(f"\nKey phrase: 'Skat-Abende'")
print(f"Words: {ihno_msg.split()}")

# Look for hidden patterns in word positions
words = ihno_msg.split()
print(f"\nWord count: {len(words)}")
print(f"Word at position 5: '{words[4] if len(words) > 4 else 'N/A'}'")
print(f"Word at position 24: '{words[23] if len(words) > 23 else 'N/A'}'")

# 6. RHYMING PATTERNS
print("\n\n6. RHYME AND RHYTHM ANALYSIS")
print("-"*80)
# Check endings of German words
endings = {}
for m in messages:
    words = m['text'].split()
    for w in words:
        w = w.strip('.,!?;:"').lower()
        if len(w) > 3:
            ending = w[-3:]
            endings[ending] = endings.get(ending, 0) + 1

print("Most common word endings (potential rhymes):")
sorted_endings = sorted(endings.items(), key=lambda x: x[1], reverse=True)[:10]
for ending, count in sorted_endings:
    print(f"  -{ending}: {count} occurrences")

# 7. HIDDEN NUMBERS IN TEXT
print("\n\n7. NUMBERS IN TEXT")
print("-"*80)
for m in messages:
    numbers = re.findall(r'\d+', m['text'])
    if numbers:
        print(f"  {m['author']}: {numbers}")

# 8. CHECK FOR FIRST LETTERS OF ALL SENTENCES (FULL ACROSTIC)
print("\n\n8. COMPLETE ACROSTIC - ALL MESSAGES")
print("-"*80)
all_text = ' '.join([m['text'] for m in messages])
sentences = re.split(r'[.!?]+', all_text)
acrostic = ''.join([s.strip()[0] for s in sentences if s.strip()])
print(f"Acrostic from all sentences: {acrostic[:100]}...")

# 9. LOOK FOR INITIALISM PATTERNS
print("\n\n9. INITIALISM PATTERNS")
print("-"*80)
# Check if any combination spells something meaningful
# Try different starting positions
for start in range(min(5, len(messages))):
    test = ''.join([m['text'][0] for m in messages[start:start+10]])
    print(f"  Positions {start}-{start+9}: {test}")

# 10. REVERSE ACROSTIC (LAST LETTERS)
print("\n\n10. REVERSE ACROSTIC - LAST LETTERS")
print("-"*80)
last_letters = ''.join([m['text'][-2] if len(m['text']) > 1 else '' for m in messages])
print(f"Last letters: {last_letters}")

# 11. CHECK FOR PALINDROMIC STRUCTURES
print("\n\n11. PALINDROME CHECK IN TEXT")
print("-"*80)
for m in messages[:5]:  # Check first 5 messages
    text_clean = re.sub(r'[^a-zA-Z]', '', m['text']).lower()
    # Check if any word is palindrome
    words = text_clean.split()
    for w in words:
        if len(w) > 3 and w == w[::-1]:
            print(f"  Palindrome found: '{w}' in {m['author']}'s message")

# 12. CHECK FOR DATE INITIALISMS
print("\n\n12. DATE PATTERN INITIALISMS")
print("-"*80)
dates = [m['date'] for m in messages]
print("Date initials:")
for d in dates[:10]:
    # Format: DD.MM.YYYY HH:MM
    day = d[:2]
    month = d[3:5]
    year = d[6:10]
    print(f"  {d} -> D:{day} M:{month} Y:{year[2:]} -> Initials: {day[0]}{month[0]}{year[2]}")

# 13. LOOK FOR REPEATED PATTERNS
print("\n\n13. REPEATED PATTERNS")
print("-"*80)
# Check for repeated letter sequences
text_combined = ''.join([m['text'].lower() for m in messages])
text_clean = re.sub(r'[^a-z]', '', text_combined)

print("Checking for repeated 3-letter sequences...")
sequences = {}
for i in range(len(text_clean)-2):
    seq = text_clean[i:i+3]
    sequences[seq] = sequences.get(seq, 0) + 1

unusual = [(s, c) for s, c in sequences.items() if c > 5 and len(set(s)) > 1]
unusual.sort(key=lambda x: x[1], reverse=True)
for seq, count in unusual[:15]:
    print(f"  '{seq}': {count} times")

# 14. FINAL MNEMONIC SYNTHESIS
print("\n\n14. MNEMONIC SYNTHESIS")
print("-"*80)
print("\nPossible mnemonics found:")
print(f"  - Author initials: {author_initials[:20]}...")
print(f"  - Text acrostic: {text_initials[:20]}...")
print(f"  - First words pattern: {' | '.join(first_words[:10])}")

# Check if first words spell something
first_word_initials = ''.join([w[0] for w in first_words])
print(f"\n  - First word initials: {first_word_initials}")

# German mnemonic check
print("\nGerman words in first word initials:")
for i in range(len(first_word_initials)-2):
    three = first_word_initials[i:i+3].lower()
    if three in ['dir', 'die', 'das', 'ich', 'und', 'mit', 'für', 'von', 'zum', 'bei', 'ist', 'sind', 'ruh', 'fre']:
        print(f"    '{three}' at position {i}")

print("\n" + "="*80)
print("MNEMONIC HUNT COMPLETE")
print("="*80)
