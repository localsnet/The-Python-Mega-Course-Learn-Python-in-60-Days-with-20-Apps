ids = ["XF345_89_", "XER7_68_49", "XA_454_55"]

x = 0
#for index, id in enumerate(ids):
for id in ids:
    for single in id:
        if '_' in single:
            x = x + 1
print(x)