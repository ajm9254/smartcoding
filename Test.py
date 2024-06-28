import random

random_number = random.randint(1, 100)

#print(random_number)
conut = 1

while True :
    try : 
        my_number = int(input("1부터 100 사이의 숫자를 입력하세요"))

        if my_number > random_number : 
            print ("다운")

        elif my_number < random_number :
            print ("업")

        elif my_number == random_number :
            print (f"{conut}한방에 맞춤 축하")
            break

        conut = conut + 1

    except:
            print ("숫자로입력하세요")