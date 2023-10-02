def my_function():
    return None

def my_generator():
    yield
    return

print(f'{my_function  = }')
print(f'{my_function()  = }') # Results

print(f'{my_generator  = }')
print(f'{my_generator()  = }') # Intermediation for getting results

print(f'\n\n\n')

def my_function_1( data, *, mode):
    if mode:
        return data ** 2
    
    return data ** 3

def my_generator_2(data, *, mode):
    if mode:
        yield data ** 2
    
    yield data ** 3

print(f"{my_function_1(3,mode=True) = }")