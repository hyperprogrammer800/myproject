
num = int(input("enter how many numbers"))
lst = [int(input("enter numbers")) for _ in range(num)]
lar = 0
seclar = 0
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        lar,lst[i+1],lst[i],seclar = lst[i],lst[i],lst[i+1],lst[i+1]
    else:
        lar = lst[i+1]
print(lar)
for j in range(len(lst)-1):
    if lar > lst[j] and seclar < lst[j]:
        seclar = lst[j]
    elif lar > lst[j+1] and seclar < lst[j+1]:
        seclar = lst[j+1]
print(seclar)
