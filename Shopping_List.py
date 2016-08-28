shopping_list =[]

#Print Shopping List
def list_print():
    print("Your List: ")
    for item in shopping_list:
        print(item)

#Help Function
def help_me():
    print('Typing "DONE" Exits the Program...')
    print('Typing "SHOW" Displays the Items Currently in the List...')
    print('Typing "HELP" Runs this Help Dialog...')

def add_to_list(new_item):
     shopping_list.append(new_item)
     print('Added {} to your list, there are now {} items in your list.'.format(new_item, len(shopping_list)))

print('Enter a name of your list item. If you type DONE, the program will exit.  If you type Show, your current list is shown. Type HELP for help.')
#Ask for a List Item
while True:
    new_item = input("Name an item to add it to your list: ")
    #Exit App When DONE
    if new_item == 'DONE' or new_item == 'done':
        break
    #Show List Contents
    elif new_item == 'SHOW' or new_item == 'show':
        list_print()
        continue
    #Display Help Dialog
    elif new_item == 'HELP' or new_item == 'help' or new_item == '?':
        help_me()
        continue
    #Add New Item to Shopping List
    add_to_list(new_item)
