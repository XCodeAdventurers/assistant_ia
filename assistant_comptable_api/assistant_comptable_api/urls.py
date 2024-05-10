"""
URL configuration for assistant_comptable_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from web.views import authView
from web.views import homeViews

urlpatterns = [
    path('', view=homeViews.home, name="login"),
    path('politiques/', view=authView.politique, name="politiques"),
    path('login/', view=authView.custom_login, name="login"),
    path('register/', view=authView.custom_register, name="register"),
    path('logout/', view=authView.custom_logout, name="logout"),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('money_tracker/', include('web.urls')),
    path('', include('paypal.standard.ipn.urls')),
    path('checkout/', authView.checkout, name='checkout'),
    path('payment-success/', authView.success, name='payment-success'),
    path('payment-failed/', authView.errors, name='payment-failed'),
    path('cinet_pay_payement/', authView.cinet_pay_payement, name="cinet_pay_payement"),
    path('payment-cinet-pay-success/', authView.cinet_pay_success, name='payment-cinet-pay-success'),
    path('payment-cinet-pay-failed/', authView.cinet_pay_errors, name='payment-cinet-pay-failed'),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT)

