from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def inicio(request):

    if request.method == 'POST':

        nombre = request.POST['nombre']
        correo = request.POST['correo']
        mensaje = request.POST['mensaje']

        # =========================
        # CORREO PARA TI
        # =========================

        asunto_admin = f'Nuevo mensaje de {nombre}'

        mensaje_admin = f'''
Nombre: {nombre}

Correo: {correo}

Mensaje:
{mensaje}
        '''

        send_mail(
            asunto_admin,
            mensaje_admin,
            settings.EMAIL_HOST_USER,
            ['novasolutionsfka@gmail.com'],
            fail_silently=False
        )

        # =========================
        # CORREO PARA EL CLIENTE
        # =========================

        asunto_cliente = 'Hemos recibido tu mensaje 🚀'

        mensaje_cliente = f'''
Hola {nombre},

Gracias por contactar con NovaSolutions.

Hemos recibido tu mensaje correctamente y pronto nos comunicaremos contigo.

Tu mensaje:
{mensaje}

— NovaSolutions
        '''

        send_mail(
            asunto_cliente,
            mensaje_cliente,
            settings.EMAIL_HOST_USER,
            [correo],
            fail_silently=False
        )

        return render(request, 'index.html', {
            'mensaje_enviado': True
        })

    return render(request, 'index.html')