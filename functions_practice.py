#hello function
def hello():
    print("Hello, user!")

hello()

#pack function
def pack(item1, item2, item3):
    return[item1, item2, item3]

print(pack("boat", "car", "plane"))

#eat_lunch function
def eat_lunch(lunch_items):
    if not len(lunch_items):
        print("My Lunch Box is Empty!")
    elif lunch_items:
        print("First I eat " + lunch_items[0])
        for i in lunch_items[1:]:
            print("Next I eat " + i)
   
eat_lunch("sub")        
eat_lunch(["sub", "cheeseburger", "tacos"]) #prints list 
eat_lunch([]) #if list is empty
