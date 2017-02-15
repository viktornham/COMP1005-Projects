
first1=ord(input("Starting letter: "))
first2=ord(input("Ending letter: "))
second1=int(input("Starting number: "))
second2=int(input("Ending number: "))
third1=ord(input("Starting letter: "))
third2=ord(input("Starting number: "))

counter=0

for S in range(first1, first2+1):
    
    for M in range(second1, second2+1):
        
        for H in range(third1, third2+1):

            print(chr(S),int(M),chr(H))

            counter+=1

print('A total of', counter, 'codes')
    
