num_1 = int(input(" Enter a number:"))
num_2 = int(input("Enter another number:"))
choice = input(" Enter the operation + - + /:")
if choice == "+":
    sum = num_1 + num_2
    print(" The sum is", sum)

elif choice == "-":
    diff = num_1 - num_2
    print("The diff is", diff)

elif choice == "*":
    mul = num_1 * num_2
    print("The product is", mul)

elif choice == "/":
    div = num_1 / num_2
    print(" The quoatient is", div)
else:
    print("Invalid choice")

print(type(num_1))
