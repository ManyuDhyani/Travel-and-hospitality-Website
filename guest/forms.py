from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Articles
		fields = '__all__'
		exclude = ['category', 'slug', 'published_on', 'updated', 'status']

class sendmail(forms.Form):
	Name = forms.CharField(max_length=50, label='Name', required=False)
	Email = forms.EmailField(label='Email')
	Mobile = forms.CharField(max_length=15, label='Mobile', required=False)
	Msg = forms.CharField(widget=forms.Textarea, label='Msg')




class CustomerForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    OPTIONS = (
        ("Rock climbing", "Rock climbing"),
        ("Abseiling/Rappelling", "Abseiling/Rappelling"),
        ("Canyoning", "Canyoning"),
        ("Slacklining ", "Slacklining"),
    )
    
    NOTIFY = (
        ("WhatsApp", "WhatsApp"),
        ("Call", "Call"),
        ("SMS", "SMS"),
    )
    
    Activities = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS, required=False)
    notify_on = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=NOTIFY, required=False)
    class Meta:
        model = Customer
        fields = '__all__'



class Upcoming_Event_CustomerForm(forms.ModelForm):
    NOTIFY = (
        ("WhatsApp", "WhatsApp"),
        ("Call", "Call"),
        ("SMS", "SMS"),
    )

    notify_on = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=NOTIFY, required=False)

    class Meta:
        model = Event
        fields = '__all__'

"""
class FeedbackForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    email = forms.EmailField()
    body = forms.CharField(max_length=245, label="Write a review.", widget=forms.Textarea)

    class Meta:
        model = Feedback
        fields = ('name', 'gender', 'email', 'body')


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('image', )
"""