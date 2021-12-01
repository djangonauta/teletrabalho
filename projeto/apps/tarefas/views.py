from django import forms, shortcuts
from django.contrib import messages

from . import models


class ComplexidadeForm(forms.ModelForm):

    class Meta:
        model = models.Complexidade
        fields = '__all__'


def complexidade(request):
    form = ComplexidadeForm()

    if request.method == 'POST':
        form = ComplexidadeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Complexidade Cadastrada com sucesso.')
            return shortcuts.redirect('tarefas:complexidade')

    return shortcuts.render(request, 'tarefas/complexidade_form.html', {
        'form': form,
    })


class AtividadeForm(forms.ModelForm):

    class Meta:
        model = models.Atividade
        fields = '__all__'


def atividade(request):
    form = AtividadeForm()

    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Atividade Cadastrada com sucesso.')
            return shortcuts.redirect('tarefas:atividade')

    return shortcuts.render(request, 'tarefas/atividade_form.html', {
        'form': form,
    })


class PlanoForm(forms.ModelForm):

    class Meta:
        model = models.PlanoTrabalho
        fields = '__all__'


def plano(request):
    form = PlanoForm()

    if request.method == 'POST':
        form = PlanoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Plano Cadastrado com sucesso.')
            return shortcuts.redirect('tarefas:plano')

    return shortcuts.render(request, 'tarefas/plano_form.html', {
        'form': form,
    })
