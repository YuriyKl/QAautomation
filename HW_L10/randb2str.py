# #!/usr/bin/python3

import random
def get_random_string(length: int) -> str:
    lowalphabet = [chr(value) for value in range(97, 123)]
    upperalphabet = [chr(value) for value in range(65, 90)]
    nums = [chr(value) for value in range(48, 57)]
    reslst = [*lowalphabet, *upperalphabet, *nums]
    print("".join(random.sample(reslst, k=length)))

get_random_string(9)
