from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag = False
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                if main_tag is True:
                    raise ValidationError('Только один тег может быть главным')
                else:
                    main_tag = True
        if main_tag is False:
            raise ValidationError('Добавьте основной тег')
        return super().clean()  # вызываем базовый код переопределяемого метода

            
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'published_at']
    inlines=[ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name']
    inlines=[ScopeInline]