from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render


def contact_email(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        mensagem = request.POST.get('mensagem')

        data = {
            'name':nome,
            'email':email,
            'subject':subject,
            'message':mensagem,
        }
        message = '''
        New message: {}

        From:{}
        '''.format(data['message'],data['email'])
        
        send_mail(data['subject'], message, '', ['andreportol@yahoo.com.br'])
        return HttpResponse('Thank you for submmiting the form, we will be in touch soon')
    return render(request, 'contactform2/index.html', {})