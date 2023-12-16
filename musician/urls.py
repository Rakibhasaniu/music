from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_musician.as_view(), name='add_musician'),
    path('edit/<int:id>', views.Edit_Post.as_view(), name='edit_musician'),
    
]