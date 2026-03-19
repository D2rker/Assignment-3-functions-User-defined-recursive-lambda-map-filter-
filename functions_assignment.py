def task1():
    print("Basic function: Price after discount")
    def apply_discount(price, discount_percent=5):
        if discount_percent > 60:
            discount_percent = 60
            
        final_price = price - (price * discount_percent / 100)
        return final_price

    result1 = apply_discount(1000, 10)
    print(f"Price after 10% discount: {result1}")

    result2 = apply_discount(500)
    print(f"Price after default 5% discount: {result2}")



def task2():
    print("Recursive function: Fatorial untility")
    def factorial(n):
        if n < 0:
            return None
        # The "Exit Door" (Base Case)
        if n == 1 or n == 0:
            return 1
        
        # The Recursive Step
        return n * factorial(n - 1)

    # Testing the function
    print(f"factorial of 5 is : {factorial(5)}")
    print(f"factorial of 0 is : {factorial(0)}")
    print(f"factorial of -3 is : {factorial(-3)}") 
    print(f"factorial of 10 is : {factorial(10)}")



def task3():
    print("Lambda function: GST calculator")
    # Lambda function for 18% GST
    gst = lambda price: price * 1.18

    print(gst(100))  



def task4():
    print("Using map(): Apply GST to list of prices")
    prices = [100, 250, 400, 1200, 50]

    gst = lambda price: price * 1.18
    prices_with_gst = list(map(gst, prices))

    print("Original prices:", prices)
    print("Prices after GST:", prices_with_gst)



def task5():
    print("Using filter(): filter expensive products")
    prices = [100, 250, 400, 1200, 50, 2000, 850]

    expensive_prices = list(filter(lambda p: p > 500, prices))

    affordable_prices = list(filter(lambda p: p <= 500, prices))

    print("Prices greater than 500:", expensive_prices)
    print("Prices less than or equal to 500:", affordable_prices)



def task6():
    print("Combined utility function")
    def process_prices(prices):

        discounted_prices = list(map(lambda p: p * 0.9, prices))
        
        filtered_prices = list(filter(lambda p: p > 300, discounted_prices))
        
        return discounted_prices, filtered_prices

    input_prices = [100, 500, 900, 50, 750]
    disc_list, filt_list = process_prices(input_prices)

    print("Discounted Prices:", disc_list)
    print("Filtered Prices (Above 300):", filt_list)



def task7():
    print("Mini problem: Menu using functions")
    def add_price(prices_list, price):
        prices_list.append(price)
        print(f"Price {price} added successfully!")

    def get_average_price(prices_list):
        if not prices_list:
            return 0
        return sum(prices_list) / len(prices_list)

    def get_max_price(prices_list):
        if not prices_list:
            return 0
        return max(prices_list)

    # --- Menu Logic ---

    my_prices = []

    while True:
        print("\n--- Menu ---")
        print("1 → Add price")
        print("2 → Show average price")
        print("3 → Show highest price")
        print("q → Quit")
        
        choice = input("Enter your choice: ").lower()

        if choice == '1':
            new_price = float(input("Enter price to add: "))
            add_price(my_prices, new_price)
        
        elif choice == '2':
            avg = get_average_price(my_prices)
            print(f"The average price is: {avg:.2f}")
        
        elif choice == '3':
            highest = get_max_price(my_prices)
            print(f"The highest price is: {highest}")
        
        elif choice == 'q':
            print(" Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")



print("Task 1: Basic function: Price after discount")
print("Task 2: Recursive function: Fatorial untility")
print("Task 3: Lambda function: GST calculator")
print("Task 4: Using map(): Apply GST to list of prices")
print("Task 5: Using filter(): filter expensive products")
print("Task 6: Combined utility function")
print("Task 7: Mini problem: Menu using functions")
choice = input("Type '1' for task1, '2' for task2, '3' for task3, '4' for task4, '5' for task5, '6' for task6, '7' for task7:\n")

if choice == "1":
    task1()
elif choice == "2":
    task2()
elif choice == "3":
    task3()
elif choice == "4":
    task4()
elif choice == "5":
    task5()
elif choice == "6":
    task6()
elif choice == "7":
    task7()
else:
    print("Invalid choice! Please enter 1, 2, 3, 4, 5, 6, or 7.")
