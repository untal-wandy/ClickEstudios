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



def DeletePlans(request):
      p = models.Plans.objects.get(id=request.GET.get('p_id'))
      p.delete()
      return JsonResponse(list(),  safe=False)


def CreateCaract(request):
      try:
            p = models.Plans.objects.get(id=request.GET.get('id'))
            cr = models.CaratPlanes.objects.create(plans=p, name=request.GET.get('input'))
            caract_list = []
            for p in p.plans.all():
                  caract_list.append(
                        {
                              'id': p.id,
                              'name': p.name
                        }
                  )
            return JsonResponse(caract_list,  safe=False)
      except models.Plans.DoesNotExist:
            pass
      return JsonResponse(caract_list,  safe=False)


