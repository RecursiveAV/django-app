from django.shortcuts import render, get_object_or_404
from .models import Lab
from .models import Index
from .models import Services
from .models import Project_Examples
from .models import Clients
from .models import Testimonials
from .models import Awards
from .models import Team
from .models import Contact
from .models import About
from .models import Our_Work
from .models import Case_Studies
# Create your views here.


def index(request):
    #first assign a variable to the objects we wish to see
    jobs = Services.objects
    examples = Project_Examples.objects
    clients = Clients.objects
    testimonials = Testimonials.objects
    awards = Awards.objects
    team = Team.objects
    contact = Contact.objects
    #These terms create dictionary entries which are then referenced in the templates to render the data within a for loop inside the html
    return render(request, 'jobs/index.html', {'jobs': jobs, 'examples': examples, 'clients': clients, 'testimonials': testimonials, 'awards': awards, 'team': team, 'contact': contact})


def lab(request):
    jobs = Lab.objects
    contact = Contact.objects
    return render(request, 'jobs/lab.html', {'jobs': jobs, 'contact': contact})


def about(request):
    #first assign a variable to the objects we wish to see
    contact = Contact.objects
    images = About.objects
    #These terms create dictionary entries which are then referenced in the templates to render the data within a for loop inside the html
    return render(request, 'jobs/about.html', {'contact': contact, 'images': images})


def career(request):
    contact = Contact.objects
    return render(request, 'jobs/career.html', {'contact': contact})


def contact(request):
    contact = Contact.objects
    return render(request, 'jobs/contact.html', {'contact': contact})


def our_work(request):
    images = Our_Work.objects
    clients = Clients.objects
    testimonials = Testimonials.objects
    contact = Contact.objects
    case_studies = Case_Studies.objects
    return render(request, 'jobs/our_work.html', {'images': images, 'clients': clients, 'testimonials': testimonials, 'contact': contact, 'case_studies': case_studies})


def detail(request, job_id):
    job_detail = get_object_or_404(Lab, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})


def projectdetail(request, project_id):
    contact = Contact.objects
    job_detail = get_object_or_404(Case_Studies, pk=project_id)
    next_project_id = (project_id + 1)
    prev_project_id = (project_id - 1)
    return render(request, 'jobs/projectdetail2.html', {'job': job_detail, 'contact': contact, 'next': next_project_id, 'prev': prev_project_id})
