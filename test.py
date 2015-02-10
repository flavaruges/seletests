def function ():
    print 'choa'
    a = ['choa','choo', 'multi']
    fl = open('nombres.txt','w')
    for i in a :
        print i
        fl.write(i)
        fl.write('\n')
        
    fl.close()
    fl= open('nombres.txt','r')
    fl.readlines()
    fl.close()

function()