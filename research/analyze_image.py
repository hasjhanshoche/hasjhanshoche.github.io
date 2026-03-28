#!/usr/bin/env python3
"""
Image metadata and steganography analysis for haian.de memorial image
"""

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
import sys

IMAGE_PATH = "research/01_assets/images/haian_mit_text_skaliert_rand.jpeg"

def extract_exif(image_path):
    """Extract all EXIF metadata from image"""
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        
        print("=" * 60)
        print("EXIF METADATA ANALYSIS")
        print("=" * 60)
        
        if exif_data:
            exif = {}
            gps_info = {}
            
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                exif[tag] = value
                
                # Check for GPS info
                if tag == "GPSInfo":
                    for key in value:
                        sub_tag = GPSTAGS.get(key, key)
                        gps_info[sub_tag] = value[key]
                
                print(f"{tag:25s}: {value}")
            
            if gps_info:
                print("\n" + "=" * 60)
                print("GPS COORDINATES FOUND")
                print("=" * 60)
                for tag, value in gps_info.items():
                    print(f"{tag:25s}: {value}")
            
            return exif, gps_info
        else:
            print("No EXIF data found")
            return {}, {}
            
    except Exception as e:
        print(f"Error extracting EXIF: {e}")
        return {}, {}

def analyze_image_properties(image_path):
    """Analyze basic image properties"""
    try:
        image = Image.open(image_path)
        
        print("\n" + "=" * 60)
        print("IMAGE PROPERTIES")
        print("=" * 60)
        print(f"Format: {image.format}")
        print(f"Mode: {image.mode}")
        print(f"Size: {image.size}")
        print(f"Width: {image.width}")
        print(f"Height: {image.height}")
        print(f"File size: {os.path.getsize(image_path)} bytes")
        
        # Check for transparency/alpha channel
        if image.mode in ('RGBA', 'LA', 'P'):
            print("Image has alpha channel (potential for hidden data)")
        
        # Get color palette if applicable
        if image.mode == 'P':
            palette = image.getpalette()
            print(f"Palette size: {len(palette) if palette else 0} entries")
            
    except Exception as e:
        print(f"Error analyzing image: {e}")

def extract_lsb(image_path, bits=1):
    """Extract LSB data from image"""
    try:
        image = Image.open(image_path)
        
        print("\n" + "=" * 60)
        print(f"LSB EXTRACTION ({bits} bit(s))")
        print("=" * 60)
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        pixels = list(image.getdata())
        
        # Extract LSB from each channel
        extracted_bytes = []
        byte = 0
        bit_count = 0
        
        for pixel in pixels:
            for channel in pixel[:3]:  # R, G, B
                # Extract LSB(s)
                lsb = channel & ((1 << bits) - 1)
                byte = (byte << bits) | lsb
                bit_count += bits
                
                if bit_count >= 8:
                    extracted_bytes.append(byte & 0xFF)
                    byte = 0
                    bit_count = 0
        
        # Save extracted data
        output_path = f"research/05_stego/lsb_extractions/lsb_{bits}bit_extracted.raw"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(bytes(extracted_bytes))
        
        # Check for printable content at start
        preview = bytes(extracted_bytes[:200])
        print(f"First 200 bytes (raw): {preview}")
        print(f"First 200 bytes (hex): {preview.hex()}")
        
        # Try to decode as text
        try:
            text_preview = preview.decode('utf-8', errors='ignore')
            print(f"First 200 bytes (utf-8): {text_preview[:200]}")
        except:
            pass
        
        # Check for common file signatures
        signatures = {
            b'\x89PNG': 'PNG',
            b'\xff\xd8\xff': 'JPEG',
            b'GIF87a': 'GIF',
            b'GIF89a': 'GIF',
            b'PK\x03\x04': 'ZIP',
            b'Rar!': 'RAR',
            b'%PDF': 'PDF',
            b'<?xml': 'XML',
            b'<html': 'HTML',
        }
        
        data = bytes(extracted_bytes)
        for sig, ftype in signatures.items():
            if data.startswith(sig):
                print(f"*** FOUND {ftype} SIGNATURE IN LSB DATA ***")
                output_file = f"research/05_stego/lsb_extractions/extracted.{ftype.lower()}"
                with open(output_file, 'wb') as f:
                    f.write(data)
                print(f"Saved to: {output_file}")
        
        return extracted_bytes
        
    except Exception as e:
        print(f"Error extracting LSB: {e}")
        return []

def check_specific_bytes(image_path):
    """Check specific byte patterns that might indicate stego"""
    try:
        with open(image_path, 'rb') as f:
            data = f.read()
        
        print("\n" + "=" * 60)
        print("BINARY PATTERN ANALYSIS")
        print("=" * 60)
        
        # Check for appended data after EOI marker
        eoi_marker = data.find(b'\xff\xd9')
        if eoi_marker != -1:
            print(f"EOI marker found at offset: {eoi_marker}")
            trailing_data = data[eoi_marker+2:]
            if trailing_data:
                print(f"*** TRAILING DATA FOUND: {len(trailing_data)} bytes ***")
                print(f"First 100 bytes (hex): {trailing_data[:100].hex()}")
                print(f"First 100 bytes (raw): {trailing_data[:100]}")
                
                # Save trailing data
                output_path = "research/05_stego/trailing_data.bin"
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'wb') as f:
                    f.write(trailing_data)
            else:
                print("No trailing data after EOI marker")
        
        # Check for unusual markers
        print("\nScanning for hidden markers...")
        markers = [b'stego', b'hidden', b'secret', b'flag', b'key', b'password',
                   b'-----BEGIN', b'-----END', b'<?php', b'<script']
        
        for marker in markers:
            pos = data.find(marker)
            if pos != -1:
                print(f"Found '{marker.decode()}' at offset {pos}")
                context = data[max(0, pos-50):min(len(data), pos+100)]
                print(f"  Context: {context}")
        
    except Exception as e:
        print(f"Error checking patterns: {e}")

if __name__ == "__main__":
    print("Analyzing memorial image from haian.de")
    print("=" * 60)
    
    analyze_image_properties(IMAGE_PATH)
    extract_exif(IMAGE_PATH)
    check_specific_bytes(IMAGE_PATH)
    extract_lsb(IMAGE_PATH, bits=1)
    extract_lsb(IMAGE_PATH, bits=2)
    
    print("\n" + "=" * 60)
    print("Analysis complete")
    print("=" * 60)
