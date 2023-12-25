def even_or_odd(n: int) -> str:
    # return odd or even depending on the number
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

if __name__ == "__main__":
    print(even_or_odd(2))
    print(even_or_odd(3))