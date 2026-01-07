import pytest

def addition(a, b):
    return a+b 

def subtraktion(a, b):
    return a-b 

def multiplikation(a, b):
    return a*b 

def division(a, b):
    if b!=0: 
        return a/b 
    else: 
        raise ZeroDivisionError("Division durch Null ist nicht erlaubt") 


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-5, 10) == 5

def test_subtraktion():
    assert subtraktion(5,3) == 2
    assert subtraktion(10,5) == 5

def test_multiplikation():
    assert multiplikation(5,5) == 25
    assert multiplikation(6,6) == 36

def test_divison():
    assert division(10,2) == 5
    assert division(30,10) == 3

def test_division_by_Zero():
    with pytest.raises(ZeroDivisionError):
        division(2,0)

def erhoehe_um_vier(zahl):
    return zahl + 4 
def multipliziere_mit_5(zahl):
    return zahl * 5 
def subtrahiere_zehn(zahl):
    return zahl - 10
def teile_durch_vier(zahl):
    if zahl%4!=0: 
        raise ValueError("ist nicht durch vier teilbar") 
    return zahl / 4 

#Versuche danach zu ermitteln, was der folgende Test genau macht: 
@pytest.mark.parametrize("num1, num2, expected", [          #Testet mit den 4 Tupel unter jedesmal
 (1,5,5),
 (2,8,16),
 (-5,-2,10),
 (-7,+3,-21) 
])

def test_multiplikation_mehrfach(num1, num2, expected):
 assert multiplikation(num1, num2) == expected