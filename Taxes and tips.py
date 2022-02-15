print('Расчёт стоимости заказа с НДС и чаевых: \n')
order_amount = float(input('Введите сумму заказа: '))
nds = order_amount + (order_amount / 100 * 20)  # 20%
tips = order_amount + (order_amount / 100 * 18)  # 18%
print(f"Стоимость заказа с НДС {nds} р.")
print(f"стоимость с чаевыми {tips} р.")

n = order_amount + (order_amount / 100 * 20) + (order_amount / 100 * 18)
print(f"Общая стоимость заказа чаевых + НДС: {n} р.")