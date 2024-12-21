from django import forms
from .models import Member, Book, Copy, IssuedBook

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CopyForm(forms.ModelForm):
    class Meta:
        model = Copy
        fields = '__all__'

class UpdateMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['address', 'email', 'phone_no', 'account_no']