import PySimpleGUI as sg
from day14.convert13 import convert

sg.theme("Black")

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")
label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")
convert_button = sg.Button("Convert")
output_label = sg.Text(key='output', text_color="orange")
exit_button = sg.Button("Exit")

window = sg.Window("Measure Converter",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, output_label, exit_button]])

while True:

    try:
        event, values = window.read()
        match event:
            case 'Exit':
                break
            case sg.WIN_CLOSED:
                break
        feet = int(values['feet'])
        inches = int(values['inches'])

        converted = convert(feet, inches)
        window['output'].update(value= f"{converted} m")
    except ValueError:
        sg.popup("Please provide two numbers.", font=("Verdana", 10))



window.close()