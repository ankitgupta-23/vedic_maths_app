from flask import Blueprint, render_template
from werkzeug.exceptions import HTTPException

handle_exceptions =  Blueprint('handle_exceptions', __name__)

@handle_exceptions.app_errorhandler(HTTPException)
def handle_404(err):
    if(err.code == 404):
        return render_template('err_404.html', title  = 'Not found - 404 error'), 400
    elif(err.code == 500):
        return "500 error - we will use a custom template", 500


# @handle_exceptions.app_errorhandler(Exception)
# def handle_any_uncertainity(err):
#     return {"err": err}
