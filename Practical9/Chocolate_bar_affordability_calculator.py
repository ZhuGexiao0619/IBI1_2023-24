def chocolate_bar_affordability(total_money, price_per_bar):
    number_of_bars = total_money // price_per_bar
    change_left_over = total_money % price_per_bar
    return number_of_bars, change_left_over
total_money = 100
price_per_bar = 7
bars, change = chocolate_bar_affordability(total_money, price_per_bar)
print(f"Number of bars: {bars}, Change left over: {change}")