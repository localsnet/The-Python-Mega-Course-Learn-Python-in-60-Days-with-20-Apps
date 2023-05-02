contexts = ["Statistics we are collected for "
            "calculations", "Receipt of bread",
            "Indian Jo - 9378765432"]
files = ["reports", "cookbook", "phonebook"]
for context, file in zip(contexts, files):
    file = open(f"{file}.txt","w")
    file.write(context)
    file.close()