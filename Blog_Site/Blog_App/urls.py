from django.urls import path
from Blog_App import views

urlpatterns=[
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<str:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('drafts/',views.DraftListView.as_view(),name='draft_list'),
    path('post/publish/<str:pk>',views.post_publish,name='post_publish'),
    path('comment/approve/<str:pk>',views.comment_approve,name='comment_approve'),
    path('comment/remove/<str:pk>',views.comment_remove,name='comment_remove'),
    path('post/create/',views.CreatePostView.as_view(),name='post_new'),
    path('post/update/<str:pk>',views.UpdatePostView.as_view(),name='post_edit'),
    path('post/delete/<str:pk>',views.DeletePostView.as_view(),name='post_delete'),
    path('post/addcomment/<str:pk>',views.add_comment_to_post,name='add_comment'),
]
