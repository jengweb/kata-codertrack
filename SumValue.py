INPUT1 = "893880539957604781622135818781054154760092"
INPUT2 = "458875111557430000227050141224806041518870"

TOOD = "0"
OUTPUT = ""
for Index in reversed(range(len(INPUT1))):
    Sum = str(int(INPUT1[Index]) + int(INPUT2[Index])+ int(TOOD))
    if Index != 0:
        TOOD = "0"
        if len(Sum) == 2:
            TOOD = Sum[0]
            Sum = Sum[1]
        else:
            TOOD = 0

    OUTPUT = Sum + OUTPUT

print(OUTPUT)
