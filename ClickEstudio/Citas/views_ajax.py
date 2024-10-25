from . import models 
from django.http import JsonResponse

def FinishedCita(request):
      c = models.Customer.objects.get(id=request.GET.get('c_id'))
      if c.finished == False:
            c.finished = True
            c.save()
      return JsonResponse(list(),  safe=False)



def DeleteService(request):
      s = models.ServiceImage.objects.get(id=request.GET.get('s_id'))
      s.delete()
      return JsonResponse(list(),  safe=False)

def DeleteMomentImage(request):
      m = models.MomentImage.objects.get(id=request.GET.get('m_id'))
      m.delete()
      return JsonResponse(list(),  safe=False)


def DeledeteImgMoment(request):
      m = models.MomentRelatedImage.objects.get(id=request.GET.get('delete_img_moment_id'))
      print(m.id)
      m.delete()
      return JsonResponse(list(),  safe=False)



def DeletePlans(request):
      p = models.Plans.objects.get(id=request.GET.get('p_id'))
      p.delete()
      return JsonResponse(list(),  safe=False)


def CreateCaract(request):
      try:
            p = models.Plans.objects.get(id=request.GET.get('id'))
            cr = models.CaratPlanes.objects.create(plans=p, name=request.GET.get('input'))
            caract_list = []
            dick  =  {
                        'id': p.id,
                        'name': p.name
            }
                  
            return JsonResponse(dick,  safe=False)
      except models.Plans.DoesNotExist:
            pass
      return JsonResponse(caract_list,  safe=False)


def DeleteCaract(request):
      cr = models.CaratPlanes.objects.get(id=int(request.GET.get('id')),)
      cr.delete()
      return JsonResponse(list(),  safe=False)

def Reserver(request):
      sale = models.Sale.objects.get(id=request.GET.get('id'))
      print(sale.cliente.name)

      print(int(request.GET.get('input')), 'Mas', request.GET.get('id'))
      if sale.reserver == False:
            sale.reserver = True
            
            sale.reserver_mount = int(request.GET.get('input'))
            sale.abonado =  sale.plan.price -  sale.reserver_mount 
            sale.save()

      else:

            abonado =   sale.reserver_mount  + int(request.GET.get('input'))
            sale.reserver_mount = abonado
            sale.abonado =   sale.plan.price -  sale.reserver_mount
            sale.save()
      if sale.reserver_mount >=  sale.plan.price:
            sale.saled = True
            sale.save() 
      return JsonResponse(list(),  safe=False)

def SaleService(request):
      c = models.Customer.objects.get(id=request.GET.get('id'))
      print(c.id)

      if c.saled == False:
            c.saled = True
            c.saled_mount = c.plans.price
            c.save()
            print(c.id)
      return JsonResponse(list(),  safe=False)


def SaleCancel(request):
      c = models.Customer.objects.get(id=request.GET.get('id'))

      if c.reserve == True:
            c.reserve = False
            c.save()
      return JsonResponse(list(),  safe=False)



def Search(request):
      lista = []
      for s in models.Sale.objects.all():
            dict_customer = { 
                  'id': s.id,
                  'name': s.cliente.name 
            }
            lista.append(dict_customer)
      return JsonResponse(lista,  safe=False)

def SearchingClient(request):
      sale = models.Sale.objects.get(id=int(request.GET.get('id')))
      # Obtener todos los planes asociados a ese cliente específico
      print(sale.plan.name)
      # Obtener todos los planes asociados a ese cliente específico
      if sale.plan:
            planes = models.Plans.objects.filter(plan=sale)
            # for p in planes:
            #       print(p.sale)
      dict_client = { 
            'id': sale.cliente.id,
            'name': sale.cliente.name, 
            'email': sale.cliente.email,
            'number': sale.cliente.number,
            'sale': sale.id,
            'plans':  [{"id": plan.id, "name": plan.name, 
                        "img": plan.img.url, "price": "{:,.2f}".format(plan.price),
                        "is_activate": plan.is_activate  , 
                        "final_price": plan.final_price,
                        } for plan in planes],
      }
      return JsonResponse(dict_client,  safe=False)         

def Adicionales(request):
      # Obtener el plan
      plan = models.Plans.objects.get(id=int(request.GET.get('id')))


# Get all additional features associated with the plan

      # Verificar si el plan tiene adicionales
      lista = []
      if plan.adicionales.exists():
            adicionales = models.Adicionales.objects.filter(plans=plan)
            for a in adicionales:
                  dict_client = { 
                        'description': a.description ,

                  }
                  lista.append(dict_client)

      # pln = models.Plans.objects.filter(id=int(request.GET.get('id')))

      return JsonResponse(lista,  safe=False)         

def CreateAdicionales(request):
      print(request.GET.get('id'))

      p = models.Plans.objects.get(id=request.GET.get('id'))
      adicional = models.Adicionales(plans=p, 
                  description=request.GET.get('input'))
      adicional.save()
      adicionales_list = []

      return JsonResponse(adicionales_list,  safe=False)    


def Create_P_Adicionales(request):

      p = models.Plans.objects.get(id=request.GET.get('id'))
      p.final_price = int(request.GET.get('input'))
      
      p.save()
      adicionales_list = []
      return JsonResponse(adicionales_list,  safe=False)    


def Terminar_Cita(request):
      sale = models.Sale.objects.get(id=request.GET.get('id'))
      sale.saled_confirm = True
      sale.save()

      # Create a FinancialRecord for the sale
      if sale.saled_confirm == True:
            record = models.FinancialRecord.objects.create(
            name=sale.cliente.name,
            description=sale.plan.name,
            ingreso = sale.price_total
            )

            record.save()
      
      return JsonResponse(list(),  safe=False)          