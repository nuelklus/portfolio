from django.urls import path
from .views import IndexView,ContactCreateView

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('contact/',ContactCreateView.as_view(),name='contact'),
    # url(r'^$',views.PostListView.as_view(),name='post_list'),
]
