
'''
Programs:100_python_program_20_generator.py
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

'''

#val = (num for num in range(0,1000) if num % 7 == 0 )

#print val

def generate_eg(max):
    for num in range(0, max):
        if num % 7 == 0:
            yield num

generate = generate_eg(1000)
print generate
print next(generate)
print next(generate)
print next(generate)
print next(generate)

print list(generate)
