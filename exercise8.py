n= int(input("Enter n: "))
A= []
for i in range(n):
    number= int(input(f"Enter A[{i}]: "))
    A.append(number)
score= sorted(set(A))
print(score[-2])
