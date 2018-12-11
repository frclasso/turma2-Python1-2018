#!/usr/bin/env python3

def kelvinToFahreinehit(Temperature):
    assert (Temperature >= 0), 'Colder than absolute zero'
    return ((Temperature - 273) * 1.8) + 32

print(kelvinToFahreinehit(273))
print(kelvinToFahreinehit(505.78))
print(kelvinToFahreinehit(0))
print(kelvinToFahreinehit(-1))