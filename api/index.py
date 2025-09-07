from myproject.wsgi import application  # Adjust if your project name is different

def handler(environ, start_response):
    return application(environ, start_response)
