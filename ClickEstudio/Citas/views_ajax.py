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
      c = models.Customer.objects.get(id=request.GET.get('id'))
      print(int(request.GET.get('input')), 'Mas', request.GET.get('id'))
      if c.reserve == False:
            c.reserve = True
            c.reserver_mount = int(request.GET.get('input'))
            c.price_reserved =  c.plans.price -  c.reserver_mount 
            c.save()
      else:
            abonado =   c.reserver_mount  + int(request.GET.get('input'))
            c.reserver_mount = abonado
            c.price_reserved =   c.plans.price -  c.reserver_mount
            c.save()
      if c.reserver_mount ==  c.plans.price:
            c.saled = True
            c.save()
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
      for c in models.Customer.objects.all():
            dict_customer = { 
                  'id': c.id,
                  'name': c.name 
            }
            lista.append(dict_customer)
      return JsonResponse(lista,  safe=False)

def SearchingClient(request):
      c = models.Customer.objects.get(id=int(request.GET.get('id')))
      print(c.name)
      # Obtener todos los planes asociados a ese cliente específico
      if c.plans_more.exists():
            planes = c.plans_more.all()
      else:
            planes = models.Plans.objects.filter(plans_customer=c)
      dict_client = { 
            'id': c.id,
            'name': c.name, 
            'email': c.email,
            'number': c.number,
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
      print(request.GET.get('id'))
      p = models.Plans.objects.get(id=request.GET.get('id'))
      p.is_activate = False
      p.save()
      
      return JsonResponse(list(),  safe=False)          