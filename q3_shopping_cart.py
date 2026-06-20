def add_item(item,cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk",cart=["bread"]))
print(add_item("eggs"))

def add_item(item,cart=None):
    if cart is None:
        cart=[]
    cart.append(item)
    return cart


def create_cart(owner,discount=0):
    return{"owner":owner,"items":[],"discount":discount}

def add_to_cart(cart,name,price,qty=1):
    cart["items"].append({"name":name,"price":price,"qty":qty})

def update_price(price_tuple,new_price):
    try:
        price_tuple[0]=new_price
    except TypeError as e:
        print(f"Error:{e}.Tuples cannot be modified once created.")

def calculate_total(cart):
    total=sum(item["price"]*item["qty"]for item in cart["items"])
    final_total=total*(1-cart["discount"]/100)
    return final_total

alice_cart=create_cart("Alice",discount=10)
bob_cart=create_cart("Bob")

add_to_cart(alice_cart,"Laptop",1000)
add_to_cart(bob_cart,"Headphones",150)

print(f"Alice's Total:${calculate_total(alice_cart)}")
print(f"Bob's Total:${calculate_total(bob_cart)}")

item_price=(100,)
update_price(item_price,120)

#Discussion Points
#1.discount=0 vs cart=[]:integers are immutable,so a new value is created for each cell.lists re mutable;if defined as a default argument,the same list object is reused across every function call,leadinf to unexcepted data persistence.
#2.rebinding vs mutating:rebinding(x=[1])changes which object a name points to.Mutating(x.append(1))modifies the existing object in place.
#3.mutable:list,dict,set and immutable:tuple,str,int.
#4.when you pass a list to a function and modify it(mutable).the changes will reflect outside because both the internal and external names point to the same memory address



    
