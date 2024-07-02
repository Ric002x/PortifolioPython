from calculators import temperature_calculator


class CoversorDeUnidades:
    def __init__(self) -> None:
        self.get_measure()
        self.get_convertion_units()
        self.get_unit_value()
        self.convert_temperature()

    def get_measure(self):
        while True:
            print('Selecione primeiro a medida de conversão.'
                  '\nDigite:\n    1 se: Temperatura\n    2 se: Comprimento')
            self.measure = input()

            try:
                if self.measure == '1':
                    self.measure = 'Temperatura'
                elif self.measure == '2':
                    raise ValueError(
                        'Essa opção ainda não está disponível no momento...\n'
                    )
                else:
                    raise ValueError(
                        'Opção Inválida! Digite um número'
                        ' correspondente a uma medida')

                print(f"Você selecionou: {self.measure}!\n")
                return self.measure

            except ValueError as err:
                print(err)

    def get_convertion_units(self):
        if self.measure == 'Temperatura':
            unidades = ['Celsius', 'Fahrenheit', 'Kelvin']
            print('Selecione a unidade de origem e a unidade final:\n'
                  '1: Celsius para Fahrenheit\n'
                  '2: Celsius para Kelvin\n'
                  '3: Fahrenheit para Celsius\n'
                  '4: Fahrenheit para Kelvin\n'
                  '5: Kelvin para Celsius\n'
                  '6: Kelvin para Fahrenheit\n'
                  )

            self.client_input = input()
            try:
                int(self.client_input)
            except ValueError as err:
                print(err)

            if self.client_input == '1':
                self.initial_unit = unidades[0]
                self.final_unit = unidades[1]
            elif self.client_input == '2':
                self.initial_unit = unidades[0]
                self.final_unit = unidades[2]
            elif self.client_input == '3':
                self.initial_unit = unidades[1]
                self.final_unit = unidades[0]
            elif self.client_input == '4':
                self.initial_unit = unidades[1]
                self.final_unit = unidades[2]
            elif self.client_input == '5':
                self.initial_unit = unidades[2]
                self.final_unit = unidades[0]
            elif self.client_input == '6':
                self.initial_unit = unidades[2]
                self.final_unit = unidades[1]
            else:
                raise ValueError('Opção inválida! Escolha'
                                 ' um número de 1 a 6.')

            self.convertion_units = (f'{self.initial_unit}'
                                     f' para {self.final_unit}')

            print(f'você irá converter {self.convertion_units}\n')

    def get_unit_value(self):
        print('Digite o valor para a'
              f' unidade inicial {self.initial_unit}: ')
        self.initial_unit_value = input()

    def convert_temperature(self):
        final_value = temperature_calculator(
            initial_unit_value=self.initial_unit_value,
            initial_unit=self.initial_unit,
            final_unit=self.final_unit)
        print('')
        print(final_value)


if __name__ == "__main__":
    start = CoversorDeUnidades()
