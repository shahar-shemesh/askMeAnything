from flask import jsonify
from werkzeug.exceptions import HTTPException
from app.errors import bp


@bp.app_errorhandler(HTTPException)
def not_found_error(err):
    
    return jsonify({
        "code": err.code,
        "name": err.name,
        "description": err.description,
    })
    
    """ Error handler for HTTP exceptions.
    Args: err (HTTPException): The HTTP exception that was raised.
    Return: Response: A JSON response containing the error code, name, and description. """