from rest_framework import status
from rest_framework.test import APIClient

from backend.auth_jwt.tests import BaseTestClass
from backend.post.models import Post
from .models import Vote


class TestPostResource(BaseTestClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.endpoint = '/api/v1/votes/'

    def setUp(self):
        super().setUp()
        self.post = Post.objects.create(
            author=self.base_user,
            title='Some title',
            text='Some text'
        )

    def test_create_vote_success(self):
        resp = self.client.post(self.endpoint, {'post': self.post.pk})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vote.objects.count(), 1)
        self.assertEqual(resp.json(), 'success')

    def test_create_vote_no_token(self):
        anonimus = APIClient()
        resp = anonimus.post(self.endpoint)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unvote_success(self):
        resp = self.client.post(self.endpoint, {'post': self.post.pk})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vote.objects.count(), 1)

        resp = self.client.post(self.endpoint, {'post': self.post.pk})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(Vote.objects.count(), 0)
