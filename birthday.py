Birthday = {
    'albert einstein' : "27/06/1999",
    'benjamin' : "11/12/1999 ",
   'ada lovelace': "18/09/2000",
}
print('please checkout my friends birthday')

temp = input("please enter my friend name:")
if temp in Birthday:
    print("The Birthday is on:", temp)
    print(Birthday[temp])