# logging_demo

#### 1.配置 LOGGING
```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGGING_URL = os.path.join(BASE_DIR, 'logs')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            # {lineno:3} 里的 :3 表示至少显示3格，{levelname:7} 同理 
            # 详见 https://docs.python.org/3/library/logging.html#logrecord-attributes
            'format': '{asctime} {module}.{funcName} {lineno:3} {levelname:7} => {message}',
            # 这里 style 选择 { ，是指 {asctime} 这种形式。
            # 如果选择 % ，则是 %(asctime)s 这种形式。
            # 还有一种选择，是 $ ，是 $asctime 或 ${asctime} 这种形式。
            # 详见 https://docs.python.org/3/howto/logging-cookbook.html#use-of-alternative-formatting-styles。
            'style': '{',
            # 可以配置时间格式
            # 'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'verbose',
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
        # 处理我们自己写的 log
        '': {
            'handlers': ['console', 'file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        # 处理 django 自己打印的 log
        'django': {
            'handlers': ['console', 'file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            # 设置 False 时不会再向上广播，也就是这条 log 不会再发送给 'django' 的上级 '' 处理，
            # 使得 django 自己的 log 都在 'django' 处理，而我们自己写的 log 就会在 '' 处理
            'propagate': False,
        },
    },
}
```

####  2.配置 LOGGING 发送邮件
```python
import os

# 配置邮件
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.qq.com'  # 如果是 163 改成 smtp.163.com
EMAIL_PORT = 465
EMAIL_HOST_USER = 'your_account@qq.com'  # 帐号
EMAIL_HOST_PASSWORD = "your_password"  # 授权码（****）
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = EMAIL_HOST_USER  # 邮箱账号

ADMINS = (
    ('bugs', EMAIL_HOST_USER),
)

# 配置 LOGGING
LOGGING = {
    # 以下省略不重要配置
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'email_backend': 'django.core.mail.backends.smtp.EmailBackend',
            'include_html': True,
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

####  3.使用 LOGGING
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
