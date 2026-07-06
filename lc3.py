def list_add(l1,l2):
        final_int = int("".join(map(str,l1[::-1])))
        final_int2 = int("".join(map(str,l2[::-1])))
        result=final_int+final_int2
        to_print=list(map(int,str(result)))
        return to_print[::-1]
l1=[2,4,3]
l2=[5,6,4]
print(list_add(l1,l2))
