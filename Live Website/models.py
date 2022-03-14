from django.db import models

# Create your models here.


class Index(models.Model):
    Introtext = models.CharField(
        max_length=200, null=True, verbose_name="Main Intro text")

    headervideo = models.FileField(
        upload_to='videos/', null=True, verbose_name="Header video")

    Introimage = models.ImageField(
        upload_to='images/', null=True, verbose_name="Main Image")

    def __str__(self):
        return self.Introtext


class Lab(models.Model):

    summary = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Main Summary text")

    sub_summary = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="Sub Summary text")

    title_image = models.ImageField(
        upload_to='images/', null=True, blank=True, verbose_name="Main Image")

    title_video = models.FileField(
        upload_to='videos/', null=True, blank=True, verbose_name="Main Video")

    video_checkbox = models.BooleanField(
        "is this a video? (y/n)", default=1, blank=True)

    description1 = models.CharField(
        max_length=500, null=True, blank=True, verbose_name="Main description text")

    video = models.FileField(
        upload_to='videos/', null=True, blank=True, verbose_name="video 1")

    description2 = models.CharField(
        max_length=500, null=True, blank=True, verbose_name="Second section text")

    video2 = models.FileField(
        upload_to='videos/', null=True, blank=True, verbose_name="video 2")

    description3 = models.CharField(
        max_length=500, null=True, blank=True, verbose_name="Third Section Text")

    video3 = models.FileField(
        upload_to='videos/', null=True, blank=True, verbose_name="video 3")

    description4 = models.CharField(
        max_length=500, null=True, blank=True, verbose_name="Conclusion text")

    def __str__(self):
        return self.summary


class Services(models.Model):

    av = models.CharField(
        max_length=130, null=True, verbose_name="AV Services Text")

    acoustics = models.CharField(
        max_length=130, null=True, verbose_name="Acoustics Services Text")

    it = models.CharField(
        max_length=130, null=True, verbose_name="IT Services Text")

    softwareandcontent = models.CharField(
        max_length=130, null=True, verbose_name="Software & Content Services Text")

    def __str__(self):
        return 'Services Text'


class Project_Examples(models.Model):

    project_text = models.CharField(
        max_length=130, null=True, verbose_name="project text")

    project_image = models.ImageField(
        upload_to='images/', null=True, verbose_name="project image")

    project_size = models.CharField(
        max_length=130, null=True, verbose_name="project size (-big/-wide/-horizontal or - for standard)")

    project_services = models.CharField(
        max_length=130, null=True, verbose_name="project services (Software/Acoustics/AV Design)")

    def __str__(self):
        return self.project_text


class Clients(models.Model):

    client_name = models.CharField(
        max_length=130, null=True, verbose_name="client name")

    client_logo = models.ImageField(
        upload_to='images/', null=True, verbose_name="client logo")

    def __str__(self):
        return self.client_name


class Testimonials(models.Model):

    text = models.CharField(
        max_length=370, null=True, verbose_name="testimonial text")

    name = models.CharField(
        max_length=370, null=True, verbose_name="name of person")

    role = models.CharField(
        max_length=370, null=True, verbose_name="role or position")

    def __str__(self):
        return self.name


class Awards(models.Model):

    year = models.CharField(
        max_length=100, null=True, verbose_name="year")

    category = models.CharField(
        max_length=100, null=True, verbose_name="entry")

    award = models.CharField(
        max_length=100, null=True, verbose_name="award")

    link = models.CharField(
        max_length=250, null=True, verbose_name="link")

    def __str__(self):
        return self.year


class Team(models.Model):

    team_image = models.ImageField(
        upload_to='images/', null=True, verbose_name="team image")

    def __str__(self):
        return 'Team Image'


class Contact(models.Model):

    building = models.CharField(
        max_length=100, null=True, verbose_name="street name")
    street = models.CharField(
        max_length=150, null=True, verbose_name="street name")
    town = models.CharField(
        max_length=150, null=True, verbose_name="town and county")
    postcode = models.CharField(
        max_length=150, null=True, verbose_name="postcode")
    country = models.CharField(
        max_length=150, null=True, verbose_name="country")
    email = models.CharField(
        max_length=100, null=True, verbose_name="email")
    telephone = models.CharField(
        max_length=100, null=True, verbose_name="telephone")

    def __str__(self):
        return 'Contact Details'


