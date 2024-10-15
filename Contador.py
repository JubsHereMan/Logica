lenList = int(input('Digite um numero de 1 a 100!\n'))
print(f'o numero escolhido foi {lenList}')

while lenList > 100 or lenList < 1:
    print('O NUMERO PRECISA SER MENOR DO QUE 100! E MAIOR DO QUE 1 ')
    lenList=int(input('DIGITE UM NUMERO DE  1 a 100!'))

c=0
listNum=[]

while c != lenList:
        c+= 1
        listNum.append(c)

print(f' a lista é {listNum}')









