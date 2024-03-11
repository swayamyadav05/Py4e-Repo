#This is the continuation of traceback.py program
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First',istr)
# When the first conversion fails - it just drops into the except: clause and the program continues.

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)
# When the second conversion succeeds - it just skips the except: clause and the program continues

