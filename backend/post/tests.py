from rest_framework import status
from rest_framework.test import APIClient

from backend.auth_jwt.tests import BaseTestClass, create_user
from .models import Post
from .serializers import PostSerializer


class TestPostResource(BaseTestClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.endpoint = '/api/v1/posts/'

    def setUp(self):
        super().setUp()
        self.post = Post.objects.create(
            author=self.base_user,
            title='title1',
            text='text1'
        )
        Post.objects.create(
            author=create_user('new@email.com'),
            title='title 2',
            text='text2'
        )
        self.new_post = {
            'title': 'title 3',
            'text': 'text3'
        }
        self.third_post = {
            'title': 'title 4',
            'text': 'text 4'
        }

    def test_get_all_posts(self):
        resp = self.client.get(self.endpoint)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_all_posts_no_token(self):
        unknown_user = APIClient()
        resp = unknown_user.get(self.endpoint)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_post_success(self):
        resp = self.client.post(self.endpoint, self.new_post)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp.json(), {'id': Post.objects.last().id})
        self.assertEqual(Post.objects.count(), 3)

    def test_update_post(self):
        resp = self.client.post(f'{self.endpoint}{self.post.id}/')
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_posts_no_token(self):
        unknown_user = APIClient()
        resp = unknown_user.post(self.endpoint)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_post_duplicate_title(self):
        self.new_post['title'] = 'title 2'
        resp = self.client.post(self.endpoint, self.new_post)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            resp.json(),
            {'title': ['post with this title already exists.']}
        )

    def test_create_post_without_text(self):
        self.new_post['text'] = ''
        resp = self.client.post(self.endpoint, self.new_post)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            resp.json(),
            {'text': ['This field may not be blank.']}
        )

    def test_create_post_without_title(self):
        self.new_post['title'] = ''
        resp = self.client.post(self.endpoint, self.new_post)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            resp.json(),
            {'title': ['This field may not be blank.']}
        )

    def test_get_post_unauth(self):
        unknown_user = APIClient()
        resp = unknown_user.get(f'{self.endpoint}{self.post.id}/')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_post_success(self):
        resp = self.client.get(f'{self.endpoint}{self.post.id}/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        expected = PostSerializer(
            Post.objects.get(pk=self.post.pk)).data
        self.assertEqual(resp.json(), expected)

