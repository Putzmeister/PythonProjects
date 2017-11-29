days = int(input())
sumLiters = 0
concentration = 0
quantity = 0

for i in range(0, days):
    quantity = float(input())
    graduses = float(input())
    sumLiters += quantity
    concentration += quantity * graduses

gradusesFinal = concentration / sumLiters


print('Liter: %.2f' % sumLiters)
print('Degrees: %.2f' % gradusesFinal)

if gradusesFinal < 38:
    print('Not good, you should baking!')
elif 38 <= gradusesFinal <= 42:
    print('Super!')
else:
    print('Dilution with distilled water!')