from . import models 


def FinishedCita(request):
      """
            This function is called when the user has finished the cusomer. 
            It will set the status of the cusomer to "Finished" and will redirect the user to the home page.
      """
      c = models.Customer.objects.get(id=request.GET.get('c_id'))
      if c.finished == False:
            c.finished = True
            c.save()
      return JsonResponse(list(),  safe=False)