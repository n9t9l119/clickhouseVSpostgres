import timeit

print(timeit.timeit("1+1", number=10000000))
print(timeit.timeit("1+1", number=100000000))
