from django.db.models.fields import return_None
from django.shortcuts import render,get_object_or_404,HttpResponse
from django.urls import reverse_lazy
from django.utils.text import slugify
from unicodedata import category

from .models import News,Category
from  .forms import ContactForm
from django.views.generic import TemplateView, ListView,CreateView,UpdateView,DeleteView


# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context={
        'news_list':news_list
    }
    return render(request,'news/news_list.html',context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    # To‘g‘ri ishlatish
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)


def homepageViews(request):
    news_list=News.published.all().order_by("-publish_time")[:10]
    categories=Category.objects.all()
    main_local_news=News.published.filter(category__name="Mahalliy").order_by("-publish_time")[:1]
    local_news=News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[1:6]
    context={
        'news_list':news_list,
        'categories':categories,
        'main_local_news':main_local_news,
        'local_news':local_news

    }

    return render(request,'news/index.html',context)
class HomePageViews(ListView):
    template_name = 'news/index.html'
    model = News
    context_object_name = 'news'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        context['news_list']=News.published.all().order_by("-publish_time")[:5]
        context['mahalliy_xabarlar']=News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[:5]
        context['xorij_xabarlar']=News.published.all().filter(category__name="Xorij").order_by("-publish_time")[:5]
        context['sport_xabarlar']=News.published.all().filter(category__name="Sport").order_by("-publish_time")[:5]
        context['texnologiya_xabarlar']=News.published.all().filter(category__name="Texnologiya").order_by("-publish_time")[:5]
        return context
# def contactPageViews(request):
#
#     form=ContactForm(request.POST or None)
#     if request.method== "POST" and form.is_valid():
#         form.save()
#         return HttpResponse(" <h2> Biz bilan bog'langaniz uchun tashakkur!")
#     context={
#         'form':form
#     }
#     return render(request,'news/contact.html',context)
class ContactPageViews(TemplateView):
    template_name = 'news/contact.html'

    def get(self,request,*args,**kwargs):
        form=ContactForm()
        context={
            'form':form
        }
        return render(request,'news/contact.html',context)

    def post(self,request,*args,**kwargs):
        form=ContactForm(request.POST)
        if   request.method=='POST' and form.is_valid():
           form.save()
           return HttpResponse("<h2> Biz bilan bog'langaniz uchun tashakkur!")
        context={
            'form':form
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
class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news=self.model.published.all().filter(category__name="Mahalliy")
        return news

class ForignNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Xorij")
        return news

class TechnologiyaNewsView(ListView):
    model = News
    template_name = 'news/texnologiya.html'
    context_object_name = 'texnologik_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Texnologiya")
        return news
class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Sport")
        return news

class UpdateViews(UpdateView):
    model = News
    fields = ('title','body','image','category','status',)
    template_name = 'crud/news_edit.html'

class DeleteViews(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')

class NewsCreateViews(CreateView):
    model = News
    template_name = 'crud/create_news.html'
    fields = ('title','slug','body','image','category','status')
