from app import app

# NOT FOUND ERROR
@app.errorhandler(404)
def not_found_error(error):
    return 'That resource cannot be found on our servers'


# INTERNAL SERVER ERROR
@app.errorhandler(500)
def internal_server_error(error):
    return 'There was an arror with the server. Please contact that system administrator for assistance'