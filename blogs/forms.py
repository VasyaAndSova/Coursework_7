from django.core.exceptions import ValidationError
from django.forms import ModelForm

from blogs.models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content", "image", "is_published"]

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update({"class": "form-control", "placeholder": "Введите заголовок блога"})
        self.fields["content"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите содержимое блога"}
        )
