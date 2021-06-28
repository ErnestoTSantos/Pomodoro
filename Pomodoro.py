from PySimpleGUI import PySimpleGUI as SG
from time import sleep
from playsound import playsound

class Temporizador:
    def __init__(self):
        SG.theme('Material2')
        layout = [
            [SG.Text('Temporizador: ', size=(20, 2))],
            [SG.Output(size=(40, 1))],
            [],
            [SG.Button('Start Timer')]
        ]

        #Declaração window
        self.janela = SG.Window('Pomodoro', layout)
    
    def Timer(self):
        while True:
            evento, valores = self.janela.read()
            if evento == SG.WINDOW_CLOSED:
                break
            if evento == 'Start Timer':
                pomodoro = self.startTimer()
                print(pomodoro)

    def startTimer(self):
        vezes = 1
        while vezes and True:
            for minutes in range(24, -1, -1):
                for seconds in range(59, -1, -1):
                    sleep(1)
                    print('')
                    print(f'{minutes:2}m:{seconds:2}s')
            playsound('alarme.mp3')
            print('Desance por 5 minutos!')
            print('Até logo! :)')
            sleep(300)
            playsound('SomAlarme2.mp3')
            vezes += 1
            if vezes == 4:
                print('Faça um descanso de 15 minutos e retorne!')
                print('Até logo :)')
                break


timer = Temporizador()
timer.Timer()
