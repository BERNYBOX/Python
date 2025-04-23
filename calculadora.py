def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

currencies = {
    "1": {"name": "Baht tailandés", "rate": 0.028},
    "2": {"name": "Won surcoreano", "rate": 0.00073},
    "3": {"name": "Dirham EAU", "rate": 0.27},
    "4": {"name": "Rand sudafricano", "rate": 0.055},
    "5": {"name": "Rupia indonesia", "rate": 0.000064}
}

selection = input("Ingrese el número de la moneda (1 a 5): ")

if selection in currencies:
    amount = float(input("\nIngrese la cantidad en USD que desea convertir: "))
    
    selected_currency = currencies[selection]
    result = exchange_money(amount, selected_currency["rate"])
    
    print("\n" + str(amount) + " USD = " + str(round(result, 2)) + " " + selected_currency["name"])
    print("Tasa de cambio: 1 " + selected_currency["name"] + " = " + str(selected_currency["rate"]) + " USD\n")
else:
    print("\nSelección no válida. Por favor, elija un número entre 1 y 5.\n")
