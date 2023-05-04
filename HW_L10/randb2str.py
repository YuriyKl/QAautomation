# #!/usr/bin/python3

import random
def get_random_string(length: int) -> str:
    lowalphabet = [chr(value) for value in range(97, 123)]
    upperalphabet = [chr(value) for value in range(65, 91)]
    nums = [chr(value) for value in range(48, 58)]
    reslst = [*lowalphabet, *upperalphabet, *nums]
    # print("".join(random.sample(reslst, k=length))) '''this solution with 'random.sample' takes unique symbol
    # from the string thus it causes limits string length to 62 (26+26+10) symbols'''
    return print("".join(random.choices(reslst, k=length)))

get_random_string(180)

