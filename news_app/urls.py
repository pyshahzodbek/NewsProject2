from  django.urls import path
from .views import new_list,news_detail,homepageViews,contactPageViews,tortPageViews,aboutPageviews

urlpatterns=[
    path('',homepageViews,name='home_page'),
    path('news',new_list,name='all_news_list'),
    path('news/<int:id>/',news_detail,name='news_detail_page'),
    path('contact-us/',contactPageViews,name='contact_page'),
    path('404/',tortPageViews,name='404_page'),
    path('about/',aboutPageviews,name='about_page')
]