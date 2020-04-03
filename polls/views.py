import textwrap
from django.http import HttpResponse
from django.views.generic.base import View
# import Http Response from django
from django.shortcuts import render
# print(k)
# create a function



def geeks_view(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data": "Nguyen Van Dat ",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "geeks.html", context)
''' 
# create a function
def geeks_view(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"Nguyen Van Dat",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "geeks.html", context)


'''
class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Hello, world!</p>
            </body>
            </html>
        ''')


        return HttpResponse(response_text)





