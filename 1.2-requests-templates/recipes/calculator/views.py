from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def start_page(request):
    return HttpResponse('Вас приветствует помощник в приготовлении блюд!')

def omlet(request):
    person = int(request.GET.get('servings', 1))
    template_name='calculator/index.html'
    context = {'recipe':{}}
    for ingridient, amount in DATA['omlet'].items():
        context['recipe'][ingridient] = amount * person
   
    return render(request, template_name, context)


def pasta(request):
    person = int(request.GET.get('servings', 1))
    template_name='calculator/index.html'
    context = {'recipe':{}}
    for ingridient, amount in DATA['pasta'].items():
        context['recipe'][ingridient] = amount * person
   
    return render(request, template_name, context)

def buter(request):
    person = int(request.GET.get('servings', 1))
    template_name='calculator/index.html'
    context = {'recipe':{}}
    for ingridient, amount in DATA['buter'].items():
        context['recipe'][ingridient] = amount * person
   
    return render(request, template_name, context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
# def omlet_view(request):
#     quantity = int(request.GET.get('servings')) if request.GET.get('servings') else 1
#     context = {
#         'recipe': {k: v * quantity for k, v in DATA['omlet'].items()}
#     }
#     return render(request, 'calculator/index.html', context)


# def pasta_view(request):
#     quantity = int(request.GET.get('servings')) if request.GET.get('servings') else 1
#     context = {
#         'recipe': {k: v * quantity for k, v in DATA['pasta'].items()}
#     }
#     return render(request, 'calculator/index.html', context)


# def butter_view(request):
#     quantity = int(request.GET.get('servings')) if request.GET.get('servings') else 1
#     context = {
#         'recipe': {k: v * quantity for k, v in DATA['butter'].items()}
#     }
#     return render(request, 'calculator/index.html', context)