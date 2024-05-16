def prime_numbers():
    user=int(input('Enter the number:'))
    temp=0
    for i in range(2,user):
        if(user%i==0):
            temp+=1
            break
        if(temp==0):
            return "prime number"
        else:
            return "not a prime number"
