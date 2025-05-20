# blog/tests.py
from django.test import TestCase
from django.urls import reverse
from blog.models import Post

class PostModelTest(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(title="Тестовий Заголовок", content="Це тестовий контент.")
        self.assertEqual(post.title, "Тестовий Заголовок")
        self.assertEqual(post.content, "Це тестовий контент.")
        self.assertIsNotNone(post.created_at)

class PostViewTest(TestCase):
    def setUp(self):
        self.client = TestCase().client # Створюємо клієнт для тестування в'юшок
        Post.objects.create(title="Мій Перший Пост", content="Дуже цікавий контент.")

    def test_post_list_view(self):
        # Припустимо, у вас є URL-шаблон з назвою 'post_list'
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Мій Перший Пост")
        self.assertTemplateUsed(response, 'blog/post_list.html') 

    def test_post_detail_view(self):
        post = Post.objects.get(title="Мій Перший Пост")
        # Припустимо, у вас є URL-шаблон з назвою 'post_detail' і він приймає PK
        response = self.client.get(reverse('post_detail', args=[post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Мій Перший Пост")
        self.assertContains(response, "Дуже цікавий контент.")
        self.assertTemplateUsed(response, 'blog/post_detail.html') 
