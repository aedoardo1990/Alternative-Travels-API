from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):

    def setUp(self):
        User.objects.create_user(username='edo', password='pass')

    def test_can_list_posts(self):
        edo = User.objects.get(username='edo')
        Post.objects.create(owner=edo, title='test title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='edo', password='pass')
        response = self.client.post('/posts/', {'title': 'test title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'test title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):

    def setUp(self):
        edo = User.objects.create_user(username='edo', password='pass')
        john = User.objects.create_user(username='john', password='pass')
        Post.objects.create(
            owner=edo, title='title1', content='content1'
        )
        Post.objects.create(
            owner=john, title='title2', content='content2'
        )

    def test_can_retrieve_post_with_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'title1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_fetch_post_with_invalid_id(self):
        response = self.client.get('/posts/23/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_post(self):
        self.client.login(username='edo', password='pass')
        response = self.client.put('/posts/1/', {'title': 'new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_cant_update_someone_else_post(self):
        self.client.login(username='edo', password='pass')
        response = self.client.put('/posts/2/', {'title': 'new title'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
