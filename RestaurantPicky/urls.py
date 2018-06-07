"""RestaurantPicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views  import LoginView, LogoutView

from restaurants.views import ContactView,AboutView
from menu.views import HomeView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(), name="home"),
    url(r'^Contact/$',ContactView.as_view(), name="contact"),
    url(r'^About/$',AboutView.as_view(), name="about"),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^register/', RegisterView.as_view(), name="register"),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name="activate"),
    url(r'^follow/$', ProfileFollowToggle.as_view(), name="follow"),
    url(r'^restaurants/', include('restaurants.urls', namespace="restaurants")),
    url(r'^menu/', include('menu.urls', namespace="menu")),
    url(r'^u/', include('profiles.urls', namespace="profiles"))
    # url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),

]
