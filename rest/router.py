from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('owner', views.OwnerViewSet)
router.register('website', views.WebsiteViewSet)
router.register('page', views.PageViewSet)
router.register('question', views.QuestionViewSet)
router.register('choice', views.ChoiceViewSet)
router.register('answer', views.AnswerViewSet)
