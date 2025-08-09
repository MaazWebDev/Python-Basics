# Question 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10

while True:
    user_input = int(input('Enter Value B/W 1 To 10 : '))
    if 1 <= user_input <= 10:
        print('Thanks')
        break
    else:
        print('Invalid Number')