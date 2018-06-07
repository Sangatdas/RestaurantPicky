from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
# Create your views here.

# @login_required()
# def restaurant_createview(request):
# 	# print(request.POST)
# 	form = RestaurantLocationCreateForm(request.POST or None)
# 	# if request.method == "POST":
# 	# 	# name = request.POST.get("name")
# 	# 	# location = request.POST.get("location")
# 	# 	# city = request.POST.get("city")
# 	# 	# category = request.POST.get("category")
# 	# 	form = RestaurantCreateForm(request.POST)
# 	if form.is_valid():
# 		if request.user.is_authenticated():
# 			instance = form.save(commit=False)
# 			# customize like a pre_save
# 			instance.owner = request.user
# 			instance.save()
# 			#customize like a post_save
# 			# obj = RestaurantLocation.objects.create(
# 			# 		name = name,
# 			# 		location = location,
# 			# 		city = city,
# 			# 		category = category
# 			# 	)

# 			# obj = RestaurantLocation.objects.create(
# 			# 		name = form.cleaned_data.get("name"),
# 			# 		location = form.cleaned_data.get("location"),
# 			# 		city = form.cleaned_data.get("city"),
# 			# 		category = form.cleaned_data.get("category")
# 			# 	)
# 			return HttpResponseRedirect("/restaurants/")
# 		else:
# 			return HttpResponseRedirect("/login/") 

# 	if form.errors:
# 		print(form.errors)

# 	template_name = "restaurants/form.html"
# 	context = {"form":form}

# 	return render(request, template_name, context)

class HomeView(TemplateView):
	template_name = "index.html"

class ContactView(TemplateView):
	template_name = "contact.html"

class AboutView(TemplateView):
	template_name = "about.html"

class RestaurantListView(ListView):
	# template_name = "restaurants/restaurants_list.html"

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)
		# print(self.kwargs)
		# slug = self.kwargs.get('slug')
		# if slug:
		# 	qs = RestaurantLocation.objects.filter(
		# 			Q(category__iexact=slug) |
		# 			Q(category__icontains=slug)
		# 		)
		# else:
		# 	qs = RestaurantLocation.objects.all()
		# return qs	

class RestaurantDetailView(DetailView):
	# template_name = "restaurants/restaurants_list.html"
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	# login_url = "/login/"
	template_name = "form.html"
	# success_url = "/restaurants/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(RestaurantCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
		context["title"] = "Add Restaurant"
		return context
	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get("rest_id")
	# 	obj = get_object_or_404(RestaurantLocation, id=rest_id) # or pk = rest_id
	# 	return obj
class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantLocationCreateForm
	# login_url = "/login/"
	template_name = "restaurants/detail-update.html"
	# success_url = "/restaurants/"
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		context["title"] = "Update Restaurant"
		return context


# def home(request):
# 	context = {}
# 	return render(request, "index.html", context)

# def contact(request):
# 	context = {}
# 	return render(request, "contact.html", context)

# def about(request):
# 	context = {}
# 	return render(request, "about.html", context)

# class ContactView(View):
# 	def get(self,request,*args,**kwargs):
# 		context = {}
# 		return render(request,"contact.html", context)

# def restaurant_list_view(request):
# 	template_name = "restaurants/restaurants_list.html"
# 	queryset = RestaurantLocation.objects.all()
# 	context = {
# 		"object_list": queryset
# 	}
# 	return render(request, template_name, context)

# class IndianRestaurantListView(ListView):
# 	queryset = RestaurantLocation.objects.filter(category__iexact="indian")
# 	template_name = "restaurants/restaurants_list.html"		

# class ItalianRestaurantListView(ListView):
# 	queryset = RestaurantLocation.objects.filter(category__iexact="italian")
# 	template_name = "restaurants/restaurants_list.html"		

# class SearchRestaurantListView(ListView):
# 	template_name = "restaurants/restaurants_list.html"

# 	def get_queryset(self):
# 		print(self.kwargs)
# 		slug = self.kwargs.get('slug')
# 		if slug:
# 			qs = RestaurantLocation.objects.filter(
# 				Q(category__iexact=slug) |
# 				Q(category__icontains=slug)
# 				)
# 		else:
# 			qs = RestaurantLocation.objects.none()
# 		return qs		