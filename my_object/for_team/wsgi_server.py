import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","for_team.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
#于主机test.py不同