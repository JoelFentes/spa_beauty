from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models.payment import Payment
from ..models.appointment import Appointment

@view_config(route_name='payment_list', renderer='templates/payments/list.jinja2')
def list_payments(request):
    payments = request.dbsession.query(Payment).all()
    return {'payments': payments}

@view_config(route_name='payment_create', renderer='templates/payments/create.jinja2', request_method=['GET', 'POST'])
def create_payment(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        valor = request.POST.get('valor')
        metodo = request.POST.get('metodo')

        payment = Payment(
            appointment_id=appointment_id,
            valor=float(valor),
            metodo=metodo
        )
        request.dbsession.add(payment)
        return HTTPFound(location=request.route_url('payment_list'))
    # GET
    appointments = request.dbsession.query(Appointment).all()
    return {'appointments': appointments}

@view_config(route_name='payment_edit', renderer='templates/payments/edit.jinja2', request_method=['GET', 'POST'])
def edit_payment(request):
    payment_id = request.matchdict.get('id')
    payment = request.dbsession.query(Payment).get(payment_id)
    if not payment:
        raise HTTPNotFound()

    if request.method == 'POST':
        payment.appointment_id = request.POST.get('appointment_id')
        payment.valor = float(request.POST.get('valor'))
        payment.metodo = request.POST.get('metodo')
        return HTTPFound(location=request.route_url('payment_list'))

    appointments = request.dbsession.query(Appointment).all()
    return {'payment': payment, 'appointments': appointments}

@view_config(route_name='payment_delete', request_method='POST')
def delete_payment(request):
    payment_id = request.matchdict.get('id')
    payment = request.dbsession.query(Payment).get(payment_id)
    if not payment:
        raise HTTPNotFound()
    request.dbsession.delete(payment)
    return HTTPFound(location=request.route_url('payment_list'))
