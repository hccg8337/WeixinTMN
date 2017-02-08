import sae
from WeixinTMN import wsgi

application = sae.create_wsgi_app(wsgi.application)