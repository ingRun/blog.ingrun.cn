from app import blog


@blog.route('/')
def hello_world():
    return 'Hello World!'
