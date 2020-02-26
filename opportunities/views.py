from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils import timezone
from django.shortcuts import render
from opportunities.models import Opportunity, Category, Language, Skills
from opportunities.forms import OpportunityForm, CategoryForm, LanguageForm, SkillsForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

"""
    Gig Create, update, List, Detail and Delete Views
"""

class OpportunityCreate(CreateView):
    model = Opportunity
    fields = ['name', 'location', 'description', 'skills', 'is_verified', 
            'availability', 'experience', 'age', 'amount', 'education', 'logo',
            'language', 'status',]
    success_url = reverse_lazy('opportunities')

class OpportunityUpdate(UpdateView):
    model = Opportunity
    fields = ['name', 'location', 'description', 'skills', 'is_verified', 
            'availability', 'experience', 'age', 'amount', 'education', 'logo',
            'language', 'status']

class OpportunityDelete(DeleteView):
    model = Opportunity
    success_url = reverse_lazy('opportunities')

class OpportunityList(ListView):
    form_class = OpportunityForm
    # template_name = 'home_.html'

    def get_queryset(self):
        return Opportunity.objects.order_by('id')

class OpportunityDetailView(DetailView):
    queryset = Opportunity.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj

"""
    Category Create, update, List, Detail and Delete Views
"""

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

class CategoryDeleteView(DeleteView):
    model = Category
    fields = ['name']

class CategoryListView(ListView):
    form_class = CategoryForm

    def get_queryset(self):
        return Category.objects.order_by('id')

class CategoryDetailView(DetailView):
    queryset = Category.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj

"""
    Skills Create, update, List, Detail and Delete Views
"""

class SkillsCreateView(CreateView):
    model = Skills
    fields = ['name']

class SkillsUpdateView(UpdateView):
    model = Skills
    fields = ['name']

class SkillsDeleteView(DeleteView):
    model = Skills
    fields = ['name']

class SkillsListView(ListView):
    form_class = SkillsForm

    def get_queryset(self):
        return Skills.objects.order_by('id')

class SkillsDetailView(DetailView):
    queryset = Skills.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj

"""
    Language Create, update, List, Detail and Delete Views
"""

class LanguageCreateView(CreateView):
    model = Language
    fields = ['name']

class LanguageUpdateView(UpdateView):
    model = Language
    fields = ['name']

class LanguageDeleteView(DeleteView):
    model = Language
    fields = ['name']

class LanguageListView(ListView):
    form_class = LanguageForm

    def get_queryset(self):
        return Language.objects.order_by('id')

class LanguageDetailView(DetailView):
    queryset = Language.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj