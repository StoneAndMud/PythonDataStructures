def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    my_dict = {}
    for char in phrase:
        if char.lower() in "aeiou":
            if char.lower() not in my_dict:
                my_dict[char.lower()] = 1
            else:
                my_dict[char.lower()] += 1
        else:
            continue
    return my_dict


print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))
