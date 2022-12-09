'''
Description:
Welcome.
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
'''
def alphabet_position(my_str):
    my_str = my_str.casefold()
    new_str = ''
    for i in my_str:
        if i.isalpha():
            new_str = new_str + ''.join(i)
    abc = new_str.maketrans({'a': '1 ', 'b': '2 ', 'c': '3 ', 'd': '4 ', 'e': '5 ', 'f': '6 ', 'g': '7 ', 'h': '8 ',
                        'i': '9 ', 'j': '10 ', 'k': '11 ', 'l': '12 ', 'm': '13 ', 'n': "14 ", 'o': '15 ', 'p': '16 ',
                        'q': '17 ', 'r': '18 ', 's': '19 ', 't': '20 ', 'u': '21 ', 'v': '22 ', 'w': '23 ', 'x': '24 ',
                        'y': '25 ', 'z': '26 '})
    return new_str.translate(abc).strip()
