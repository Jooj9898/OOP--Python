class ShoppingCart:
    def __init__(self,item,price,products):
        self.item = item
        self.price = price
        self.products = products
        self.products.append((item,price))

    def add_item(self,items,prices):
        new_item = (items,prices)
        self.products.append(new_item)
        if len(self.products) > 100:
            exit()
    def remove_item(self,item):
        for new_item in self.products:
            if item in new_item:
                self.products.remove(new_item)
    def total(self):
        total = 0
        for new_item in self.products:
            if price in new_item:



acc1 = ShoppingCart('car',500,[])
acc1.add_item("table",10000)
print(acc1.products)
acc1.add_item("susie",1000)
print(acc1.products)
acc1.add_item("bomb",50)
print(acc1.products)

acc1.remove_item("table")
print(acc1.products)




