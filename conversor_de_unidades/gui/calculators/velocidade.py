def speed_calculator(initial_unit, final_unit, initial_unit_value):
    try:
        speed_value = float(initial_unit_value)
    except ValueError:
        return 'Valor inválido!'

    if initial_unit == final_unit:
        result = 'Selecione unidades diferentes'

    elif initial_unit == 'Metros por segundo' and final_unit == 'Kilômetros por hora':  # noqa: E501
        result = speed_value * 3.6

    elif initial_unit == 'Metros por segundo' and final_unit == 'Milhas por segundo':  # noqa: E501
        result = speed_value / 1609

    elif initial_unit == 'Metros por segundo' and final_unit == 'Milhas por hora':  # noqa: E501
        result = speed_value * 2.237

    elif initial_unit == 'Kilômetros por hora' and final_unit == 'Milhas por segundo':  # noqa: E501
        result = speed_value / 5794

    elif initial_unit == 'Kilômetros por hora' and final_unit == 'Milhas por hora':  # noqa: E501
        result = speed_value / 1.609

    elif initial_unit == 'Milhas por segundo' and final_unit == 'Milhas por hora':  # noqa: E501
        result = speed_value * 3600

    else:
        ...

    speed_dict = {
        'Metros por segundo': 'm/s',
        'Kilômetros por hora': 'km/h',
        'Milhas por segundo': 'mi/s',
        'Milhas por hora': 'mi/h',
    }

    result = (f'{speed_value} {speed_dict[initial_unit]} ='
              f' {result} {speed_dict[final_unit]}')

    return result
