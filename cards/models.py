from django.db import models
from django.contrib.auth import get_user_model
from ordered_model.models import OrderedModel


class Owner(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__()


class Website(models.Model):
    name = models.CharField(max_length=254)
    shortname = models.SlugField(max_length=50)
    address = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shortname


# class Domain(models.Model):
#     """ Approved domains for loading a publication """
#     domain = models.URLField()
#     website = models.ForeignKey(Website, on_delete=models.CASCADE)


class Page(models.Model):
    address = models.URLField()
    title = models.CharField(max_length=254)
    identifier = models.CharField(max_length=50)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Question(OrderedModel):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    question = models.TextField()
    # is_approved = models.BooleanField(default=False)
    # is_archived = models.BooleanField(default=False)
    # submitted_by = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True,  on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)
    order_with_respect_to = 'page'

    def __str__(self):
        return self.question[:50]
    
    class Meta:
        ordering = ('order',)


class Choice(OrderedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.TextField()
    correct = models.BooleanField(default=False)
    order_with_respect_to = 'question'

    def __str__(self):
        return self.choice[:50]
    
    class Meta:
        ordering = ('order',)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)
    correct = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.__str__()
