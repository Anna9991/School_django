from django.shortcuts import render, redirect
from .models import Teacher, Faq, Lesson, Review
from .forms import QuestionForm, ReviewForm
import telegram
from asgiref.sync import AsyncToSync


BOT_TOKEN = ''
CHAT_ID = 874580719


async def send_telegram_message(name, email, subject, message):
    bot = telegram.Bot(token=BOT_TOKEN)
    text = f"📬 Новое сообщение с сайта:\n\n" \
           f"Имя: {name}\n" \
           f"Email: {email}\n" \
           f"Тема: {subject}\n" \
           f"Сообщение: {message}"
    await bot.send_message(chat_id=CHAT_ID, text=text)


# Create your views here.
def index(request):
    reviews = Review.objects.all()
    for review in reviews:
        review.stars_range = range(review.stars)
        review.empty_stars_range = range(5 - review.stars)
    return render(request, "index.html", {'reviews': reviews})


def about(request):
    teachers = Teacher.objects.all()
    return render(request, "about.html", {"teachers_obj": teachers})


def classes(request):
    lessons = Lesson.objects.all()
    return render(request, "classes.html", {"lessons_obj": lessons})


def faq(request):
    questions = Faq.objects.all()
    return render(request, "faq.html", {"questions_obj": questions})


def contacts(request):
    question_form = QuestionForm(prefix='question') 
    review_form = ReviewForm(prefix='review')

    if request.method == 'POST':
        if 'submit_question' in request.POST:
            question_form = QuestionForm(request.POST, prefix='question')
            if question_form.is_valid():
                name = question_form.cleaned_data['name']
                email = question_form.cleaned_data['email']
                subject = question_form.cleaned_data['subject']
                message = question_form.cleaned_data['message']
                print(name, email, subject, message)

                AsyncToSync(send_telegram_message)(name, email, subject, message)

                return redirect('contacts')

        if 'submit_review' in request.POST:
            review_form = ReviewForm(request.POST, prefix='review')
            if review_form.is_valid():
                # review_name = review_form.cleaned_data['name']
                # review_review = review_form.cleaned_data['review']
                # review_stars = review_form.cleaned_data['stars']
                review_form.save()
                return redirect('index')

    return render(request, "contacts.html", {'question_form': question_form, 'review_form': review_form})