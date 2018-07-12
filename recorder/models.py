from django.db import models
import os
from django.shortcuts import render

from django import forms
# Create your models here.


# class Audio(models.Model):
#     surname = models.CharField(max_length=250)
#     gender = models.CharField(max_length=12)
#     result = models.FileField(upload_to='audio/')
#
#     def __str__(self):
#         return self.surname.title() + '-' + self.gender.title()
#
#
# class RussianText(models.Model):
#     russian_text = models.CharField(max_length=10000)
#     was_read = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.russian_text
#
#     def __getitem__(self, item):
#         return RussianText.russian_text_box[item]
#
#     def __len__(self):
#         return len(RussianText.russian_text_box)
#
#
# class EnglishText(models.Model):
#     english_text = models.CharField(max_length=10000)
#     was_read = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.english_text
#
#     def __getitem__(self, item):
#         return EnglishText.english_text_box[item]
#
#     def __len__(self):
#         return len(EnglishText.english_text_box)


########## New models ####################################################

def content_file_name(instance, filename):
    ext = 'waw'
    filename = "%s.%s" % (instance.audio_title, ext)
    final_path = os.path.join('audio/', instance.get_surname())
    if not os.path.exists(final_path):
        os.makedirs(final_path)
    return os.path.join(instance.get_surname(), filename)


class Participant(models.Model):
    surname = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    russian_progress = models.IntegerField(default=1)
    english_progress = models.IntegerField(default=0)

    def __str__(self):
        return self.surname


class Phrase(models.Model):
    phrase = models.TextField(max_length=1000)
    phrase_language = models.CharField(max_length=10)

    def __str__(self):
        return self.phrase


class Audio(models.Model):
    surname = models.ForeignKey(Participant, on_delete=models.CASCADE)
    audio_title = models.CharField(max_length=250)
    phrase_id = models.ForeignKey(Phrase, on_delete=models.PROTECT)
    recording_date = models.DateTimeField(auto_now=True)
    audio_file = models.FileField(upload_to=content_file_name, max_length=70000)

    def __str__(self):
        return self.audio_title + str(self.recording_date)

    def get_surname(self):
        return str(self.surname.surname.title())

