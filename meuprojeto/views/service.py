from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from ..models import DBSession
from ..models.service import Service

@view_config(route_name='service_list', renderer='templates/servicos/list.jinja2')
def listar_servicos(request):
    servicos = request.dbsession.query(Service).all()
    return {'servicos': servicos}


@view_config(route_name='service_create', renderer='templates/servicos/novo.jinja2')
def criar_servico(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST.get('descricao')
        imagem = request.POST.get('imagem')  # <- Adicionado aqui
        duracao = int(request.POST['duracao_minutos'])
        preco = float(request.POST['preco'])

        servico = Service(
            nome=nome,
            descricao=descricao,
            imagem=imagem,  
            duracao_minutos=duracao,
            preco=preco
        )
        DBSession.add(servico)
        return HTTPFound(location=request.route_url('service_list'))
    return {}

@view_config(route_name='service_edit', renderer='templates/servicos/form.jinja2')
def editar_servico(request):
    servico = DBSession.query(Service).get(int(request.matchdict['id']))
    if request.method == 'POST':
        servico.nome = request.POST['nome']
        servico.descricao = request.POST.get('descricao')
        servico.duracao_minutos = int(request.POST['duracao_minutos'])
        servico.preco = float(request.POST['preco'])
        return HTTPFound(location=request.route_url('service_list'))
    return {'servico': servico}

@view_config(route_name='service_delete')
def deletar_servico(request):
    servico = DBSession.query(Service).get(int(request.matchdict['id']))
    DBSession.delete(servico)
    return HTTPFound(location=request.route_url('service_list'))
