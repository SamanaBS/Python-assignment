for i in range (0,5):
        for j in range (0,i+1):
            print('*', end=' ')
        print('\r')
c=1
for i in range (0,5):
        for j in range (0,i+1):
            print (chr(64+c), end=' ')
            c=c+1
        print('\r')
