summer = 0 
counter = 0
maxer = 0
miner = 0        
lastreader = int()

while True:
    reader = input('Enter an integer: ')
    if reader == 'q' or reader == 'quit' or reader == 'Q':
       print('Min is',miner)
       print('Max is',maxer)
       print('Sum is',summer)
       print ('Avg is',summer/counter)
       break
            
    elif reader.isdigit:
        reader = int(reader)
        counter +=1
        summer = reader + summer
        #if lastreader < reader:
        #   print(lastreader)
        #   print(miner)
        if reader > maxer:
            maxer = reader
        if reader < miner:
            miner = reader
        if counter == 1:
            maxer = reader
            miner = reader

        lastreader = reader
    
 
        
                    
    
