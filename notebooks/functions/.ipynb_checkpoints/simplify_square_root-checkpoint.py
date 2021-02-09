def simplify_square_root(whole_number, radicand):
    radicand_not_prime = True
    
    while radicand_not_prime:
        #start with perfect square of 4
        perfect_square = 4
        #while our perfect square is less than our radicand
        while perfect_square < radicand:
            #if the radicand is divisable by our perfect square
            if radicand % perfect_square == 0:
                #multiply our whole number by the square root of our perfect square
                whole_number *= perfect_square ** 0.5
                #divide the radicand by the perfect square
                radicand /= perfect_square
                break
            #otherwise
            else:
                 #try again with the next perfect square
                perfect_square = (perfect_square ** 0.5 + 1) ** 2
         #if we did not find a perfect square then the radicand is prime
        else:
            radicand_not_prime = False
     #return the whole number and the radicand
    return whole_number, radicand