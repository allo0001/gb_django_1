from django.conf import settings
from django.db import models

class Order(models.Model):
    STATUS_FORMING = 'FM'
    STATUS_SEN_TO_PROCEED = 'STP'
    STATUS_PROCEEDED = 'PRD'
    STATUS_PAID = 'PD'
    STATUS_CANCEL = 'CNL'
    STATUS_DONE = 'DN'

    STATUSES = {
        (STATUS_FORMING, 'формируется'),
        (STATUS_SEN_TO_PROCEED, 'отправлено в обработку'),
        (STATUS_PROCEEDED, 'обработано'),
        (STATUS_PAID, 'оплачено'),
        (STATUS_CANCEL, 'отменено'),
        (STATUS_DONE, 'завершено'),
    }

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES)