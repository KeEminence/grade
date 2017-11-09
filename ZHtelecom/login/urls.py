from django.conf.urls import include, url
import views

urlpatterns=[
	url(r'^$',views.loginui),
	url(r'^test/$',views.test),
]
