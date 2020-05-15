from django.shortcuts import render
from .models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from home.models import Book, Person
from django.db.models.signals import post_save, class_prepared
from django.dispatch import receiver
from requests.exceptions import HTTPError

# Create your views here.
def cabinet(request):
	human = get_object_or_404(User, id=request.user.id)
	written = Book.objects.filter(author_name_id=request.user.id)
	read = get_object_or_404(Person, user_id=request.user.id).read.all
	return render(request, "cabinet/cabinet.html", {"human": human, "written": written, "read": read})

def addbook(request, book_id):
	print(1)
	book = get_object_or_404(Book, id=book_id)
	user = get_object_or_404(Person, user_id=request.user.id) #Защита от незареганных 
	user.read.add(book)
	return redirect(f"/book/{book_id}")


@receiver(post_save, sender = User)
def add_person(instance, **kwargs):
	try:
		person = get_object_or_404(Person, user_id=instance.id) # Если не найдено намерено вызывается ошибка 404
	except:
		person = Person()
		person.user_id = instance.id
		person.save()