def get_answers(key, language):

    response = {
        'welcome': {
            'es': "Hola bienvenido a savelink.io, hemos creando una cuenta con tu número: %s",
            'en': 'Welcome to savelink.io, we have created an account with your phone: %s',
        },
        'error_create': {
            'es': 'Error al crear nueva cuenta, escribe: *crear cuenta*, para volver a intentar.',
            'en': 'Error creating new account, type: *create account*, to try again.',
        },
        'save_link': {
            'es': 'El link fue guardado con éxito: %s',
            'en': 'The link was saved successfully: %s',
        },
        'search_text': {
            'es': 'Buscando links con esta frase',
            'en': '',
        }
    }

    return response[key][language]