class About(models.Model):
    header = models.FileField(
        upload_to='videos/', null=True, verbose_name="Header video")

    av = models.ImageField(
        upload_to='images/', null=True, verbose_name="av image")

    acoustics = models.ImageField(
        upload_to='images/', null=True, verbose_name="acoustics image")

    software = models.ImageField(
        upload_to='images/', null=True, verbose_name="software image")

    lighting = models.ImageField(
        upload_to='images/', null=True, verbose_name="lighting image")

    content = models.ImageField(
        upload_to='images/', null=True, verbose_name="content image")

    richard = models.ImageField(
        upload_to='images/', null=True, verbose_name="richard image")

    paul = models.ImageField(
        upload_to='images/', null=True, verbose_name="paul image")

    george = models.ImageField(
        upload_to='images/', null=True, verbose_name="george image")

    david = models.ImageField(
        upload_to='images/', null=True, verbose_name="david image")

    def __str__(self):
        return 'Images'


class Our_Work(models.Model):
    header = models.FileField(
        upload_to='videos/', null=True, verbose_name="Header video")

    def __str__(self):
        return 'Images'


class Case_Studies(models.Model):

    project_text = models.CharField(
        max_length=130, null=True, blank=True, verbose_name="project text")

    project_image = models.ImageField(
        upload_to='images/', null=True, verbose_name="project image")

    project_size = models.CharField(
        max_length=130, null=True, blank=True, verbose_name="project size (-big/-wide/-horizontal/-long or - for standard)")

    project_services = models.CharField(
        max_length=130, null=True, blank=True, verbose_name="project services (Software/Acoustics/AV Design)")

    project_category = models.CharField(
        max_length=130, null=True, blank=True, verbose_name="project category (content/AV/acoustics/development/experiential/retail)")

    video_checkbox = models.BooleanField(
        "is this a video? (y/n)", default=1, blank=True)

    project_header_image = models.ImageField(
            upload_to='images/', null=True, blank=True, verbose_name="case study header image")

    project_header_video = models.FileField(
            upload_to='videos/', null=True, blank=True, verbose_name="case study header video")

    video_checkbox = models.BooleanField(
        "Choose video for header (y/n)", default=1, blank=True)

    project_duration = models.CharField(
        max_length=130, null=True, blank=True, verbose_name="project duration")

    project_client = models.CharField(
        max_length=130, null=True, blank=True, verbose_name="client's name")

    project_01_intro = models.CharField(
        max_length=130, null=True, blank=True, verbose_name="01-The Client intro text")

    project_01_main = models.CharField(
        max_length=750, null=True, blank=True, verbose_name="01-The Client main text")

    project_01_image = models.ImageField(
        upload_to='images/', null=True, blank=True, verbose_name="Section 01 image")

    project_02_intro = models.CharField(
        max_length=130, null=True, blank=True, verbose_name="02-The Brief intro text")

    project_02_main = models.CharField(
        max_length=1450, null=True, blank=True, verbose_name="02-The Brief main text")

    project_02_image1 = models.ImageField(
        upload_to='images/', null=True, blank=True, verbose_name="Section 02 image1")

    project_02_image2 = models.ImageField(
        upload_to='images/', null=True, blank=True, verbose_name="Section 02 image2")

    project_02_image3 = models.ImageField(
        upload_to='images/', null=True, blank=True, verbose_name="Section 02 image3")

    project_03_intro = models.CharField(
        max_length=130, null=True, blank=True, verbose_name="03-The Challenge intro text")

    project_03_main = models.CharField(
        max_length=1450, null=True, blank=True, verbose_name="03-The Challenge main text")

    project_04_intro = models.CharField(
        max_length=130, null=True, blank=True, verbose_name="03-The Outcome intro text")

    project_04_main = models.CharField(
        max_length=1450, null=True, blank=True, verbose_name="03-The Outcome main text")

    project_05_link1 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="05 - link 1")

    project_05_hyperlink1 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="05 - Hyperlink1")

    project_05_link2 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="05 - link 2")

    project_05_hyperlink2 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="05 - Hyperlink 2")

    project_05_link3 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="05 - link 3")

    project_05_hyperlink3 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="05 - Hyperlink 3")

    project_06_link1 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="06 - manufacturer 1")

    project_06_Hyperlink1 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="06 - Hyperlink1")

    project_06_link2 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="06 - manufacturer 2")

    project_06_Hyperlink2 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="06 - Hyperlink2")

    project_06_link3 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="06 - manufacturer 3")

    project_06_Hyperlink3 = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="06 - Hyperlink3")

    def __str__(self):
        return self.project_text
