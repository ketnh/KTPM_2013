def detect_triangle(a, b, c):
    #if (type(a) != float and type(a) != int) or (type(b) != float and type(b) != int) or (type(c) != float and type(c) != int): 
        #return 'khong dung kieu'
    if (a > 2**32 - 1) or (b > 2**32 - 1) or (c > 2**32 - 1) or (type(a) not in [int, long, float]) or (type(b) not in [int, long, float]) or (type(c) not in [int, long, float]) : 
        return 'dau vao khong hop le'
    if (a <0 or b<0 or c<0): return 'dau vao khong hop le'   
    if (a + b <= c) or (b + c <= a) or (c + a <= b):
        return 'khong la tam giac'
    elif (a == b) and (b == c):
        return 'tam giac deu'
    elif (a == b) or (b == c) or (c == a) :
        if (abs(b*b + c*c - a*a) < 10**-5 ) or (abs(c*c + a*a - b*b) < 10**-5) or (abs(a*a + b*b - c*c) < 10**-5):
            return 'tam giac vuong can'            
        return 'tam giac can'
    elif (a*a == b*b + c*c) or (b*b == c*c + a*a) or (c*c == a*a + b*b):
        return 'tam giac vuong'
    else: return 'tam giac thuong'
