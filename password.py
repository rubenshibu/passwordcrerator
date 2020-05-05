import random
import re
s="abcdefghijkl\
    mnopqrstuvwxyz1234\
        567890ABCDEFGHIJKLM\
            NOPQRSTUVWXYZ!@#$%^&*\
            ()_-+[{};/"

p = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])
    (?=.*[!@#$%^&*])
    (?=.*[0-9].*[0-9])
    (?=.*[a-z].*[a-z].*[a-z])
    .{10,}
    $
)''',re.VERBOSE)            
passwordlen = 16
password = "".join(random.sample(s,passwordlen))
re.sub(r"^\s+", "", password)
print(password)
def passwordcheck(password):
    m=p.search(password)
    if(not m):
        print("Weak Password")
        return False
    else:
        print("strong password")
        return True


passwordcheck(password)




