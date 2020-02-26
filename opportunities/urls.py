# urls.py
from django.urls import path
from opportunities.views import (
    OpportunityList, OpportunityDetailView, OpportunityCreate, OpportunityUpdate, OpportunityDelete,
    CategoryCreateView, CategoryUpdateView, CategoryListView, CategoryDetailView, CategoryDeleteView,
    SkillsCreateView, SkillsUpdateView, SkillsListView, SkillsDetailView, SkillsDeleteView,
    LanguageCreateView, LanguageUpdateView, LanguageListView, LanguageDetailView, LanguageDeleteView)

urlpatterns = [
    # """
    #     Opportunity Create, update, List, Detail and Delete Urls
    # """
    path('', OpportunityList.as_view(), name='opportunities'),
    path('<int:pk>/', OpportunityDetailView.as_view(), name='opportunity'),
    path('add/', OpportunityCreate.as_view(), name='opportunity-add'),
    path('<int:pk>/', OpportunityUpdate.as_view(), name='opportunity-update'),
    path('<int:pk>/delete/', OpportunityDelete.as_view(), name='opportunity-delete'),

    # """
    #     Category Create, update, List, Detail and Delete Urls
    # """
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    # """
    #     Skills Create, update, List, Detail and Delete Urls
    # """
    path('skills/', SkillsListView.as_view(), name='skills-list'),
    path('skills/<int:pk>/', SkillsDetailView.as_view(), name='skills-detail'),
    path('skills/add/', SkillsCreateView.as_view(), name='skills-add'),
    path('skills/<int:pk>/', SkillsUpdateView.as_view(), name='skills-update'),
    path('skills/<int:pk>/delete/', SkillsDeleteView.as_view(), name='skills-delete'),

    # """
    #     Language Create, update, List, Detail and Delete Urls
    # """
    path('lan/', LanguageListView.as_view(), name='lang-list'),
    path('lang/<int:pk>/', LanguageDetailView.as_view(), name='lang-detail'),
    path('lang/add/', LanguageCreateView.as_view(), name='lang-add'),
    path('lang/<int:pk>/', LanguageUpdateView.as_view(), name='lang-update'),
    path('lang/<int:pk>/delete/', LanguageDeleteView.as_view(), name='lang-delete'),

]