from django.db import models
from traveloft.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.core.validators import MaxValueValidator, MinValueValidator
from embed_video.fields import EmbedVideoField

# Create your models here.
class ArticleCategories(models.Model):
    category = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = 'Article Categories'

    def __str__(self):
        return self.category


STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish')
)

class Articles(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ArticleCategories, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    photo1 = models.ImageField(upload_to='upload/articles')
    description1 = models.TextField()
    photo2 = models.ImageField(upload_to='upload/articles', null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    Author = models.CharField(max_length=50)
    Author_email = models.EmailField()
    published_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        db_table = 'Articles'
        ordering = ('-published_on',)
        verbose_name_plural = 'Articles'

    @staticmethod
    def get_articles_by_id(ids):
        return Articles.objects.filter(id__in=ids)

    @staticmethod
    def get_all_articles():
        return Articles.objects.filter(status='publish')

    @staticmethod
    def get_all_articles_by_categoryid(category_id):
        if category_id:
            return Articles.objects.filter(category=category_id, status='publish')
        else:
            return Articles.get_all_articles()



def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Articles)

class Terms_and_Conditions(models.Model):
    heading = models.CharField(max_length=200)
    para1 = models.TextField()
    para2 = models.TextField(null=True, blank=True)
    para3 = models.TextField(null=True, blank=True)
    para4 = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Terms and Conditions'

class Cancellation_Policy(models.Model):
    point = models.TextField()
    class Meta:
        verbose_name_plural = 'Cancellation Policies'


class Activities_Grid_Photos(models.Model):
    trekking = models.ImageField(upload_to='upload/activities')
    village_Tour = models.ImageField(upload_to='upload/activities')
    adventure_Sports = models.ImageField(upload_to='upload/activities')
    community_Work = models.ImageField(upload_to='upload/activities')

    class Meta:
        verbose_name_plural = 'Activities Grid Photos'

class Location(models.Model):
    district = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.district

class Trek(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    best = models.BooleanField(null=True, blank=True, default=False)
    altitude = models.CharField(max_length=20)
    duration_days = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=20)
    district = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    distance = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    quote = models.TextField(null=True, blank=True)
    photo1 = models.ImageField(upload_to='upload/treks')
    desc1 = models.TextField()
    photo2 = models.ImageField(upload_to='upload/treks', null=True, blank=True)
    desc2 = models.TextField(null=True, blank=True)
    photo3 = models.ImageField(upload_to='upload/treks', null=True, blank=True)
    desc3 = models.TextField(null=True, blank=True)
    photo4 = models.ImageField(upload_to='upload/treks', null=True, blank=True)
    desc4 = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Treks'
    def __str__(self):
        return self.title

    @staticmethod
    def get_all_treks():
        return Trek.objects.all()

    @staticmethod
    def get_all_treks_by_categoryid(placeID):
        if placeID:
            return Trek.objects.filter(district=int(placeID))
        else:
            return Trek.get_all_treks()

pre_save.connect(slug_generator, sender=Trek)

class Trek_days(models.Model):
    trek = models.ForeignKey(Trek, on_delete=models.CASCADE)
    day_no = models.CharField(max_length=4)
    days = models.TextField()
    class Meta:
        verbose_name_plural = 'Trek Days'
    def __str__(self):
        return self.days


class About_trek(models.Model):
    image1 = models.ImageField(upload_to='upload/treks')
    para1 = models.TextField()
    paraE1 = models.TextField(default='')
    head1 = models.CharField(max_length=250, null=True, blank=True)
    para2 = models.TextField(null=True, blank=True)
    image2 = models.ImageField(upload_to='upload/treks', null=True, blank=True)
    para3 = models.TextField(null=True, blank=True)
    image3 = models.ImageField(upload_to='upload/treks', null=True, blank=True)
    para4 = models.TextField(null=True, blank=True)
    head2 = models.CharField(max_length=250, null=True, blank=True)
    para5 = models.TextField(null=True, blank=True)
    image4 = models.ImageField(upload_to='upload/treks', null=True, blank=True)
    para6 = models.TextField(null=True, blank=True)
    image5 = models.ImageField(upload_to='upload/treks', null=True, blank=True)
    para7 = models.TextField(null=True, blank=True)
    head3 = models.CharField(max_length=250, null=True, blank=True)
    para8 = models.TextField(null=True, blank=True)
    image6 = models.ImageField(upload_to='upload/treks', null=True, blank=True)
    para9 = models.TextField(null=True, blank=True)
    para10 = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'About Trekking'

class About_villageTours(models.Model):
    image1 = models.ImageField(upload_to='upload/VillageTours')
    para1 = models.TextField()
    paraE1 = models.TextField(default='')
    head1 = models.CharField(max_length=250, null=True, blank=True)
    para2 = models.TextField(null=True, blank=True)
    image2 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    para3 = models.TextField(null=True, blank=True)
    image3 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    para4 = models.TextField(null=True, blank=True)
    head2 = models.CharField(max_length=250, null=True, blank=True)
    para5 = models.TextField(null=True, blank=True)
    image4 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    para6 = models.TextField(null=True, blank=True)
    image5 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    para7 = models.TextField(null=True, blank=True)
    head3 = models.CharField(max_length=250, null=True, blank=True)
    para8 = models.TextField(null=True, blank=True)
    image6 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    para9 = models.TextField(null=True, blank=True)
    para10 = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'About Village Tours'


class Village_Tours(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    best = models.BooleanField(null=True, blank=True, default=False)
    altitude = models.CharField(max_length=20)
    duration_days = models.CharField(max_length=20)
    population = models.CharField(max_length=20)
    district = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    price = models.CharField(max_length=20)
    quote = models.TextField(null=True, blank=True)
    photo1 = models.ImageField(upload_to='upload/VillageTours')
    desc1 = models.TextField()
    photo2 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    desc2 = models.TextField(null=True, blank=True)
    photo3 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    desc3 = models.TextField(null=True, blank=True)
    photo4 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    desc4 = models.TextField(null=True, blank=True)
    photo5 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    desc5 = models.TextField(null=True, blank=True)
    photo6 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    desc6 = models.TextField(null=True, blank=True)
    photo7 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    desc7 = models.TextField(null=True, blank=True)
    photo8 = models.ImageField(upload_to='upload/VillageTours', null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Village Tours'
    def __str__(self):
        return self.title

    @staticmethod
    def get_all_VillageTours():
        return Village_Tours.objects.all()

    @staticmethod
    def get_all_VillageTours_by_categoryid(placeID):
        if placeID:
            return Village_Tours.objects.filter(district=int(placeID))
        else:
            return Village_Tours.get_all_VillageTours()


pre_save.connect(slug_generator, sender=Village_Tours)

class VillageTour_days(models.Model):
    village_Tour = models.ForeignKey(Village_Tours, on_delete=models.CASCADE)
    day_no = models.CharField(max_length=4)
    days = models.TextField()
    class Meta:
        verbose_name_plural = 'Village Tour Days'
    def __str__(self):
        return self.days

class Privacy_Policy(models.Model):
    heading = models.CharField(max_length=200)
    para1 = models.TextField()
    para2 = models.TextField(null=True, blank=True)
    para3 = models.TextField(null=True, blank=True)
    para4 = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Privacy Policies'

class Disclaimer(models.Model):
    disclaimer = models.TextField()
    class Meta:
        verbose_name_plural = 'Disclaimer'



class Testimonials(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    email = models.EmailField()
    place = models.CharField(max_length=250)
    profile_pic = models.ImageField(upload_to='upload/profilePicture', default="profile1.png", null=True, blank=True)
    review = models.CharField(max_length=250)
    published_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        db_table = 'Testimonials'
        ordering = ('-updated',)
        verbose_name_plural = 'Testimonials'

pre_save.connect(slug_generator, sender=Testimonials)

class Gallery_category(models.Model):
    category = models.CharField(max_length=40)
    class Meta:
        verbose_name_plural = 'Gallery Categories'

    def __str__(self):
        return self.category



class Gallery_photo(models.Model):
    category = models.ForeignKey(Gallery_category, on_delete=models.CASCADE, null=True, blank=True)
    #title
    #paranoma
    image = models.ImageField(upload_to='upload/gallery')
    published_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Gallery Photos'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @staticmethod
    def get_all_photos():
        return Gallery_photo.objects.order_by('-updated')

    @staticmethod
    def get_all_photos_by_categoryid(photoID):
        if photoID:
            return Gallery_photo.objects.filter(category=photoID)
        else:
            return Gallery_photo.get_all_photos()


class Item(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True, default="Video")
    video = EmbedVideoField()  # same like models.URLField()
    published_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Youtube Videos'
    def __str__(self):
        return self.title

class about_us(models.Model):
    image1 = models.ImageField(upload_to='upload/aboutus')
    image2 = models.ImageField(upload_to='upload/aboutus', null=True, blank=True)
    image3 = models.ImageField(upload_to='upload/aboutus', null=True, blank=True)
    image4 = models.ImageField(upload_to='upload/aboutus', null=True, blank=True)
    image5 = models.ImageField(upload_to='upload/aboutus', null=True, blank=True)
    image6 = models.ImageField(upload_to='upload/aboutus', null=True, blank=True)
    image7L = models.ImageField(upload_to='upload/aboutus', null=True, blank=True)
    image8R = models.ImageField(upload_to='upload/aboutus', null=True, blank=True)
    image9 = models.ImageField(upload_to='upload/aboutus', null=True, blank=True)
    image10 = models.ImageField(upload_to='upload/aboutus', null=True, blank=True)
    para1 = models.TextField()
    para2 = models.TextField(null=True, blank=True)
    para3 = models.TextField(null=True, blank=True)
    para4 = models.TextField(null=True, blank=True)
    para5 = models.TextField(null=True, blank=True)
    para6 = models.TextField(null=True, blank=True)
    para7 = models.TextField(null=True, blank=True)
    para8 = models.TextField(null=True, blank=True)
    para9 = models.TextField(null=True, blank=True)
    para10 = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'About Us'

class Customer(models.Model):
    Name = models.CharField(max_length=250, default='', blank=True)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=15, default='', blank=True)
    Place = models.CharField(max_length=250, default='', blank=True)
    Number_of_people = models.IntegerField(default=1, blank=True, validators=[MaxValueValidator(200), MinValueValidator(1)])
    Trek1 = models.ForeignKey(Trek, related_name='trek1', on_delete=models.CASCADE, null=True, blank=True)
    Trek2 = models.ForeignKey(Trek, related_name='trek2', on_delete=models.CASCADE, null=True, blank=True)
    Trek3 = models.ForeignKey(Trek, related_name='trek3', on_delete=models.CASCADE, null=True, blank=True)
    Trek4 = models.ForeignKey(Trek, related_name='trek4', on_delete=models.CASCADE, null=True, blank=True)
    Activities = models.TextField(null=True, blank=True)
    VillageTours1 = models.ForeignKey(Village_Tours, related_name='VillageTours1', on_delete=models.CASCADE, null=True, blank=True)
    VillageTours2 = models.ForeignKey(Village_Tours, related_name='VillageTours2', on_delete=models.CASCADE, null=True, blank=True)
    VillageTours3 = models.ForeignKey(Village_Tours, related_name='VillageTours3', on_delete=models.CASCADE, null=True, blank=True)
    VillageTours4 = models.ForeignKey(Village_Tours, related_name='VillageTours4', on_delete=models.CASCADE, null=True, blank=True)
    notify_on = models.TextField(null=True, blank=True)
    terms_confirmed = models.BooleanField(default=False)
    RegDate = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Customer'
        verbose_name_plural = 'Customers'
    def __str__(self):
        return self.Email

class Community_Work(models.Model):
    image1 = models.ImageField(upload_to='upload/CommunityWork')
    para1 = models.TextField(default='')
    paraE1 = models.TextField(default='')
    line1 = models.TextField(default='')
    line2 = models.TextField(default='')
    line3 = models.TextField(default='')
    paraE2 = models.TextField(default='')
    head1 = models.CharField(max_length=250, null=True, blank=True)
    para2 = models.TextField(null=True, blank=True)
    image2 = models.ImageField(upload_to='upload/CommunityWork', null=True, blank=True)
    para3 = models.TextField(null=True, blank=True)
    image3 = models.ImageField(upload_to='upload/CommunityWork', null=True, blank=True)
    para4 = models.TextField(null=True, blank=True)
    head2 = models.CharField(max_length=250, null=True, blank=True)
    para5 = models.TextField(null=True, blank=True)
    image4 = models.ImageField(upload_to='upload/CommunityWork', null=True, blank=True)
    para6 = models.TextField(null=True, blank=True)
    image5 = models.ImageField(upload_to='upload/CommunityWork', null=True, blank=True)
    para7 = models.TextField(null=True, blank=True)
    head3 = models.CharField(max_length=250, null=True, blank=True)
    para8 = models.TextField(null=True, blank=True)
    image6 = models.ImageField(upload_to='upload/CommunityWork', null=True, blank=True)
    para9 = models.TextField(null=True, blank=True)
    para10 = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Community Work'


class Upcoming_Events(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=150)
    trek = models.ForeignKey(Trek, on_delete=models.CASCADE, null=True, blank=True)
    Activities = models.BooleanField(default=False, null=True, blank=True)
    VillageTours = models.ForeignKey(Village_Tours, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='upload/UpcomingEvents')
    starts_on = models.DateTimeField()
    duration_days = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        verbose_name_plural = 'Upcoming Events'


    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Event(models.Model):
    Name = models.CharField(max_length=250, default='', blank=True)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=15, default='', blank=True)
    Place = models.CharField(max_length=250, default='', blank=True)
    Number_of_people = models.IntegerField(default=1, blank=True, validators=[MaxValueValidator(200), MinValueValidator(1)])
    event = models.ForeignKey(Upcoming_Events, on_delete=models.CASCADE)
    notify_on = models.TextField(null=True, blank=True)
    terms_confirmed = models.BooleanField(default=False)
    RegDate = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Event'
        verbose_name_plural = 'Upcomig Events Customer'
    def __str__(self):
        return self.Email

class Adventure_Sports(models.Model):
    head = models.CharField(max_length=250)
    image1 = models.ImageField(upload_to='upload/AdventureSports')
    para1 = models.TextField()
    image2 = models.ImageField(upload_to='upload/AdventureSports', null=True, blank=True)
    para2 = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Adventure Sports'
    def __str__(self):
        return self.head


class Main_Slider(models.Model):
    image1 = models.ImageField(upload_to='upload/MainSlider')
    image2 = models.ImageField(upload_to='upload/MainSlider')
    image3 = models.ImageField(upload_to='upload/MainSlider', null=True, blank=True)
    image4 = models.ImageField(upload_to='upload/MainSlider', null=True, blank=True)
    image5 = models.ImageField(upload_to='upload/MainSlider', null=True, blank=True)
    image6 = models.ImageField(upload_to='upload/MainSlider', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Main Slider Photos'

class Contact_Us(models.Model):
    address = models.CharField(max_length=60, default='')
    pin_code = models.CharField(max_length=10, default='')
    mobile_1 = models.CharField(max_length=15, default='')
    mobile_2 = models.CharField(max_length=15, default='')
    time_am = models.CharField(max_length=5, default='')
    time_pm = models.CharField(max_length=5, default='')

    mobile_job_1 = models.CharField(max_length=15, default='')
    mobile_job_2 = models.CharField(max_length=15, default='')
    time_job_am = models.CharField(max_length=5, default='')
    time_job_pm = models.CharField(max_length=5, default='')

    class Meta:
        verbose_name_plural = 'Contact Us'

Gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Rather not say', 'Rather not say')
)
"""
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=Gender, max_length=20)
    email = models.EmailField()
    body = models.TextField()

def get_image_filename(instance, filename):
    id = instance.feedback.id
    return "feedback_images/%s.jpg" % (id)


class Images(models.Model):
    feedback = models.ForeignKey(Feedback, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')

"""