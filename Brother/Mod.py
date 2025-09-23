# num = int(input("enter number :"))
# if num <= 0: print("It's underflow. please try again.")
# elif num > 12: print("It's overflow. please try again.")
# else:
#     for i in range(12): print(f"{num} x {i+1} = {num * (i+1)}") 

while True:
    num = int(input("enter number :"))
    if num <= 0: print("It's underflow. please try again.\n-------------------------------")
    elif num > 12: print("It's overflow. please try again.\n-------------------------------")
    else:[print(f"{num} x {i+1} = {num * (i+1)}") for i in range(12)]; break
    

# num = int(input("enter number :")); print("It's underflow. please try again.") if num <= 0 else print("It's overflow. please try again.") if num > 1000 else [print(f"{num} x {i+1} = {num * (i+1)}") for i in range(12)]