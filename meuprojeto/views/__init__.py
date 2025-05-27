from pyramid.view import view_config
from pyramid.view import view_config
from ..models import DBSession, Service  # <- Importa o DBSession e o modelo Service


@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    servicos = DBSession.query(Service).all()
    return {'servicos': servicos}
