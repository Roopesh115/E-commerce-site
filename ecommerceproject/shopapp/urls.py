from django.urls import path, include
from . import views
app_name='shopapp'
urlpatterns = [
    path('', views.AllProductCat, name='AllProductCat'),
    path('<slug:c_slug>/', views.AllProductCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.productDetails, name='productDetails'),

    # path('add/', views.add_movie, name='add_movie'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('delete/<int:id>/', views.delete, name='delete'),

]