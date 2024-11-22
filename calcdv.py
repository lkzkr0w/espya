import sys
import re

TAB_VAL = {
    'A': (1, 4), 'B': (0, 1), 'C': (0, 0),
    'D': (1, 6), 'E': (0, 5), 'F': (2, 0),
    'G': (1, 9), 'H': (0, 9), 'I': (2, 4),
    'J': (0, 7), 'K': (2, 1), 'L': (0, 8),
    'M': (0, 4), 'N': (1, 3), 'O': (2, 5),
    'P': (2, 2), 'Q': (1, 8), 'R': (1, 0),
    'S': (0, 2), 'T': (0, 6), 'U': (1, 2),
    'V': (2, 3), 'W': (1, 1), 'X': (0, 3),
    'Y': (1, 5), 'Z': (1, 7)
}

VALID_DOMAINS_REGEX = re.compile(
    r'^[A-Z]{3}[0-9]{3}$|^[0-9]{3}[A-Z]{3,4}$|^[A-Z][0-9]{7}$|^[A-Z]{2}[0-9]{3}[A-Z]{2}$|^[A-Z][0-9]{3}[A-Z]{3}$'
)

def validate_domain(domain):
    return VALID_DOMAINS_REGEX.match(domain)

def make_list(domain):
    return [
        digit for char in domain[::-1]
        for digit in (TAB_VAL[char] if char in TAB_VAL else (int(char),))
    ]

def calculate_verifier(list_values):
    total = sum(list_values)
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    return total

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    if not validate_domain(domain):
        print("[-] Invalid domain")
        sys.exit(1)

    reversed_values = make_list(domain)
    odd_positions = reversed_values[::2]
    even_positions = reversed_values[1::2]

    verifier_1 = calculate_verifier(odd_positions)
    verifier_2 = calculate_verifier(even_positions)

    print(f"[+] The verifier digit for {domain} is {verifier_1}{verifier_2}")

if __name__ == "__main__":
    main()
