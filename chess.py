e_r="2468"
o_r="1357"

e_c="bdfh"
o_c="aceg"
s="g4"
if s[0] in e_c:
    if s[1] in e_r:
        print("Black")
    else:
        print("White")
else:
    if s[1] in e_r:
        print("White")
    else:
        print("Black")