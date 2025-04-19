from  django.urls import path
from .views import news_list,news_detail,HomePageViews,ContactPageViews,tortPageViews,aboutPageviews,SportNewsView,LocalNewsView,TechnologiyaNewsView,ForignNewsView,UpdateViews,DeleteViews,NewsCreateViews


urlpatterns=[
    path('',HomePageViews.as_view(),name='home_page'),
    path('news',news_list,name='all_news_list'),
    path('news/create/',NewsCreateViews.as_view(),name='create_news'),
    path('news/<slug:news>/',news_detail,name='news_detail_page'),
    path('news/<slug>/edit/',UpdateViews.as_view(),name='news_update'),
    path('news/<slug>/delete/',DeleteViews.as_view(),name='news_delete'),
    path('contact-us/',ContactPageViews.as_view(),name='contact_page'),
    path('404/',tortPageViews,name='404_page'),
    path('about/',aboutPageviews,name='about_page'),
    path('local/',LocalNewsView.as_view(),name='local_news_page'),
    path('foreign/',ForignNewsView.as_view(),name='foreign_news_page'),
    path('technology/',TechnologiyaNewsView.as_view(),name='technology_news_page'),
    path('sport/',SportNewsView.as_view(),name='sport_news_page'),
]