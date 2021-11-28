def header(request):
    auth = request.META.get('HTTP_AUTHORIZATION')
    if auth:
        auth = auth.split()
    # print(auth)
    if auth and auth[1]:
        return auth[1]

    return False

def client(request):
    client = request.META.get('HTTP_X_CLIENT_DATA')
    if not client:
        return False
    return client

def client_type(request):
    client = request.META.get('HTTP_X_CLIENT_TYPE')
    if not client:
        return False
    return client

def client_agent(request):
    client = request.META.get('HTTP_USER_AGENT')
    if not client:
        return False
    return client

def client_type(request):
    client = request.META.get('HTTP_X_CLIENT_TYPE')
    if not client:
        return False
    return client

def client_timezone(request):
    client = request.META.get('HTTP_X_CLIENT_TIMEZONE')
    if not client:
        return False
    return client

def client_country(request):
    client = request.META.get('HTTP_X_CLIENT_COUNTRY')
    if not client:
        return False
    return client

def client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip