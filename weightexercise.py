weight = input("What is your weight? ")

units = input("(L)bs or (K)gs ")

if units.lower() == 'l':
    converted = float(weight)*.45359237
    print('weight in kgs: ' + str(converted))
else:
    converted = float(weight)*2.20462
    print('weight in lbs: ' + str(converted))
