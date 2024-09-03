from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('registro/', views.registro, name = "registro"),
    path('logout/', views.users_logout, name='logout'),
    
    path('editar_user/', views.editar_user, name = "editar_user"),
    path('cambiar_contra/', views.CambiarContra.as_view(), name = "cambiar_contra"),
    path('user_ok/', views.user_ok, name = "user_ok"),    
]
