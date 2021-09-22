import time
import random
punten = 0
opnieuw = 'ja'
for opnieuw in range (0,20,1):
    a = random.randint(1,1000)
    for raden in range(0,10,1):
        raden = input('type hier een nummer tussen de 1 en de 1000: ')
        if a == int(raden):
            print('goedzo!, je hebt het cijfer geraden!')
            punten = punten + 1
            break
        elif a < int(raden):
            print('je moet lager raden')
            if int(raden) > a-20 and int(raden) < a+20:
                print('je bent héél warm')
            elif int(raden) > a-50 and int(raden) < a+50:
                print('je bent warm')
        elif a > int(raden):
            print("je moet hoger raden")
            if int(raden) > a-20 and int(raden) < a+20:
                print('je bent héél warm')
            elif int(raden) > a-50 and int(raden) < a+50:
                print('je bent warm')
    time.sleep(0.5)
    print('het cijfer was ' + str(a))
    time.sleep(0.5)
    print('u heeft na deze ronde ' + str(punten) + ' punt(en)')
    opnieuw = input('wil je opnieuw spelen? ')
    if opnieuw == 'ja':
        print('oke, u gaat nu opnieuw spelen')
        print()
        time.sleep(1)
    else:break
print('u heeft in totaal ' + str(punten) + ' punten')