from django.core.management import BaseCommand

from authapp.models import ShopUser, ShopUserProfile


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for user in ShopUser.objects.all():
            #if not user.shopuserprofile:
            user_profile = ShopUserProfile.objects.create(user=user)
