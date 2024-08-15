from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_admin',views.admin_login,name='home_admin'),
    path('',views.admin_index,name='admin_dashboard'),
    path('pending_users',views.pending_users,name='pending_users'),
    path('accept_user/<int:id>',views.accept_user,name='accept_user'),
    path('all_users',views.all_users,name='all_users'),
    path('delete_user/<int:id>/',views.delete_user,name='delete_user'),
    path('upload_data',views.upload_data,name='upload_data'),
    path('excel_graph/<int:dp>/<int:udp>',views.excel_graph,name='excel_graph'),
    path('excel_data_analysis',views.excel_data_analysis,name='excel_data_analysis'),
    path('user_feedback',views.user_feedback,name='user_feedback'),
    path('admin_graph',views.admin_graph,name='admin_graph'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
]