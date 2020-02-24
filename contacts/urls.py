from django.urls import path, include
from contacts import views

urlpatterns = [
    path('groups/', views.group_list, name='group_list'),
    path('group_count/', views.group_count, name='group_count'),
    path('groups/add/', views.group_create, name='group_create'),
    path('groups/<int:pk>/update/', views.group_update, name='group_update'),
    path('groups/<int:pk>/delete/', views.group_delete, name='group_delete'),
]

urlpatterns += [
    # path('import_sheet/', views.import_sheet, name="import_sheet"),
    # path('search/', views.search, name='search'),
]

urlpatterns += [
    path('add/', views.contact_create, name='contact_create'),
    path('count/', views.contact_count, name='contact_count'),
    path('<int:pk>/edit/', views.contact_update, name='contact_update'),
    path('delete/<int:pk>/', views.contact_delete, name='contact_delete'),
    path('export/', views.export_contact_csv, name='export_contact_csv'),
    # path('import/$', views.contact_upload, name='contact_upload'),
    path('', views.contact_list, name='contact_list'),
]
