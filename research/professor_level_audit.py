#!/usr/bin/env python3
"""
PROFESSOR-LEVEL DEEP MATHEMATICAL AUDIT
Think like a mathematician: look for abstract connections, symmetries, invariants
"""

import math
from collections import Counter
from PIL import Image
import os

# All key numbers from the puzzle
KEY_NUMBERS = {
    'birth_year': 1986,
    'birth_month': 10,
    'birth_day': 30,
    'death_year': 2011,
    'death_month': 10,
    'death_day': 20,
    'age_years': 24,
    'age_months': 11,
    'age_days': 20,
    'days_lived': 9121,
    'skat_24': 24,
    'skat_120': 120,
    'thomas_55': 55,
    'thomas_60': 60,
    'key_number': 5,
    'image_width': 700,
    'image_height': 1000,
    'image_bytes': 269508,
}

# Isabella's date: 24.02.2012
ISABELLA_DATE = (24, 2, 2012)

def prime_factorization(n):
    """Full prime factorization"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def totient(n):
    """Euler's totient function"""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def deep_factorization_analysis():
    """Deep analysis of prime factorizations - professor level"""
    print("="*70)
    print("PROFESSOR-LEVEL DEEP FACTORIZATION ANALYSIS")
    print("="*70)
    
    print("\n1. COMPLETE PRIME FACTORIZATION OF ALL KEY NUMBERS")
    print("-"*70)
    
    for name, num in KEY_NUMBERS.items():
        factors = prime_factorization(num)
        if len(factors) == 1 and factors[0] == num:
            print(f"{name:15s}: {num:8d} = PRIME")
        else:
            factor_str = ' × '.join(map(str, factors))
            print(f"{name:15s}: {num:8d} = {factor_str}")
    
    print("\n2. EULER'S TOTIENT FUNCTION ANALYSIS")
    print("-"*70)
    print("Totient phi(n) counts numbers < n coprime to n")
    
    interesting_totients = []
    for name, num in KEY_NUMBERS.items():
        phi = totient(num)
        # Check if phi relates to other numbers
        for other_name, other_num in KEY_NUMBERS.items():
            if other_name != name:
                if phi == other_num:
                    interesting_totients.append((name, num, phi, other_name))
        print(f"{name:15s}: phi({num}) = {phi}")
    
    if interesting_totients:
        print("\n[!] TOTIENT CONNECTIONS FOUND:")
        for name, num, phi, other in interesting_totients:
            print(f"\nGolden ratio phi = {phi:.6f} = {other}")

def advanced_gcd_analysis():
    """GCD and LCM analysis - looking for hidden structures"""
    print("\n" + "="*70)
    print("ADVANCED GCD/LCM ANALYSIS")
    print("="*70)
    
    numbers = list(KEY_NUMBERS.values())
    names = list(KEY_NUMBERS.keys())
    
    print("\n3. PAIRWISE GCD MATRIX (Greatest Common Divisors)")
    print("-"*70)
    
    # Find pairs with interesting GCDs
    interesting_pairs = []
    for i, (n1_name, n1) in enumerate(KEY_NUMBERS.items()):
        for j, (n2_name, n2) in enumerate(KEY_NUMBERS.items()):
            if i < j:  # Avoid duplicates
                g = math.gcd(n1, n2)
                if g > 1:
                    print(f"gcd({n1_name}, {n2_name}) = {g}")
                    if g == 5 or g == 24 or g == 120:
                        interesting_pairs.append((n1_name, n2_name, g))
    
    if interesting_pairs:
        print("\n[!] SPECIAL GCD CONNECTIONS:")
        for n1, n2, g in interesting_pairs:
            print(f"    {n1} and {n2} share factor {g}")
    
    print("\n4. LEAST COMMON MULTIPLE ANALYSIS")
    print("-"*70)
    
    # LCM of key pairs
    key_pairs = [
        ('skat_24', 'skat_120'),
        ('thomas_55', 'thomas_60'),
        ('age_years', 'skat_24'),
        ('image_width', 'image_height'),
    ]
    
    for n1_name, n2_name in key_pairs:
        if n1_name in KEY_NUMBERS and n2_name in KEY_NUMBERS:
            n1, n2 = KEY_NUMBERS[n1_name], KEY_NUMBERS[n2_name]
            lcm = (n1 * n2) // math.gcd(n1, n2)
            print(f"lcm({n1_name}, {n2_name}) = lcm({n1}, {n2}) = {lcm}")
            
            # Check if LCM relates to other numbers
            for other_name, other in KEY_NUMBERS.items():
                if other_name not in [n1_name, n2_name]:
                    if lcm == other:
                        print(f"    [!] LCM equals {other_name}!")

