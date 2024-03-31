import PySimpleGUI as sg
from classes.Labirinto import Labirinto
class Tela:
    def __init__(self):
        self.__labirinto = Labirinto()
    
    def desenhar_labirinto(self):
        layout = [
            [sg.Text('Selecione o método de busca:'),sg.Combo(['Profundidade', 'Amplitude'], default_value='', key='-METODO-', readonly=True),
            sg.Button('Fazer busca', key = '-BUSCA-'), sg.Button('Criar outro mapa', key='-CRIAR_MAPA-')],
            [sg.Multiline(default_text='\n'.join([' '.join(map(str, linha)) for linha in self.__labirinto.get_mapa()]),
                size=(40, 20), font=('Courier New', 12), disabled=True, no_scrollbar=True, key='-MAPA-'),
            sg.Multiline(default_text='',size=(40, 20), font=('Courier New', 12), disabled=True, no_scrollbar=True, key='-RESULT-', visible=False)]    
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
                 window['-RESULT-'].update(visible = True, value='\n'.join([' '.join(map(str, linha)) for linha in resultado]))

            if event == '-CRIAR_MAPA-':
                window['-MAPA-'].update(visible = True, value='\n'.join([' '.join(map(str, linha)) for linha in self.__labirinto.get_mapa()]))
                window['-RESULT-'].update(visible = False)