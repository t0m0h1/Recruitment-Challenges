s1 = 'listen'
s2 = 'silent'

def is_anagram(s1, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

if __name__ == '__main__':
    print('\n')
    print('Is this an anagram: ')
    print(is_anagram(s1, s2), '\n')