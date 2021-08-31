import base64 as helper


def base64ToString(b):
    b.decode(encoding)
    return helper.b64decode(b, altchars=None, validate=False).decode('utf-8')


b = "aHR0cHM6Ly9tZWdhLm56L2ZvbGRlci9CZFJuU0FwYiNRelQzQnRORjhURFVQZkM0cVI0WHNn"

print(base64ToString(b))
