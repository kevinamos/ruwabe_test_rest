from django.conf.urls import url
from ruwabe_app.api import views

urlpatterns = [
	url(r'^$', views.PostListAPIView.as_view())
    # url(r'^$', views.HomePageView.as_view(), name='home'),
    # url(r'^order$', views.OrderPageView.as_view(), name='order'),
    # url(r'^home$',  views.HomePageView.as_view(), name='home' ),


]