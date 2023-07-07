
import re
from flask import Blueprint, render_template, url_for, request, redirect, abort, jsonify
from werkzeug.exceptions import HTTPException

from . import solver


main = Blueprint('main', __name__)

@main.route('/')
def index():
    try:
        return render_template('index.html', active = 'home', title = "Home")
    except HTTPException:
        return abort(404)
    except Exception:
        return abort(500)


@main.route('/about')
def about():
    try: 
        return render_template('about.html', active = 'about', title = "About")
    except HTTPException:
        return abort(404)
    except Exception:
        return abort(500)


@main.route('/contact')
def contact():
    try:
        return render_template('contact_page.html', active = 'contact', title = "Contact")

    except HTTPException:
        return abort(404)
    except Exception:
        return abort(500)

@main.route('/contact', methods = ["POST"])
def contact_mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')


    return jsonify({"status": "success"})



@main.route('/calc')
def calc():
    
    params = request.args.get('p')
    print(params)
    if(params == 's-1'):
        return render_template('s1.html', title = "s1")
    elif(params == 's-2'):
        
        return render_template('s2.html', title = "Determinant", message = '')

    elif(params == 's-3'):
        print("sutra-3 is requested")
        return render_template("s3.html", title = "Inverse of Matrix", message = '')
    elif(params == 's-4'):
        
        return render_template("s4.html", title = "Equations")

    elif(params == 's-5'):
        return render_template("s5.html", title = "Pair of Linear Equations in two variable")
    else:
        return abort(404)


@main.route('/calc', methods = ['POST'])
def calc_answer():
    # try:
        params = request.args.get('p')

        print(params)

        if(params == 's-2-que'):            ## determinant solution
            #print("solve determinant...")
            inputs = request.form.items()
            elements = []
            for i,j in inputs:
                if(i and j):
                    elements.append({i:int(j)})
            #print(elements)
            if(len(elements) < 9):
                #print("some elements might be missing!")
                
                return render_template('s2.html', title = "Determinants", message = ["Some elements might be missing", "Enter all values in the Determinant"])
                #message = 
            elif(len(elements) == 9):           ## determinant solution (3 x 3)
                #print("3 x 3 determinant")
                sol = solver.det_9(elements)
            
                return render_template('s2_answer.html', solution = sol, size = 9, title = "solution determinant")
            elif(len(elements) == 16):          ## determinant solution (4 x 4)
                #print("4 x 4 determinant")
                sol  = solver.det_16(elements)
                return render_template('s2_answer.html', solution = sol, size = 16, title = "solution determinant")
            else:
                return render_template('s2.html', title = "Error", message  = ["Something Went Wrong!", "Please retry..."])
        
        elif(params == 's-3-que'):              ## matrix inverse solution (3 x 3)
            #print("solving inverse of matrix...")
            inputs = request.form.items()
            elements = []
            for i,j in inputs:
                if(i and j):
                    elements.append({i:int(j)})
            
            solution = solver.mat_inverse(elements)
            if(len(solution)>2):
                return render_template("s3_answer.html", title = "Inverse of Matrix Solution", solution = solution, sol_yes = "Yes")
            else:
                return render_template("s3_answer.html", title = "Inverse of Matrix Solution", solution = solution, sol_yes = "No")
            
            
            
        elif(params == 's-4-que'):          ## equations solution
            #print("solving equations......!")
            eq_type = request.args.get('t')


            inp_iter = request.form.items()
            
            inp_values = {}

            for i, j in inp_iter:
                if(i and j):
                    inp_values.update( {i : int(j)})
                

            #print(inp_values)


            if(eq_type == 'type-1'):
                
                sol = solver.simple_eq_type1(inp_values)
                
                if(sol["solution"] or sol["type"] == "infinite"):
                    
                    return render_template('s4_answer.html', title = "solution of linear equation", solution = sol, sol_exists = "Yes", eq_type = "type-1")
                    
                else:
                    return render_template('s4_answer.html', title = "solution of linear equation", solution = sol, sol_exists = "No", eq_type = "type-1")
                
                    

            elif(eq_type == 'type-2'):
                sol = solver.simple_eq_type2(inp_values)

                if(sol["solution"]):
                
                    return render_template('s4_answer.html', title = "solution of linear equation", solution = sol, sol_exists = "Yes", eq_type = "type-2")
                    
                else:
                    return render_template('s4_answer.html', title = "solution of linear equation", solution = sol, sol_exists = "No", eq_type = "type-2")


            elif(eq_type == 'type-3'):
                
                sol = solver.simple_eq_type3(inp_values)

                if(sol["solution"]):
                    
                    return render_template('s4_answer.html', title = "solution of linear equation", solution = sol, sol_exists = "Yes", eq_type = "type-3")
                    
                else:
                    return render_template('s4_answer.html', title = "solution of linear equation", solution = sol, sol_exists = "No", eq_type = "type-3")

            elif(eq_type == 'type-4'):

                sol = solver.simple_eq_type4(inp_values)

                if(sol["solution"]):
                    
                    return render_template('s4_answer.html', title = "solution of linear equation", solution = sol, sol_exists = "Yes", eq_type = "type-4")
                    
                else:
                    return render_template('s4_answer.html', title = "solution of linear equation", solution = sol, sol_exists = "No", eq_type = "type-4")
            
            
            elif(eq_type == 'type-5'):

                sol = solver.simple_eq_type5(inp_values)

                if(sol["solution"]):
                    
                    return render_template('s4_answer.html', title = "solution of linear equation", solution = sol, sol_exists = "Yes", eq_type = "type-5")
                    
                else:
                    return render_template('s4_answer.html', title = "solution of linear equation", solution = sol, sol_exists = "No", eq_type = "type-5")
            else: 
                return redirect(url_for('main.calc', p = ['s-4']))
        
        elif(params == 's-5-que'):          ## pair of linear equations in two variables solution
            inp_iter = request.form.items()
            
            inp_values = {}

            for i, j in inp_iter:
                if(i and j):
                    inp_values.update( {i : int(j)})

            
            sol = solver.lin_eq_pair(inp_values)

            
            return render_template('s5_answer.html', solution = sol, title = "Solution to pair of linear equation")

        else:
            return abort(404)
    
    # except HTTPException:
    #     return abort(404)
    # except Exception:
    #     return abort(500)


# @main.route('/favicon.ico')
# def favicon():
#     return url_for('static', filename='favicon.ico')
