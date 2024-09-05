from django.urls import path, include
from . import views
app_name='search_app'
urlpatterns = [
    path('', views.serch_results, name='serch_results'),
    # path('<slug:c_slug>/', views.AllProductCat, name='products_by_category'),
    

]