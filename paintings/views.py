from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Painting, Artist, Subject, Trend, Media
from .forms import NewPainting

# Create your views here.

def list_paintings_view(request):
    paintings_list = Painting.objects.all()
    return render(request,  'paintings_list.html', {'paintings': paintings_list})

def detail_paintings_view(request, id=None):
    painting = get_object_or_404(Painting, id=id)
    return render(request, 'painting_detail.html', {'painting': painting})

@login_required
def add_painting_view(request):

    if request.method == 'POST':
        if request.user.profile.profile_type == 'ARTIST':
            painting_form = NewPainting(request.POST, request.FILES)
            if painting_form.is_valid():
                painting_form.save()
                messages.success(request,'Your painting has been successfully uploaded.')
                return redirect(reverse('paintings'))
            else:
                messages.error(request,"We couldn't upload your painting.")
        else:
            messages.error(request,"Don't try to cheat, please register as an artist.")
            return redirect(reverse('register'))
    else:
        painting_form = NewPainting()

    return render(request, 'new_painting.html', 
                {'painting_form': painting_form})
        
