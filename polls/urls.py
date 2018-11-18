from django.urls import path
from . import views

app_name = 'polls'

# will follow first matching pattern
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/vote/
    path('vote/', views.vote, name='vote'),
    # ex: /polls/comment/
    path('comment/', views.comment, name='comment'),
    # ex: /polls/question/
    path('question/', views.question, name='question'),

]