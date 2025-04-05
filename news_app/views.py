from django.db.models.fields import return_None
from django.shortcuts import render,get_object_or_404
from .models import News,Category

# Create your views here.

def new_list(request):
    new_list = News.objects.filter(status=News.Status.Published)

    context={
        'new_list':new_list
    }
    return render(request,'news/news_list.html',context)

def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    # To‘g‘ri ishlatish
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)


def homepageViews(request):
    news=News.published.all()
    categories=Category.objects.all()
    context={
        'news':news,
        'categories':categories
    }

    return render(request,'news/index.html',context)
def contactPageViews(request):
    context={

    }
    return render(request,'news/contact.html',context)
def tortPageViews(request):
    context={

    }
    return render(request,'news/404.html',context)

def aboutPageviews(request):
    context={

    }
    return render(request,'news/single_page.html',context)
