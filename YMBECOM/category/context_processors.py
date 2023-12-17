from .models import category

#we are going to fetch all the data from categories databases
# we have to declare it in setting in templates method
def menu_links(request):
    links= category.objects.all()
    return dict(links=links)
