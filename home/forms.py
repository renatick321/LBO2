from .models import Book, Chapter, Comment
from django import forms


class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'image', "description", "price", "tags", "genres"]


class ChapterForm(forms.ModelForm):
	class Meta:
		model = Chapter
		fields = ['title', 'text']


class CommentForm(forms.Form):
	comment_text = forms.CharField(widget=forms.Textarea)