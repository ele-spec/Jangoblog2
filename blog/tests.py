# Jangoblog2/blog/tests.py

from django.test import TestCase
# Припустимо, у вас є модель Post у blog/models.py
from .models import Post

class PostModelTest(TestCase):
    def test_post_creation(self):
        # Створюємо тестовий об'єкт Post
        post = Post.objects.create(
            title="Тестовий Заголовок",
            content="Це тестовий контент для статті блогу."
        )
        # Перевіряємо, чи коректно створено об'єкт
        self.assertEqual(post.title, "Тестовий Заголовок")
        self.assertEqual(post.content, "Це тестовий контент для статті блогу.")
        self.assertIsNotNone(post.created_at) # Перевіряємо, що дата створення не None

    # Можете додати більше тестів, наприклад, для URL-ів або в'юшок
    # from django.urls import reverse
    # def test_post_list_view(self):
    #     response = self.client.get(reverse('post_list')) # Замініть 'post_list' на ваш фактичний URL-pattern name
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/post_list.html') # Замініть на ваш фактичний шаблон
