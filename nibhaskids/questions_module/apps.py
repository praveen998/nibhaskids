from django.apps import AppConfig
from django.core.cache import cache

cache.set('question_path','media/questions/question_images/',timeout=None)
cache.set('option_path','media/questions/options/',timeout=None)
cache.set('answer_path','media/questions/answers/',timeout=None)
cache.set('image_number',100,timeout=None)


class QuestionsModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'questions_module'
