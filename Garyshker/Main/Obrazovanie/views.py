from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.urls import reverse
from .forms import *
from django.views.generic import View




class SearchField(View):
    model = Item
    template = 'obrazovanie/search.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            search = request.POST['search']
        else:
            search = ''
        item = self.model.objects.filter(name__icontains=search)
        context = {
            'item':item
        }
        return render(request, self.template, context)



def show_item(request):
    type = Type.objects.all()
    item = Item.objects.all()
    genre = Genre.objects.all()


    context = {
        'type': type,
        'item': item,
        'genre': genre
    }
    return render(request, 'obrazovanie/obrazovanie.html', context)


def genre_detail(request, slug):
    genre_all = Genre.objects.all()
    genre = Genre.objects.filter(slug=slug)
    return render(request, 'obrazovanie/genre_detail.html', context={'genre':genre, 'genre_all': genre_all})


def item_detail(request, id):
    item = Item.objects.filter(id=id)
    return render(request, 'obrazovanie/item_detail.html', context={'item': item})



def all_reports(request):
    reports = Report.objects.all()
    genre_all = Genre.objects.all()

    # genre = Genre.objects.filter(slug=slug)
    # if reports.likes.get(id=request.user.id).exists():
    #
    #     is_liked=True





    context = {
        'reports': reports,
        'genre_all': genre_all,

        # 'genre':genre
    }
    return render(request, 'obrazovanie/all_reports.html', context)


def report_detail(request, id):
    report = Report.objects.get(id=id)
    comments = Comment.objects.filter(report=report, reply=None).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(report=report, user = request.user, content=content, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(reverse('report_detail_url', kwargs={'id': report.id}))

    else:
        comment_form = CommentForm()


    context = {
        'report': report,
        'comments': comments,
        'comment_form': comment_form,

    }

    return render(request, 'obrazovanie/report_detail.html', context)


def genre_detail_report(request, slug):
    genre_all = Genre.objects.all()
    genre = Genre.objects.filter(slug=slug)
    # is_liked = False
    # if report.likes.filter(id=request.user.id).exists():
    #     is_liked=True
    return render(request, 'obrazovanie/genre_detail_report.html', context={'genre': genre, 'genre_all':genre_all})



def like_report(request):
    report = Report.objects.get(id=request.POST.get('post_id'))
    is_liked = False
    if report.likes.filter(id=request.user.id).exists():
        report.likes.remove(request.user)
        is_liked=False
    else:
        report.likes.add(request.user)
        is_liked=True
    return HttpResponseRedirect(reverse('report_detail_url', kwargs={'id':report.id}))
