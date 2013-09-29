'''
Created on Sep 26, 2013

@author: trer
'''
import decimal
import math
e = decimal.Decimal('10')**-9
maxf = 2**32
def check_can(a,b,c):
    if (a == b or b == c or a ==c):
        return 1
    return 0
def check_deu(a,b,c):
    if ( a== b and b ==c ):
        return 1
    return 0
def check_input(a,b,c):
    if ( a < maxf and b < maxf and c < maxf and a >= e and b >= e and c >= e ):
        return 1
    return 0
def check_vuong(a,b,c):
    if b > c:
        d = b
        b = c
        c = d
    if a > c:
        d = a
        a = c
        c = d
    if ((a*a+b*b-c*c)>0):
        if ( a*a+b*b-c*c) < e**2:
            return 1
    else:
        if ( c*c-a*a-b*b) < e**2:
            return 1
    return 0
def check_triangle(a,b,c):
    if (( a+b ) > c and ( b+c ) > a and ( a+c ) > b):
        return 1
    return 0
def detect_triangle(a,b,c):
    if check_input(a,b,c):
        if check_triangle(a,b,c):
            if check_deu(a,b,c):
                return "deu"
            elif check_vuong(a,b,c) and check_can(a,b,c):
                return "vuongcan"
            elif check_vuong(a,b,c):
                return "vuong"
            elif check_can(a,b,c):
                return "can"
            else:
                return "thuong"
        else:
            return "khongphaitamgiac"
    else:
        return "wronginput"  