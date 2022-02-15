bottle_05_price = 0.10
bottle_1_price = 0.25
print('Вычисление стоимости и количества бутылок объемом 1 и 0,5 л')
print(f"Стоимость бутылки объемом 0,5 л равна {bottle_05_price} р")
print('Введите кол-во бутылок объемом 0,5 л: ')
bottle_05 = int(input())
amount_per_bottle05 = bottle_05 * bottle_05_price
print(f"Стоимость за количество бутылок {bottle_05} равна {amount_per_bottle05} р")

print(f"Стоимость бутылки объемом 1 л равна {bottle_1_price} р.")
print('Введите кол-во бутылок объемом 1 л: ')
bottle_1 = int(input())
amount_per_bottle1 = bottle_1 * bottle_1_price
print(f"Стоимость за количество бутылок {bottle_1} равна {amount_per_bottle1} р.")

total = amount_per_bottle05 + amount_per_bottle1
print(f"Сумма к выдачи: {total} р.")
