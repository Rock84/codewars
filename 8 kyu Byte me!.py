'''If I were to ask you the size of "hello", what would you say?

Wait, let me rephrase the question:

If I were to ask you the total byte size of "hello",
how many bytes do you think it takes up?

I'll give you a hint: it's not 5.'''

import sys
def total_bytes(object):
    return sys.getsizeof(object)


