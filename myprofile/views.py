from django.shortcuts import render

# Create your views here.
def myprofile(request):
    """
    Render the 'myprofile' page.
    """
    return render(request, 'myprofile/myprofile.html')