from django.shortcuts import render
from django.db.models import Q

from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    # Заключаем вызов методов в скобки
    # (это стандартный способ переноса длинных строк в Python);
    # каждый вызов пишем с новой строки, так проще читать код:
    ice_cream_list = IceCream.objects.values(
            'id', 'title', 'description'
        # Верни только те объекты, у которых в поле is_on_main указано True:
        ).filter(Q(is_published=True) & (Q(is_on_main=False) | Q(title__contains='пломбир'))).order_by('title')[1:4] 
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context) 