import math
from fractions import Fraction

########################################################### 
#                           s-2                           #
#                solution of 3 x 3 Determinant            #
########################################################### 
def det_9(mat):
    #print("3 x 3 determinant")
    d1 = mat[3]["a4"]*mat[7]["a8"] - mat[6]["a7"]*mat[4]["a5"]
    d2 = mat[3]["a4"]*mat[8]["a9"] - mat[6]["a7"]*mat[5]["a6"]
    d3 = mat[4]["a5"]*mat[8]["a9"] - mat[5]["a6"]*mat[7]["a8"]

    answer = mat[0]["a1"]*d3 - mat[1]["a2"]*d2 + mat[2]["a3"]*d1
    
    solution = {"mat":mat ,"d1":d1, "d2":d2, "d3": d3, "answer": answer}

    return solution



###########################################################
#                           s-2                           #
#                solution of 4 x 4 Determinant            #
########################################################### 

def det_16(mat):
    #print("4 x 4 determinant")
    # upper half
    d1 = mat[0]["a1"]*mat[5]["a6"] - mat[4]["a5"]*mat[1]["a2"]
    d2 = mat[0]["a1"]*mat[6]["a7"] - mat[4]["a5"]*mat[2]["a3"]
    d3 = mat[0]["a1"]*mat[7]["a8"] - mat[4]["a5"]*mat[3]["a4"]
    d4 = mat[1]["a2"]*mat[6]["a7"] - mat[5]["a6"]*mat[2]["a3"]
    d5 = mat[1]["a2"]*mat[7]["a8"] - mat[5]["a6"]*mat[3]["a4"]
    d6 = mat[2]["a3"]*mat[7]["a8"] - mat[6]["a7"]*mat[3]["a4"]

    #lower half
    d7 = mat[8]["a9"]*mat[13]["a14"] - mat[12]["a13"]*mat[9]["a10"]
    d8 = mat[8]["a9"]*mat[14]["a15"] - mat[12]["a13"]*mat[10]["a11"]
    d9 = mat[8]["a9"]*mat[15]["a16"] - mat[12]["a13"]*mat[11]["a12"]
    d10 = mat[9]["a10"]*mat[14]["a15"] - mat[13]["a14"]*mat[10]["a11"]
    d11 = mat[9]["a10"]*mat[15]["a16"] - mat[13]["a14"]*mat[11]["a12"]
    d12 = mat[10]["a11"]*mat[15]["a16"] - mat[14]["a15"]*mat[11]["a12"]

    answer = d1*d12 - d2*d11 + d3*d10 + d4*d9 - d5*d8 + d6*d7
    
    solution = {"mat":mat,
                 "d1":d1, 
                 "d2":d2, 
                 "d3":d3, 
                 "d4":d4, 
                 "d5":d5, 
                 "d6":d6, 
                 "d7":d7, 
                 "d8":d8,
                 "d9":d9,
                 "d10":d10,
                 "d11":d11,
                 "d12":d12,
                 "answer": answer
                }
    return solution



########################################################### 
#                           s-3                           #
#                   Inverse of a Matrix                   #
########################################################### 

def mat_inverse(mat):

    # adjoint first row:
    adj_11 = mat[4]["a5"] * mat[8]["a9"] - mat[7]["a8"] * mat[5]["a6"]
    adj_12 = mat[7]["a8"] * mat[2]["a3"] - mat[1]["a2"] * mat[8]["a9"]
    adj_13 = mat[1]["a2"] * mat[5]["a6"] - mat[4]["a5"] * mat[2]["a3"]

    #adjoint second row:
    adj_21 = mat[5]["a6"] * mat[6]["a7"] - mat[8]["a9"] * mat[3]["a4"]
    adj_22 = mat[8]["a9"] * mat[0]["a1"] - mat[2]["a3"] * mat[6]["a7"]
    adj_23 = mat[2]["a3"] * mat[3]["a4"] - mat[5]["a6"] * mat[0]["a1"]

    #adjoint third row:

    adj_31 = mat[3]["a4"] * mat[7]["a8"] - mat[6]["a7"] * mat[4]["a5"]
    adj_32 = mat[6]["a7"] * mat[1]["a2"] - mat[0]["a1"] * mat[7]["a8"]
    adj_33 = mat[0]["a1"] * mat[4]["a5"] - mat[3]["a4"] * mat[1]["a2"]

    adjA = [adj_11, adj_12, adj_13, adj_21, adj_22, adj_23, adj_31, adj_32, adj_33]

    detA = det_9(mat)["answer"]

    inverseA = []
    count = []

    print("Adjoint of A: " , adjA)
    if(detA==0):
        return {"mat":mat, "detA":detA}

    for i in adjA:
        ans = Fraction(i, detA).as_integer_ratio()
        if(ans[1]==1):
            inverseA.append({"num": ans[0]})
            count.append(1)
        else:
            inverseA.append({"num": ans[0], "deno": ans[1]})
            count.append(2)
    
    #print(count)
    solution = {"mat":mat, "adjA":adjA, "inverseA": inverseA, "detA":detA, "count":count}

    return solution



