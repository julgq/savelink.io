def get_answers(key, language):

    response = {
        'welcome': {
            'es': "Hola bienvenido a savelink.io, we have created an account with your phone: %s",
            'en': 'Welcome to savelink.io, we have created an account with your phone: %s',

        }
    }

    return response[key][language]
