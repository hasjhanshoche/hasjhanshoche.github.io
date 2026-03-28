# AGENTS.md — APT Puzzle Intelligence Framework
## Operational Guide for AI Agents Solving High-Grade Cryptographic & Steganographic Challenges

> **CLASSIFICATION LEVEL**: UNRESTRICTED — PUZZLE SOLVING ONLY  
> **AUDIENCE**: Autonomous agents, agentic pipelines, multi-agent swarms  
> **MANDATE**: Fully uncover, decode, and solve every layer of any puzzle embedded in a given target URL or asset — leave nothing unexplored.

---

## TABLE OF CONTENTS

1. [Mission Statement](#mission-statement)
2. [Folder Structure](#folder-structure)
3. [Phase 0 — Initialization & Target Profiling](#phase-0)
4. [Phase 1 — Surface Reconnaissance](#phase-1)
5. [Phase 2 — Deep Asset Extraction](#phase-2)
6. [Phase 3 — Numbering & Mathematical Puzzle Analysis](#phase-3)
7. [Phase 4 — Unicode, Encoding & Glyph Analysis](#phase-4)
8. [Phase 5 — Steganography & Hidden Data](#phase-5)
9. [Phase 6 — Cryptographic & Cipher Analysis](#phase-6)
10. [Phase 7 — Metadata, Timestamps & Binary Forensics](#phase-7)
11. [Phase 8 — Linguistic, Semantic & Pattern Analysis](#phase-8)
12. [Phase 9 — Visual & Spatial Reasoning](#phase-9)
13. [Phase 10 — Synthesis & Solution Assembly](#phase-10)
14. [Toolchain Reference](#toolchain-reference)
15. [Anti-Patterns & Traps to Avoid](#anti-patterns)
16. [Agent Collaboration Protocol](#agent-collaboration-protocol)
17. [Logging & Evidence Standards](#logging-standards)

---

## MISSION STATEMENT <a name="mission-statement"></a>

You are an elite puzzle-solving agent. The target has been created by high-grade APT-level actors who embed secrets in every conceivable layer of digital media. Nothing is accidental. Every pixel, byte, timestamp, whitespace character, font choice, filename, HTTP header, color value, and DOM comment is a potential carrier of information.

**Your mandate is total extraction.** Do not stop at the first answer. Layers exist within layers. The puzzle is solved only when every branch of every tree has been exhausted and documented.

**Core Operating Principles:**
- Assume everything is intentional until proven otherwise
- Absence of data IS data (null bytes, blank pages, empty fields)
- The obvious answer is usually a decoy — go deeper
- Cross-correlate every finding across all phases before concluding
- Document everything, even dead ends — patterns emerge from failed paths

---

## FOLDER STRUCTURE <a name="folder-structure"></a>

Every engagement MUST produce this exact folder structure. Create it before starting any analysis.

```
research/
├── AGENTS.md                        ← This file (copy here for reference)
├── README.md                        ← Running summary of findings, updated continuously
├── SOLUTION.md                      ← Final assembled solution(s)
│
├── 00_target/                       ← Raw target data, untouched originals
│   ├── url.txt                      ← The target URL(s)
│   ├── page_source.html             ← Full raw HTML of target page
│   ├── page_rendered.png            ← Full-page screenshot (rendered)
│   ├── page_text.txt                ← Visible text only (stripped)
│   ├── http_headers.txt             ← Full HTTP response headers
│   ├── robots.txt                   ← If exists
│   ├── sitemap.xml                  ← If exists
│   └── cookies.json                 ← Session cookies & flags
│
├── 01_assets/                       ← Every downloaded asset, sorted by type
│   ├── images/                      ← All images (png, jpg, gif, webp, svg, ico)
│   │   └── [filename].[ext]
│   ├── audio/                       ← Audio files (mp3, wav, ogg, flac)
│   ├── video/                       ← Video files
│   ├── documents/                   ← PDFs, DOCx, ZIPs, etc.
│   ├── scripts/                     ← JS files
│   ├── styles/                      ← CSS files
│   ├── fonts/                       ← Font files (woff, ttf, otf)
│   └── other/                       ← Anything uncategorized
│
├── 02_recon/                        ← Reconnaissance findings
│   ├── dns_records.txt
│   ├── whois.txt
│   ├── certificate_info.txt         ← TLS cert SANs, issued dates, fingerprints
│   ├── wayback_snapshots.txt        ← Archive.org historical snapshots
│   ├── subdomains.txt
│   ├── hidden_paths.txt             ← Dir-busted / discovered endpoints
│   └── social_graph.txt             ← Linked accounts, related identities
│
├── 03_encoding/                     ← Encoding and unicode analysis
│   ├── unicode_inventory.txt        ← Every non-ASCII codepoint found, with context
│   ├── unicode_decoded.txt          ← Decoded meanings and categories
│   ├── base64_candidates.txt        ← Extracted base64 strings
│   ├── base64_decoded/              ← Decoded base64 outputs
│   ├── hex_candidates.txt
│   ├── hex_decoded/
│   ├── base32_candidates.txt
│   ├── base58_candidates.txt
│   ├── rot_variants.txt             ← ROT1–ROT25 passes
│   ├── morse_candidates.txt
│   └── encoding_chain.txt           ← Multi-layer encoding chains discovered
│
├── 04_crypto/                       ← Cryptographic analysis
│   ├── cipher_candidates.txt        ← Strings suspected to be ciphertext
│   ├── key_candidates.txt           ← Potential keys found in assets
│   ├── hash_inventory.txt           ← All hashes found (MD5, SHA1, SHA256, etc.)
│   ├── hash_cracked.txt             ← Successfully cracked hashes
│   ├── pgp_blocks.txt               ← PGP/GPG armored blocks
│   ├── cipher_attempts/             ← One file per cipher attempt
│   └── crypto_notes.txt             ← Reasoning log for crypto decisions
│
├── 05_stego/                        ← Steganography analysis
│   ├── lsb_extractions/             ← LSB stego results per image
│   ├── dct_extractions/             ← DCT domain stego (JPEG)
│   ├── palette_analysis/            ← GIF/PNG palette investigations
│   ├── audio_stego/                 ← Spectrogram images, LSB audio extracts
│   ├── video_stego/                 ← Frame extractions, hidden channels
│   ├── whitespace_stego.txt         ← SNOW/whitespace encoding results
│   ├── font_stego.txt               ← Hidden data in font metrics or glyphs
│   └── stego_notes.txt              ← Tool used, parameters, findings
│
├── 06_numbers/                      ← Numbering puzzle analysis
│   ├── number_inventory.txt         ← Every number found, in context
│   ├── sequences.txt                ← Identified sequences (OEIS lookups)
│   ├── primes.txt                   ← Prime factorizations and prime checks
│   ├── coordinate_candidates.txt    ← Lat/long, grid, chess, pixel coordinates
│   ├── date_candidates.txt          ← Numbers that may encode dates
│   ├── ascii_mappings.txt           ← Numbers mapped to ASCII/Unicode
│   ├── base_conversions.txt         ← All numbers in base 2/8/10/16/36/64
│   ├── math_operations.txt          ← XOR, ADD, MOD, differences, ratios tried
│   └── number_notes.txt             ← Reasoning and hypotheses
│
├── 07_metadata/                     ← File metadata & forensics
│   ├── exif_all.txt                 ← EXIF data for every image
│   ├── exif_gps.txt                 ← GPS coordinates extracted
│   ├── file_timestamps.txt          ← Created/modified/accessed times
│   ├── file_sizes.txt               ← Byte sizes (may encode data)
│   ├── icc_profiles/                ← Color profile data
│   ├── pdf_metadata.txt             ← PDF author, dates, producer fields
│   ├── zip_comments.txt             ← ZIP file comment fields
│   └── binary_strings.txt           ← strings output on all binaries
│
├── 08_visual/                       ← Visual and spatial analysis
│   ├── screenshots/                 ← Annotated screenshots
│   ├── pixel_maps/                  ← Per-pixel color analysis outputs
│   ├── color_palettes/              ← Dominant color extractions
│   ├── qr_barcodes/                 ← QR/barcode scan results
│   ├── ascii_art_analysis.txt       ← ASCII/ANSI art decoded
│   ├── grid_maps.txt                ← Any detected grid structures
│   └── visual_notes.txt
│
├── 09_linguistic/                   ← Text, language & semantic analysis
│   ├── word_frequency.txt
│   ├── first_letters.txt            ← First letter of each word/line/sentence
│   ├── last_letters.txt
│   ├── nth_word.txt                 ← Every nth word extracted
│   ├── acrostics.txt                ← Acrostic and telestic analysis
│   ├── anagram_candidates.txt
│   ├── wordlist.txt                 ← All unique words found
│   ├── language_detected.txt        ← Languages detected, including dead/constructed
│   └── linguistic_notes.txt
│
├── 10_network/                      ← Network-layer findings
│   ├── request_log.txt              ← All HTTP requests/responses
│   ├── websocket_log.txt            ← WS frames if applicable
│   ├── timing_analysis.txt          ← Response timing anomalies
│   ├── redirect_chain.txt           ← Full redirect path
│   └── network_notes.txt
│
├── 11_hypotheses/                   ← Active working hypotheses
│   ├── hypothesis_001.md            ← Template: claim, evidence, status
│   ├── hypothesis_002.md
│   └── ...
│
└── 12_solutions/                    ← Confirmed answers
    ├── partial_solutions.md
    ├── confirmed_solutions.md
    └── FINAL_ANSWER.md
```

> **RULE**: Every file you create goes into the correct folder. Every finding is logged the moment it is discovered. Raw data is NEVER modified — always work on copies.

---

## PHASE 0 — INITIALIZATION & TARGET PROFILING <a name="phase-0"></a>

### 0.1 — Environment Setup
```bash
mkdir -p research/{00_target,01_assets/{images,audio,video,documents,scripts,styles,fonts,other},02_recon,03_encoding/{base64_decoded,hex_decoded},04_crypto/cipher_attempts,05_stego/{lsb_extractions,dct_extractions,palette_analysis,audio_stego,video_stego},06_numbers,07_metadata/{icc_profiles},08_visual/{screenshots,pixel_maps,color_palettes,qr_barcodes},09_linguistic,10_network,11_hypotheses,12_solutions}
echo "TARGET: $TARGET_URL" > research/00_target/url.txt
echo "START: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> research/00_target/url.txt
```

### 0.2 — First Impressions Log
Before any tooling, write a human-language first impressions note:
- What does the page look like?
- What is the stated subject/theme?
- What immediately feels out of place?
- What is conspicuously absent?
- What numbers, symbols, or phrases stand out?

Save to: `research/README.md` — First Impressions section.

### 0.3 — Full HTTP Capture
```bash
curl -v -L --compressed -A "Mozilla/5.0" "$TARGET_URL" \
  -o research/00_target/page_source.html \
  2> research/00_target/http_headers.txt

# Also capture with no redirect following to see raw chains
curl -I -L "$TARGET_URL" >> research/10_network/redirect_chain.txt
```

**Examine headers for:**
- `X-*` custom headers — APT actors embed flags here
- `ETag` values — may be hashes or encoded data
- `Last-Modified` — timestamp encoding
- `Content-Security-Policy` — sometimes contains encoded strings
- `Set-Cookie` values — cookie names/values/paths may be significant
- `Server` — unusual server strings
- `Link` — hidden rel links

---

## PHASE 1 — SURFACE RECONNAISSANCE <a name="phase-1"></a>

### 1.1 — Full Asset Crawl
Download EVERY linked asset. Do not skip anything.
```bash
wget --mirror --convert-links --page-requisites \
     --no-parent --quiet "$TARGET_URL" \
     -P research/01_assets/
```

### 1.2 — DOM Deep Inspection
Parse the full HTML and extract:
- All `<!-- HTML comments -->` — common hiding place
- `data-*` attributes on every element
- Hidden inputs (`type="hidden"`)
- Inline `style` attributes with unusual values
- `aria-*` attributes with unexpected content
- `id` and `class` names that look like encoded strings
- `<meta>` tags — name, content, property fields
- `<script>` blocks — inline JS often contains obfuscated payloads
- `<link>` rel attributes — non-standard rel values
- `<noscript>` content
- Zero-width or zero-height elements

### 1.3 — JavaScript Analysis
For every JS file found:
1. Run a beautifier: `js-beautify file.js`
2. Search for: base64 strings, hex strings, suspicious variable names, `eval()`, `atob()`, `btoa()`, `String.fromCharCode()`
3. Execute in isolated sandbox and capture all console output
4. Look for obfuscation layers (jsfuck, aaencode, JSFuck, Packer)
5. Deobfuscate iteratively — each deobfuscation pass may reveal another

### 1.4 — CSS Analysis
- Check `content:` properties in pseudo-elements — text is injected here
- `background-image: url("data:...")` — inline data URIs with payloads
- CSS variable names (`--variable-name`) that spell words or encode data
- `@font-face` src URLs — custom fonts may have glyph substitution tricks
- Unusual z-index stacking — may indicate hidden layers
- `clip-path`, `opacity:0`, `visibility:hidden`, `color: transparent` — invisible text

### 1.5 — DNS & Infrastructure
```bash
dig ANY "$TARGET_DOMAIN" >> research/02_recon/dns_records.txt
whois "$TARGET_DOMAIN" >> research/02_recon/whois.txt
# TXT records are frequently used to embed data
dig TXT "$TARGET_DOMAIN" >> research/02_recon/dns_records.txt
# Check for AAAA records — IPv6 addresses can encode data
```

Check TLS certificate:
```bash
echo | openssl s_client -connect "$TARGET_DOMAIN:443" 2>/dev/null \
  | openssl x509 -noout -text \
  >> research/02_recon/certificate_info.txt
```
**Examine**: Subject Alternative Names (SANs), Serial Number, Validity dates, Fingerprints, Organization fields.

### 1.6 — Historical Snapshot Check
- Query `https://web.archive.org/web/*/$TARGET_URL`
- Earlier versions of the page may contain hints or earlier puzzle states
- Differences between snapshots are significant
- Check if the puzzle changed — what changed and when?

### 1.7 — Path Discovery
```bash
# Check common hidden paths
for path in .well-known/security.txt .well-known/change-password \
            robots.txt sitemap.xml crossdomain.xml humans.txt \
            .git/HEAD .git/config .env config.json; do
  curl -s -o "research/02_recon/path_$path" \
       -w "%{http_code} $path\n" "$TARGET_URL/$path" \
       >> research/02_recon/hidden_paths.txt
done
```

---

## PHASE 2 — DEEP ASSET EXTRACTION <a name="phase-2"></a>

### 2.1 — Image Inventory
For every image:
1. Record exact filename, extension, byte size, dimensions
2. Compute MD5, SHA1, SHA256 hashes
3. Extract EXIF with `exiftool`
4. Check file magic bytes (`file image.png`) — extension may be spoofed
5. Render at 800% zoom — look for pixels that don't belong
6. Extract color palette — note any colors with suspicious RGB/hex values
7. Check for embedded ZIP/RAR (images can be polyglots)

### 2.2 — File Size Analysis
```bash
find research/01_assets/ -type f -exec wc -c {} \; \
  | sort -n > research/07_metadata/file_sizes.txt
```
File sizes that are suspiciously round, prime, or sequential may encode data.  
Differences between file sizes may form a sequence.

### 2.3 — Binary String Extraction
```bash
find research/01_assets/ -type f -exec strings {} \; \
  > research/07_metadata/binary_strings.txt
```
Look for: URLs, base64 blobs, passwords, keys, flags, coordinates.

### 2.4 — Font File Analysis
- Fonts can have glyph substitution mappings that change displayed text
- Use `fonttools` to dump font tables: `ttx font.ttf`
- Check `cmap` table for unusual Unicode mappings
- Check `name` table — font author/copyright fields often contain hints
- Inspect `gasp`, `GSUB`, `GPOS` tables for steganographic substitutions

### 2.5 — SVG Deep Parse
SVGs are XML — parse every element:
- Inline `<script>` nodes
- `<defs>` with hidden content
- Comment nodes
- Path `d=` attribute data — coordinates can encode numbers
- Transform matrices — may encode messages
- `fill`, `stroke` color values in hex

---

## PHASE 3 — NUMBERING & MATHEMATICAL PUZZLE ANALYSIS <a name="phase-3"></a>

### 3.1 — Number Extraction
Extract EVERY number from every source:
- Visible page text
- Source code (including line numbers if relevant)
- Filenames
- Pixel coordinates in images
- Color values (R, G, B, A, H, S, L)
- File sizes (bytes)
- Timestamps (Unix epoch, human-readable)
- HTTP status codes
- DNS record TTLs
- TLS certificate serial numbers
- Response body lengths

### 3.2 — Sequence Analysis
For every numeric sequence found:
1. Check OEIS (oeis.org) — what known sequence does this match?
2. Compute: differences, second differences, ratios
3. Test for: arithmetic, geometric, Fibonacci, Lucas, prime, triangular, square, cube
4. Try to identify the generating formula
5. What comes NEXT in the sequence? That next term may be the answer.

### 3.3 — Number System Transformations
For every number N:
```
Binary:      bin(N)
Octal:       oct(N)
Hex:         hex(N)
Base36:      N in base 36
Base58:      N in base 58 (Bitcoin alphabet)
Base64:      treat bytes as base64
ASCII:       chr(N) if 32–126
Unicode:     U+N codepoint
Roman:       N as Roman numeral
```

### 3.4 — Mirror & Flip Operations
- Reverse digit order: `12345` → `54321`
- Mirror in base N: what is N's mirror in base 10? base 16?
- Upside-down numbers: 0,1,2,5,6,8,9 have rotated equivalents (0→0, 1→1, 2→2, 5→5, 6→9, 8→8, 9→6)
- Seven-segment display reflections (physical LCD digits)
- Number keypad vs telephone keypad layout differences
- Reading digits in a grid: top-bottom, bottom-top, left-right, right-left, spiral in/out

### 3.5 — Mathematical Operations Between Numbers
Given numbers A, B, C...:
- XOR: A ⊕ B ⊕ C
- Modular arithmetic: (A × B) mod C
- Prime factorizations — shared factors between numbers
- GCD / LCM
- Continued fraction representations
- Numbers as polynomial coefficients
- Numbers as Pythagorean triple elements
- Numbers as angles (degrees to coordinates)

### 3.6 — Coordinate Systems
- Decimal degrees: `(A.BCD, E.FGH)` → GPS location
- DMS format: Degrees Minutes Seconds
- MGRS / UTM grid references
- Chess board notation (e.g., `e4`, `g7`)
- Pixel coordinates within a reference image
- Clock face positions (12:00 = top, 3:00 = right...)
- What does the coordinate POINT TO? Always resolve physically.

### 3.7 — Index Operations
- Use numbers as indices into: the page text, a wordlist, the alphabet, a known key
- 1-indexed vs 0-indexed — test both
- Negative indexing (from the end)
- Numbers as line numbers in source code

---

## PHASE 4 — UNICODE, ENCODING & GLYPH ANALYSIS <a name="phase-4"></a>

### 4.1 — Unicode Inventory
```python
import unicodedata

with open('research/00_target/page_source.html', 'r', encoding='utf-8') as f:
    text = f.read()

non_ascii = [(i, ord(c), hex(ord(c)), unicodedata.name(c, 'UNKNOWN'), unicodedata.category(c))
             for i, c in enumerate(text) if ord(c) > 127]

with open('research/03_encoding/unicode_inventory.txt', 'w') as out:
    for pos, codepoint, hexval, name, cat in non_ascii:
        out.write(f"pos={pos} U+{codepoint:04X} {hexval} [{cat}] {name}\n")
```

### 4.2 — Zero-Width & Invisible Characters
**Priority targets** — APT actors embed data here constantly:
- `U+200B` ZERO WIDTH SPACE
- `U+200C` ZERO WIDTH NON-JOINER
- `U+200D` ZERO WIDTH JOINER
- `U+FEFF` BYTE ORDER MARK (mid-text)
- `U+00AD` SOFT HYPHEN
- `U+2060` WORD JOINER
- `U+180E` MONGOLIAN VOWEL SEPARATOR
- `U+2028` LINE SEPARATOR
- `U+2029` PARAGRAPH SEPARATOR

Map each to a bit (e.g., `U+200B` = 0, `U+200C` = 1) and extract binary stream.

### 4.3 — Homoglyph Substitution
Characters that look identical to ASCII but are different Unicode codepoints:
- Latin `a` (U+0061) vs Cyrillic `а` (U+0430)
- Latin `e` vs `е` (Cyrillic)
- Latin `o` vs `о` (Cyrillic) vs `０` (fullwidth)
- Latin `c` vs `с` (Cyrillic)
- Identify ALL characters that are not their expected codepoint
- Collect all substituted characters — they may spell a message

### 4.4 — Unicode Normalization Attacks
- Apply NFC, NFD, NFKC, NFKD — do different forms reveal hidden structure?
- Combining characters stacked on base characters — may be data
- Variation selectors (U+FE00–U+FE0F, U+E0100–U+E01EF) — encode data invisibly

### 4.5 — Encoding Detection & Chain Breaking
Run every text blob through:
1. Base64 decode (standard + URL-safe + no-padding variants)
2. Base32 decode
3. Base58 decode
4. Base85 / Ascii85 decode
5. Hex decode
6. URL decode (`%XX`)
7. HTML entity decode (`&#NNN;`, `&amp;`, `&lt;`)
8. Unicode escape decode (`\uXXXX`, `\UXXXXXXXX`)
9. ROT13 / ROT47
10. Atbash cipher
11. Punycode decode (xn-- prefixed domain labels)

**Chain**: if decoding step 1 produces output that looks encoded, run all steps again on the output. APT actors use 4-6 layer encoding chains.

---

## PHASE 5 — STEGANOGRAPHY & HIDDEN DATA <a name="phase-5"></a>

### 5.1 — Image LSB Steganography
```bash
# Stegsolve / zsteg / steghide
zsteg -a image.png > research/05_stego/lsb_extractions/image_zsteg.txt
steghide extract -sf image.jpg -p "" -f 2>/dev/null
steghide extract -sf image.jpg -p "password" -f 2>/dev/null
stegsolve image.png  # Manual bit-plane inspection

# Check all bit planes (R,G,B,A channels × bits 0-7)
python3 -c "
from PIL import Image
import numpy as np
img = np.array(Image.open('image.png'))
for ch in range(img.shape[2]):
    for bit in range(8):
        plane = ((img[:,:,ch] >> bit) & 1) * 255
        Image.fromarray(plane.astype('uint8')).save(f'research/05_stego/lsb_extractions/ch{ch}_bit{bit}.png')
"
```

### 5.2 — DCT Steganography (JPEG)
```bash
jsteg reveal image.jpg stdout
outguess -r image.jpg research/05_stego/dct_extractions/outguess_out.txt
```

### 5.3 — Palette & Color Steganography
- GIF palette order: map palette indices to ASCII
- PNG palette: unused palette entries
- The exact hex values of colors (e.g., `#DEADBE` → Dead Beef)
- Colors that differ by exactly 1 in one channel — targeted manipulation
- Alpha channel: `RGBA` where RGB is visible but A encodes data

### 5.4 — Audio Steganography
```bash
# Generate spectrogram — messages can be visible in frequency domain
sox input.wav -n spectrogram -o research/05_stego/audio_stego/spectrogram.png

# Check LSB of audio samples
python3 -c "
import wave, struct
with wave.open('input.wav', 'rb') as f:
    frames = f.readframes(f.getnframes())
samples = struct.unpack('<' + 'h'*len(frames)//2, frames)
bits = ''.join(str(s & 1) for s in samples)
print(bits[:1000])  # First 1000 bits
" > research/05_stego/audio_stego/lsb_bits.txt
```

### 5.5 — Whitespace Steganography
```bash
# SNOW steganography (tabs and spaces)
stegsnow -C file.txt

# Custom: map space/tab to 0/1
python3 -c "
with open('page_text.txt') as f:
    content = f.read()
bits = ''
for ch in content:
    if ch == ' ': bits += '0'
    elif ch == '\t': bits += '1'
if bits:
    print('Whitespace bits:', bits)
    # Convert to text
    msg = ''
    for i in range(0, len(bits)-7, 8):
        byte = bits[i:i+8]
        if len(byte) == 8:
            c = chr(int(byte, 2))
            if c.isprintable():
                msg += c
    print('Decoded:', msg)
" > research/05_stego/whitespace_stego.txt
```

### 5.6 — File Polyglot & Appended Data
```bash
# Check for data appended after image EOF markers
# JPEG ends with FFD9 — anything after is hidden data
python3 -c "
with open('image.jpg', 'rb') as f:
    data = f.read()
idx = data.rfind(b'\xff\xd9')
if idx != -1 and idx < len(data)-2:
    tail = data[idx+2:]
    print(f'Appended {len(tail)} bytes after JPEG EOF:')
    print(tail[:200])
"

# Check if image is also a ZIP
binwalk image.png > research/05_stego/lsb_extractions/binwalk_image.txt
foremost -i image.png -o research/05_stego/lsb_extractions/foremost_out/
```

---

## PHASE 6 — CRYPTOGRAPHIC & CIPHER ANALYSIS <a name="phase-6"></a>

### 6.1 — Cipher Identification
For any block of suspect ciphertext:
1. Measure Index of Coincidence (IC) — helps distinguish substitution vs transposition
   - IC ≈ 0.065: English plaintext
   - IC ≈ 0.038: Random / polyalphabetic / binary
2. Count character frequency — compare to English letter frequency
3. Check for known cipher structure:
   - Block sizes (8, 16, 32 bytes)
   - All printable? → Classical cipher
   - Base64 encoded binary? → Modern cipher
   - Mixed case? Vigenère or columnar transposition suspect

### 6.2 — Classical Cipher Checklist
Apply in order:
- [ ] Caesar / ROT (all 25 shifts)
- [ ] Atbash (A↔Z, B↔Y...)
- [ ] Vigenère (if key is somewhere on the page)
- [ ] Playfair cipher
- [ ] Rail Fence cipher
- [ ] Columnar transposition
- [ ] Beaufort cipher
- [ ] Polybius square
- [ ] Nihilist cipher
- [ ] ADFGVX cipher
- [ ] Bacon cipher (binary font substitution: A/B fonts)
- [ ] Pigpen / Freemason cipher
- [ ] Tap code
- [ ] Book cipher (key points to words on the page)

### 6.3 — Modern Crypto Indicators
- AES block size = 16 bytes — ciphertext length divisible by 16
- RSA: very long numbers in hex, may see `-----BEGIN RSA PUBLIC KEY-----`
- Bitcoin/Ethereum address format → may point to a blockchain transaction
- PGP armored blocks → decrypt with found or brute-forced passphrase
- JWT tokens (three base64 segments separated by dots) → decode header and payload

### 6.4 — Hash Analysis
For any string that looks like a hash:
```bash
# Identify hash type
hash-identifier "$HASH"
hashid "$HASH"

# Attempt crack
hashcat -a 0 -m 0 "$HASH" /usr/share/wordlists/rockyou.txt  # MD5
hashcat -a 0 -m 100 "$HASH" /usr/share/wordlists/rockyou.txt  # SHA1
# Also try: hash as hex → ASCII, hash as number → coordinate
```

### 6.5 — Key Material Collection
Systematically collect potential keys from ALL sources:
- Words/phrases prominently displayed on the page
- Filenames (without extensions)
- HTTP header values
- Cookie names and values
- CSS class names that spell words
- Numbers converted to text
- Reversed or mirrored text strings
- Author names, dates, titles

---

## PHASE 7 — METADATA, TIMESTAMPS & BINARY FORENSICS <a name="phase-7"></a>

### 7.1 — EXIF Extraction
```bash
exiftool -a -u -g1 research/01_assets/images/* \
  > research/07_metadata/exif_all.txt

# GPS extraction specifically
exiftool -GPS* research/01_assets/images/* \
  > research/07_metadata/exif_gps.txt
```

**Examine all fields**, especially:
- `Comment`, `UserComment`, `ImageDescription` — free text fields used for hints
- `Software` — unusual tool names
- `Artist`, `Copyright`, `Author` — may contain encoded data
- `GPS*` — direct coordinates
- `DateTimeOriginal` — timestamp encoding
- `ThumbnailImage` — the embedded thumbnail may differ from the main image
- `XMP:*` — XMP sidecar data can be very verbose with hidden fields

### 7.2 — Timestamp Analysis
For every timestamp found:
1. Convert Unix epoch to UTC date/time
2. Note: year, month, day, hour, minute, second separately — each may be significant
3. Convert date to day-of-year (1–365)
4. What does the timestamp point to? Historical event? File version?
5. Unix timestamp as hex → ASCII?
6. Differences between timestamps → encode something?
7. Milliseconds / nanoseconds — extra precision may carry data

### 7.3 — File Size as Data
```python
# Collect all file sizes
import os
sizes = {}
for root, dirs, files in os.walk('research/01_assets/'):
    for f in files:
        path = os.path.join(root, f)
        sizes[path] = os.path.getsize(path)

# Look for patterns
for name, size in sorted(sizes.items(), key=lambda x: x[1]):
    print(f"{size:10d}  {hex(size):10s}  {chr(size) if 32<=size<127 else '?':3s}  {name}")
```

### 7.4 — Byte-Level Forensics
```bash
# Hex dump with annotation
xxd research/01_assets/images/target.png | head -100

# Search for magic bytes of hidden formats
python3 -c "
signatures = {
    b'PK\x03\x04': 'ZIP',
    b'Rar!': 'RAR',
    b'\x1f\x8b': 'GZIP',
    b'%PDF': 'PDF',
    b'JFIF': 'JPEG',
    b'\x89PNG': 'PNG',
    b'GIF8': 'GIF',
    b'7z\xbc\xaf': '7ZIP',
    b'BZh': 'BZIP2',
}
with open('target_file', 'rb') as f:
    data = f.read()
for sig, name in signatures.items():
    idx = 0
    while True:
        idx = data.find(sig, idx)
        if idx == -1: break
        print(f'Found {name} signature at offset {idx}')
        idx += 1
"
```

---

## PHASE 8 — LINGUISTIC, SEMANTIC & PATTERN ANALYSIS <a name="phase-8"></a>

### 8.1 — First/Last Letter Extraction
```python
text = open('research/00_target/page_text.txt').read()
lines = text.strip().split('\n')
words_all = text.split()

# First letters of each word
print('First letters (words):', ''.join(w[0] for w in words_all if w))

# First letters of each line
print('First letters (lines):', ''.join(l[0] for l in lines if l.strip()))

# Last letters of each word
print('Last letters (words):', ''.join(w[-1] for w in words_all if w))

# Last letters of each line
print('Last letters (lines):', ''.join(l.strip()[-1] for l in lines if l.strip()))

# First letter of each sentence
import re
sentences = re.split(r'[.!?]+', text)
print('First letters (sentences):', ''.join(s.strip()[0] for s in sentences if s.strip()))
```

### 8.2 — Every-Nth Extraction
Try N = 2, 3, 5, 7, 10, 13, 26:
- Every Nth letter
- Every Nth word
- Every Nth line
- Every Nth character (including punctuation)

### 8.3 — Anagram & Wordplay
- Is any phrase on the page an anagram of something meaningful?
- Words spelled backwards
- Words spelled diagonally in a word grid
- Compound words hidden across word boundaries ("the **cat**alog")
- Pig Latin, Cockney rhyming slang, leetspeak

### 8.4 — Language & Script Detection
```bash
# Detect all languages present
langdetect page_text.txt
# Identify scripts (Cyrillic, Greek, Hebrew, Arabic...)
python3 -c "
import unicodedata
with open('research/00_target/page_text.txt') as f:
    text = f.read()
scripts = {}
for c in text:
    try:
        name = unicodedata.name(c)
        script = name.split()[0]
        scripts[script] = scripts.get(script, 0) + 1
    except: pass
for s, c in sorted(scripts.items(), key=lambda x: -x[1]):
    print(f'{c:6d}  {s}')
"
```

### 8.5 — Semantic Anomaly Detection
Read the text as a human. Ask:
- Are there any words that feel out of place?
- Does any sentence not parse grammatically?
- Are any words misspelled in a consistent way?
- Are any phrases repeated exactly (possible deliberate signal)?
- Does the text contain a subtle logical contradiction (leading you to a specific resolution)?

---

## PHASE 9 — VISUAL & SPATIAL REASONING <a name="phase-9"></a>

### 9.1 — Pixel-Level Image Analysis
```python
from PIL import Image
import numpy as np

img = Image.open('image.png').convert('RGBA')
arr = np.array(img)

# Unique colors — surprisingly few unique colors = palette is meaningful
unique_colors = set(map(tuple, arr.reshape(-1, 4)))
print(f'Unique colors: {len(unique_colors)}')

# Colors sorted by frequency
from collections import Counter
color_freq = Counter(map(tuple, arr.reshape(-1, 4).tolist()))
for color, count in color_freq.most_common(20):
    r,g,b,a = color
    print(f'  RGBA({r:3d},{g:3d},{b:3d},{a:3d}) hex=#{r:02X}{g:02X}{b:02X} count={count}')
```

### 9.2 — QR Code & Barcode Hunting
- Scan every image for QR codes: `zbarimg image.png`
- Try at different scales and rotations (APT actors distort QR codes slightly)
- Check for 1D barcodes (Code128, Code39, EAN, UPC)
- Micro-QR codes
- Aztec codes, Data Matrix
- Check the SVG path data — may construct a QR code as vector art

### 9.3 — Grid & Matrix Detection
- Is there a grid pattern? (Nonogram, picross, crossword)
- Color blocks that form binary when threshold applied
- Dots/dashes (Morse code visually encoded)
- Pixels arranged in a known grid format (e.g., 8×8 chess-like)
- Numbered grid: what is at position (row, col)?

### 9.4 — ASCII Art Decoding
- Standard ASCII art: read as text
- Braille pattern blocks (U+2800–U+28FF): `⠓⠑⠇⠇⠕` → decode each cell
- Box-drawing characters forming a diagram: what does the diagram represent?
- ASCII art at different zoom levels — zooming out may reveal a different image

### 9.5 — Rotation & Reflection
- Rotate the image 90°, 180°, 270° — does new content appear?
- Mirror horizontally and vertically
- Apply these to text blocks, tables, and number grids
- Numbers that look like letters when rotated (7 → L, 1 → I, 0 → O, 6 → 9)
- Seven-segment digit rotation/reflection

---

## PHASE 10 — SYNTHESIS & SOLUTION ASSEMBLY <a name="phase-10"></a>

### 10.1 — Cross-Correlation Matrix
Create a matrix: for every finding, ask:
> "Which other findings does this constrain or connect to?"

```markdown
| Finding ID | Description          | Connects To     | Confidence |
|------------|----------------------|-----------------|------------|
| F-001      | Base64 blob in JS    | F-003, F-011    | HIGH       |
| F-003      | AES key in EXIF      | F-001, F-007    | MEDIUM     |
```

### 10.2 — Layered Decoding Protocol
When you think you have a final answer:
1. Is this a decoy? APT setups frequently have a "first layer" obvious answer that redirects to the real puzzle.
2. Apply ALL encoding checks to the answer itself.
3. Does the answer point to another URL, file, or coordinate?
4. What does the answer MEAN in context? Is the meaning itself significant?

### 10.3 — Completeness Checklist
Before declaring a puzzle solved, verify:
- [ ] Every image has been analyzed (stego, EXIF, pixels)
- [ ] Every file has been analyzed (strings, metadata, format quirks)
- [ ] Every number has been tested through all transforms
- [ ] Every text block has been processed (encoding, acrostic, first/last letters)
- [ ] All HTTP artifacts examined (headers, cookies, timing)
- [ ] DNS and certificate examined
- [ ] Historical snapshots compared
- [ ] JavaScript fully deobfuscated
- [ ] CSS fully inspected
- [ ] All found coordinates resolved to physical locations
- [ ] All found hashes tested against common wordlists
- [ ] Zero-width and invisible characters extracted
- [ ] Homoglyphs detected and collected

### 10.4 — Solution Documentation
```markdown
# FINAL_ANSWER.md

## Puzzle: [Name/URL]
## Date Solved: [timestamp]
## Solvers: [agent IDs]

### The Answer
[State the complete answer clearly]

### Solution Path
1. [First significant discovery and how found]
2. [Second step...]
...

### Evidence Chain
- Finding F-001 → [description] → led to [next step]
- Finding F-002 → [description] → confirmed by [evidence]

### Alternate Paths Explored (Dead Ends)
- [Hypothesis]: [why it failed]

### Artifacts
- Key file: research/04_crypto/cipher_attempts/final_decrypt.txt
- Key image: research/05_stego/lsb_extractions/stage3.png
```

---

## TOOLCHAIN REFERENCE <a name="toolchain-reference"></a>

### Encoding & Crypto
| Tool | Purpose |
|------|---------|
| `CyberChef` | Universal encoding chain builder (web UI) |
| `python3` + `base64` | Programmatic decode/encode |
| `openssl` | Modern crypto operations |
| `hashcat` / `john` | Hash cracking |
| `hash-identifier` | Hash type detection |
| `gpg` | PGP decryption |

### Steganography
| Tool | Purpose |
|------|---------|
| `steghide` | Stego in JPEG/BMP/WAV |
| `zsteg` | PNG/BMP LSB stego |
| `stegsolve` | Bit-plane viewer (Java) |
| `binwalk` | Embedded file detection |
| `foremost` | File carving |
| `outguess` | JPEG DCT stego |
| `sox` | Audio spectrogram |
| `stegsnow` | Whitespace stego |

### Image Analysis
| Tool | Purpose |
|------|---------|
| `exiftool` | Full metadata extraction |
| `identify` (ImageMagick) | Image properties |
| `zbarimg` | QR/barcode scanning |
| `PIL/Pillow` | Python pixel analysis |

### Text & Linguistic
| Tool | Purpose |
|------|---------|
| `strings` | Binary string extraction |
| `unicode` Python module | Codepoint analysis |
| `xortool` | XOR analysis |

### Network
| Tool | Purpose |
|------|---------|
| `curl` | HTTP capture |
| `wget` | Site mirroring |
| `dig` | DNS queries |
| `openssl s_client` | TLS inspection |
| `wireshark` / `tshark` | Packet capture |

---

## ANTI-PATTERNS & TRAPS TO AVOID <a name="anti-patterns"></a>

### ❌ STOP. Do NOT do these things.

1. **Stopping at the first answer.** APT-level puzzles have minimum 3 layers. Your first "answer" is usually the decoy.

2. **Ignoring zero-width characters.** Check EVERY text blob with a hex editor. What looks empty may be full.

3. **Assuming the file type from the extension.** A `.jpg` may be a ZIP. A `.png` may be a PDF. Always verify magic bytes.

4. **Skipping the HTTP headers.** The puzzle answer has been in an `X-Hint` header before. Check every header.

5. **Treating numbers as just numbers.** Every number has at least 6 different interpretations. Try all of them.

6. **Ignoring whitespace.** The difference between tabs and spaces, between single and double spaces, is signal.

7. **Only checking visible text.** Hidden `<div>` elements, `opacity:0`, `color:#fff` on white background — all common tricks.

8. **Assuming encryption means you need a key you don't have.** The key is always somewhere in the puzzle. You have not looked hard enough.

9. **Not examining the thumbnail.** The embedded JPEG thumbnail in EXIF is often completely different from the main image.

10. **Giving up on a dead end without recording it.** Document every path. Dead ends form patterns.

11. **Reading only left-to-right.** Hebrew, Arabic, Tibetan, and other RTL scripts in unexpected places are intentional.

12. **Ignoring the filename.** The filename (without extension) is part of the puzzle. So is the file extension. So is the path.

13. **Not checking the SVG path data as coordinates.** `d="M 42 137 L 255 0"` — those numbers mean something.

14. **Forgetting that colors are numbers.** `#C0FFEE` is a number. `rgb(13, 37, 42)` is a number. So is the alpha channel.

---

## AGENT COLLABORATION PROTOCOL <a name="agent-collaboration-protocol"></a>

### Multi-Agent Swarm Structure
When deploying multiple agents on the same puzzle:

```
COORDINATOR_AGENT
├── RECON_AGENT         ← Handles Phases 0–2
├── ENCODING_AGENT      ← Handles Phases 3–4
├── STEGO_AGENT         ← Handles Phase 5
├── CRYPTO_AGENT        ← Handles Phase 6
├── FORENSICS_AGENT     ← Handles Phase 7
├── LINGUISTIC_AGENT    ← Handles Phase 8
├── VISUAL_AGENT        ← Handles Phase 9
└── SYNTHESIS_AGENT     ← Handles Phase 10
```

### Inter-Agent Communication Format
Every agent MUST report findings in this format:
```json
{
  "agent": "STEGO_AGENT",
  "phase": 5,
  "timestamp": "2025-01-01T00:00:00Z",
  "finding_id": "F-042",
  "type": "stego_lsb",
  "asset": "research/01_assets/images/banner.png",
  "description": "LSB extraction yielded base64 string",
  "raw_data": "SGVsbG8gV29ybGQ=",
  "confidence": "HIGH",
  "next_action": "Pass to ENCODING_AGENT for base64 decode",
  "connects_to": ["F-037", "F-011"]
}
```

### Coordinator Rules
- COORDINATOR maintains the master `README.md` — updated after every agent report
- No finding is ignored — even if it seems irrelevant, log it
- SYNTHESIS_AGENT only activates when ALL other agents have completed their initial pass
- Agents may be re-tasked based on synthesis findings
- The puzzle is not solved until COORDINATOR signs off on the final solution

---

## LOGGING & EVIDENCE STANDARDS <a name="logging-standards"></a>

### Evidence Chain of Custody
Every piece of evidence must be traceable:
```
Source → Extraction Method → Finding → Interpretation → Connection
```

### Confidence Levels
- **CONFIRMED**: Independently verifiable, no ambiguity
- **HIGH**: Strong evidence, minimal alternative explanations
- **MEDIUM**: Plausible but requires corroboration
- **LOW**: Speculative, needs more evidence
- **DEAD_END**: Exhausted, no results, documented for pattern analysis

### The Iron Rule of Logging
> **If it is not written down, it did not happen.**

Log every command you run. Log every output. Log every hypothesis, even wrong ones. The pattern of wrong hypotheses often points to the right one.

### README.md Structure (Living Document)
```markdown
# Puzzle Research Log

## Target: [URL]
## Status: IN_PROGRESS | PARTIAL | SOLVED

## Timeline
- [timestamp] — Phase X started
- [timestamp] — Finding F-001 discovered: [one-line description]
- [timestamp] — Hypothesis H-001 formed: [claim]
- [timestamp] — Hypothesis H-001 CONFIRMED / REJECTED

## Current Best Hypothesis
[One paragraph describing the most likely solution path]

## Open Questions
1. What does [X] decode to?
2. Where is the key for [cipher]?

## Confirmed Facts
- [Fact 1]
- [Fact 2]

## Dead Ends
- [Approach]: [Why it failed]
```

---

*"In the world of APT puzzles, what is hidden is not random — it is precise, intentional, and layered. Your job is not to guess. Your job is to be more systematic than the person who hid it."*

---

**AGENTS.md** · APT Puzzle Intelligence Framework · v1.0  
*Created for autonomous and human-agent hybrid puzzle-solving operations.*
