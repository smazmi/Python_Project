x= True
while x:
    print("Enter a positive range \n") # Requesting a positive range 
    a=int(input("Enter starting of the range: ")) 
    b=int(input("Enter ending of the range: "))
    if a<0 or b <0:     # Checking if the range inputs were positive
        print("input less than 0 try again")
        continue
    cp=cc=0             
    for i in range(a,b+1):
        if i==0 or i ==1:
            print("{} is a neither a composite nor a prime number".format(i))
            continue
        f=0
        for j in range(2,i):
            if i%j==0:
                f+=1
        if f>0:
            print("{} is a composite number".format(i))
            cc+=1
        else:
            print("{} is a prime number".format(i))
            cp+=1
    # print("Composite numbers: {}".format(cc))
    # print("Prime numbers: {}".format(cp))
    print("There are {} prime and {} composite numbers in the given range".format(cp,cc))
    r=True
    while r:
            y=int(input("Enter 1 to run again, 2 to exit: "))
            if y==1:
                r= False
            elif y==2:
                r=False
                x=False
                print("End of Code")
            else:
                print("Invalid input")