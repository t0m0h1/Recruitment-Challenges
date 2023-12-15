# Description: Check if a string is a palindrome.

s = 'a man, a plan, a canal: panama'

def preprocess(s: str) -> str:
    # Preprocess a string to remove all non-alphanumeric characters and convert to lowercase.
    return "".join(filter(str.isalnum, s)).lower()

def palindrome(s: str) -> bool:
    # Check if a string is a palindrome.
    return s == s[::-1]

if __name__ == '__main__':
    print('\n')
    print('Palindrome String: ')
    print(palindrome(preprocess(s)))


