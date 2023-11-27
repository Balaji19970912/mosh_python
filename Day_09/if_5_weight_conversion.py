input_weight = input('Enter your weight: ')
input_weight_unit = input('(L) for Pounds (K) for Kilo Grams: ')

if input_weight_unit.lower() == 'l':
    final_weight = 0.45 * float(input_weight)
    print(f'You are {final_weight} Kg')
elif input_weight_unit.lower() == 'k':
    final_weight = 2.2 * float(input_weight)
    print(f'You are {final_weight} lb')
    print('KG to Pound')
else:
    print("Invalid input!")