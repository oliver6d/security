from django.urls import path
from . import views

app_name = 'polls'

# will follow first matching pattern
urlpatterns = [
	path('', views.login, name='login'),
	path('form/<int:id>/', views.form, name='form'),
	# to question page
	path('poll/<int:id>/', views.index, name='index'),
	# page section refreshed
	path('poll/<int:id>/vote/', views.vote, name='vote'),
	path('poll/<int:id>/comment/', views.comment, name='comment'),
	path('poll/<int:id>/question/', views.question, name='question'),

]