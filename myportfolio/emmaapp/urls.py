from django.urls import path
from .views import IndexView,ContactFormView,PDFCreateView,PDFListView

app_name = 'emmaapp'
urlpatterns = [
    path('', IndexView.as_view(), name = 'sameindex'),
    path('create/',ContactFormView.as_view(),name='createcontact'),
    path('createpdf/',PDFCreateView.as_view(),name='createpdf'),
    path('pdflist/',PDFListView.as_view(),name='pdflist')
    # url(r'^$',views.PostListView.as_view(),name='post_list'),
]
