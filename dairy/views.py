from django.shortcuts import render,get_object_or_404
from .models import Diary
from .forms import Entryform
from datetime import datetime


# Create your views here.

def add(request):
    form = Entryform()

    if request.method == 'POST':
        filled_form = Entryform(request.POST)
        if filled_form.is_valid():
            info = 'Your diary'
            note = ' is store !'
            filled_form.post_date = datetime.now()
            filled_form.save()
            newform = Entryform()
            return render(request, 'add.html', { 'form':newform, 'info': info, 'note':note })

        """
           Store the diaries and show the message
           3:18 PM 11/18/22 by Deepesh Mahato
        """
    else:
        form = Entryform()
        return render(request, 'add.html',{ 'form':form, })



def detail(request,diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    return render(request, 'detaildairy.html', { 'diary':diary})




def diarylist(request):
    """
        Display the diaries sorted by date posted in descending order
        3:31 PM 11/18/22 by Deepesh Mahato
    """

    diaries = Diary.objects.order_by('-post_date')
    notice= True if len(diaries) == 0 else None

    return render(request, 'dairylist.html', {'diaries':diaries, 'notice':notice })


