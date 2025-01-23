def prime_num_generator(num):
    for i in range(0, num+1):
        for j in range(2, i//2 + 1):
            if i % j != 0:
                print(j)

prime_num_generator(100)

    