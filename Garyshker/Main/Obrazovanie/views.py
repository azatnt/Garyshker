from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.urls import reverse
from .forms import *
from django.views.generic import View
from django.db.models import F
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Count





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
            'item': item
        }
        return render(request, self.template, context)


class SearchFieldReport(View):
    model = Report
    template = 'obrazovanie/search_report.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            search_report = request.POST['search_report']
        else:
            search_report = ''
        report = self.model.objects.filter(title__icontains=search_report)
        context = {
            'report': report
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
    item = Item.objects.get(id=id)
    item.views = item.views + 1
    item.save()
    return render(request, 'obrazovanie/item_detail.html', context={'item': item})



def all_reports(request):
    reports = Report.objects.filter(moderation=True)
    # reports = Report.objects.all()
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
    genre_all = Genre.objects.all()
    popular_post = Report.objects.annotate(like_report=Count('likes')).order_by('-like_report')[:4]
    # popular_post_comment = Comment.objects.filter(report = popular_post[0], reply=None)
    is_liked = False
    if report.likes.filter(id=request.user.id).exists():
        is_liked=True


    is_favourite=False
    if report.favourite.filter(id=request.user.id).exists():
        is_favourite=True

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
        'is_favourite': is_favourite,
        'comments': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
        'genre_all': genre_all,
        'popular_post': popular_post,
        # 'popular_post_comment': popular_post_comment



    }

    if request.is_ajax():
        html = render_to_string('obrazovanie/comments.html', context, request=request)
        return JsonResponse({'form':html})

    return render(request, 'obrazovanie/report_detail.html', context)


def genre_detail_report(request, slug):
    genre_all = Genre.objects.all()
    genre = Genre.objects.filter(slug=slug)

    return render(request, 'obrazovanie/genre_detail_report.html', context={'genre': genre, 'genre_all':genre_all})




def like_report(request):
    # report = Report.objects.get(id=request.POST.get('report_id'))
    report = Report.objects.get(id=request.POST.get('id'))
    is_liked = False
    if report.likes.filter(id=request.user.id).exists():
        report.likes.remove(request.user)
        is_liked=False
    else:
        report.likes.add(request.user)
        is_liked=True

    context = {
        'report': report,
        'is_liked': is_liked

    }
    if request.is_ajax():
        html = render_to_string('obrazovanie/like_section.html', context, request=request)
        return JsonResponse({'form':html})
    # return HttpResponseRedirect(reverse('report_detail_url', kwargs={'id':report.id}))


def report_create(request):
    if request.method == 'POST':
        form = ReportCreateForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save()
            report.author = request.user
            report.save()
            # if report.status == 'READY':
            #
            #
            return HttpResponseRedirect(reverse('after_writing_post_url'))
    else:
        form = ReportCreateForm()
    return render(request, 'obrazovanie/report_create.html', context={'form':form})



def after_writing_post(request):
    return render(request, 'obrazovanie/after_writing_post.html')



def comment_delete(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
