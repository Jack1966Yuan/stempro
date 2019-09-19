# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import (View, CreateView, ListView)
from django.views.generic import TemplateView
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .forms import CustomUserCreationForm, SubscribeForm, RegisterActiveForm, SubscribePresentationForm
from .models import SubscribeEmail, InvolvedActive, Course, TutorActive, Program, RegisterActive, SubscribePresentation


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Recommend(TemplateView):
    template_name = 'recommended.html'

class MyPage(TemplateView):
    template_name = 'mypage.html'

class SubscribeProgramView(CreateView):
    form_class = SubscribePresentationForm
    template_name = 'register_program.html'
    queryset = SubscribePresentation.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class SubscribeView(CreateView):
    form_class = SubscribeForm
    template_name = 'home.html'
    queryset = SubscribeEmail.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    #def get_context_data(self, **kwargs):
    #    context = super(SubscribeView, self).get_context_data(**kwargs)
    #    context['active'] = 'active'
    #    return context


class RegisterView(CreateView):
    form_class = RegisterActiveForm
    #fields = ['active_name', 'who_register', 'type']
    #initial = {"active_name": "nameqwq", "who_register": "Placeholder who_register", "type": "Placehold type"}
    queryset = RegisterActive.objects.all()
    template_name = 'register_activities.html'

  #  def form_valid(self, form):
  #      print(form.cleaned_data)
  #      return super().form_valid(form)

    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(RegisterView, self).dispatch(*args, **kwargs)

#if request.user.is_authenticated():
#    return render(request, 'items.html')
#else
#    return render(request, 'login.html')


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            name = request.GET['name']
            type = request.GET['type']
            who_register = request.user.username
            initial = {"active_name": name, "who_register": who_register, "type": type}
            form = self.form_class(initial= initial)
            return render(request, self.template_name, {'form': form})

        else:
            response = redirect('login')
            return response

  #from django.http import HttpResponseRedirect
  #from django.shortcuts import render
  #from django.views.generic import View
  #from .forms import MyForm

  #class MyFormView(View):
  #    form_class = MyForm
  #    initial = {'key': 'value'}
  #    template_name = 'form_template.html'

  #    def get(self, request, *args, **kwargs):
  #        form = self.form_class(initial=self.initial)
  #        return render(request, self.template_name, {'form': form})

  #    def post(self, request, *args, **kwargs):
  #        form = self.form_class(request.POST)
  #        if form.is_valid():
  #            # <process form cleaned data>
  #            return HttpResponseRedirect('/success/')
  #        return render(request, self.template_name, {'form': form})



def thanks_subscribe_view(request):
    return render(request, 'thanks_subscribe.html')

class InvolvedActiveView(ListView):
    queryset = InvolvedActive.objects.all()
    template_name = 'activities.html'

class CourseView(ListView):
    queryset = Course.objects.all()
    template_name = 'activities.html'

class TutorActiveView(ListView):
    queryset = TutorActive.objects.all()
    template_name = 'activities.html'

class ProgramView(ListView):
    queryset = Program.objects.all()
    template_name = 'activities.html'

