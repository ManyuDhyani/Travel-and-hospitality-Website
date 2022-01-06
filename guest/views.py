from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import modelformset_factory


from traveloft import settings
from .forms import *
from .models import *


def home(request):
    slider = Main_Slider.objects.first()
    latest_updates = Articles.objects.filter(status='publish').order_by("-updated")[:6]
    treks = Trek.objects.filter(best=True)[:6]
    village_tour = Village_Tours.objects.filter(best=True)[:4]
    reviews = Testimonials.objects.filter(status='publish').order_by("-updated")[:9]
    data = {
        'slider': slider,
        'articles': latest_updates,
        'treks': treks,
        'villages': village_tour,
        'reviews': reviews,
    }
    return render(request, "guest/index.html", data)


def articles(request):
    categories = ArticleCategories.objects.all()

    categoryID = request.GET.get('category')

    if categoryID:
        articles = Articles.get_all_articles_by_categoryid(categoryID)

    else:
        articles = Articles.get_all_articles()


    data = {}
    data['articles'] = articles
    data['categories'] = categories

    return render(request, 'guest/Articles.html', data)

def article(request, slug_text):
    article_query = Articles.objects.filter(slug=slug_text)
    if article_query:
        article_query = article_query.first()
    else:
        return HttpResponse("<h1>Page Not Found</h1>")
    data = {
        'article': article_query
    }
    return render(request, 'guest/article.html', data)


def article_form(request):
    msg_s = ""
    msg_f = ""
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                title = form.cleaned_data.get('title')
                image1 = form.cleaned_data.get('photo1')
                paragraph1 = form.cleaned_data.get('description1')
                image2 = form.cleaned_data.get('photo2')
                paragraph2 = form.cleaned_data.get('description2')
                author = form.cleaned_data.get('Author')
                author_email = form.cleaned_data.get('Author_email')
                form.save()
                msg_s = "Your Article has been submitted Successfully. Article will be Published after Evaluation and you will be notified through Email."
            except:
                msg_f = "Something went Wrong! Resubmit your Article."
    else:
        form = ArticleForm()

    msg = {}
    msg['msg_s'] = msg_s
    msg['msg_f'] = msg_f
    return render(request, "guest/article_form.html", {'article': form, 'msg': msg})

def terms(request):
    terms_and_condition = Terms_and_Conditions.objects.all()
    data = {'terms': terms_and_condition}
    return render(request, 'guest/termsconditions.html', data)

def Cancellation(request):
    cancellationPolicy = Cancellation_Policy.objects.all()
    data = {'policies': cancellationPolicy}
    return render(request, 'guest/cancellationpolicy.html', data)

def contacts(request):
    contact = Contact_Us.objects.first()
    data = {'contact': contact}
    return render(request, 'guest/contacts.html', data)

def aboutus(request):
    about = about_us.objects.first()
    data = {'about': about}
    return render(request, 'guest/aboutus.html', data)

def jobs(request):
    return render(request, 'guest/jobs.html')


def page_not_found(request, exception):
    return render(request, 'guest/404.html')


def activities(request):
    photos = Activities_Grid_Photos.objects.first()
    data = {'photos': photos}
    return render(request, 'guest/Activities.html', data)


def trek(request, slug_text):
    trek_query = Trek.objects.filter(slug=slug_text)

    if trek_query:
        trek_query = trek_query.first()

        itinerary = Trek_days.objects.filter(trek=int(trek_query.id))

    else:
        return HttpResponse("<h1>Page Not Found</h1>")
    data = {
        'trek': trek_query,
        'itineraries': itinerary
    }
    return render(request, 'guest/trek.html', data)

def trek_main(request):
    categories = Location.objects.all()

    categoryID = request.GET.get('category')

    if categoryID:
        treks = Trek.get_all_treks_by_categoryid(categoryID)

    else:
        treks = Trek.get_all_treks()


    data = {}
    data['treks'] = treks
    data['categories'] = categories

    return render(request, 'guest/trekMain.html', data)

def VillageTour(request, slug_text):
    VillageTour_query = Village_Tours.objects.filter(slug=slug_text)
    if VillageTour_query:
        VillageTour_query = VillageTour_query.first()
        itinerary = VillageTour_days.objects.filter(village_Tour=int(VillageTour_query.id))
        print(itinerary)
    else:
        return HttpResponse("<h1>Page Not Found</h1>")
    data = {
        'village': VillageTour_query,
        'itineraries': itinerary
    }
    return render(request, 'guest/villageTour.html', data)

