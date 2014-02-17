p1 = 10.123
p2 = 5.519

REVERTBIT = 2

def price_round(price):
    return round(price, REVERTBIT)

if __name__ == "__main__":
    print p1 , " to ", price_round(p1)
    print p2, "to " ,price_round(p2)
