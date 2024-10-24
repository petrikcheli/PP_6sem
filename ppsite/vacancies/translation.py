# vacancies/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import Vacancies

@register(Vacancies)
class VacanciesTranslationOptions(TranslationOptions):
    fields = ('name', 'body') 