def VillageTour_main(request):
    categories = Location.objects.all()

    categoryID = request.GET.get('category')

    if categoryID:
        villages = Village_Tours.get_all_VillageTours_by_categoryid(categoryID)
    else:
        villages = Village_Tours.get_all_VillageTours()

    data = {}
    data['villages'] = villages
    data['categories'] = categories

    return render(request, 'guest/VillageTourMain.html', data)

def privacy(request):
    PrivacyPolicies = Privacy_Policy.objects.all()
    data = {'policies': PrivacyPolicies}
    return render(request, 'guest/privacypolicy.html', data)


def disclaimer(request):
    para = Disclaimer.objects.first()
    data = {'disclaimer': para}
    return render(request, 'guest/disclaimer.html', data)

def inquiry(request):
    msg_s = ""
    msg_f = ""
    if request.method == 'POST':
        form = sendmail(request.POST)
        if form.is_valid():
            to = 'traveloftenquiry@gmail.com'
            Name = form.cleaned_data['Name']
            Email = form.cleaned_data['Email']
            Mobile = form.cleaned_data['Mobile']
            msg = form.cleaned_data['Msg']
            subject = Name + " || " + Email + " || " + Mobile + " || " + "INQUIRY"
            res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
            if (res == 1):
                msg_s = "Your INQUIRY is sent successfully. We will Contact you within 48 hours."
            else:
                msg_f = "Your INQUIRY message Failed. Resend the INQUIRY!"
    else:
        form = sendmail()
    msg = {}
    msg['msg_s'] = msg_s
    msg['msg_f'] = msg_f
    return render(request, 'guest/inquiry.html', {'form': form, 'msg': msg})


def gallery(request):
    flag = 0
    categories = Gallery_category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID == str(1):
        youtube = Item.objects.order_by('-updated')[:21]
        data = {
            'youtube': youtube,
        }
        return render(request, 'guest/gallery.html', data)

    elif categoryID!=None and categoryID!=str(1):
        pics = Gallery_photo.get_all_photos_by_categoryid(categoryID)
        pics = pics.order_by('-updated')
        flag = 1

    else:
        pics = Gallery_photo.get_all_photos()
        photos = Paginator(pics, 12)
        page_num = request.GET.get('page', 1)
        try:
            page = photos.page(page_num)
        except:
            page = photos.page(1)

    data = {}
    if flag == 1:
        data['photos'] = pics
    else:
        data['photos'] = page
        data['pages'] = photos.num_pages
    data['categories'] = categories

    return render(request, 'guest/gallery.html', data)



def create_package(request):
    msg_s = ""
    msg_f = ""
    flag = 0

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                Name = form.cleaned_data.get('Name')
                Email = form.cleaned_data.get('Email')
                Mobile = form.cleaned_data.get('Mobile')
                Place = form.cleaned_data.get('Place')
                Number_of_people = form.cleaned_data.get('Number_of_people')
                Trek1 = form.cleaned_data.get('Trek1')
                Trek2 = form.cleaned_data.get('Trek2')
                Trek3 = form.cleaned_data.get('Trek3')
                Trek4 = form.cleaned_data.get('Trek4')
                Activities = form.cleaned_data.get('Activities')
                VillageTours1 = form.cleaned_data.get('VillageTours1')
                VillageTours2 =form.cleaned_data.get('VillageTours2')
                VillageTours3 = form.cleaned_data.get('VillageTours3')
                VillageTours4 = form.cleaned_data.get('VillageTours4')
                notify_on = form.cleaned_data.get('notify_on')
                terms_confirmed = form.cleaned_data.get('terms_confirmed')

                if notify_on and Mobile == '':

                    msg_f = "Please either FILL your Phone Number or DESELECT the Notification mode options."
                    flag = 1
                elif terms_confirmed and flag == 0:
                    if Trek1 or Activities or VillageTours1:
                        form.save()
                        msg_s = "Your Package Created successfully.  We will Contact you within 48 hours with your Package Estimation."
                    else:
                        msg_f = "To create package select minimum of one Trek / Adventure Sport / Village Tour."
                else:
                    msg_f = "Please Agree to Terms & Conditions."

            except:

                msg_f = "Your Package Creation Failed. Create your Package Again!"

    else:
        form = CustomerForm()
    msg = {}
    msg['msg_s'] = msg_s
    msg['msg_f'] = msg_f
    return render(request, "guest/CreatePackageForm.html", {'reg': form, 'msg': msg})



