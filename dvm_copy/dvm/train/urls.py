from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("custsign",views.custsign,name='custsign'),
    path("custlogin",views.custlogin,name='custlogin'),

    path('', include('social_django.urls', namespace='social')),
    path("home",views.home,name="home"),
    path("add",views.add,name="add"),
    path("compile",views.adding,name="addinng"),
    path("cancel",views.cancel,name="cancel"),
    path("search",views.search,name="search"),
    path("search_results",views.search_result,name="search_results"),
    path("booking",views.booking,name="booking"),
    path("wallet",views.wallet1,name="wallet"),
    path("customer",views.process_data,name="customer"),
    path("login",views.login,name="login"),
    path("view1",views.view1,name="view1"),
    path("view",views.view,name="view"),
    path("viewc",views.viewc,name="viewc"),
    path("export",views.download,name="download"),
    path("export1",views.export,name="export"),
    path("payment",views.payment,name="payment"),
    path("tracking",views.tracking,name="tracking"),
    path("track1",views.track1,name="track1"),
    path("journey",views.journeys1,name="cancel"),
    path("journey_cancel",views.cancelp,name="cancel_passenger"),
    
    path('social-auth/',include('social_django.urls',namespace='social')),
    path('login/',views.login1,name='login'),
    path('sign/',views.SignupPage,name='signup'),
    path('login1/',views.LoginPage,name='login1'),
    path('custview',views.custview,name='custview'),
    path('',views.h1,name='before_login'),
    path('update',views.update,name='update'),


   
]