# #!/usr/bin/python3

import random
def get_random_string(length: int) -> str:
    lowalphabet = [chr(value) for value in range(97, 123)]
    print(lowalphabet)
    upperalphabet = [chr(value) for value in range(65, 91)]
    print(upperalphabet)
    nums = [chr(value) for value in range(48, 58)]
    print(nums)
    reslst = [*lowalphabet, *upperalphabet, *nums]
    # print("".join(random.sample(reslst, k=length)))
    print("".join(random.choices(reslst, k=length)))

get_random_string(180)

