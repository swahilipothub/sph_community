from django import forms
from opportunities.models import Opportunity, Category, Language, Skills


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)

class SkillsForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = ('name',)

class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ('name',)

class OpportunityForm(forms.ModelForm):

    class Meta:
        model = Opportunity
        fields = ('name', 'location', 'description', 'skills', 'is_verified', 
            'availability', 'experience', 'age', 'amount', 'education', 'logo',
            'language', 'status')