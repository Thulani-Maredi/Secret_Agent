
n = []
plus = 0
while True:
    num = int(input("Enter number:\n"))
    n.append(num)
    if num == 0:
        break
    plus += num
average = plus/int(len(n)-1)
print(int(average))
        
        