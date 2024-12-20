def multiply_tuples(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must have the same length.")
    
    product_tuple = tuple(a * b for a, b in zip(tuple1, tuple2))
    return product_tuple

tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)

result = multiply_tuples(tuple1, tuple2)

print(f"The product of {tuple1} and {tuple2} is: {result}")