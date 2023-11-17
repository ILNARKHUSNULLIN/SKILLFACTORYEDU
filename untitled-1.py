n = int(input())
a1 = input().split()
q = int(input())
a2 = ['0']
for i in range(n):
    a2.append(str(int(a1[i]) + int(a2[i])))
answers = []
for i in range(q):
    lr = input().split()
    result = 0
    if lr[0] == lr[1]:
        result = int(a2[int(lr[0])]) - int(a2[int(lr[0])-1])
        answers.append(result)
    elif int(lr[1]) == 1:
        result = int(a2[int(lr[1])]) - int(a2[int(lr[0])])
        answers.append(result)
    else:
        result = int(a2[int(lr[1])]) - int(a2[int(lr[0])-1])
        answers.append(result)
        
for i in answers:
    print(i)