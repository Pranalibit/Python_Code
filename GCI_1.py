#Give an array A of N positive integers and another number X. Determine whether or
# not there exists two elements in A whose sum is exactly X
N = 6
X = 16
A = [1,4,45,6,10,8]
print(A)
for i in range(0,len(A)):
    if i == 5:
        break
    for j in range(i+1,len(A)):
        if int(A[i]) + int(A[j]) == X:
            print('{}+{}={}'.format(A[i],A[j],A[i]+A[j]))
            print('Yes')
