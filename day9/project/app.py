user_card = list(input("Please enter your card number: "))
checking_digit = user_card.pop()
user_card.reverse()

for index, num in enumerate(user_card):
    user_card[index] = int(num)

    if index % 2 == 0:
        double = int(num) * 2
        if double > 9:
            double -= 9
        user_card[index] = double


total = sum(user_card) + int(checking_digit)

if total % 10 == 0:
    print("This is valid card")
else:
    print("This is invalid card")
