```python
from flask import g, request, jsonify
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature
from .models import User
from . import app

auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def verify_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None  # valid token, but expired
    except BadSignature:
        return None  # invalid token
    g.user = User.query.get(data['id'])
    return g.user is not None

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.verify_password(password):
        g.user = user
        token = g.user.generate_auth_token()
        return jsonify({'token': token.decode('ascii')})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
```