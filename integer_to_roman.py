# integer to roman

def solve(no):
    d = {
        1:"I",
        2:"II",
        3:"III",
        4:"IV",
        5:"V",
        6:"VI",
        7:"VII",
        8:"VIII",
        9:"IX",
        10:"X",
        20:"XX",
        30:"XXX",
        40:"XL",
        50:"L",
        60:"LX",
        70:"LXX",
        80:"LXXX",
        90:"XC",
        100:"C",
        200:"CC",
        300:"CCC",
        400:"CD",
        500:"D",
        600:"DC",
        700:"DCC",
        800:"DCCC",
        900:"CM",
        1000:"M",
        2000:"MM",
        3000:"MMM"
    }
    string = ""
    dig = 1
    s = 10
    while no > 0:
        r = no%s 
        while r == 0:
            s *= 10
            r = no % s 
        string = d[r*dig] + string
        dig *= s
        no //= s
        s = 10
    return string

print(solve(50))   # DLVI