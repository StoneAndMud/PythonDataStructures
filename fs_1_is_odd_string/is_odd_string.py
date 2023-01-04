def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:

        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:

        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:

        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here
    total = 0
    for char in word:
        #     print(f"this is current char: {char} in word: {word}")
        #     print(f"this is the num value of char: {ord(char)} in word: {word}")
        total += ord(char)
        # print(f"this is new total: {total}")
    if total % 2 != 0:
        # print(f"the number:{ord(char)} is divisible by 3")
        return True
    return False


print(is_odd_string('a'))
print(is_odd_string('A'))
print(is_odd_string('aaaa'))
print(is_odd_string('AAaa'))
print(is_odd_string('amazing'))
