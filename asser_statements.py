def divisor(num):
    divisor = []
    if num < 1:
            raise ValueError("Error negative number")
    else:
        for i in range(1, num+1):
            if num % i == 0:
                divisor.append(i)
        return divisor

def run():
    num = input(f'write a number: ')
    assert num.isnumeric(), "you must enter a positive number"
    print(divisor(int(num)))
    print(f'Finish my program')
    
if __name__ == '__main__':
    run()