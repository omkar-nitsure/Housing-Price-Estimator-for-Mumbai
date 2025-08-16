max_keep = 32000

found = [0,0,0,0,0]

# lines = []
aus = []
can = []
en = []
sco = []
us = []

with open("accent_splits/valid.tsv") as f:
    root = f.readline().strip()
    for ind, line in enumerate(f):
        items = line.strip().split("\t")
        if(items[2] == "australia" and int(items[1]) >= max_keep):
            aus.append(line)
        if(items[2] == "canada" and int(items[1]) >= max_keep):
            can.append(line)
        if(items[2] == "england" and int(items[1]) >= max_keep):
            en.append(line)
        if(items[2] == "scotland" and int(items[1]) >= max_keep):
            sco.append(line)
        if(items[2] == "us" and int(items[1]) >= max_keep):
            us.append(line)

with open("accent-targets/val_aus_acc.tsv", "w") as f:
    f.writelines(root + "\n")
    for i in range(len(aus)):
        f.writelines(aus[i])

with open("accent-targets/val_can_acc.tsv", "w") as f:
    f.writelines(root + "\n")
    for i in range(len(can)):
        f.writelines(can[i])

with open("accent-targets/val_en_acc.tsv", "w") as f:
    f.writelines(root + "\n")
    for i in range(len(en)):
        f.writelines(en[i])

with open("accent-targets/val_sco_acc.tsv", "w") as f:
    f.writelines(root + "\n")
    for i in range(len(sco)):
        f.writelines(sco[i])

with open("accent-targets/val_us_acc.tsv", "w") as f:
    f.writelines(root + "\n")
    for i in range(len(us)):
        f.writelines(us[i])

with open("accent-targets/valid_acc.tsv", "w") as f:
    f.writelines(root + "\n")
    for i in range(len(aus)):
        f.writelines(aus[i])
    for i in range(len(can)):
        f.writelines(can[i])
    for i in range(len(en)):
        f.writelines(en[i])
    for i in range(len(sco)):
        f.writelines(sco[i])
    for i in range(len(us)):
        f.writelines(us[i])