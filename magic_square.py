def magic_Square(n):
    magicsquare=[]
    """for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicsquare.append(l)"""

    """we can create 2d array or list by one more method 
    that is given below"""


    magicsquare=[[0 for i in range(n)] for j in range(n)]

    
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j],end=" ")
        print()

    i=n//2
    j=n-1
    num=n*n
    count=1

    while(count<=num):
        if(i==-1 and j == n): # condition 4
            j=n-2
            i=0
        else:
            if(j==n): #coloum =n 
                j=0
            if(i<0):
                i=n-1

        if(magicsquare[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else :
            magicsquare[i][j]=count
            count+=1

        i=i-1
        j=j+1 
        # condition 2
    
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j],end=" ")
        print()
    
    print("the sum of the row coloum and diagnoal is  is"+str(n*(n**2+1)/2))






n=int(input("enter the number "))
magic_Square(n)