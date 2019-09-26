import logging

from django.views.generic import ListView

from app1.models import App1

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
        except ZeroDivisionError as e:
            # 可以显示报错信息
            logger.error('(%s)开始执行 App1ListView get 方法', 'ERROR', exc_info=e)
            logger.critical('(%s)开始执行 App1ListView get 方法', 'CRITICAL')

        return super(App1ListView, self).get(request, *args, **kwargs)
