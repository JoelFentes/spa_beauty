from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models import User

@view_config(route_name='user_list', renderer='users/list.jinja2')
def list_users(request):
    users = request.dbsession.query(User).all()
    return {'users': users}

@view_config(route_name='user_create', renderer='users/create.jinja2', request_method=['GET', 'POST'])
def create_user(request):
    if request.method == 'POST':
        username = request.params.get('username')
        password_hash = request.params.get('password_hash')
        role = request.params.get('role', 'admin')
        if not username or not password_hash:
            return {'error': 'username e password_hash obrigatórios'}
        user = User(username=username, password_hash=password_hash, role=role)
        request.dbsession.add(user)
        return HTTPFound(location=request.route_url('user_list'))
    return {}

@view_config(route_name='user_edit', renderer='users/edit.jinja2', request_method=['GET', 'POST'])
def edit_user(request):
    user_id = request.matchdict.get('id')
    user = request.dbsession.query(User).get(user_id)
    if not user:
        raise HTTPNotFound()
    if request.method == 'POST':
        user.username = request.params.get('username', user.username)
        user.password_hash = request.params.get('password_hash', user.password_hash)
        user.role = request.params.get('role', user.role)
        return HTTPFound(location=request.route_url('user_list'))
    return {'user': user}

@view_config(route_name='user_delete', request_method='POST')
def delete_user(request):
    user_id = request.matchdict.get('id')
    user = request.dbsession.query(User).get(user_id)
    if not user:
        raise HTTPNotFound()
    request.dbsession.delete(user)
    return HTTPFound(location=request.route_url('user_list'))
