import sys

def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 palindrome.py <string>")
        sys.exit(1)
    input_str = sys.argv[1]
    if is_palindrome(input_str):
        print(f"{input_str} is a palindrome")
    else:
        print(f"{input_str} is not a palindrome")