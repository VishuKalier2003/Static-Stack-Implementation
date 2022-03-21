# Implementation of Stack using Arrays ( Static Implementation )
def Push(arr, n):       # Adding element as Push in Stack Terminology
    arr.append(n);
    print("The Stack is Pushed... Updated !");


def Pop(arr, top):        # Deleting elements as Pop in Stack Terminology
    if len(arr) == 0:     # If Stack is Empty, then nothing can be popped
        print("Since Stack is empty, no element can be popped !");
    else:
        del arr[top];
        print("The Stack is Popped... Updated !");


def Display(arr):   # Displaying the Stack
    p = len(arr);
    st = " ---> Base";          # The first element is termed as Base and the Last element is termed
    en = " ---> Top";           # as Top, Last-In First-Out ( LIFO ) Data Structure
    print("The Stack is : ");
    for i in range(p, -1, -1):  # Printing list in Reversed sequence to get top first
        if i == p-1:
            print(arr[i],en);
        elif i == 0:             # Various conditions for printing effective Data Structure
            print(arr[i],st);
        elif i > 0 and i < p-1:
            print("^");
            print(arr[i]);
            print("^");


def HeightOfStack(arr):   # Displays Size of the Stack
    p = len(arr);               # The Size of the array is the height of the Stack
    print("The Size of Stack till now is : ",p);


def IsStackEmpty(top):
    if top == -1:        # If top again evaluates to negative, then the Stack becomes Empty
        print("The Stack for now is Empty !!");
    else:
        print("Stack is Not Empty !! ");


ar = [];   # Empty Stack
top = -1;  # Top pointer, only one pointer is required for Stack Operations
a = int(input("Enter How many operations to perform on Stack Data Structure : "));
for choice in range(0, a):
    choice = input("Write Push to Add, Pop to Remove, Size to get Size and Empty to check if empty : ");
    if choice == "Push" or choice == "PUSH" or choice == "push":
        n = int(input("Enter data value to add to the List : "));
        top = top + 1;      # Top pointer increments before adding of any element
        Push(ar, n);
        Display(ar);              # Displaying Stack
    if choice == "Pop" or choice == "POP" or choice == "pop":
        Pop(ar, top);
        top = top - 1;     # Top pointer decrements before removing of any element
        if len(ar) != 0:           # If the Stack does not empty itself, display the result
            Display(ar);
    if choice == "Size" or choice == "SIZE" or choice == "size":
        HeightOfStack(ar);
    if choice == "Empty" or choice == "EMPTY" or choice == "empty":
        IsStackEmpty(top);