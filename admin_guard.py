from functools import wraps
from flask import request, session, jsonify




def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('is_admin'):
            return jsonify({'error': 'admin_required'}), 403
        return fn(*args, **kwargs)
    return wrapper  