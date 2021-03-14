import json
from flask import jsonify


def code_word(code,data,msg):  
    msg = {
        'code': code,
        'data': data,
        'message': msg
    } 
    return msg

