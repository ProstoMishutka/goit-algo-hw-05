def caching_fibonacci():
    cache = {} # Creating a cache

    def fibonacci(n):
        print(cache)
        if n <= 1:
            return n
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci # Return the function - fibonacci.

func = caching_fibonacci() # Receive the function - fibonacci
print(func(10)) # Pass arguments to the function fibonacci(10)