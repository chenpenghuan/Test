import django
class AddForm(django.forms.Form):
    a = django.forms.IntegerField()
    b = django.forms.IntegerField()
