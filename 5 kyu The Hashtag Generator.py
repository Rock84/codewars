'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

'''

def generate_hashtag(my_str):
    new_str = ['#']
    my_str = my_str.split()
    if my_str:
        for _ in range(len(my_str)):
            my_str[_] = my_str[_].capitalize()
            new_str.append(my_str[_])
        if len(''.join(new_str)) > 140:
            return False
        else:
            return ''.join(new_str)
    else:
        return False