########################################################### 
#                          s-4                            #
#                Simple Linear Equations                  #
###########################################################


# simple linear equation of type-1

def simple_eq_type1(terms):
    
    if( (terms["a"] == terms["c"]) and (terms["b"] == terms["d"]) ):
        return {"terms":terms, "solution": None, "type" : "infinite"}
    
    if ( (terms["a"] == terms["c"]) and (terms["b"] != terms["d"]) ):
        return {"terms":terms, "solution": None, "type" : "no solution"}

    num = terms["d"] - terms["b"]
    deno = terms["a"] - terms["c"]
    count = 0
    ans = None

    if(deno == 0):
        return {"terms":terms, "num":num, "deno":deno, "solution": ans}
    
    ans = Fraction(num, deno).as_integer_ratio()
    

    if(ans[1]==1):
        count = 1
    else:
        count = 2
    
    return {"terms":terms,"num":num, "deno":deno, "solution": ans, "count":count, "type" : "one solution"}


# simple linear equation of type-2

def simple_eq_type2(terms):

    ans = None

    num = (terms["p"] * terms["q"]) - (terms["m"] * terms["n"])
    deno = (terms["m"] + terms["n"]) - (terms["p"] + terms["q"])
    

    if(deno==0):
        return {"terms":terms, "num":num, "deno":deno, "solution": ans}
        
    ans = Fraction(num, deno).as_integer_ratio()
    
    count = 0

    if(ans[1]==1):
        count = 1
    else:
        count = 2
    
    return {"terms":terms, "num":num, "deno":deno, "solution": ans, "count": count}



# simple linear equation of type-3

def simple_eq_type3(terms):

    num = (terms["p"] * terms["d"]) - (terms["b"] * terms["q"])
    deno = (terms["a"] * terms["q"]) - (terms["c"] * terms["p"])
    
    ans = None
    
    if(deno==0):
        return {"terms":terms,"num":num, "deno":deno, "solution": ans}
    
    ans = Fraction(num, deno).as_integer_ratio()

    count = 0

    if(ans[1]==1):
        count = 1
    else:
        count = 2
    
    return {"terms":terms, "num":num, "deno":deno, "solution": ans, "count":count}


# simple linear equation of type-4

def simple_eq_type4(terms):
    num = -(terms["m"] * terms["b"]) - (terms["n"] * terms["a"])
    deno = (terms["m"] + terms["n"])
    ans = None

    if(deno==0):
        return {"terms":terms,"num":num, "deno":deno, "solution": ans}
    
    ans = Fraction(num, deno).as_integer_ratio()
    count = 0

    if(ans[1]==1):
        count = 1
    else:
        count = 2
    
    return {"terms":terms,"num":num, "deno":deno, "solution": ans, "count":count}



# simple linear equation of type-5

def simple_eq_type5(terms):
    num = (terms["p"] * (-terms["c"])) + (terms["q"] * (-terms["a"])) + (terms["r"] * (-terms["b"]))
    deno = (terms["p"] + terms["q"] + terms["r"])

    ans = None
    
    if(deno==0):
        return {"terms":terms, "num":num, "deno":deno, "solution": ans}
        
    ans = Fraction(num, deno).as_integer_ratio()
    

    count = 0

    if(ans[1]==1):
        count = 1
    else:
        count = 2
    
    return {"terms":terms, "num":num, "deno":deno, "solution": ans, "count":count}





########################################################### 
#                          s-5                            #
#                Pair of Linear Equations                 #
#                    in two variables                     #
###########################################################

def eq_pair_general(coeff):
    ## general case (normal method)

    x_num = (coeff["b1"] * coeff["c2"]) - (coeff["b2"] * coeff["c1"])
    y_num = (coeff["c1"] * coeff["a2"]) - (coeff["c2"] * coeff["a1"])
    
    x_y_deno = - ((coeff["a1"] * coeff["b2"]) - (coeff["a2"] * coeff["b1"]))
    
    x = Fraction(x_num, x_y_deno).as_integer_ratio()
    y = Fraction(y_num, x_y_deno).as_integer_ratio()

    x_count = 1
    y_count = 1

    if(x[1] != 1):
        x_count = 2
    
    if(y[1] != 1):
        y_count = 2

    return {"coeff" : coeff, "x_num" : x_num, "y_num": y_num, "x_y_deno": x_y_deno, "x" : x, "y": y, "x_c":x_count, "y_c":y_count, "type":"normal"}


