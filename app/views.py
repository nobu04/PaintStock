from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from .filters import ItemFilter
from .forms import ItemForm, BuyerForm, SignUpForm, LoginForm, ProfileForm
from .models import Item, User, Buyer, Profile
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



User = get_user_model()

# Create your views here.
# 検索一覧画面
class ItemFilterView(LoginRequiredMixin, FilterView):
    model = Item
    def get_queryset(self):
        return Item.objects.filter(created_by_id=self.request.user.id).order_by('-created_at')

    # django-filter用設定
    filterset_class = ItemFilter
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 4

    # 検索条件をセッションに保存する
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)


# 詳細画面
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


# 登録画面
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('index')

# 購入者情報登録
class BuyerCreateView(LoginRequiredMixin, CreateView):
    model = Buyer
    form_class = BuyerForm
    def form_valid(self, form):
        form.instance.related_user = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('index')

# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('index')

def sign_up(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if signup_form.is_valid() and profile_form.is_valid():
            username = signup_form.cleaned_data.get('username')
            email = signup_form.cleaned_data.get('email')
            password = signup_form.cleaned_data.get('password')
            gender = profile_form.cleaned_data.get('gender')
            age = profile_form.cleaned_data.get('age')
           
            user = User.objects.create_user(username, email, password)
            user.profile.gender = gender
            user.profile.age = age
            user.save()

            user = authenticate(request, username=username, password=password)
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')                
            return redirect('index')
    else:
        signup_form = SignUpForm()
        profile_form = ProfileForm()



    login_form = LoginForm()
    context = {
        'signup_form': signup_form,
        'profile_form': profile_form,
    }
    return render(request, 'registration/sign_up.html', context)

# class CustomerView(LoginRequiredMixin, ListView):
#     model = Item
#     def get_queryset(self):
#         return Item.objects.filter(created_by_id=self.request.user.id, status=2).order_by('-created_at')