from django.contrib import admin
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

# Register your models here.
admin.site.register(Lab)
admin.site.register(Index)
admin.site.register(Services)
admin.site.register(Project_Examples)
admin.site.register(Clients)
admin.site.register(Testimonials)
admin.site.register(Awards)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Our_Work)
admin.site.register(Case_Studies)
