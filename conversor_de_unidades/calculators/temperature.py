def temperature_calculator(initial_unit, final_unit, initial_unit_value):
    try:
        temperature_value = float(initial_unit_value)
    except ValueError:
        return 'Valor inválido!'

    # Faça a conversão de temperatura conforme as unidades selecionadas
    if initial_unit == "Celsius" and final_unit == "Fahrenheit":
        result = round((temperature_value * 9/5) + 32, 2)
    elif initial_unit == "Celsius" and final_unit == "Kelvin":
        result = round(temperature_value + 273.15, 2)
    elif initial_unit == "Fahrenheit" and final_unit == "Celsius":
        result = round((temperature_value - 32) * 5/9, 2)
    elif initial_unit == "Fahrenheit" and final_unit == "Kelvin":
        result = round((temperature_value - 32) * 5/9 + 273.15, 2)
    elif initial_unit == "Kelvin" and final_unit == "Celsius":
        result = round(temperature_value - 273.15, 2)
    elif initial_unit == "Kelvin" and final_unit == "Fahrenheit":
        result = round((temperature_value - 273.15) * 9/5 + 32, 2)
    else:
        result = temperature_value  # Se as unidades forem iguais, não há conversão  # noqa: E501

    return f'{temperature_value} {initial_unit} = {result} {final_unit}'
