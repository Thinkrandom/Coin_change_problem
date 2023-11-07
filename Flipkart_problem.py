size = int(input())
arr = list(map(int, input().split()))
max_num = int(input())


diff = max_num - sum(arr)

a = 1
b = 1

output = ""
count = 0

while diff > 0:
    if a not in arr:
        output = output + str(a) + " "
        count = count + 1
        diff = diff - a
    a = a + b
    b = a - b
    
print(output)
print(count)

    

