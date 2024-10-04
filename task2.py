
comp = int(input())
def get_computer_declension(number):

    last_two_digits = number % 100
    last_digit = number % 10
    
    if 11 <= last_two_digits <= 14:
        return f"{number} компьютеров"
   
    if last_digit == 1:
        return f"{number} компьютер"
    elif 2 <= last_digit <= 4:
        return f"{number} компьютера"
    else:
        return f"{number} компьютеров"

#Ввод пользователя
#print(get_computer_declension(comp))

#пример из задания
print(get_computer_declension(25))   
print(get_computer_declension(41))   
print(get_computer_declension(1048))