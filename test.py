def get_max_number(arrayA,kit1):
    arrayA.sort()
    kit=sorted(kit1,key=lambda a:a[1],reverse=False)
    print(kit)
    currentIndex = 0
    for i in range(len(kit)):
        if currentIndex >len(arrayA):
            break
        x=kit[i][0]
        y=kit[i][1]
        print(y)
        for j in range(0,x):
            if currentIndex >len(arrayA):
                break
            if y > arrayA[currentIndex]:
                arrayA[currentIndex]=y
                currentIndex =currentIndex +1
    sum = 0
    for a in arrayA:
        sum +=a
    print(arrayA)

    return sum

if __name__ == '__main__':
    arrayA =[5,2,4,4,1]
    kit=[[3,2]]
    print(get_max_number(arrayA,kit))
