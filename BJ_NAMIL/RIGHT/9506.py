import sys


def findingDivisors(number):
    divisors = []
    divider = 1
    while divider < number:
        if number % divider == 0:
            divisors.append(divider)
            divider += 1
        else:
            divider += 1
    return divisors


while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    else:
        divisors = findingDivisors(n)
        total = sum(divisors)
        if total == n:
            strAns = ""
            for i in divisors:
                strAns = strAns + str(i) + " + "
            strAns = strAns.rstrip(" + ")
            print(n, "=", strAns)
        else:
            print(f"{n} is NOT perfect.")
