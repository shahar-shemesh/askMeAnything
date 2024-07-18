from flask import current_app, jsonify
from werkzeug.exceptions import HTTPException
from app.errors import bp


@bp.app_errorhandler(HTTPException)
def not_found_error(err):
    # format error response
    response = {
        f'error_{key}': getattr(err, key, f"Error {key.capitalize()} Not Found")
        for key in ['code', 'name', 'description']
    }
    return jsonify(response), getattr(err, 'code', 400)

    
    
@bp.app_errorhandler(Exception)
def handle_exception(err):
    response = {
        "error": str(err),
        "message": "An Error Occurred"
    }
    # log error details
    current_app.logger.info(f'Exception: {str(err)}')
    return jsonify(response), 500