user_card_number = input("Card Number: ")

total_w2 = 0
total_w1 = 0
index = 0

for digit_char in user_card_number:
    digit = int(digit_char)
    if index % 2 == 0:
        digit *= 2
        if digit > 9:
            digit = digit // 10 + digit % 10
        total_w1 += digit
    if index % 2 == 1:
        total_w2 += digit
    index += 1

check_sum = total_w1 + total_w2
if not check_sum % 10 == 0:
    print("Invalid")

if len(user_card_number) == 15 and (user_card_number[:2] == '34' or user_card_number[:2] == '37'):
    print("American Express")

elif len(user_card_number) == 16 and ('51' <= user_card_number[:2] <= '55'):
    print("Master Card")

elif (len(user_card_number) == 13 or len(user_card_number) == 16) and user_card_number[:1] == '4':
    print("Visa Card")




