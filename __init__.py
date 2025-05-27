import os
from pyramid.session import SignedCookieSessionFactory
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application. """
    config = Configurator(settings=settings)
    
    my_session_factory = SignedCookieSessionFactory('sua_chave_secreta_aqui')
    config.set_session_factory(my_session_factory)

    # Configuração do SQLAlchemy
    engine = engine_from_config(settings, 'sqlalchemy.')
    
    # Importa e inicializa os modelos
    from .models.base import initialize_sql
    initialize_sql(engine)
    
    # Configuração de transações
    config.include('pyramid_tm')
    
    # Adiciona dbsession ao request
    from .models.base import DBSession
    config.add_request_method(
        lambda request: DBSession,
        'dbsession',
        property=True
    )
    
    # Configuração do Jinja2
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path(os.path.join(os.path.dirname(__file__), 'templates'))
    config.add_static_view(name='static', path='meuprojeto:static', cache_max_age=3600)

    
    # Inclui rotas e faz scan dos modelos e views
    config.include('.routes')

    config.scan()  # Para registrar as views
    
    return config.make_wsgi_app()