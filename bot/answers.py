def get_answers(key, language):

    response = {
        'welcome': {
            'es': "Hola bienvenido a savelink.io, hemos creando una cuenta con tu número: %s",
            'en': 'Welcome to savelink.io, we have created an account with your phone: %s',

        }
    }

    return response[key][language]
