from django.shortcuts import render, redirect
from .models import Key
def revKey(request):
   if request.method == 'POST':
      chave = request.POST.get('key')
      k = Key.objects.filter(key=chave)
      if k:
         for i in k:
            print(i.link)
            return redirect(f'/?sucess=1&key={chave}')
      else:
         return redirect('/?sucess=0')
   elif request.method == 'GET':
      validacao = request.GET.get('sucess')
      key = request.GET.get('key')
      k = Key.objects.filter(key=key)
      render_data = {'validar': validacao, 'keyV': k}
      rendered_page = render(request, 'consulta.html', render_data)
      k.delete()
      return rendered_page