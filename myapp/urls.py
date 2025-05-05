# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact-thankyou/', views.contact_thankyou, name='contact_thankyou'),
    path('newsletter/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('favorite-games/', views.favorite_games_list, name='favorite_games_list'),
    path('favorite-game/create/', views.favorite_game_create, name='favorite_game_create'),
    path('favorite-game/update/<int:pk>/', views.favorite_game_update, name='favorite_game_update'),
    path('favorite-game/delete/<int:pk>/', views.favorite_game_delete, name='favorite_game_delete'),
    path('login/', views.login_view, name='login'),         # Fixed: use login_view
    path('logout/', views.logout_view, name='logout'),      # Fixed: use logout_view
]
