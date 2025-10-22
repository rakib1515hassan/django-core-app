# views.py এ যোগ করুন
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

class TranslationTestView(TemplateView):
    template_name = 'test/languageTest.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['translations'] = {
            'question'   : _("question-1"),
            'email'      : _("Email address"),
            'phone'      : _("Phone number"),
            'first_name' : _("First name"),
            'last_name'  : _("Last name"),
            'gender'     : _("Gender"),
            'religion'   : _("Religion"),
            'welcome'    : _("Welcome to our application"),
            'required'   : _("Please fill in all required fields"),
        }
        
        return context