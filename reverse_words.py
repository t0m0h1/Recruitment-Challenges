def reverse_words(string: str) -> str:
    output = " "
    return output.join(string.split()[::-1])



if __name__ == "__main__":
    print(reverse_words("hello world here"))


# The reverse_words function splits the input string into a list of words using split().
# It then reverses the list with [::-1]
# then joins the reversed list back into a string with spaces in between the words using join().