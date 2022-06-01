#Inventory servce


#Dictionaries
name={}
quantity={}
price={}

#Open file with inventory
details = open("inventory.txt","r")

#First line of the file is the number of items
no_items  = int((details.readline()).rstrip("\n"))

#Add items to dictionaries
for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    name.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=int(x2)
    quantity.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=float(x2)
    price.update({x1: x2})

details.close()

c="y" #Runs the while loop as long as user wants


#Instructions
print("Welcome to InventoryX")
print()
print("A-Add an item")
print("R-Remove an item")
print("E-Edit specifics of an item")
print("L-List all items")
print("Q-Quit")
print("help-See all commands again")
print()


while(c!= "q" or c!= "Q"):
    c= input("What would you like to do? ")
    
    if(c=="q" or c=="Q"):
        print()
        print("Thank you for using InventoryX")
        break
        
    elif(c=="A" or c=="a"):#Add a inventory
        inv_no = int(input("Enter inventory number: "))
        inv_name = input("Enter name: ")
        inv_quantity = int(input("Enter quantity: "))
        inv_pr = float(input("Enter price: "))
        
        m=0
        for i in range(0,len(price)):
            if(inv_no in price):
                inv_no+=1
                m=1
        if(m==1):
            print()
            print("That inventory number already exists :(, changing value to ",inv_no)
        
        name.update({inv_no: inv_name})
        price.update({inv_no: inv_pr})
        if(inv_quantity > -1):
            quantity.update({inv_no: inv_quantity})
        else:
            inv_quantity = 0
            quantity.update({inv_no: inv_quantity})
            print("The quantity of an item cannot be negative, the quantity has been set to 0.")
        print()
        print("Inventory number: ",inv_no," Name: ",name.get(inv_no)," Price: ",price.get(inv_no)," Quantity: ",quantity.get(inv_no))
        print("Inventory was added successfully!")
        print()
        
    elif(c=="E" or c=="e"):#Update inventory
        print()
        inv_no = int(input("Enter inventory number: "))
        if(inv_no in price):
            inv_name = input("Enter inventory name: ")
            inv_quantity = int(input("Enter inventory quantity: "))
            inv_pr = float(input("Enter inventory price: ")) 

            name.update({inv_no: inv_name})
            quantity.update({inv_no: inv_quantity})
            price.update({inv_no: inv_pr})

        else:
            print("That item does not exist, to add an item use a")
        print()
    
            
    elif(c=="R" or c=="r"):#Remove a part of Inventory
        print()
        inv_no = int(input("Enter inventory number: "))
        if(inv_no in price):
            are_you_sure = input("Are you sure you want to remove that item(y/n)? ")
            if(are_you_sure=="y" or are_you_sure=="Y"):
                price.pop(inv_no)
                name.pop(inv_no)
                quantity.pop(inv_no)
                print("Item successfully removed!")
            print()
        else:
            print("Sorry, item not found!")
            print()
        
    elif(c=="L" or c=="l"):#List all items in inventory
        print()
        print("Inventory numbers and their Names:      ",name)
        print("Inventory numbers and their Quantities: ",quantity)
        print("Inventory numbers and their Prices:     ",price)
        print()
        
    elif(c=="help"):#Display all commands
        print()
        print("Help Centre")
        print("A-Add an item")
        print("R-Remove an item")
        print("E-Edit specifics of an item")
        print("L-List all items")
        print("help-See all commands again")
        print("If you have any other questions or concerns please contact the manager.")
        print()
       
#Write the updated inventory to the file
details = open("inventory.txt","w")
no_items=len(price)
details.write(str(no_items)+"\n")
for i in range(0,no_items):
    details.write(str(i+1)+"#"+name[i+1]+"\n")
    
for i in range(0,no_items):
    details.write(str(i+1)+"#"+str(quantity[i+1])+"\n")

for i in range(0,no_items):
    details.write(str(i+1)+"#"+str(price[i+1])+"\n")
details.close()