def upcoming_event(request):
    events = Upcoming_Events.objects.filter(status='publish').order_by("starts_on")[:12]
    ID = request.GET.get('id')
    detail = Upcoming_Events.objects.filter(id=ID)

    if detail and detail[0].trek:
        trek_id = detail[0].trek.id
        trek = Trek.objects.filter(id=trek_id)
        slug_link = trek[0].slug

        url = '/treks/'+slug_link

        return redirect(url)
    elif detail and detail[0].Activities:
        return redirect('/adventure-sports')
    elif detail and detail[0].VillageTours:
        village_id = detail[0].VillageTours.id
        village = Village_Tours.objects.filter(id=village_id)
        slug_link = village[0].slug
        url = '/village-tours/' + slug_link
        return redirect(url)
    data = {
        'events': events
    }
    return render(request, 'guest/upcomingEvents.html', data)



def upcoming_event_form(request):
    msg_s = ""
    msg_f = ""
    flag = 0

    if request.method == 'POST':
        form = Upcoming_Event_CustomerForm(request.POST)
        if form.is_valid():
            try:
                Name = form.cleaned_data.get('Name')
                Email = form.cleaned_data.get('Email')
                Mobile = form.cleaned_data.get('Mobile')
                Place = form.cleaned_data.get('Place')
                Number_of_people = form.cleaned_data.get('Number_of_people')
                event = form.cleaned_data.get('event')
                notify_on = form.cleaned_data.get('notify_on')
                terms_confirmed = form.cleaned_data.get('terms_confirmed')

                if notify_on and Mobile == '':

                    msg_f = "Please either FILL your Phone Number or DESELECT the Notification mode options."
                    flag = 1
                elif terms_confirmed and flag == 0:
                    form.save()

                    msg_s = "Your Package Created successfully.  We will Contact you within 48 hours with your Package Estimation."
                else:
                    msg_f = "Please Agree to Terms & Conditions."

            except:

                msg_f = "Your Package Creation Failed. Create your Package Again!"

    else:
        form = Upcoming_Event_CustomerForm
    msg = {}
    msg['msg_s'] = msg_s
    msg['msg_f'] = msg_f
    return render(request, "guest/EventForm.html", {'reg': form, 'msg': msg})


def adventure_sports_manyu(request):
    adv_manyu = Adventure_Sports.objects.all()
    data = {
        'sports': adv_manyu
    }
    return render(request, 'guest/adventureSports.html', data)


def community_work(request):
    community = Community_Work.objects.first()
    data = {
        'community': community
    }
    return render(request, 'guest/CommunityWork.html', data)

def about_Trek(request):
    trek = About_trek.objects.first()
    data = {
        'trek': trek
    }
    return render(request, 'guest/aboutTreks.html', data)


def about_Village(request):
    village = About_villageTours.objects.first()
    data = {
        'village': village
    }
    return render(request, 'guest/aboutVillagetours.html', data)

def search(request):
    query = request.GET['query']
    if query == '':
        return redirect('/')
    elif len(query) > 60:
        treks = Trek.objects.none()
        villages = Village_Tours.objects.none()
        lt = 0
        lv = 0
    else:

        location = Location.objects.filter(district__startswith=query)

        treks_title = Trek.objects.filter(title__startswith=query)
        treks_district = Trek.objects.filter(district__in=location)
        lt = len(treks_title) + len(treks_district)
        treks = (treks_title | treks_district).distinct()

        village_title = Village_Tours.objects.filter(title__startswith=query)
        village_district = Village_Tours.objects.filter(district__in=location)
        lv = len(village_title) + len(village_district)
        villages = (village_title | village_district).distinct()

    data = {
        'treks': treks,
        'villages': villages,
        'query': query,
        'lt': lt,
        'lv': lv,
    }
    return render(request, 'guest/search.html', data)

def testimonials(request):
    testimonials = Testimonials.objects.filter(status='publish')

    paginator = Paginator(testimonials, 9)
    page_request_variable = 'page'
    page = request.GET.get(page_request_variable)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    data = {
        'testimonials': paginated_queryset,
        'page_request_variable': page_request_variable
    }
    return render(request, 'guest/testimonials.html', data)

"""
def feedback(request):

    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=1)

    if request.method == 'POST':

        feedForm = FeedbackForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())


        if feedForm.is_valid() and formset.is_valid():
            feed = feedForm.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(feedback=feed, image=image)
                photo.save()
            return redirect("/")
        else:
            print(feedForm.errors, formset.errors)
    else:
        feedForm = FeedbackForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'guest/feedback.html', {'feedForm': feedForm, 'formset': formset})

"""