"""farmakami URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login/', include('authentication.urls')),
    path('register/', include('registration.urls')),
    path('navigate/', include('navigation.urls')),
    path("balai-pengobatan/", include('balai_pengobatan.urls')),
    path('apotek/', include('apotek.urls')),
    path('produk-apotek/', include('produk_apotek.urls')),
    path("obat/", include('obat.urls')),
    path('list-produk-dibeli/', include('list_product_beli.urls')),
    path('pengantaran-farmasi/', include('pengantaran_farmasi.urls')),
    path('transaksi-pembelian/', include('transaksi_pembelian.urls')),
    path('user-profile/', include('user_profile.urls')),
    path('logout/', include('logout.urls'))
]
