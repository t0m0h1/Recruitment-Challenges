def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.
    """
    vowels = 'aeiou'
    return sum(1 for char in s if char in vowels)


if __name__ == '__main__':
    # Test the function with sample inputs
    input_str = "hello"
    input_str2 = "world"
    
    print(count_vowels(input_str))  # Output: 2
    print(count_vowels(input_str2))  # Output: 1