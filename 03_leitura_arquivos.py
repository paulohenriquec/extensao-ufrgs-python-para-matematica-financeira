#%%
x = [4,10,20,40]
f = open("ola, mundo!", 'w')
#%%
f.write('%d %d %d' % (x[0], x[1], x[2]))
#%%
f.close()

#%%
f = open ('ola, mundo!', 'r')
y = f.read()
#%%
f.close()
#%%
f = open('ola2.txt', 'w')
f.write('%d \n%d \n%d' %(x[0], x[1], x[2]))
f.close()