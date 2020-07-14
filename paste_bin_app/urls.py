from django.urls import path
#from paste_bin_app.helper_functions import get_all_url
from paste_bin_app import views

urlpatterns = [
         path('',views.paste_bin,name='pasteBin'),
         path('<slug:URL>',views.text_page),
        ]

#all_urls = get_all_url()


#for url in all_urls:
#    urlpatterns.append(path(url,views.text_page,{'URL':url}))