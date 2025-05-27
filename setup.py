from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_jinja2',
    'sqlalchemy',
    'pyramid_tm',  # Para gerenciamento de transações
    'zope.sqlalchemy',  # Para integração SQLAlchemy com Pyramid
    'psycopg2-binary',
    'waitress',
    'alembic'
]

setup(
    name='meuprojeto',
    packages=find_packages(),  
    include_package_data=True, 
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = meuprojeto:main',
        ],
    },
)
