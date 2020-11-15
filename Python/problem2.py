def divide(divided, divisor):
    count = 0
    while (divided > 0):
        for i in range(divisor):
            divided -= 1
            if(divided < 0):
                return count
        count += 1
    return count

if __name__ == "__main__":
    print(divide(4,3))