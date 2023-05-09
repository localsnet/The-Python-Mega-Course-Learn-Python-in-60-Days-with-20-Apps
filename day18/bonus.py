import PySimpleGUI as sg
from day16.zip_creator import extract_archive

label1 = sg.Text("Select archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key='files')

label2 = sg.Text("Select destination directory: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract")
output_label = sg.Text(key='output', text_color="green")

window = sg.Window("Archive extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    filepaths = values['files']
    folder = values['folder']
    extract_archive(filepaths, folder)
    window['output'].update(value="Extraction completed!")

window.close()