nr=7
if nr==1:
    pass
elif nr=32:
    pass    
else:
    arr=[[1],[1,1]]
    i=2
    for a in range(nr-2):
        arr1=[1,1]
        j=0
        while len(arr1)<=i:
            x=arr[i-1][j]+arr[i-1][j+1]
            j+=1
            arr1.insert(-1,x)
            print(arr1)
        i+=1
        arr.append(arr1)
print(arr)