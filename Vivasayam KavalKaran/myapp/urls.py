from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.main,name='main'),
    path('uregister/',views.uregister,name='uregister'),
    path('fregister/',views.fregister,name='fregister'),
    path('ulogin/',views.ulogin,name='ulogin'),
    path('flogin/',views.flogin,name='flogin'),
    path('uindex/',views.uindex,name='uindex'),
    path('findex/',views.findex,name='findex'),
    path('upload/', views.upload_product,name='upload_product'),
    path('logout/',views.log_out,name='logout'),
]