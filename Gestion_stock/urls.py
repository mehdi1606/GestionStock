
from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('API/', include('API.urls')),
    path('', include('frontoffice.urls')),

    path('admindash/', TemplateView.as_view(template_name='frontoffice/master_page.html')),
    path(r'admindash/statistiques', TemplateView.as_view(template_name='frontoffice/page/statistiques.html')),
    path(r'admindash/produits', TemplateView.as_view(template_name='frontoffice/page/produit.html')),
    path(r'admindash/clients', TemplateView.as_view(template_name='frontoffice/page/client.html')),
    path(r'admindash/fournisseurs', TemplateView.as_view(template_name='frontoffice/page/fournisseur.html')),
    path(r'admindash/achats', TemplateView.as_view(template_name='frontoffice/page/achat.html')),
    #path("logout/", TemplateView.as_view(), name="logout")

]
