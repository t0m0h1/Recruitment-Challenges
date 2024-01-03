def palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    print(palindrome(12345))
    print(palindrome(1111))
    print(palindrome(1000))
    print(palindrome(1))
    print(palindrome(0))
    print(palindrome(12321))