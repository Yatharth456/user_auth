from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView
from . models import Task, TaskRating
from . serializers import TaskSerializer, RatingSerializer, UpdateSerializer, serializers, SalarySerializer
from accounts.decorators import ManagerPermission
from accounts.serializers import UpdateHourlyRate
from accounts.models import CustomUser
from django.db.models import F

# Create your views here.

class TaskCreate(APIView):
    permission_classes = (permissions.IsAuthenticated, ManagerPermission)

    def post(self, request):
        data = request.data
        user_id = request.user.id          # manager id
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save(
                reporter_id=user_id
            )
            return Response(
                serializer.data,
                status=200
            )
        else:
            return Response(
                serializer.errors,
                status=400
            )
    

    def delete(self, request, pk):
        item = Task.objects.get(pk=pk)
        item.delete()
        return Response({
            'message': 'Task Deleted Successfully'

        })
    #permission_classes = (permissions.AllowAny,)
    def get(self, request):
        item = Task.objects.all()
        serializer = TaskSerializer(item, many=True)
        return Response (serializer.data)

    def put(self, request, pk):
        instance = Task.objects.get(pk=pk)

        serializer = TaskSerializer(instance, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                serializer.data
            )
        

    def patch(self, request, pk):
        id = pk
        data = Task.objects.get(pk=id)
        serializer = TaskSerializer(data, data=request.data,)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                serializer.data
            )

class RatingAPI(APIView):
    serializer_class = RatingSerializer
    def post(self, request):
        data = request.data
        serializer = RatingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response (
                serializer.data
            )
        else:
            return Response (
                serializer.errors,
                status=400
            )

    def delete(self, request, pk):
        item = TaskRating.objects.get(pk=pk)
        item.delete()
        return Response({
            'message': 'Task Deleted Successfully'

        })
    def get(self, request):
        item = TaskRating.objects.all()
        serializer = RatingSerializer(item, many=True)
        return Response (serializer.data)

    def put(self, request, pk):
        data = Task.objects.get(pk=pk)
        serializer = RatingSerializer(data, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                serializer.data
            )
        else:
            return Response (
                serializer.errors,
                status=400
            )

    def patch(self, request, pk):
        id = pk
        data = Task.objects.get(pk=id)
        serializer = RatingSerializer(data, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                serializer.data
            )

class AllAssigneeAPI(APIView):
    # serializer = Update?Serializer
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        user = request.user.id
        #data = Task.objects.get(id=5)
        #data = Task.objects.filter(status=0)

        data = Task.objects.filter(assignee=user)
        
        #data = Task.objects.filter()
        #data = Task.objects.get(status=0)
        #data = Task.objects.all()
        '''
        data = TaskRating.objects.get()
        data = TaskRating.objects.filter()
        data = TaskRating.objects.all()
        '''
        serializer = TaskSerializer(data, many=True)
        # serializer = TaskSerializer(data)
        return Response(serializer.data)
'''
0. Change assignee
1. my all assigned tasks
2. update status or add comment
'''
class UpdateAPI(APIView):
    serializer = UpdateSerializer
    def patch(self, request, pk):
        data = Task.objects.get(pk=pk)
        print(data.assignee_id)
        serializer = UpdateSerializer(data, data=request.data, partial= True)
        if serializer.is_valid(raise_exception=True):
            if data.assignee_id == request.user.id:
                serializer.save()
                return Response({
                    "status": "success",
                    "data": serializer.data
                })
            else:
                return Response(
                serializer.errors,
                status=400
            )
        else:
            return Response(
            serializer.errors,
            status=401
        )



class HourlyRate(APIView):
    permission_classes = (permissions.IsAuthenticated, ManagerPermission)

    def patch(self, request):
        data = request.data
        user_id = request.user.id       
         # manager id
        

        user_insance = CustomUser.objects.get(pk=data["id"])

        # user_insance.hourly_rate = data["hourly_rate"]
        # user_insance.save()

        print("sASDFGHJKKKHJG",user_insance)
        serializer = UpdateHourlyRate(user_insance, data=request.data, partial= True)
        if serializer.is_valid(raise_exception=True):
            print("JKHGFDSFGHJK")
            serializer.save()

            return Response({
                    "status": "success",
                    "data": serializer.data
                })
        else:
            return Response(
            serializer.errors,
            status=400
            )

class SalaryView(APIView):
    def get(self, request):
        user_id = request.user.id
        # hours = Task.objects.filter(working_hours=Task.working_hours)
        # print("aaaabbbbbbbcccccccc",hours)
        # a =Task.objects.filter(status=1)
        # b = 0
        # data = Task.objects.filter(working_hours=hours)
        # print(data) 

        # rates = CustomUser.objects.filter(id=user_id)
        
        
        # serializer = TaskSerializer(data, many=True)

        # user_id = 2
        # hourly_rate = ?

        user_instance = CustomUser.objects.get(id=user_id)
        hourly_rate = user_instance.hourly_rate
        print(hourly_rate)

        print(user_id, "Ugh")
        task_instance = Task.objects.filter(assignee_id=user_id).values_list("working_hours", flat=True)
        print(sum(list(task_instance)),"FGDHCFUFUYVFYUY")

        # total_hours = task_instance.annotate(totals=sum('total_hours'))
        # print(total_hours)
        
        # {
        #     "id": 2,
        #     "email": "example.com",
        #     "role": "employee",
        #     "hourly_rate": 8..........n
        # }


        working_hours = sum(task_instance)
        print(working_hours)

        total = hourly_rate * working_hours
        return Response(total)
        # result = Task.objects.annotate(prod = F('working_hours') * F('hourly_rate'))
        # return Response ({"result": result})


'''
1. fetch  hourly rate employee by user ID
2. fetch all working hours or sum of workig hours from TASK table by assignee email or id
3. salary = rate  * sum of wh 

'''
class Data(APIView):
    def get(self, request):
        user_id = request.user.id
        hour_instance = Task.objects.filter(assignee_id=user_id)
        print("POIUYTREWQ",hour_instance.values_list("working_hours"))

        desc = Task.objects.filter(assignee_id=user_id)
        print("ASDFGHJKLKJHBVN",desc.values_list("description"))

        name = CustomUser.objects.get(id=user_id)

        comments = Task.objects.filter(assignee_id=user_id)
        commet = comments.values_list("comment")

        stt = Task.objects.filter(assignee_id=user_id)
        stats = stt.values_list("status").count()


        return Response({
            "name": name.email,
            "description": desc.values_list("description"),
            "hours": hour_instance.values_list("working_hours"),
            "comment": commet,
            "total status": stats,
            # "Pending":
            # "Done":
            # "Todo":
            # "Inprogress":

        })