def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    fin_word = ''
    vowels = []

    for char in s:
        # print(f"this is current char: {char}")
        if char in 'aeiouAEIOU':
            # print(f"this is a vowel: {char}")
            # print(f"this is vowel list before appending new char: {vowels}")

            vowels.append(char)

            # print(f"this is vowel liste after appending new char: {vowels}")

    # print(f"this is vowel list before reversing: {vowels}")
    vowels.reverse()
    # print(f"this is vowel list after reversing: {vowels}")
    for letter in s:
        # print(f"this is current letter: {letter}")
        if letter.lower() in 'aeiou':
            # print(f"this is finished word before adding the reversed vowel: {fin_word}")

            fin_word += vowels[0]

            # print(
            #     f"this is fin word after adding the reversed vowel: {fin_word}")
            # print(f"this is vowel list before popping letter off: {vowels}")

            vowels.pop(0)

            # print(f"this is vowerl list after popping off letter: {vowels}")
        else:
            fin_word += letter
    return fin_word


print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))
