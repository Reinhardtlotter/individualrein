
def print_fibonacci():
    print("Fibonacci")
    # number of terms
    usercount = int(input("How many terms? "))

    sequence = calc_fibonacci(usercount)
    if (len(sequence) > 0):
        print("Fibonacci sequence: \n", sequence)

def calc_fibonacci(fibnumber):
    sequence = []
    # starternum
    n1, n2 = 0, 1
    count = 0
    while count < fibnumber:
        sequence.append(n1)
        sum = n1 + n2
        # update values
        n1 = n2
        n2 = sum
        count += 1
    return sequence