from celery import shared_task
from django.core.mail import send_mail
from biblioteca_backend_drf_celery import settings

@shared_task
def send_email_authors(author, book):
    asunto = f'Se ha registrado un libro del que usted es autor {book.title}'
    mensaje = f'Estimado {author.name} {author.lastname}:\n' \
              f'Se ha registrado un libro del que usted es autor\n' \
              f'Libro: {book.title}'
    send_mail(
        asunto,
        mensaje,
        settings.EMAIL_HOST_USER,
        [author.email],
        fail_silently=False,
    )

    resultado = f'Mensaje enviado a {author.name} {author.lastname} ({author.email})'
    print(resultado)
    return True
