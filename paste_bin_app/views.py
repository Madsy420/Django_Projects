from django.shortcuts import render

from paste_bin_app.forms import PasteBinDBForm
from paste_bin_app.models import PasteBinDB
from paste_bin_app.helper_functions import randURLGen

# Create your views here.

def paste_bin(request):

    form = PasteBinDBForm()
    
    if request.method == "POST":
        posted_request = request.POST
        form = PasteBinDBForm(posted_request)
        URL = randURLGen(length = 20)
        print(form)
        if len(posted_request.get('text')) != 0:
            if form.is_valid():
            #user input
                saved_form = form.save(commit = False)
                saved_form.url = URL
                saved_form.save()
                
                return render(request, 'paste_bin_app/paste_bin.html',{'Submitted':"true",
                                                                       'error':"false",
                                                                       'URL':URL,
                                                                       'PB':form,
                                                                       'invalid_form':"false",})
            else:
                return render(request, 'paste_bin_app/paste_bin.html',{'Submitted':"false",
                                                                       'error':"true",
                                                                       'PB':form,
                                                                       'invalid_form':"false",})
        else:
            return render(request, 'paste_bin_app/paste_bin.html',{'Submitted':"true",
                                                                       'error':"true",
                                                                       'PB':form,
                                                                       'invalid_form':"true",})
    return render(request, 'paste_bin_app/paste_bin.html',{'Submitted':"false",
                                                           'error':"false",
                                                           'PB':form,
                                                           'invalid_form':"false",})

    
def text_page(request,URL):
    try:
        print("Trying webpage")
        required_db_object = PasteBinDB.DBManager.filter(url = URL)
        if required_db_object.values().__len__() == 0:
            return render(request, 'paste_bin_app/text_page.html',{'url_is_valid':"false"})
        #print(URL)
        #required_db_object = PasteBinDB.objects.filter(url = URL)
    except:
        print("Error happend")
        return render(request, 'paste_bin_app/text_page.html',{'url_is_valid':"false"})
    #print(required_db_object)
    text = required_db_object.values()[0]["text"]
    print(text)
    return render(request, 'paste_bin_app/text_page.html',{'url_is_valid':"true",
                                                    'text':text,})
    