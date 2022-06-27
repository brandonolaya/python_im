from functools import reduce

####filter
my_list = [1,2,3,4,5,6,7,8,9,14,16,19]
odd = list(filter(lambda modulo: modulo % 2 != 0, my_list))
print(f'print filter of my list {odd}')

#####map
#comprehensions
#odd2 = [i**2 for i in my_list]
odd2 = list(map(lambda potencia: potencia**2, my_list))
print(f'print another list{odd2}')

#####reduce
#reduce normal
#cont = 1
#for i in my_list:
#    cont += i
odd3 = reduce(lambda x, y: x+y, my_list)
#example
# [2*2*2*2*2]
#[4*2*2*2]
#[8*2*2]
#[16*2]
#[32]

print(odd3)
