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
        cursor.execute("select count(*) from questions_module_admin where username = %s and password = %s",[username,password])
        row=cursor.fetchone()
        count=row[0]
        if count == 1:
            return True
        else:
            return False