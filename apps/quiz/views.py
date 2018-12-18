from django.shortcuts import render

# function based views
def home(request):
    template = 'home.html'
    context = {
        "username": 'Sunil',
        'title': 'Home page ',
        # 'data': ['santosh', 'ram', 'shyam'],
    }
    return render(request, template, context)

