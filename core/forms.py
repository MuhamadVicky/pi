from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

class MyUserCreationForm(UserCreationForm):
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.is_staff = True
            user.save()
            g = Group.objects.get(name='user')
            g.user_set.add(user)
        return user

