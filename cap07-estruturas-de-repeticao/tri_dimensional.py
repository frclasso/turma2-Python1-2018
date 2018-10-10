lot_3d = [
    [
        ['Tesla', 'Fiat', 'BMW'],
        ['Honda', 'Jeep'],
        ['Saab', 'Kia', 'Ford']
    ],
    [
        ['Subaru', 'Nissan'],
        ['Volvo']
    ],
    [
        ['Mazda', 'Chevy'],
        ['Fusca'],
        ['Volkswagen']
    ]
]

#print(lot_3d)
# todos os carros
# for floor in lot_3d:
#     for row in floor:
#         for car in row:
#             print(car)

# Pegando apenas o primeiro carro
for floor in lot_3d:
    for row in floor:
       print(row[0])
