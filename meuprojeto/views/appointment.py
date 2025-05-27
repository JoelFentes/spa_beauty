from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models import Appointment, Client, Funcionario, Service
from datetime import datetime
from sqlalchemy.orm import joinedload


@view_config(route_name='appointment_list', renderer='appointments/list.jinja2')
def list_appointments(request):
    appointments = request.dbsession.query(Appointment).all()
    return {'appointments': appointments}

@view_config(route_name='appointment_create', renderer='appointments/novo.jinja2', request_method=['GET', 'POST'])
def create_appointment(request):
    funcionarios = request.dbsession.query(Funcionario).all()
    services = request.dbsession.query(Service).all()

    if request.method == 'POST':
        client_nome = request.params.get('client_nome')
        funcionario_id = request.params.get('funcionario_id')
        service_id = request.params.get('service_id')
        data_hora_str = request.params.get('data_hora')
        status = request.params.get('status', 'agendado')

        if not client_nome:
            return {
                'error': 'Por favor, informe o nome do cliente.',
                'funcionarios': funcionarios,
                'services': services
            }

        # Tenta converter data/hora
        try:
            data_hora = datetime.strptime(data_hora_str, '%Y-%m-%d %H:%M')
        except Exception:
            return {
                'error': 'Data/hora inválida, use AAAA-MM-DD HH:MM',
                'funcionarios': funcionarios,
                'services': services
            }

        # Procura cliente pelo nome, ou cria um novo (se quiser)
        client = request.dbsession.query(Client).filter(Client.nome == client_nome).first()
        if not client:
            client = Client(nome=client_nome)
            request.dbsession.add(client)
            request.dbsession.flush()  # Para garantir que client.id está preenchido

        appointment = Appointment(
            client_id=client.id,
            funcionario_id=funcionario_id,
            service_id=service_id,
            data_hora=data_hora,
            status=status
        )
        request.dbsession.add(appointment)
        return HTTPFound(location=request.route_url('appointment_list'))

    
    agendamentos = request.dbsession.query(Appointment).options(joinedload(Appointment.funcionario)).all()
    horarios_ocupados = [
        a.data_hora.strftime('%Y-%m-%d %H:%M') for a in agendamentos
    ]

    return {
        'funcionarios': funcionarios,
        'services': services,
        'horarios_ocupados': horarios_ocupados,
    }



@view_config(route_name='appointment_edit', renderer='appointments/edit.jinja2', request_method=['GET', 'POST'])
def edit_appointment(request):
    appointment_id = request.matchdict.get('id')
    appointment = request.dbsession.query(Appointment).get(appointment_id)
    if not appointment:
        raise HTTPNotFound()
    clients = request.dbsession.query(Client).all()
    funcionarios = request.dbsession.query(Funcionario).all()
    services = request.dbsession.query(Service).all()

    if request.method == 'POST':
        appointment.client_id = request.params.get('client_id', appointment.client_id)
        appointment.funcionario_id = request.params.get('funcionario_id', appointment.funcionario_id)
        appointment.service_id = request.params.get('service_id', appointment.service_id)
        data_hora_str = request.params.get('data_hora')
        if data_hora_str:
            try:
                appointment.data_hora = datetime.strptime(data_hora_str, '%Y-%m-%d %H:%M')
            except Exception:
                return {'error': 'Data/hora inválida, use AAAA-MM-DD HH:MM', 'appointment': appointment, 'clients': clients, 'funcionarios': funcionarios, 'services': services}
        appointment.status = request.params.get('status', appointment.status)
        return HTTPFound(location=request.route_url('appointment_list'))

    return {'appointment': appointment, 'clients': clients, 'funcionarios': funcionarios, 'services': services}

@view_config(route_name='appointment_delete', request_method='POST')
def delete_appointment(request):
    appointment_id = request.matchdict.get('id')
    appointment = request.dbsession.query(Appointment).get(appointment_id)
    if not appointment:
        raise HTTPNotFound()
    request.dbsession.delete(appointment)
    return HTTPFound(location=request.route_url('appointment_list'))
