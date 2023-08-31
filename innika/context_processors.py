from menu.models import Menu

def categories_processor(request):
    menu = Menu.objects.all()
    return {'menu': menu}