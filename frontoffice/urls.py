
from django.contrib import admin
from django.urls import path

from frontoffice import views


from frontoffice.views import LoginView, LogoutView

urlpatterns = [
    path(r'', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    #path('admindash/produit/add/', views.post_new, name='addProduit'),
    # path('post/<int:pk>/edit/', views.produit_edit, name='produit_edit'),
     #path('produits/', views.produit_all, name='produits'),
    #path('admindash/',views.counts_all)
]
