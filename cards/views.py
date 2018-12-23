from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.forms.models import model_to_dict
from rest_framework import serializers

from .models import Page, Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('order', 'id', 'choice', 'correct')


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('order', 'id', 'question', 'choice_set')


class PageSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ('id', 'address', 'identifier', 'title', 'website', 'date_added', 'question_set')


def quiz_detail(request, shortname, identifier):
    obj = get_object_or_404(Page, website__shortname=shortname, identifier=identifier)
    serializer = PageSerializer(obj)
    return JsonResponse(serializer.data)
