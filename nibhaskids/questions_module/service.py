import secrets
import hashlib
from django.db import connection


def random_hash(length=10):
    random_bytes = secrets.token_bytes(length)
    random_hash = hashlib.sha256(random_bytes).hexdigest()[:length]
    return random_hash

def save_file(upload_path, uploaded_file):
    print('directory:',upload_path)
    with open(upload_path, 'wb') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)

def admin_authentication(username,password):
    with connection.cursor() as cursor:
        cursor.execute("select count(*) from questions_module_admin where username = %s and password=%s",[username,password])
        row=cursor.fetchone()
    if row[0] == 1:
        return True
    else:
        return False

        
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # The first IP address in the list is typically the original client IP address
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    return ip_address

    



