'''
Move the first letter of each word to the end of it, then add "ay"
to the end of the word. Leave punctuation marks untouched.
'''

def pig_it(my_str):
    new_str = []
    my_str = my_str.split()
    for _ in range(len(my_str)):
        if my_str[_].isalpha():
            new_str.append(my_str[_][1::] + my_str[_][:1:] + 'ay')
        else:
            if len(my_str[_]) == 1:
                new_str.append(my_str[_])
            else:
                my_str[_] = my_str[_].replace(',', '')
                new_str.append(my_str[_][1::] + my_str[_][:1:] + 'ay,')
    return (' '.join(new_str))