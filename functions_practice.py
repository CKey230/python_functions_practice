def hello(name):
    print("Hello"+ ' ' + name)
hello("user")

def pack(item1, item2, item3):
    return[item1, item2, item3]
items = ("boat", "car", "plane")
print(items)

lunch_items = ["sub", "cheeseburger", "tacos"]
def eat_lunch(lunch_items):
    if not len(lunch_items):
        print("My Lunch Box is Empty!")
    elif lunch_items:
        print("First I eat " + lunch_items[0])
        for i in lunch_items[1:]:
            print("Next I eat " + i)
    else:
        print("My lunchbox is Empty!")
eat_lunch(lunch_items) #prints list of any length
eat_lunch([]) #if list is empty
