filenames = ["1.Data report.txt", "2.Document.txt", "3.Presentation.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)