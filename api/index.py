
import sys
import os
from django.core.wsgi import get_wsgi_application

# Add project root to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# Point to Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Expose WSGI app for Vercel
app = get_wsgi_application()