def number_theory_deep_dive():
    """Deep number theory analysis"""
    print("\n" + "="*70)
    print("NUMBER THEORY DEEP DIVE")
    print("="*70)
    
    print("\n5. MODULAR ARITHMETIC ANALYSIS")
    print("-"*70)
    
    # Check congruences
    mod_bases = [5, 24, 120, 55, 60, 9121]
    
    for base in mod_bases:
        print(f"\nModulo {base}:")
        residues = {}
        for name, num in KEY_NUMBERS.items():
            r = num % base
            if r not in residues:
                residues[r] = []
            residues[r].append(name)
        
        # Find collisions (same residue)
        for r, names_list in residues.items():
            if len(names_list) > 1:
                print(f"    [!] Same residue {r}: {', '.join(names_list)}")
    
    print("\n6. SUM OF DIVISORS ANALYSIS")
    print("-"*70)
    
    def sum_of_divisors(n):
        total = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
        return total
    
    for name, num in KEY_NUMBERS.items():
        if num <= 10000:  # Only for smaller numbers
            sigma = sum_of_divisors(num)
            # Check if sum of divisors relates to other numbers
            for other_name, other in KEY_NUMBERS.items():
                if sigma == other:
                    print(f"[!] sigma({name}) = {sigma} = {other_name}")

def abstract_algebra_connections():
    """Abstract algebra perspective"""
    print("\n" + "="*70)
    print("ABSTRACT ALGEBRA PERSPECTIVE")
    print("="*70)
    
    print("\n7. GROUP THEORY CONNECTIONS")
    print("-"*70)
    
    # Check if any numbers form cyclic groups
    print("Checking multiplicative orders...")
    
    for name, n in KEY_NUMBERS.items():
        if n > 1 and is_prime(n - 1):
            print(f"{name} = {n}: {n-1} is prime -> Z_{n}* is cyclic of order {n-1}")
    
    print("\n8. SYMMETRY ANALYSIS")
    print("-"*70)
    
    # Check for symmetric properties
    print("Checking for palindromic properties in different bases...")
    
    for name, num in KEY_NUMBERS.items():
        # Check if palindrome in different bases
        for base in [2, 8, 16]:
            s = ''
            n = num
            while n > 0:
                digit = n % base
                s = str(digit) + s
                n //= base
            if s == s[::-1] and len(s) > 1:
                print(f"[!] {name} = {num} is palindrome in base {base}: {s}")

def experimental_approaches():
    """Experimental mathematical approaches"""
    print("\n" + "="*70)
    print("EXPERIMENTAL MATHEMATICAL APPROACHES")
    print("="*70)
    
    print("\n9. FIBONACCI AND LUCAS NUMBER CHECKS")
    print("-"*70)
    
    # Generate Fibonacci numbers
    fib = [0, 1]
    for _ in range(50):
        fib.append(fib[-1] + fib[-2])
    
    fib_set = set(fib)
    
    for name, num in KEY_NUMBERS.items():
        if num in fib_set:
            idx = fib.index(num)
            print(f"[!] {name} = {num} is F_{idx} (Fibonacci number)")
    
    print("\n10. TRIANGULAR, SQUARE, CUBE NUMBER CHECKS")
    print("-"*70)
    
    for name, num in KEY_NUMBERS.items():
        # Triangular: n(n+1)/2
        # Solve n^2 + n - 2*num = 0
        disc = 1 + 8*num
        if disc >= 0:
            n = (-1 + math.sqrt(disc)) / 2
            if n == int(n) and n > 0:
                print(f"    [!] {name} = {num} is T_{int(n)} (triangular number)")
        
        # Square
        root = math.sqrt(num)
        if root == int(root):
            print(f"[!] {name} = {num} = {int(root)}^2 (perfect square)")
        
        # Cube
        croot = round(num ** (1/3))
        if croot**3 == num:
            print(f"[!] {name} = {num} = {croot}^3 (perfect cube)")
    
    print("\n11. MERSENNE AND FERMAT NUMBER CONNECTIONS")
    print("-"*70)
    
    # Mersenne: 2^p - 1
    for exp in range(2, 20):
        mersenne = 2**exp - 1
        for name, num in KEY_NUMBERS.items():
            if num == mersenne:
                print(f"[!] {name} = {num} = 2^{exp} - 1 (Mersenne number)")
            if num == exp:
                print(f"[!] {name} = {num} appears as Mersenne exponent for {mersenne}")

if __name__ == "__main__":
    deep_factorization_analysis()
    advanced_gcd_analysis()
    number_theory_deep_dive()
    abstract_algebra_connections()
    experimental_approaches()
    
    print("\n" + "="*70)
    print("PROFESSOR-LEVEL ANALYSIS COMPLETE")
    print("="*70)
