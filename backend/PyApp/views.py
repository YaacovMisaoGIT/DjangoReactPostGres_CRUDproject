from rest_framework.views import APIView
from .serializers import StudentSerializer
from django.http.response import JsonResponse
from .models import Student
from django.http.response import Http404
from rest_framework.response import Response
 
class PyAppView(APIView):
        def post(self, request):
         data = request.data
         serializer = StudentSerializer(data=data)

         if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Created Successfully", safe=False)
         return JsonResponse("Failed to Add Student", safe=False)
        
        # utility function
        def get_student(self, pk): 
         try:
            student = Student.objects.get(StudentId=pk)
            return student
         except  Student.DoesNotExist():
           raise Http404
         
        #      except:   
        #    return JsonResponse("Student does Not Exist", safe=False)
        
        def get(self, request, pk=None):
         if pk:
            data = self.get_student(pk)
            serializer = StudentSerializer(data)
         else:
            data = Student.objects.all()
            serializer = StudentSerializer(data, many=True)
         return Response(serializer.data)
        
        def put(self, request, pk=None):
         student_to_update = Student.objects.get(StudentId=pk)
         serializer = StudentSerializer(instance=student_to_update, data=request.data, partial=True)

         if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Updated Successfully", safe=False)
         return JsonResponse("Failed to Update Student")
        
        def delete(self, request, pk=None):
         student_to_delete = Student.objects.get(StudentId=pk)
         student_to_delete.delete()
         return JsonResponse("Student Deleted Successfully", safe=False)