from django.urls import path
from django.urls import re_path
from django.views.generic.base import RedirectView
from . import views

app_name = 'polls'

# will follow first matching pattern
urlpatterns = [
	path('', views.login, name='login'),
	path('form/', views.form, name='form'),
	path('example/<int:id>/', views.example, name='example'),
	# to question page
	path('poll/<int:id>/', views.index, name='index'),
	# page section refreshed
	path('poll/<int:id>/vote/', views.vote, name='vote'),
	path('poll/<int:id>/comment/', views.comment, name='comment'),
	path('poll/<int:id>/delete/', views.delete, name='delete'),
	path('poll/<int:id>/question/', views.question, name='question'),
	re_path(r'^.*/$', RedirectView.as_view(url='/', permanent=False)),

]