import sys
import random
import time



def ex_function(vctr ):


    y=0
    i=0
    n= len(vctr)

    for X in vctr:

        if(X==0):

            for j in range(i, n):

                k=n

                while(k>=1):

                    y=y+1
                    k=k//2

        else:

            for m in range(i, n):

                for t in range(1, n+1):
                    x=n
                    while(x>0):

                        x=x-t
                        y=y+1
        i=i+1

    return y



def average_case_creator(size_of_input):

    case=[]

    for i in range(0,size_of_input):

        if(random.randint(0,2)==0):

            case= case+ [0]

        else:

            case=case+ [1]


    return case



best_case1= [0]
best_case10=[0]*10
best_case50= [0]*50
best_case100= [0]*100
best_case200= [0]*200
best_case300= [0]*300
best_case400= [0]*400
best_case500= [0]*500
best_case600= [0]*600
best_case700= [0]*700

worst_case1= [1]
worst_case10= [1]*10
worst_case50= [1]*50
worst_case100= [1]*100
worst_case200= [1]*200
worst_case300= [1]*300
worst_case400= [1]*400
worst_case500= [1]*500
worst_case600= [1]*600
worst_case700= [1]*700


average_case1= average_case_creator(1)
average_case10= average_case_creator(10)
average_case50= average_case_creator(50)
average_case100= average_case_creator(100)
average_case200= average_case_creator(200)
average_case300= average_case_creator(300)
average_case400= average_case_creator(400)
average_case500= average_case_creator(500)
average_case600= average_case_creator(600)
average_case700= average_case_creator(700)



start = time.time()
ex_function(best_case1)
end = time.time()
string= 'Case: Best Size: '+str(1)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(worst_case1)
end = time.time()
string= 'Case: Worst Size: '+str(1)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(average_case1)
end = time.time()
string= 'Case: Average Size: '+str(1)+' Elapsted Time: '+str((end-start))
print(string)

print()



start = time.time()
ex_function(best_case10)
end = time.time()
string= 'Case: Best Size: '+str(10)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(worst_case10)
end = time.time()
string= 'Case: Worst Size: '+str(10)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(average_case10)
end = time.time()
string= 'Case: Average Size: '+str(10)+' Elapsted Time: '+str((end-start))
print(string)

print()



start = time.time()
ex_function(best_case50)
end = time.time()
string= 'Case: Best Size: '+str(50)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(worst_case50)
end = time.time()
string= 'Case: Worst Size: '+str(50)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(average_case50)
end = time.time()
string= 'Case: Average Size: '+str(50)+' Elapsted Time: '+str((end-start))
print(string)

print()



start = time.time()
ex_function(best_case100)
end = time.time()
string= 'Case: Best Size: '+str(100)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(worst_case100)
end = time.time()
string= 'Case: Worst Size: '+str(100)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(average_case100)
end = time.time()
string= 'Case: Average Size: '+str(100)+' Elapsted Time: '+str((end-start))
print(string)

print()



start = time.time()
ex_function(best_case200)
end = time.time()
string= 'Case: Best Size: '+str(200)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(worst_case200)
end = time.time()
string= 'Case: Worst Size: '+str(200)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(average_case200)
end = time.time()
string= 'Case: Average Size: '+str(200)+' Elapsted Time: '+str((end-start))
print(string)

print()



start = time.time()
ex_function(best_case300)
end = time.time()
string= 'Case: Best Size: '+str(300)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(worst_case300)
end = time.time()
string= 'Case: Worst Size: '+str(300)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(average_case300)
end = time.time()
string= 'Case: Average Size: '+str(300)+' Elapsted Time: '+str((end-start))
print(string)

print()



start = time.time()
ex_function(best_case400)
end = time.time()
string= 'Case: Best Size: '+str(400)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(worst_case400)
end = time.time()
string= 'Case: Worst Size: '+str(400)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(average_case400)
end = time.time()
string= 'Case: Average Size: '+str(400)+' Elapsted Time: '+str((end-start))
print(string)

print()


start = time.time()
ex_function(best_case500)
end = time.time()
string= 'Case: Best Size: '+str(500)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(worst_case500)
end = time.time()
string= 'Case: Worst Size: '+str(500)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(average_case500)
end = time.time()
string= 'Case: Average Size: '+str(500)+' Elapsted Time: '+str((end-start))
print(string)

print()


start = time.time()
ex_function(best_case600)
end = time.time()
string= 'Case: Best Size: '+str(600)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(worst_case600)
end = time.time()
string= 'Case: Worst Size: '+str(600)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(average_case600)
end = time.time()
string= 'Case: Average Size: '+str(600)+' Elapsted Time: '+str((end-start))
print(string)

print()



start = time.time()
ex_function(best_case700)
end = time.time()
string= 'Case: Best Size: '+str(700)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(worst_case700)
end = time.time()
string= 'Case: Worst Size: '+str(700)+' Elapsted Time: '+str((end-start))
print(string)

start = time.time()
ex_function(average_case700)
end = time.time()
string= 'Case: Average Size: '+str(700)+' Elapsted Time: '+str((end-start))
print(string)

print()





