import json

def readInventory():
    print("Product Categories: " + '\n')

    with open('inventory.json') as f:
        data = json.load(f)

    for product in data['products']:
        print(product['type'])

    print('\n')
def searchInventory():
    with open('inventory.json') as f:
        data = json.load(f)

    Search = input("Search for product: ")
    print('\n')

    for product in data['products']:
        if Search == product['type']:
            print("PRODUCT: " + product['type'] + '\n')
            print("VARIANTS: ")
            for i in range(len(product['variants'])):
                print(product['variants'][i]+ ", ", sep=' ', end='', flush=True)

            print('\n')
            print("AMOUNT IN STOCK: " + product['amount'] + '\n')
            print("PRICE OF PRODUCT: " + product['price'] + ' kr')

    print('\n')
def deleteItem():
    with open('inventory.json', 'r') as json_file:
        data = json.load(json_file)

    for key in data['products']:
        if 'type' in key:
            del key['type']

    with open('inventory.json', 'w') as json_file:
        data = json.dump(data, json_file, indent=2, ensure_ascii=False)


def addItem():
    item_type = input("Enter product type: ")
    variation = input("Add variants by entering 'V', if not enter any key: ")

    if variation == 'V':
        print("Exit variations by entering 'D'.")
        var1 = input("Enter variant 1: ")
        if var1 == 'D':
            var1 = 'No Variation'
        var2 = input("Enter variant 2: ")
        if var2 == 'D':
            var2 = 'No Variation'
        var3 = input("Enter variant 3 ")
        if var3 == 'D':
            var3 = 'No Variation'
        var4 = input("Enter variant 4: ")
        if var4 == 'D':
            var4 = 'No Variation'
        var5 = input("Enter variant 5: ")
        if var5 == 'D':
            var5 = 'No Variation'
    else:
        var1 = 'No Variation'
        var2 = 'No Variation'
        var3 = 'No Variation'
        var4 = 'No Variation'
        var5 = 'No Variation'

    amount = input("Enter amount of products: ")
    price = input("Enter price of product: ")

    with open('inventory.json') as json_file:
        data = json.load(json_file)
        data['products'].append({
            "type": item_type,
            "variants": [var1, var2, var3, var4, var5],
            "amount": amount,
            "price": price
        })
        with open('inventory.json', 'w') as output_file:
            json.dump(data, output_file, indent=2, ensure_ascii=False)

exit = True
while exit == True:
    print("Press 'R' to list inventory, 'S' to Search, 'D' to delete, 'A' to add or 'T' to exit.")
    Selector = input("Please select an action: ")

    if Selector == 'R':
        readInventory()
    elif Selector == 'S':
        searchInventory()
    elif Selector == 'D':
        deleteItem()
    elif Selector == 'A':
        addItem()
    elif Selector == 'T':
        print("Exiting...")
        exit = False