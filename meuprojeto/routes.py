def includeme(config):
    config.add_route('home', '/')

    # Clientes
    config.add_route('client_list', '/clientes')
    config.add_route('client_create', '/clientes/novo')
    config.add_route('client_edit', '/clientes/{id}/editar')
    config.add_route('client_delete', '/clientes/{id}/deletar')

    # Serviços
    config.add_route('service_list', '/servicos')
    config.add_route('service_create', '/servicos/novo')
    config.add_route('service_edit', '/servicos/{id}/editar')
    config.add_route('service_delete', '/servicos/{id}/deletar')

    # Agendamentos (appointments)
    config.add_route('appointment_list', '/appointments')
    config.add_route('appointment_create', '/appointments/novo')
    config.add_route('appointment_edit', '/appointments/{id}/editar')
    config.add_route('appointment_delete', '/appointments/{id}/deletar')
    config.add_route('appointment_view', '/appointments/{id}')

    # Usuários
    config.add_route('user_list', '/users')
    config.add_route('user_create', '/users/novo')
    config.add_route('user_edit', '/users/{id}/editar')
    config.add_route('user_delete', '/users/{id}/deletar')
    config.add_route('user_view', '/users/{id}')

    # Pagamentos
    config.add_route('payment_list', '/payments')
    config.add_route('payment_create', '/payments/novo')
    config.add_route('payment_edit', '/payments/{id}/editar')
    config.add_route('payment_delete', '/payments/{id}/deletar')
    config.add_route('payment_view', '/payments/{id}')

    # Funcionários
    config.add_route('funcionario_list', '/funcionarios')
    config.add_route('funcionario_create', '/funcionarios/novo')
    config.add_route('funcionario_edit', '/funcionarios/{id}/editar')
    config.add_route('funcionario_delete', '/funcionarios/{id}/deletar')
    config.add_route('funcionario_view', '/funcionarios/{id}')

    config.scan('.views')
