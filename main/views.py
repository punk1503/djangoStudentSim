from django.shortcuts import render

# Create your views here.
def clicker(request):
    return render(request, 'pages/student.html')