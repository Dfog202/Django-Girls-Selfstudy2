from django import forms


class PostCreationForm(forms.Form):
    title = forms.CharField(
        label='제목',
        max_length=20,
        required=True,
    )
    text = forms.CharField(
        max_length=300,
        required=True,
    )