from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils.encoding import force_text

def send_email_for_process(instance, historico):
    subject = "Alteração de status no seu processo de Estágio no sistema Desenvolve NF"
    email_template_name = "estagio/email_atualizaçao_processo.txt"
    
    if instance.local_do_estagio:
        local_do_estagio = instance.local_do_estagio.local
    else:
        local_do_estagio = instance.local_do_estagio_de_pretensao.local
    c = {
        "email": force_text(instance.estudante.pessoa.user.email),
        'domain': 'desenvolve.novafriburgo.rj.gov.br/estagio/area-do-estudante/',
        'site_name': 'Desenvolve NF',
        "user": force_text(instance.estudante.pessoa.user),
        'protocol': 'https',
        'estudante': force_text(instance.estudante),
        'local_do_estagio': force_text(local_do_estagio),
        'historico': force_text(historico),
        'msg': force_text(historico.mensagem),
    }
    # print(f"SUBJECT: {subject}. EMAIL TEMPLATE NAME: {email_template_name}. EMAIL: {instance.estudante.pessoa.user.email}, 
    #       USER: {instance.estudante.pessoa.user}. ESTUDANTE: {instance.estudante}. HISTORICO: {historico}. MSG: {historico.mensagem}")
    email = render_to_string(email_template_name, c)
    try:
        send_mail(subject, email, instance.estudante.pessoa.user.email, [
                    instance.estudante.pessoa.user.email], fail_silently=False)
    except Exception as E:
        print(E)
        return 'Falha ao enviar email.'