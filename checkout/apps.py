""" imports below """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ override ready method and import signals module """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """ ready function """
        import checkout.signals
