'''
    HTTP Request Types:
        GET         : İstek URL'de gönderilir. Açıktan gönderilen istek.
        POST        : İstek data olarak gönderilir. Gizliden gönderilen istek. 
        * PUT       : POST gibidir. PrimaryKey (ID) verisi de ister. Güncelleme için kullanılır.
        * PATCH     : POST/PUT gibidir. Farkı: Belirli bir parçayı güncellemek için kullanılır.
        * DELETE    : POST gibidir. PrimaryKey (ID) verisi de ister. Sadece silme için kullanılır.
'''

from django.shortcuts import get_object_or_404
from .serializers import StudentSerializer
from .models import Student
from functools import partial
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view()  # Default method: GET
def home(request):
    return Response({'message': 'Welcome to HomePage.'})

# ---------------------------------------


# PrimaryKey (ID) istemeyenler:

# Verileri Listele:


@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()  # get data from database/table.
    # Like convert to TupleINList (JSON)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)  # Show with JSON

# Veri ekleme:


@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)

    # if valid:
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Creating Successfully'})
    # if not valid:
    # return Response({ 'message': 'Not Valid.' })
    return Response(serializer.errors)  # Hata mesajını göster.

# ---------------------------------------

# PrimaryKey (ID) isteyenler:

# Veri Görüntüle:


@api_view(['GET'])
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

# Veri Güncelle:


@api_view(['PUT', 'PATCH'])
def student_update(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(
        instance=student, data=request.data, partial=True)

    # if valid:
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)  # Yeni datayı göster
    # if not valid:
    return Response(serializer.errors)  # Hata mesajını göster.

# Veri Sil:


@api_view(['DELETE'])
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response({'message': 'Deleting Successfully'})

# ---------------------------------------

# Benzer fonksiyonları gruplayalım:

# PrimaryKey (ID) istemeyenler:


@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
        # Listele:
        students = Student.objects.all()  # get data from database/table.
        # Like convert to TupleINList (JSON)
        serializer = StudentSerializer(students, many=True)
        # Show with JSON # Default status code = 200
        return Response(serializer.data)
    elif request.method == 'POST':
        # Ekle:
        serializer = StudentSerializer(data=request.data)

        # if valid:
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Creating Successfully'}, status=status.HTTP_201_CREATED)
        # if not valid:
        # return Response({ 'message': 'Not Valid.' })
        return Response(serializer.errors)  # Hata mesajını göster.

# PrimaryKey (ID) istemeyenler:


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_update_delete(request, pk):
    # student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        # Kayıt Görüntüle:
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        # Kayıt Güncelle:
        serializer = StudentSerializer(instance=student, data=request.data)

        # if valid:
        if serializer.is_valid():
            serializer.save()
            # Yeni datayı göster
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        # if not valid:
    elif request.method == 'DELETE':
        # Kayıt Sil:
        student.delete()
        return Response({'message': 'Deleting Successfully'}, status=status.HTTP_202_ACCEPTED)
    # İşlem olmaz ise:
    # Hata mesajını göster.
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
