import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= maximum <= 1000 and quantity <= maximum - minimum + 1):
        return []

    numbers = random.sample(range(minimum, maximum + 1), quantity)
    
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(2, 31, 3)
print("Ваші лотерейні числа:", lottery_numbers)