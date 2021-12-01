from math import *

def show_table(f, a, b, n):
    print(40*"-")
    for i in range(n+1):
        print(f"| x{i} = {a+i*(b-a)/n} | y{i} = {f(a+i*(b-a)/n)} |")
        print(40*"-")

def simpsons_1_3_rule(f, a, b, n):
    h = (b-a)/n
    p1 = ""
    p2 = ""
    sum = round(f(a), 5)+round(f(b), 5)
    for i in range(1,n):
        if i%2!=0:
            p1+=str(round(f(a+i*h), 5))+" + "
        else:
            p2+=str(round(f(a+i*h), 5))+" + "
        sum += 2*(i%2+1)*round(f(a+i*h), 5)
    res = "h/3 {"+str(round(f(a), 5))+" + "+str(round(f(b), 5))+" + 4("+p1[:-3]+") + 2("+p2[:-3]+")}"
    return res+" = "+str(round(sum*h/3, 5))

def simpsons_3_8_rule(f, a, b, n):
    h = (b-a)/n
    sum = round(f(a), 5)+round(f(b), 5)
    p1 = ""
    p2 = ""
    for i in range(1,n):
        if i%3!=0:
            p1+=str(round(f(a+i*h), 5))+" + "
        else:
            p2+=str(round(f(a+i*h), 5))+" + "
        sum+=(3-int(i%3==0))*round(f(a+i*h), 5)
    res = "3h/8 {"+str(round(f(a), 5))+" + "+str(round(f(b), 5))+" + 3("+p1[:-3]+") + 2("+p2[:-3]+")}"
    return res+" = "+str(round(sum*3*h/8, 5))

def trapizoidal_rule(f, a, b, n):
    h = (b-a)/n
    sum = (round(f(a), 5)+round(f(b), 5))/2
    res = f"h {'{'}({round(f(a), 5)} + {round(f(b), 5)})/2 + "
    for i in range(1,n):
        res += str(round(f(a+i*h), 5))+" + "
        sum += f(a+i*h)
    return res[:-3]+"} = "+str(round(sum*h, 5))

def weddles_rule(f, a, b, n):
    h = (b-a)/n
    sum = (round(f(a), 5)+round(f(b), 5))
    res = f"3h/10 ({round(f(a), 5)} + {round(f(b), 5)} + "
    for i in range(1, n):
        res += str(round((2+(2111/60)*(i%6)-(1391/24)*(i%6)**2+(785/24)*(i%6)**3-(181/24)*(i%6)**4+(73/120)*(i%6)**5),0))[:-2]+"x"+str(round(f(a+i*h), 5))+" + "
        sum+= round(2+(2111/60)*(i%6)-(1391/24)*(i%6)**2+(785/24)*(i%6)**3-(181/24)*(i%6)**4+(73/120)*(i%6)**5, 0)*round(f(a+i*h), 5)
    return res[:-3]+") = "+str(round(sum*3*h/10, 5))

print("Trapizoidal rule:", trapizoidal_rule(lambda x:sin(x)/x, 1, 2, 12))
print("Simpson's 1/3 rule:", simpsons_1_3_rule(lambda x:sin(x)/x, 1, 2, 12))
print("Simpson's 3/8 rule:", simpsons_3_8_rule(lambda x:sin(x)/x, 1, 2, 12))
print("Weddle's rule:", weddles_rule(lambda x:sin(x)/x, 1, 2, 12))