def fizzbuzz():
    # Create list of numbers between 1 and 100
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'FizzBuzz {i}') # Print FizzBuzz and the particular number if divisible by both 3 and 5
        elif i % 3 == 0:
            print(f'Fizz {i}') # Print Fizz and the particular number if divisible by 3
        elif i % 5 == 0:
            print(f'Buzz {i}') # Print Buzz and the particular number if divisible by 5
        else:
            print(f'None {i}') # Print the number itself if not divisible by either 3 or 5

if __name__ == '__main__':
    fizzbuzz()

