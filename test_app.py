from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class GymManagementTests(TestCase):

    def setUp(self):
        """Налаштування тестового середовища: створюємо адміністратора"""
        self.client = Client()
        self.admin_user = User.objects.create_superuser(username="admin", password="admin")

    def test_admin_login(self):
        """Перевіряє, чи адміністратор може увійти з логіном admin/admin"""
        login_successful = self.client.login(username="admin", password="admin")
        self.assertTrue(login_successful, "❌ Не вдалося увійти адміністратору")

    def test_index_page(self):
        """Перевіряє, чи відкривається головна сторінка"""
        response = self.client.get(reverse("index"))  # Переконайтеся, що у вас є `name='index'` в `urlpatterns`
        self.assertEqual(response.status_code, 200, "❌ Головна сторінка не відкривається")

