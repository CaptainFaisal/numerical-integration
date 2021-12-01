from math import *

def show_table(f, a, b, n):
    print(40*"-")
    for i in range(n+1):
        print(f"| x{i} = {a+i*(b-a)/n} | y{i} = {f(a+i*(b-a)/n)} |")
        print(40*"-")

def simpsons_1_3_rule(f, a, b, n):
    h = (b-a)/n
    sum = h/3 * (f(a)+f(b))
    for i in range(1,n):sum += 2*(i%2+1)*(h/3)*f(a+i*h)
    return sum

def simpsons_3_8_rule(f, a, b, n):
    h = (b-a)/n
    sum = 3*h/8 * (f(a)+f(b))
    for i in range(1,n):sum+=(3-int(i%3==0))*(3*h/8)*f(a+i*h)
    return sum

def trapizoidal_rule(f, a, b, n):
    h = (b-a)/n
    sum = h*(f(a)+f(b))/2
    for i in range(1,n):sum += h*f(a+i*h)
    return sum

def weddles_rule(f, a, b, n):
    h = (b-a)/n
    sum = (3*h/10)*(f(a)+f(b))
    for i in range(1, n):sum+= (3*h/10)*(2+(2111/60)*(i%6)-(1391/24)*(i%6)**2+(785/24)*(i%6)**3-(181/24)*(i%6)**4+(73/120)*(i%6)**5)*f(a+i*h)
    return sum

print("Trapizoidal rule:", trapizoidal_rule(lambda x:e**(-x**2), 1, 2, 12))
print("Simpson's 1/3 rule:", simpsons_1_3_rule(lambda x:sin(x)/x, 1, 2, 12))
print("Simpson's 3/8 rule:", simpsons_3_8_rule(lambda x:sin(x)/x, 1, 2, 12))
print("Weddle's rule:", weddles_rule(lambda x:sin(x)/x, 1, 2, 12))