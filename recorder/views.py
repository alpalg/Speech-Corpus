from django.shortcuts import render
from . models import Participant, Phrase, Audio
from django.views.decorators.csrf import csrf_exempt
from .forms import ParticipantForm
from django.shortcuts import redirect



def index(request):
    form = ParticipantForm()
    if request.POST:
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            return redirect(fill_form)
    context = {'form': form}
    return render(request, 'recorder/index.html', context)


def finish(request):
    return render(request, 'recorder/finish.html')


def fill_form(request):
    return render(request, 'recorder/fill_form.html')


def russian_speech(request):
    participant = Participant.objects.filter(surname=request.COOKIES['surname']).last()
    text = Phrase.objects.get(pk=participant.russian_progress)
    number_of_phrases = Phrase.objects.filter(phrase_language='Russian').count()
    if participant.russian_progress > Phrase.objects.filter(phrase_language='Russian').count():
        return redirect(english_speech)

    context = {'text': text,
               'counter': participant.russian_progress,
               'number_of_phrases': number_of_phrases,
               'id': participant.russian_progress,
               }
    return render(request, 'recorder/russian_speech.html', context)


def english_speech(request):
    participant = Participant.objects.filter(surname=request.COOKIES['surname']).last()
    counter = participant.english_progress
    if counter == Phrase.objects.filter(phrase_language='English').count():
        return redirect(finish)

    text = Phrase.objects.get(pk=counter + Phrase.objects.filter(phrase_language='Russian').count()+1)
    number_of_phrases = Phrase.objects.filter(phrase_language='English').count()

    context = {'text': text,
               'counter': counter,
               'number_of_phrases': number_of_phrases,
               'id': counter,
               }
    return render(request, 'recorder/english_speech.html', context)


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        participant = Participant.objects.filter(surname=request.COOKIES['surname']).last()
        gender = participant.gender
        surname = participant

        audio_title = participant.surname + '_'+str(participant.russian_progress + participant.english_progress) + '_' + str(gender)
        phrase_id = Phrase.objects.get(pk=participant.russian_progress + participant.english_progress)
        audio_file = request.FILES.get('data')

        a = Audio.objects.create(surname=surname, audio_title=audio_title, phrase_id=phrase_id, audio_file=audio_file)
        a.save()
        print(participant.russian_progress)
        if (participant.russian_progress + participant.english_progress) <= Phrase.objects.filter(phrase_language='Russian').count():
            participant.russian_progress += 1
        else:
            participant.english_progress += 1
        participant.save()
        print(participant.russian_progress)

        # if participant.russian_progress > Phrase.objects.filter(phrase_language='Russian').count():
        #     return redirect(english_speech)
        # elif participant.russian_progress + participant.english_progress > Phrase.objects.all().count():
        #     return redirect(finish)
        # else:
        #     return redirect(russian_speech)


def redirect_to_recording(request):
    participant = Participant.objects.filter(surname=request.COOKIES['surname']).last()
    if participant.russian_progress > Phrase.objects.filter(phrase_language='Russian').count():
        return redirect(english_speech)
    elif participant.russian_progress + participant.english_progress > Phrase.objects.all().count():
        return redirect(finish)
    else:
        return redirect(russian_speech)
