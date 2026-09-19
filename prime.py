# prime=[]
# for i in range(2,7):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#     if count==0:
#         prime.append(i)
# print(prime)


# prime = [ i for i in range(2, 7) if all(i % j != 0 for j in range(2, i))]
# print(prime)

list=[]
n=int(input("Enter the number"))
for i in range(n):
    num=int(input(f"Enter a number {i+1}: "))
    list.append(num)
print(list)