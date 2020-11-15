def divide(dividend, divisor):
    add = 1
    if((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)):
        add = -1
    count = 0
    dividend = abs(dividend)
    divisor = abs(divisor)
    while (dividend > 0):
        for i in range(divisor):
            dividend -= 1
            if(dividend < 0):
                return count
        count += add
    return count

if __name__ == "__main__":
    print(divide(-4,3))