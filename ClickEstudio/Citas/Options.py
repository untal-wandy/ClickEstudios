
# GitHub Copilot
# La función SendMail se encarga de enviar un correo electrónico utilizando el protocolo SMTP (Simple Mail Transfer Protocol). Toma como parámetros el destinatario del correo (Destinario), el asunto del correo (Asunto) y el mensaje del correo (Mensaje).
from email.mime.text import MIMEText
from ClickEstudio import settings
from . import models
import smtplib

class Mail:
      def SendGmail(self, Destinario, Asunto, Mensaje):
                  MailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
                  MailServer.ehlo()
                  MailServer.starttls()
                  MailServer.ehlo()
                  MailServer.login(settings.EMAIL_USER,settings.EMAIL_HOST_PASSWORD)
                        # print("Servido Conectado con exito!")
                  Msj = MIMEText(Mensaje)
                  Msj['From']= settings.EMAIL_HOST
                  Msj['To']= Destinario
                  Msj['Subject']= Asunto
                  MailServer.sendmail(settings.EMAIL_HOST, Destinario, Msj.as_string(), ),
                  print(f'Codigo enviado a: {Destinario}')
               
               
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
class Options:
      def RedirectReverse(self, name, pk):
            return redirect(reverse(name, kwargs={'pk': pk}))



      # Esta función es útil para registrar automáticamente los ingresos en la base de datos cuando una venta ha sido confirmada.
      def Guardar_Ingreso(sale, ingreso, tipo):

            record = models.FinancialRecord.objects.create(
                  name=sale.cliente.name,
                  description=sale.plan.name + tipo,
                  ingreso = ingreso
                  # ingreso=sale.price_total
                  )
            record.save()
            return 'Ingreso Guardado'













