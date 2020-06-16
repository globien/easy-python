rates = [0.001 * i for i in range(1, 11)]
for rate in rates:
    ability = 1.0
    for i in range(365):
        if i%7 <= 5:
            ability *= 1 + rate
    print(f'N = {rate:.3f}    Ability = {ability:.3f}')
