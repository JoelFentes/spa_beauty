from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models import Funcionario

@view_config(route_name='funcionario_list', renderer='funcionarios/list.jinja2')
def list_funcionarios(request):
    funcionarios = request.dbsession.query(Funcionario).all()
    return {'funcionarios': funcionarios}

@view_config(route_name='funcionario_create', renderer='funcionarios/novo.jinja2', request_method=['GET', 'POST'])
def create_funcionario(request):
    if request.method == 'POST':
        nome = request.params.get('nome')
        cargo = request.params.get('cargo')
        telefone = request.params.get('telefone')
        email = request.params.get('email')
        if not nome:
            return {'error': 'Nome obrigatório'}
        funcionario = Funcionario(nome=nome, cargo=cargo, telefone=telefone, email=email)
        request.dbsession.add(funcionario)
        return HTTPFound(location=request.route_url('funcionario_list'))
    return {}

@view_config(route_name='funcionario_edit', renderer='funcionarios/edit.jinja2', request_method=['GET', 'POST'])
def edit_funcionario(request):
    funcionario_id = request.matchdict.get('id')
    funcionario = request.dbsession.query(Funcionario).get(funcionario_id)
    if not funcionario:
        raise HTTPNotFound()
    if request.method == 'POST':
        funcionario.nome = request.params.get('nome', funcionario.nome)
        funcionario.cargo = request.params.get('cargo', funcionario.cargo)
        funcionario.telefone = request.params.get('telefone', funcionario.telefone)
        funcionario.email = request.params.get('email', funcionario.email)
        return HTTPFound(location=request.route_url('funcionario_list'))
    return {'funcionario': funcionario}

@view_config(route_name='funcionario_delete', request_method='POST')
def delete_funcionario(request):
    funcionario_id = request.matchdict.get('id')
    funcionario = request.dbsession.query(Funcionario).get(funcionario_id)
    if not funcionario:
        raise HTTPNotFound()
    request.dbsession.delete(funcionario)
    return HTTPFound(location=request.route_url('funcionario_list'))
