import PySimpleGUI as sg
from classes.Labirinto import Labirinto
class Tela:
    def __init__(self):
        self.__labirinto = Labirinto()
    
    def desenhar_labirinto(self):
        layout = [
            [sg.Text('Selecione o método de busca:'),sg.Combo(['Profundidade', 'Amplitude'], default_value='', key='-METODO-', readonly=True),
            sg.Button('Fazer busca', key = '-BUSCA-')],
            [sg.Multiline(default_text='\n'.join([' '.join(map(str, linha)) for linha in self.__labirinto.get_mapa()]),
                size=(80, 20), font=('Courier New', 12), disabled=True, no_scrollbar=True, key='-MULTILINE-')]
        ]

        window = sg.Window('Labirinto', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event  == '-BUSCA-':
                resultado = self.__labirinto.buscar_caminho(values['-METODO-'])
                if resultado is None:
                  sg.popup_error('Não há saída')
                else:
                 window['-MULTILINE-'].update(value='\n'.join([' '.join(map(str, linha)) for linha in resultado]))