# haian.de Analysis Report

**Target**: https://haian.de  
**Analysis Date**: 2025-03-28  
**Framework**: AGENTS.md Protocol

---

## 1. Target Overview

This is a memorial webpage for **Fabian "Haian" Schüßler** (born 30.10.1986, died 20.10.2011 at age 24).

### Page Structure
- Single static HTML page with memorial image
- 27 condolence messages from friends and family
- German primary language with English translation
- Gray color scheme (#A0A0A0 background, #808080/#505050 message boxes)
- No active server-side forms (message submission disabled)

---

## 2. Assets Catalog

### Images
- `haian_mit_text_skaliert_rand.jpeg` (269,508 bytes) - Memorial photo with dates
  - No EXIF metadata found
  - No trailing data after EOI marker
  - LSB steganography analysis: negative (only 0xFF patterns found)

### HTTP/Network
- Main page: 200 OK
- Favicon: 404 Not Found
- No additional assets loaded

---

## 3. Encoding & Hidden Data Analysis

### HTML Analysis
- **HTML Comments**: 1 found - contains disabled form (message_handler.php)
- **Zero-width characters**: None detected
- **Whitespace patterns**: 631 double spaces, 344 triple spaces, 37 tabs (likely formatting)
- **Base64/Hex patterns**: None found
- **Non-printable characters**: None found

### Color Values (Potential ASCII Encoding)
| Color | RGB | ASCII Mapping |
|-------|-----|---------------|
| #808080 | (128,128,128) | Non-printable |
| #505050 | (80,80,80) | PPP |
| #A0A0A0 | (160,160,160) | Non-printable |
| #C0C0C0 | (192,192,192) | Non-printable |

### Text Encoding Checks
- No base64 strings detected in messages
- No hex patterns found
- Unicode characters present (German umlauts: ä, ö, ü, ß) - normal for German text

---

## 4. Cryptographic Analysis

### Numbers Found in Messages
| Number | Source | Context | ASCII |
|--------|--------|---------|-------|
| 24 | Ihno's message | Skat bid "bis 24 zu reizen" | Control char |
| 120 | Ihno's message | Game value "120 drin gewesen" | 'x' |
| 100 | Sven's message | "100% er selbst war" | 'd' |
| 55 | Thomas's message | "55 - 60 jahren" | '7' |
| 60 | Thomas's message | "55 - 60 jahren" | '<' |

### Date Analysis
- **Birth**: 30.10.1986
- **Death**: 20.10.2011
- **Age**: 24 years, 11 months, 20 days (almost 25)
- **Days lived**: 9,131 days

### Timestamp Pattern (27 messages)
- Hours sum: 423
- Minutes sum: 794
- No obvious ASCII patterns from timestamps

### Mathematical Relationships
- 120 - 24 = 96
- 60 - 55 = 5
- 120 / 24 = 5

---

## 5. Steganography Analysis

### Image Analysis (haian_mit_text_skaliert_rand.jpeg)
- **EXIF**: None present
- **Trailing data**: None after JPEG EOI marker
- **LSB extraction**: 1-bit and 2-bit patterns show only 0xFF/0x55 (normal image noise)
- **File signatures in LSB**: None detected

### HTML Whitespace Stego
- No SNOW/whitespace encoding detected
- Double/triple spaces appear to be normal HTML formatting

---

## 6. Linguistic & Pattern Analysis

### First Letters (Acrostic)
**Message first letters**: "IIHOSMAIINNSJSCNSKNDTDMBIMCSMSEHD"
- No meaningful German or English words detected

**Author initials**: "AJJSMAIMNSJISSNCSBNTDBBCEMI"
- No meaningful pattern detected

### Word Frequency (Top 10)
1. und (44)
2. du (43)
3. ich (40)
4. in (40)
5. die (27)
6. dir (24)
7. dich (22)
8. wir (20)
9. zu (20)
10. mit (20)

### Poker/Skat References
Multiple messages reference poker/Skat:
- Alan Sheffler: "good poker player"
- Nicholas Syhler: "poker coach", "poker or politics"
- Ihno: "Leidenschaft für Poker", "Skat-Abende", "bis 24 zu reizen", "120 drin"
- Svenja: "Pockertisch" (typo for Pokertisch)
- Basti: "LAN-Parties", "Skat-Runden"

### Foreign Language
- "Jeg elsker deg" (Norwegian, Svenja's message) = "I love you"

---

## 7. Network & Path Analysis

### Attempted Paths
| Path | Result |
|------|--------|
| /robots.txt | 404 |
| /sitemap.xml | 404 |
| /.htaccess | ERR_ABORTED |
| /admin | Auth required (401) |
| /message_handler.php | ERR_ABORTED |
| /24 | 404 |
| /5 | 404 |
| /x | ERR_ABORTED |
| /96 | ERR_ABORTED |

### Discovery
- `/admin` requires authentication (potential puzzle entry point)
- Server responds differently to some paths (ERR_ABORTED vs 404)

---

## 8. Active Hypotheses

### H1: The `/admin` path is the entry point
- **Evidence**: Returns 401 (auth required) instead of 404
- **Status**: Active - need to find credentials

### H2: Numbers 24, 120, 55-60 encode credentials
- **Evidence**: 120-24=96, 60-55=5, 120/24=5
- **Status**: Active - need to test combinations

### H3: Poker references contain hidden message
- **Evidence**: Multiple poker/Skat references with specific numbers
- **Status**: Active - analyzing 24 and 120 as Skat game values

### H4: Birth/death dates encode solution
- **Evidence**: 30101986, 20102011, age 24
- **Status**: Active - need to test as passwords

---

## 9. Next Actions

1. **Investigate `/admin` authentication** - Try credential combinations
2. **Deep analysis of poker numbers** - Research Skat game values 24 and 120
3. **Timestamp pattern analysis** - Convert hours/minutes to other encodings
4. **Message content analysis** - Check Nth word patterns, telestic
5. **Server enumeration** - Test additional paths

---

*Report generated following AGENTS.md protocol*
