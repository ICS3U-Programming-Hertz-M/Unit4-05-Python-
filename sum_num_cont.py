# !/usr/bin/env python3

# created by Hertz Antonella
# created on 29. Apr. 2022
# This program ask the user how many times
# they would like to enter a number and then
# add up from 0 to the user number


def main():
    counter = 0
    total_sum_list = []
    while True:
        # Ask the user to enter how many times they want to enter
        # an input.
        user_num1 = input("How many numbers would you like to add:")
        print("")
        # user_num1 into an int, check if it is a positive number
        try:
            user_num1 = int(user_num1)
            if user_num1 <= 0:
                print("Please enter a positive number(0,1,2..10...100..)")
                break
        except:
            print("Invalid ,Please enter a number(1,2,3..)")
            break
        while counter < user_num1:
            # Ask for the second input,cast it into an int
            # and check if the user number is positive
            user_num2 = input("Enter a number:")
            try:
                user_num2 = int(user_num2)
                if user_num2 <= 0:
                    print(
                        "Please enter a positive number,{}cannot be added".format(
                            user_num2
                        )
                    )
                    continue
                # add each number in the total_sum_list and display the sum.
                total_sum_list.append(user_num2)
                counter = counter + 1
            except:
                print("Invalid ,Please enter a number(1,2,3..)")
        total_sum = sum(total_sum_list)
        print(*total_sum_list, sep="+", end=" ")
        print("={}".format(total_sum))
        print("Sum = {}".format(total_sum))
        break


if __name__ == "__main__":
    main()
