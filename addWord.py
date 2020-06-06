print('-----Welcome to the Words Adding file of Hangman-----')
f = open("words.txt", "a")
num = int(input("Please enter the number of custom words you want to add:"))
for i in range(num):
    word = input(f'Enter word number {i+1}:')
    f.write("\n"+word)
print('All your reqested Custom Words Have been entered into the DB')
flag = input("Would you like a Print-out of the words(Y/N):").upper()
if flag == 'Y':
    fw = open("words.txt", "r")
    print(fw.read())
    print("Exiting...")
else:
    print("Exiting....")
    quit()
