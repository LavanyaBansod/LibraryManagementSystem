from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.list_members, name='list_members'),
    path('members/create/', views.create_member, name='create_member'),
    path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),
    # path('books/create/', views.create_book, name='create_book'),
    # Add more paths for other operations
]
