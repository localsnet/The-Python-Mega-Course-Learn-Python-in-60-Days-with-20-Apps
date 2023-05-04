import PySimpleGUI as sg

label1 = sg.Text("Eter feet")
label2 = sg.Text("Eter inches")
input_box1 = sg.InputText(tooltip="Enter feet")
input_box2 = sg.InputText(tooltip="Enter inches")
button= sg.Button("Convert")

window = sg.Window('Convertor', layout=[[label1, input_box1], [label2, input_box2],
                                        [button]])
window.read() #this method display the window
print("Hello")
window.close()