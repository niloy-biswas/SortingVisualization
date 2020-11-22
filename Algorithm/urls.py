from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = {
    path('', views.index, name='index'),
    path('mergesort/', views.mergesort, name="mergesort"),
    path('quicksort/', views.quicksort, name="quicksort"),
    path('selectionsort/', views.selectionsort, name="selectionsort"),
    path('bubblesort/', views.bubblesort, name="bubblesort"),
    path('insertionsort/', views.insertionsort, name="insertionsort"),
}