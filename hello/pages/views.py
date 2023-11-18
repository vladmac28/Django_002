from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render


pagedict= {
    'aries':'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini' : 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer':'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo':'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra':'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio':'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius':'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn':'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces':'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

type_zadiac={
    'fier': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def type (request):
    html_response=''
    for zadiac in type_zadiac:
        url_revers = reverse('url_page_name', args=[zadiac])
        html_response+= f'<li><a href="{url_revers}">{zadiac}</a></li>'
    result=f"""
        <ol>
            {html_response}
        </ol>
    """
    return HttpResponse(result)

def geturl(request, geturl : str):
    zdiac = pagedict.get(geturl)
    zadiac_dict = {
        'zadiac_text': zdiac,
        'zadiac_name': geturl.title(),
        'urls_list': pagedict,
        'pagedict': pagedict,
    }
    return render(request, 'pages/info_zodiac.html', context=zadiac_dict)

def index(request,):
    urls_list=list(pagedict)
    context={
        'urls_list': urls_list,
        'pagedict': pagedict,
    }
    return render(request, 'pages/index.html', context=context)

def getchislo(request, geturl: int):
    key_spisok = list(pagedict)
    if geturl > len(key_spisok):
        return HttpResponseNotFound(f'Страничка {geturl} не найдена')
    name_page = key_spisok[geturl - 1]
    page_revers = reverse('url_page_name', args=[name_page])
    return HttpResponseRedirect(page_revers)

