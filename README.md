# logging_demo

### 1.配置 LOGGING
```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGGING_URL = os.path.join(BASE_DIR, 'logs')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {module}.{funcName} {lineno:3} {levelname:7} => {message}',
            'style': '{',
            # 可以配置时间格式
            # 'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'email_backend': 'django.core.mail.backends.smtp.EmailBackend',
            'include_html': True,
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOGGING_URL, 'django.log'),
            'maxBytes': 4194304,  # 4 MB
            'backupCount': 10,
            'level': 'DEBUG',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file', 'mail_admins'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        'django': {
            'handlers': ['console', 'file', 'mail_admins'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}
```

### 2.使用 LOGGING
```python
import logging

from django.views.generic import ListView

from app1.models import App1

# 获取 logger
logger = logging.getLogger(__name__)


class App1ListView(ListView):
    model = App1
    template_name = 'app1/app1-list.html'

    def get(self, request, *args, **kwargs):
        logger.debug('(%s)开始执行 App1ListView get 方法', 'DEBUG')
        logger.info('(%s)开始执行 App1ListView get 方法', 'INFO')
        logger.warning('(%s)开始执行 App1ListView get 方法', 'WARNING')

        try:
            _ = 1 / 0
        except Exception as e:
            # 可以显示报错信息
            logger.error('(%s)开始执行 App1ListView get 方法', 'ERROR', exc_info=e)
            logger.critical('(%s)开始执行 App1ListView get 方法', 'CRITICAL')

        return super(App1ListView, self).get(request, *args, **kwargs)
```
