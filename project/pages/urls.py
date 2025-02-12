from django.urls import path
from . import views

urlpatterns = [
  path('' , views.index , name = 'index'),
  path('index.html' , views.index , name = 'login'),
  path('signup.html' , views.signup , name = 'signup'),
  path('adminlist.html' , views.adminlist , name = 'adminlist'),
  path('userList.html' , views.userList , name = 'userList'),
  path('adminAdd.html' , views.adminAdd , name = 'adminAdd'),
  path('adminEdit.html', views.adminEdit, name='adminEdit'),
  path('adminEdit/<int:book_id>/', views.adminEdit, name='adminEdit'),
  path('borrowe/<str:book_id>/' , views.borrowebook , name = 'borrowebook'),
  path('borrowedBooks.html' , views.borrowedBooks , name = 'borrowedBooks'),
  path('delete-book/<str:pk>' , views.deletebook , name = 'deletebook'),
  path('ajax/' , views.ajax_view , name = 'ajax_view'),
  path('ajax_foruser/' , views.ajax_view_foruser , name = 'ajax_view_foruser'),
  path('ajax_forBorrowed/' , views.ajax_view_forBorrowed , name = 'ajax_view_forBorrowed'),
  
]