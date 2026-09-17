print("===========Grocessory Store Manager==========")
choice=0
No_of_item_added=0
item_list=[]

while(choice!=6):
    choice = int(input("1.Add Item\n2.Remove Item\n3.Search Item\n4.Show All Item\n5.Update Item\n6.exit"))

    # Add Item
    if choice==1:
        Item_name=input("Name of Item:")
        Item_price=input("Price of Item:")
        Manufacturer_date=input("Manufacturer Date:")
        Expiry_date=input("Expiry Date:")
        add_item=[Item_name,Item_price,Manufacturer_date,Expiry_date]
        item_list.append(add_item)
        print("Succesfully Item Added.")
        print("==============================")

    #Remove Item
    elif choice==2:
        Item_name = input("Enter Item Name ")
        for i in range(len(item_list)):
            remove_item = item_list[i][0]
            if Item_name == remove_item:
                item_list.pop(i)
                print("Item removed successfully.")
                break
        print("==============================")        

    #Search Item        
    elif choice==3:
        Item_name=input("Enter item name")
        for i in range(len(item_list)):
            if Item_name==item_list[i][0]:
                print("Item Name:",item_list[i][0])
                print("Item Price:",item_list[i][1])
                print("Manufacturer Date:",item_list[i][2])
                print("Expiry Date:",item_list[i][3])
        print("==============================")

    #Show all item
    elif choice==4:
        for i in range(len(item_list)):
            print("Item Name:",item_list[i][0])
            print("Item Price:",item_list[i][1])
            print("Manufacturer Date:",item_list[i][2])
            print("Expiry Date:",item_list[i][3])
        print("==============================")

    #Update Item
    elif choice==5:
        Item_name=input("Enter the item.")
        for i in range(len(item_list)):
            if Item_name==item_list[i][0]: 
                print("Update the item")
                Item_name=input("Name of Item:")
                Item_price=input("Price of Item:")
                Manufacturer_date=input("Manufacturer Date:")
                Expiry_date=input("Expiry Date:")
                item_list[i]=[Item_name,Item_price,Manufacturer_date,Expiry_date]                  
                print("Succesfully Item Updated.")
                break
        print("==============================")

    elif choice==6:
        break
    else:
        print("Please enter the correct choice")



