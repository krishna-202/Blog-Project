from django.urls import path
from Blog_App import views

urlpatterns=[
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
]
