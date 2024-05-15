from django.urls import path
from .views import pollList, getOne, voteAgree, voteDisagree

urlpatterns =[
    path('poll', pollList, name='poll_list'),
    path('poll/<int:id>', getOne, name='poll'),
    path('poll/<int:id>/agree', voteAgree, name='poll'),
    path('poll/<int:id>/disagree', voteDisagree, name='poll')
]