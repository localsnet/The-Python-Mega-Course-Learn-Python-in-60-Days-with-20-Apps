var = input("Как тебя зовут, милейший?: ")

for i, j in enumerate(var):
    print(i+1, j)

print(f"Длина вашего имени в общем составляет {len(var)} букв")
if len(var) > 5:
    print("Слишком длинное имя, я устал считать, ...фух")
else:
    print("Посчитать было не трудно :)")