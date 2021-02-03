def simplify_square_root(whole, sqrt):
    while True: 
        for i in range(sqrt):
            if i == sqrt:
                return whole, sqrt
            elif i+1 % sqrt == 0:
                whole *= i+1
                sqrt /= i+1
                break
        return whole, sqrt
