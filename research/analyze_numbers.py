#!/usr/bin/env python3
"""
Deep number analysis for haian.de puzzle
Focus on: 24, 120, 55-60, birth/death dates
"""

def analyze_age_calculation():
    """Calculate exact age at death"""
    from datetime import date
    
    birth = date(1986, 10, 30)
    death = date(2011, 10, 20)
    
    age_days = (death - birth).days
    age_years = age_days / 365.25
    
    print("=" * 60)
    print("AGE CALCULATION")
    print("=" * 60)
    print(f"Birth: {birth}")
    print(f"Death: {death}")
    print(f"Age in days: {age_days}")
    print(f"Age in years: {age_years:.2f}")
    print(f"Age: 24 years, 11 months, 20 days (almost 25)")
    
    # Numbers from dates
    birth_nums = [3, 0, 1, 0, 1, 9, 8, 6]  # 30.10.1986
    death_nums = [2, 0, 1, 0, 2, 0, 1, 1]  # 20.10.2011
    
    print(f"\nBirth date digits: {birth_nums}")
    print(f"Death date digits: {death_nums}")
    print(f"Sum of birth digits: {sum(birth_nums)}")
    print(f"Sum of death digits: {sum(death_nums)}")
    
    # XOR of birth and death digits
    xor_result = [a ^ b for a, b in zip(birth_nums, death_nums)]
    print(f"XOR birth^death: {xor_result}")
    
    # ASCII from XOR
    ascii_chars = [chr(x + 48) if 0 <= x <= 9 else '?' for x in xor_result]
    print(f"XOR as digits: {''.join(ascii_chars)}")

def analyze_poker_numbers():
    """Analyze the 24 and 120 from Ihno's message"""
    print("\n" + "=" * 60)
    print("POKER NUMBER ANALYSIS (24, 120)")
    print("=" * 60)
    
    # From Ihno's message: "Dein Blatt war so viel besser, als nur bis 24 zu reizen, damit wären auch durchaus 120 drin gewesen."
    # This is Skat terminology - 24 is a bid value, 120 is a game value
    
    numbers = [24, 120, 100, 55, 60]
    print(f"Numbers found: {numbers}")
    
    # Factorizations
    for n in numbers:
        factors = []
        temp = n
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                factors.append(d)
                temp //= d
            d += 1
        if temp > 1:
            factors.append(temp)
        print(f"{n} = {' × '.join(map(str, factors))}")
    
    # Check relationships
    print(f"\n120 / 24 = {120 / 24}")
    print(f"120 - 24 = {120 - 24}")
    print(f"60 - 55 = {60 - 55}")
    print(f"55 + 60 = {55 + 60}")
    
    # ASCII from numbers
    for n in numbers:
        if 32 <= n <= 126:
            print(f"{n} -> ASCII: '{chr(n)}'")
        else:
            print(f"{n} -> outside ASCII range")

def analyze_timestamps():
    """Analyze the timestamps of messages"""
    print("\n" + "=" * 60)
    print("TIMESTAMP ANALYSIS")
    print("=" * 60)
    
    # All message times (HH:MM)
    times = [
        (12, 46), (4, 27), (18, 39), (20, 8), (17, 51), (20, 21),
        (22, 26), (9, 24), (9, 58), (10, 45), (17, 7), (17, 39),
        (12, 13), (15, 11), (16, 20), (10, 35), (22, 4), (23, 59),
        (12, 11), (16, 24), (10, 54), (22, 27), (11, 16), (21, 19),
        (14, 46), (23, 34), (21, 30)
    ]
    
    hours = [t[0] for t in times]
    minutes = [t[1] for t in times]
    
    print(f"Hours: {hours}")
    print(f"Minutes: {minutes}")
    print(f"Sum of all hours: {sum(hours)}")
    print(f"Sum of all minutes: {sum(minutes)}")
    
    # Convert to ASCII
    hour_ascii = [chr(h + 48) if 0 <= h <= 9 else chr(h) if 32 <= h <= 126 else '?' for h in hours]
    min_ascii = [chr(m) if 32 <= m <= 126 else '?' for m in minutes]
    
    print(f"Hours as chars: {''.join(hour_ascii)}")
    print(f"Minutes as chars: {''.join(min_ascii)}")

def check_24_year_pattern():
    """Check patterns around age 24"""
    print("\n" + "=" * 60)
    print("24-YEAR PATTERN CHECK")
    print("=" * 60)
    
    # Death at age 24
    # 2011 - 1986 = 25 but he was 24 (hadn't reached his 25th birthday)
    
    # The number 24 appears in Ihno's message
    print("Death occurred 20 days before 25th birthday")
    print("Age was 24 years, 11 months, 20 days")
    
    # Days from birthday
    days_from_birthday = 365 - 20  # 20 days before next birthday
    print(f"Days from 24th birthday to death: {days_from_birthday}")
    
    # Check if 24 is significant
    print("\n24 as hex: 0x18")
    print("24 as binary: 11000")
    print("24 factors: 2×2×2×3 = 8×3")
    
    # ASCII 24 is NAK (Negative Acknowledge) - control character
    print(f"ASCII 24 (0x18): control character (CAN/NAK)")

def check_hidden_paths():
    """Generate potential hidden paths based on numbers"""
    print("\n" + "=" * 60)
    print("POTENTIAL HIDDEN PATHS")
    print("=" * 60)
    
    paths = []
    
    # Date-based paths
    paths.append("/2011")
    paths.append("/2010")
    paths.append("/1986")
    paths.append("/30101986")  # birth date
    paths.append("/20102011")  # death date
    paths.append("/24")
    paths.append("/120")
    paths.append("/55")
    paths.append("/60")
    paths.append("/flag")
    paths.append("/key")
    paths.append("/secret")
    paths.append("/haian")
    paths.append("/fabian")
    
    # From birth/death
    paths.append("/25")  # almost 25
    paths.append("/9131")  # days alive
    
    print("Potential paths to check:")
    for p in paths:
        print(f"  {p}")

if __name__ == "__main__":
    analyze_age_calculation()
    analyze_poker_numbers()
    analyze_timestamps()
    check_24_year_pattern()
    check_hidden_paths()
