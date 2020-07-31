def CheckCorrect(p):
    st = 0
    for i in p:
        if i == "(":
            st +=1
        else:
            if st <= 0:
                return False
            else:
                st -= 1
    if st == 0:
        return True
def CheckBalance(p):
    left, right = 0, 0
    for i in p:
        if i == "(":
            left+=1
        else:
            right+=1
    if left == right:
        return True
    else:
        return False

def solution(p):
    if p == "":
        return ""
    elif CheckCorrect(p) ==True:
        return p
    else:
        u, v = p[:2], p[2:]
        while(CheckBalance(u)!=True or CheckBalance(v)!=True):
            temp = v[:2]
            u = u + temp
            v = v[2:]
        if CheckCorrect(u)== True:
            return u + solution(v)
        else:
            string = '(' + solution(v) + ')'
            new_u = u[1:-1]
            for i in new_u:
                if i == '(':
                    string += ')'
                else:
                    string += '('
            return string