import validator
import os

a = 0
b = 0
c = 0
val = validator.Validator("do i need it i dont think so")

def read_file():
    os.chdir("/home/denys/computorV1")
    cur_dir = os.getcwd()
    print (cur_dir)

    eq_file = open("/home/denys/computorV1/equation.txt")
    equation = eq_file.read()
    return equation
# split equation to 2 sides stripped from spaces at the beginning and at the end
def split_equation(equation):
    sides = equation.split('=')
    sides[0] = sides[0].replace(" ", "")
    sides[1] = sides[1].replace(" ", "")
    if (len(sides) == 2):
        return sides
    else:
        return None

# Returns 1 if evrthn is ok, and 0 if not
# drct: right side = 1, left side = -1
def grub_side(side, drct):
    sign = 1 # 1 = + , -1 = -
    while len(side) > 0:
        if val.min_or_plus(side[0]):
            sign = 1 * drct if side[0] == "+" else -1 * drct
            side = side[1:]
        ###read node
        i = 0
        while i < len(side) and (not val.min_or_plus(side[i])):
            if val.prepared_symbol(side[i]):
                i = i + 1
            else:
                return 0
        ###
        print(side[0:i])
        grub_node(side[0:i], sign)  ######## stopped here
        side = side[i:]
    return 1


def is_variable(part):
    if (len(part) >= 3):
        if (part[0] == 'x' or part[0] == 'X'):
            if (part[1] == '^'):
                try:
                    return int(part[2:]) >= 0
                except:
                    return False
    if ((len(part) == 1) and (part[0] == 'x' or part[0] == 'X')):
        return True
    return False

# node : 3*x^1*0.2*x^0*5
# return None if smth is not ok / and 1 if all ok
# sign 1 /-1
def grub_node(node, sign):
    parts = node.split('*')
    print(parts)
    fk = 1 # koef
    fpow = 0 # power
    for part in parts:
        try:
            fk = fk * float(part)
        except:
            if part == "x" or part == "X":
                fpow = fpow + 1
            elif is_variable(part):
                try:
                    fpow = fpow + int(part[2:])
                except:
                    print("There is some fucking power number in a node:" + node)
                    return None 
            else:
                return None
    if fpow > 2:
        return None
    if (fpow == 0):
        c = c + c * sign
    if (fpow == 1):
        b = b + b * sign
    if (fpow == 2):
        a = a + a * sign
    print(fk)
    print(fpow)
    return 1


sides = split_equation(" +4*5*X^5- 3 * x^22 + 3*x^1*0.2*x^0*5 = x^2 + 121 * x^3")
grub_node("3*x*0.4*X*5", "")
# grub_side(sides[1])
# print(sides[0] + "|||" + sides[1])



                   

# def split_to_nodes(sides):
#     if sides is None:
#         print("Give me normal equation please")
#         return
#     left_nodes = []
#     left_side = sides[0].split(' + ')
#     for node in left_side:
#         left_nodes.extend(node.split('-'))


#     #splt right side
#     print(left_nodes)

# if node_analize("4 * 3.3 * x^22 * 8") is None:
#     print("oy-oy")

