from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Setting up review form """
    class Meta:
        """ Fields to be shown in form """
        model = Review
        fields = ('title', 'body', 'image', 'posted_by',)

    def __init__(self, *args, **kwargs):
        """
        Add place holders, remove auto generated labels and
        set auto focus to first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Review Title',
            'body': 'Review Body',
            'image': 'Optional Image',
            'posted_by': 'Reviewed By...'
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-orange rounded orange'
            self.fields[field].label = False
