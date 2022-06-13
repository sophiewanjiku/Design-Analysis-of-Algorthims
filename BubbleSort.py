n= int(input("Enter the number of elements:"))
num= list(map(int, input("Enter elements of array:").strip().split()))[:n]

print: str = ("list before bubble sort")
for n in num:
    print(n, end =' ')
for i in range(0, len(num)-1):
    for j in range(0, len(num)-1-i):
        if num[j] > num[j+1]:
            t = num[j]
            num[j]=num[j+1]
            num[j+1]=t
    print('\n\nList after Bubble Sort')
    for n in num:
        print(n, end =' ')
