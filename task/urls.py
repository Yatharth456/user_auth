from django.urls import path
from task.views import TaskCreate, RatingAPI, AllAssigneeAPI, UpdateAPI, HourlyRate, SalaryView, Data

urlpatterns = [
    path('taskcreate/', TaskCreate.as_view(), name='taskcreate'),
    path('taskcreate/<str:pk>', TaskCreate.as_view(), name='taskcreate'),
    path('rating/', RatingAPI.as_view(), name='rating'),
    path('rating/<int:pk>', RatingAPI.as_view(), name='rating'),
    path('allassignee/', AllAssigneeAPI.as_view(), name='allassignee'),
    path('allassignee/<int:pk>', AllAssigneeAPI.as_view(), name='allassignee'),
    path('update/', UpdateAPI.as_view(), name='update'),
    path('update/<int:pk>', UpdateAPI.as_view(), name='update'),
    path('hourlyrate/', HourlyRate.as_view(), name='hourlyrate'),
    path('salaryview/', SalaryView.as_view(), name='salaryview'),
    path('salaryview/<int:pk>', SalaryView.as_view(), name='salaryview'),
    path('data/', Data.as_view(), name='data'),

]