def lin_eq_pair(coeff):

    #homogenous case:
    if(coeff["c1"] == 0 and coeff["c2"] == 0):
        return {"coeff": coeff, "type": "homogenous"}


    
    a_ratio = Fraction(coeff["a1"], coeff["a2"]).as_integer_ratio()
    b_ratio = Fraction(coeff["b1"], coeff["b2"]).as_integer_ratio()
    
    
    if(coeff["c2"] != 0):
    
        c_ratio = Fraction(coeff["c1"], coeff["c2"]).as_integer_ratio()
     
        x = None
        y = None

        # no solution case
        if( (a_ratio == b_ratio) and ((a_ratio != c_ratio) and (b_ratio != c_ratio)) ):
            return {"coeff": coeff, "a_ratio": a_ratio, "b_ratio": b_ratio, "c_ratio": c_ratio, "type":"no solution" }
    
        # infinite solution case
        if( (a_ratio == b_ratio) and (b_ratio == c_ratio) and (c_ratio == a_ratio) ):
            return {"coeff": coeff, "a_ratio": a_ratio, "b_ratio": b_ratio, "c_ratio": c_ratio, "type":"inf solution" }

    else:
        return eq_pair_general(coeff)
        

    x_count = 1
    y_count = 1
    # case 1: Anurupye Sunymanyat : 
    # ( if a1/a2 = c1/c2, then y = 0 )
    # ( if b1/b2 = c1/c2, then x = 0 )

    if(a_ratio == c_ratio):
        y = 0
        x = Fraction(coeff["c1"], coeff["a1"]).as_integer_ratio()
        if(x[1] == 1):
            x_count = 1
        else:
            x_count = 2

        return {"coeff": coeff, "a_ratio": a_ratio, "b_ratio": b_ratio, "c_ratio": c_ratio, "type":"AnuSu", "x":x, "y":y, "x_c": x_count, "y_c": y_count}
    
    elif(b_ratio == c_ratio):
        x = 0
        y = Fraction(coeff["c1"], coeff["b1"]).as_integer_ratio()
        if(y[1] == 1):
            y_count = 1
        else:
            y_count = 2

        return {"coeff": coeff, "a_ratio": a_ratio, "b_ratio": b_ratio, "c_ratio": c_ratio, "type":"AnuSu", "x":x, "y":y, "x_c": x_count, "y_c": y_count}

    
    
    # case 2: Sankalana Vyavakalanam : 
    # ( coefficient of x in first equation is equal to coefficient of y in second equation
    # add and subtract to get the solution)
    

    if (coeff["a1"] == coeff["b2"] and coeff["a2"] == coeff["b1"]):
        
        eq_4 = {}
        eq_5 = {}


        # add both equations
        
        eq_4_coeff_x = coeff["a1"] + coeff["a2"]
        eq_4_coeff_y = coeff["b1"] + coeff["b2"]
        eq_4_constant_term = coeff["c1"] + coeff["c2"]

        eq_4 = {"a41": eq_4_coeff_x, "a42": eq_4_coeff_y, "c4": eq_4_constant_term}

        # subtract both equation

        if (coeff["a1"]>=coeff["a2"]):
            eq_5_coeff_x = coeff["a1"] - coeff["a2"]
            eq_5_coeff_y = coeff["b1"] - coeff["b2"]
            eq_5_constant_term = coeff["c1"] - coeff["c2"]

            eq_5 = {"a51": eq_5_coeff_x, "a52": eq_5_coeff_y, "c5": eq_5_constant_term}
        else:
            eq_5_coeff_x = coeff["a2"] - coeff["a1"]
            eq_5_coeff_y = coeff["b2"] - coeff["b1"]
            eq_5_constant_term = coeff["c2"] - coeff["c1"]

            eq_5 = {"a51": eq_5_coeff_x, "a52": eq_5_coeff_y, "c5": eq_5_constant_term}


        
        c6 = Fraction(eq_4_constant_term, eq_4["a41"]).as_integer_ratio()
        c7 = Fraction(eq_5_constant_term, eq_5["a51"]).as_integer_ratio()

        c_6_count = 1
        c_7_count = 1

        if(c6[1] !=1):
            c_6_count = 2
        if(c7[1] != 1 ):
            c_7_count = 2

        x_num = (c6[0] * c7[1] + c7[0] * c6[1])
        x_deno = (c6[1] * c7[1])
        y_num = (c6[0] * c7[1] - c7[0] * c6[1])
        y_deno = (c6[1] * c7[1])
        
        
        x = Fraction(x_num, 2 * x_deno).as_integer_ratio()
        y = Fraction(y_num, 2 * y_deno).as_integer_ratio()
        
        
        x_count = 1
        y_count = 1
        if(x[1] !=1):
            x_count = 2
        if(y[1] != 1 ):
            y_count = 2

        return {"coeff": coeff, "eq_4": eq_4, "eq_5": eq_5, "c6":c6, "c7":c7, "c6_c": c_6_count, "c7_c": c_7_count, "x":x, "y":y, "x_c":x_count, "y_c": y_count, "x_num":x_num, "y_num":y_num, "x_deno":x_deno, "y_deno":y_deno, "type": "SanVya"}

    return eq_pair_general(coeff)







    




     



    
