from ._base import *
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}
