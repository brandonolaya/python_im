def divisor(num):
    if num < 1:
        raise ValueError("Error negative number")
    else:
        divisor = [i for i in range(1, num+1) if num % i == 0]
        return divisor
    #divisor = []
    #if num < 1:
    #        raise ValueError("Error negative number")
    #else:
    #    for i in range(1, num+1):
    #        if num % i == 0:
    #            divisor.append(i)
    #    return divisor

def run():
    try:
        num = int(input(f'write a number: '))
        print(divisor(num))
        print(f'Finish my program')
    except ValueError:
        print(f'you need write only numbers')

if __name__ == '__main__':
    run()