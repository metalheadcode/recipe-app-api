# kat sini kita nak tulis apa code yang akan execute dalam shell nanti
# mcm biasa TestCase were using in this sessions
# so docker-compose akan surun manage.py execute dari test ni
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        test creating a new user with an email is
        test_create_user_with_email_successful
        """

        email = 'test@gmail.com'
        password = '092100027h'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        test the email for a new user is test_new_user_email_normalized
        """
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, '092100027h')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        test creating user with no email raise error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '092100027h')

    def test_create_new_superuser(self):
        """
        Test creating a new is_superuser
        """
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            '092100027h'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
