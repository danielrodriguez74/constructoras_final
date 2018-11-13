from django.contrib import admin
from django.urls import path
from constructorasApp import views


urlpatterns = [
	
    path('',views.constructoras_base,name='constructora-lista'),
    path('fotos/<int:pk>/',views.carrete_detail,name='fotos-lista'),
    path('ingreso', views.ingreso, name='ingreso'),

    # path('edificios/<int:id>/',views.edificos_detail,name='edificio-lista'),
    # path('apartamentos/<int:pk>/',views.apartamentos_detail,name='apartamento-lista'),
    # path('crear_contructora', views.constructora-create, name='contructora-create'),
    # path('crear_edificio', views.edificio-create, name='edificio-create'),
    # path('crear_apartamento', views.apartamento-create, name='apartamento-create'),








    # --------------------------- CONSTRUCTORA ---------------------------------

    # List
    path('constructora/', views.ConstructoraList.as_view(), name='constructoras-lista'), 
    
    # Create
    path('constructora/create', views.ConstructoraCreate.as_view(), name='constructora-create'),
    
    # Update
    path('constructora/<int:pk>/update', views.ConstructoraUpdate.as_view(), name='constructora-update'),
    
    # Detail
    path('constructora/<int:pk>/detalles', views.ConstructoraDetail.as_view(), name='constructora-detail'),
    
    # Delete
    path('constructora/<int:pk>/delete', views.ConstructoraDelete.as_view(), name='constructora-delete'),

    # --------------------------- EDIFICIO ---------------------------------

    # List
    path('edificios/<int:pk>', views.EdificioList.as_view(), name='edificios-lista'),

    # Filter edificios
    path('edificios/<int:grado_id>/lista', views.edificioListFilter, name='edificio-filter-lista'),
    
    # Create
    path('edificios/create/', views.EdificioCreate.as_view(), name='edificio-create'),
    
    # Detail
    path('edificios/<int:pk>/detalles', views.EdificioDetail.as_view(), name='edificio-detail'), 

    # Update
    path('edificios/<int:pk>/actualizar/', views.EdificioUpdate.as_view(),name='edificio-update'),
    
    # Delete
    path('edificios/<int:pk>/eliminar/', views.EdificioDelete.as_view(),name='edificio-delete'),


    # --------------------------- APARTAMENTO ---------------------------------

    # List
    path('apartamentos/<int:pk>', views.ApartamentoList.as_view(), name='apartamentos-lista'),

    # Filter apartamentos
    path('apartamento/<int:grado_id>/lista', views.apartamentoListFilter, name='apartamento-filter-lista'),
    
    # Create
    path('apartamento/create/', views.ApartamentoCreate.as_view(), name='apartamento-create'),
    
    # Detail
    path('apartamento/<int:pk>/detalles', views.ApartamentoDetail.as_view(), name='apartamento-detail'), 

    # Update
    path('apartamento/<int:pk>/actualizar/', views.ApartamentoUpdate.as_view(),name='apartamento-update'),
    
    # Delete
    path('apartamento/<int:pk>/eliminar/', views.ApartamentoDelete.as_view(),name='apartamento-delete'),
]