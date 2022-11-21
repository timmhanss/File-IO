# 18 Nov 2022, Hansen menu order

import os

def main():        
    startMenu = ["Make Order", "Review Order"]
    print("Hello! What would you like to do?")
    for i in range(len(startMenu)): # Print all accessible menu in startMenu[]
        print(f"[{str(i+1)}] {startMenu[i]}")
    # print(len(startMenu)) # Debug Line, print what len is
    while True:
        start = int(numCheck("Insert the menu number: ")) # Ask the user for read or write the orders
        if start > 0 and start <= len(startMenu): # Check if the input is within range, Please don't use == True.
            break
        else:
            # print(f"The list is called for {start}.") # Debug line - print what start is
            print("Please insert a number provided above.")
    match startMenu[start-1]:
        case "Make Order":
            makeOrder()
        case "Review Order":
            print("Opening Review Order")
            readOrder()

def numCheck(caption): 
    while True:
        qty = input(caption)
        if qty.isnumeric() == True:
            return qty
        else:
            print("Please insert a number")
            
def makeOrder():
    menu = [] # Putting the list inside because it's not global
    qty = int(numCheck("How much do you want to order? "))
    
    for _ in range(qty):
        menu.append(input("What do you want to order? "))
    
    with open("orders.txt", "a") as f: # Open file and close after loop is done
        for menu in sorted(menu): # Order is sorted. May or may not be needed
            print (f"You are ordering {menu}")
            f.write(f"{menu}\n") # Record the order in the file
        f.write(f"\n") # then add a newline after the final order

def readOrder():
    menu = []
    with open("orders.txt") as f: # Open the file as f
        for line in f: # Read every line in f
            menu.append(line.rstrip()) # then Append it on menu[] as in menu., rstrip removes the whitespace
    for menu in menu:
        print(menu)
            
os.system('cls||clear') # this line clears the screen 'cls' = windows 'clear' = unix
main()