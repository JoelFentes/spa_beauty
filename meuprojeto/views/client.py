from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from ..models import Client

@view_config(route_name='client_list', renderer='clientes/list.jinja2')
def list_clients(request):
    clients = request.dbsession.query(Client).all()
    return {'clients': clients} 

@view_config(route_name='client_create', renderer='clientes/novo.jinja2', request_method=['GET', 'POST'])
def create_client(request):
    if request.method == 'POST':
        nome = request.params.get('nome')
        email = request.params.get('email')
        telefone = request.params.get('telefone')

        if not nome or not email:
            return {'error': 'Nome e e-mail são obrigatórios'}

        # Verifica se o cliente já está cadastrado (login simples)
        client = request.dbsession.query(Client).filter_by(email=email).first()

        if client:
            # Login bem-sucedido
            request.session['cliente_id'] = client.id
            return HTTPFound(location=request.route_url('service_list'))
        else:
            # Cadastra novo cliente
            client = Client(nome=nome, email=email, telefone=telefone)
            request.dbsession.add(client)
            request.session['cliente_id'] = client.id
            return HTTPFound(location=request.route_url('service_list'))

    return {}



""" @view_config(route_name='client_edit', renderer='clients/edit.jinja2', request_method=['GET', 'POST'])
def edit_client(request):
    client_id = request.matchdict.get('id')
    client = request.dbsession.query(Client).get(client_id)
    if not client:
        raise HTTPNotFound()
    if request.method == 'POST':
        client.nome = request.params.get('nome', client.nome)
        client.email = request.params.get('email', client.email)
        client.telefone = request.params.get('telefone', client.telefone)
        data_nascimento = request.params.get('data_nascimento')
        if data_nascimento:
            from datetime import datetime
            try:
                client.data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
            except ValueError:
                return {'error': 'Data inválida, use AAAA-MM-DD', 'client': client}
        client.observacoes = request.params.get('observacoes', client.observacoes)
        return HTTPFound(location=request.route_url('client_list'))
    return {'client': client}

@view_config(route_name='client_delete', request_method='POST')
def delete_client(request):
    client_id = request.matchdict.get('id')
    client = request.dbsession.query(Client).get(client_id)
    if not client:
        raise HTTPNotFound()
    request.dbsession.delete(client)
    return HTTPFound(location=request.route_url('client_list'))
 """