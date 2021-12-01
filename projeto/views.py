from django import shortcuts
from django.contrib.auth import decorators


@decorators.login_required
def index(request):
    return shortcuts.render(request, 'index.html', {
        'title': 'Bem vindo',
    })
