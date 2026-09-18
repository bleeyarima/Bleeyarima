#!/usr/bin/env python3
import sys

def caesar(text, shift, decrypt=False):
    """Apply Caesar cipher with given shift. If decrypt=True, reverse the shift."""
    if decrypt:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift) % 26
            result.append(chr(shifted + ascii_offset))
        else:
            result.append(char)  # preserve non‑letters
    return ''.join(result)

def main():
    if len(sys.argv) < 4:
        print("Usage:")
        print("  Encrypt: python cipher.py -e <shift> <text>")
        print("  Decrypt: python cipher.py -d <shift> <text>")
        print("Example: python cipher.py -e 3 'Hello World'")
        sys.exit(1)

    mode = sys.argv[1]
    try:
        shift = int(sys.argv[2])
    except ValueError:
        print("Shift must be an integer.")
        sys.exit(1)

    text = ' '.join(sys.argv[3:])  # allow spaces in text

    if mode == "-e":
        result = caesar(text, shift, decrypt=False)
        print(f"Encrypted: {result}")
    elif mode == "-d":
        result = caesar(text, shift, decrypt=True)
        print(f"Decrypted: {result}")
    else:
        print("Invalid mode. Use -e or -d.")

if __name__ == "__main__":
    main()