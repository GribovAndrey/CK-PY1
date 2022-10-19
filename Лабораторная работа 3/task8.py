money_capital = 10000  # подушка
salary = 5000          # зарплата
spend = 6000           # расходы
increase = 0.05        # рост цен

month = 0  # количество месяцев, которое можно прожить

while money_capital >= spend:
    money_capital -= spend
    money_capital += salary
    spend *= (1 + increase)
    month += 1

print(month)
