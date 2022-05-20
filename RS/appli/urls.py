from django.urls import path


from . import views


urlpatterns = [
    path('',views.accueil),

    path('ajout/', views.ajout),
    path('ajoutc/', views.ajoutc),

    path('traitement/', views.traitement),
    path('traitementc/', views.traitementc),

    path('affichage/', views.affichage),
    path('affichagec/', views.affichagec),

    path('affiche/<int:id>/', views.affiche),
    path('affichec/<int:id>/', views.affichec),

    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),

    path('updatec/<int:id>/', views.updatec),
    path('updatetraitementc/<int:d>/', views.updatetraitementc),

    path('delete/<int:id>/', views.delete),
    path('deletec/<int:id>/', views.deletec),
]