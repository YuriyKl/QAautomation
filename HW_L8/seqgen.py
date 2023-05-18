#!/usr/bin/python3
def generator(n, m):
    sq_gen = (i+1 for i in range(n))
    pow_gen = (pow(i+1, x+1) for x in range(m-1) for i in range(n+1))

    # def combine():
    #     sqgen = sq_gen()
    #     powgen = pow_gen()
    #     for i in sqgen:
    #         yield i
    #     for i in powgen:
    #         yield i
    #
    # for i in combine():
    #     print(i)
    '''   function combine does not operate 
    sqgen = sq_gen() 
    TypeError: 'generator' object is not callable'''

    # def combine():
    #     q1 = sq_gen()
    #     q2 = pow_gen()
    #     yield from q1
    #     yield from q2
    #
    # for i in combine():
    #     print(i) # same issue q1 = sq_gen()
    # TypeError: 'generator' object is not callable
    q1 = sq_gen()
    q2 = pow_gen()

    import itertools
    for i in itertools.chain(sq_gen(), pow_gen()):
        print(i)
     # #Grrr it`s not working  as well


generator(3,4)
