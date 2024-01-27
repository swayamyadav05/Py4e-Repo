# Breaking out of a loop
# The break statement ends the current loop and jumps to the statement immediately following the loop
# It is like a loop test that can happen anywhere in the body of the loop

while True:
    line = input('> ')
    if line  == 'done' :
        break
    print(line)
print('Done!')
