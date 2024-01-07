def reverse(x: int) -> int:
    reversed_x = 0
    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10
    return reversed_x

if __name__ == '__main__':
    print(reverse(12345))
    print(reverse(54321))
    print(reverse(1000))
    print(reverse(1))
    print(reverse(0))