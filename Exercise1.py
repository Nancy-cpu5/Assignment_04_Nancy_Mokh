#Exercise 1:
n=int(input('Choose one of the following choices:?\n Sum Tuples \n 2.Export JSON \n 3.Import JSON \n 4.Exit'))
if n==1:
    l=list(input('Enter the first tuple '))
    m=list(input('Enter the second tuple '))
    if (len(m)!=len(l)):
        print('These tuples are not of the same length')
    else:
        j=l+m
        k=tuple(j)
        print(f"The sum of these tuples is {j}")
elif n==2:
    my_dict={}
    #we can take the dictionary from the user directly or we can make the following method
    m=int(input('Enter the dimension of you dictionary'))
    i=1
    while i<=m:
        key=input(f"Enter key {i}")
        value=input(f"Enter the value of key{i}")
        my_dict[key]=value
        i+=1
    print(my_dict)
    string=str(my_dict)
    print(string)
    print(type(string))
    my_json='{'
    #here we want to transform every element in the dictionary into a string
     for key in my_dict:
            my_json+=f"str({key})"
            value=d[key]
    #here we want to check the value and convert it into a string
            my_json+=str(value)+','
    print(my_json)
        

    
    



    