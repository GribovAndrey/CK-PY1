salary = 5000  # зарплата
spend = 6000  # расходы
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(months):
    need_money += spend - salary
    spend *= (1 + increase)


print(round(need_money))
