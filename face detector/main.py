import PySimpleGUI as sg

layout = [
  [sg.Image(key = '-IMAGE-')],
  [sg.Text('People in picture: 0', key = '')]
]

window = sg.Window('Face Detector',layout).read()

while True:
  event, values = window.read()

  if event == sg.WIN_CLOSED:
    break

window.close()