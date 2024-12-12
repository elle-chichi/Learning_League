from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .forms import ClientForm
from .models import Client



# Create your views here.

def index(request):
    context = {
        'welcome_message': "Welcome to the Learning League!",
    }
    return render(request, 'index.html')
def student(request):
    return render(request, 'student_list.html')

def contact_us(request):
    return render(request, 'contact.html')

def vehicle(request):
    return render(request, 'vehicle.html')


def teacher_list(request):
    return render(request, 'teacher_list.html')

# def collect_client_data(request):
#     return render(request, 'collect_client_data.html')


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = ContactForm()
#         return render(request, 'contact.html', {'form': form})
def success(request):
    return render(request, 'success.html')

# def contact(request):
#     if request.method == 'POST':
#         form = ClientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#         else:
#             print(form.errors)
#     else:
#         form = ClientForm()
#
#     return render(request, 'contact.html', {'form': form})


def client_form(request):
    if request.method == 'POST':
        # Capture form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')

        # Create a new Client instance and save the data to the database
        client = Client(name=name, email=email, number=number, message=message)
        client.save()

        # Redirect to a success page (or the same page)
        return redirect('client_form')  # Redirect to the form page after successful submission

    return render(request, 'client_form.html')