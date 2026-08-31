MAX_RENTAL_BATCH_LIMIT = 150.0

def calculate_rental_batch(
    quantity: int,
    rental_rate: float,
    discount: float = 0.0
) -> tuple[float, bool]:
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exceeded

print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")
#Positional argument usage
result1 = calculate_rental_batch(30, 2.99)
print(
    f"Партия 1 (Academy Dinosaur): "
    f"Сумма {result1[0]}$. Превышение лимита: {result1[1]}"
)
#Keyword argument usage
result2 = calculate_rental_batch(
    quantity=40,
    rental_rate=4.99,
    discount=0.1
)
print(
    f"Партия 2 (Affair Prejudice): "
    f"Сумма {result2[0]}$. Превышение лимита: {result2[1]}"
)
result3 = calculate_rental_batch(10, 1.99)
print(
    f"Партия 3 (Agent Truman): "
    f"Сумма {result3[0]}$. Превышение лимита: {result3[1]}"
)
result4 = calculate_rental_batch(50,3.5,0.2)
print(
    f"Партия 4 (African Egg): "
    f"Сумма {result4[0]}$. Превышение лимита: {result4[1]}"
)
