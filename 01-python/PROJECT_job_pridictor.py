# i m creating a meal decider

name = input(f"tpaiko name k ho ni?")
day =input(f"aja kun bar ho?")

print(f"\n teso bhaye tpaile yo khanus:")

if day.lower() == "sunday":
    print(f" chicken khanus")
elif day.lower() == "monday":
    print(f"tarkari dal khabus")
elif day.lower() == "tuesday":
    print(f"saag rw bhat khanus")
elif day.lower() == "wednesday":
    print(f"chicken bhat khanus")
elif day.lower() == "saturday":
    print(f" aja chai khasi ko masu khanus hai")
else:
    print(f"sinki suka sag rw bhat khanus")
# print("hello\n\n\nGorkha!!!")