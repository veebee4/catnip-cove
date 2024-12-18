from django import forms
from .widgets import CustomClearableFileInput
from .models import Post, Comment, Category


class BlogForm(forms.ModelForm):

    new_category = forms.CharField(
        max_length=100,
        required=False,
        label="New Category (optional)",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a new category"}),
    )

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-control"}),
    )
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'image', 'categories', 'new_category']

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        posts = Post.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        new_category = cleaned_data.get('new_category')

        # Create a new category if the user entered a new category name
        if new_category:
            # Check if the category already exists to avoid duplication
            category, created = Category.objects.get_or_create(name=new_category)
            if created:
                cleaned_data['categories'] = [category]  # Add the new category to the post's categories
            else:
                self.add_error('new_category', 'This category already exists.')
        return cleaned_data


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )
