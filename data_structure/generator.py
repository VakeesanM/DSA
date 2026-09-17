def test_fn(num):
    return num % 2 == 0


nums =  (num for num in range(1, 100+1))

bool = [(test_fn(x)) for x in nums ]

print(bool)