from django.shortcuts import render, get_object_or_404
from .models import *
from .form import *
from Gallery.models import *
from Events.models import *


def index(request):

    cont = Contact.objects.all()  # Model Class Contact
    sli = Slider.objects.all()  # Model Class Slider
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link
    fm = FOAP.objects.all().order_by('id')
    donate_package = Package.objects.all().order_by('-id')
    News_post = New.objects.all().order_by('-Date_time')
    R_event = Event.objects.all().order_by('-id')  # Model Class Event
    review = Review.objects.all().order_by('-id')  # Model Class Review
    g_image = Image_Gallery.objects.all().order_by('-id')
    Re_list = Running_Event.objects.all().order_by('-id')
    Up_list = Upcoming_Event.objects.all().order_by('-id')

    context = {'cont': cont, 'logo': logo,
               'sli': sli, 'fm': fm, 'donate_package': donate_package,
               'News_post': News_post, 'R_event': R_event, 'review': review,
               'g_image': g_image, 'Re_list': Re_list, 'Up_list': Up_list, 'slink': slink}  # Data Dictionary
    return render(request, 'index.html', context)
##########################################################


def master(request):
    return render(request, 'master.html')

########################################################
#--blog page--#


def blog_detail(request, pk):
    N_id = get_object_or_404(New, pk=pk)  # Model class Call & pk Pass in url
    comments = N_id.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = N_id
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    cont = Contact.objects.all()  # Model Class Contact
    logo = Logo.objects.all()  # Model Class Logo
    slink = Social_link.objects.all()  # Model Class Social Link

    context = {'N_id': N_id, 'cont': cont, 'logo': logo, 'comments': comments,
               'new_comment': new_comment, 'comment_form': comment_form, 'slink': slink}
    return render(request, 'blog/blog-detail.html', context)

#############################################################################################
