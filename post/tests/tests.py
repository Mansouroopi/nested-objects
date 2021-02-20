from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from post.models import BlogPost as Post, Tag
from django.contrib.auth.models import User


class PostListCreateAPIView(APITestCase):
    def setUp(self) -> None:
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")
        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        # self.url = reverse('api-post-list', kwargs={'version': 'v1'})
        self.url = reverse('api-post-list')

    def test_create_post(self):
        self.assertEquals(
            Post.objects.count(),
            0
        )
        data = {
            'title': "some title",
            'text': "some Text"
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Post.objects.count(),
            1
        )
        post = Post.objects.first()
        self.assertEquals(
            post.title,
            data['title']
        )
        self.assertEquals(
            post.text,
            data['text']
        )

    def test_get_post_list(self):
        tag = Tag(name="Python")
        tag.save()
        self.assertEquals(
            Tag.objects.count(),
            1
        )
        post = Post(
            title='TDD in DRF',
            text="introduction to TDD in DRF..."
        )
        post.save()
        post.tags.add(tag)
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        response_json = response.json()
        self.assertEquals(
            len(response_json),
            1
        )
        data = response_json[0]
        print(data['tags'])
        self.assertEquals(
            post.title,
            data['title']
        )
        self.assertEquals(
            post.text,
            data['text']
        )
        # self.assertEquals(
        #     data['tags'][0]['name'],
        #     tag.name
        # )


class PostDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")
        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.post = Post(title='mansour', text='mansour reviewing tdd')
        self.post.save()
        self.url = reverse('api-post-details', kwargs={'pk': self.post.pk})

    def test_get_post_details(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        # print(data)
        self.assertEquals(
            data['id'],
            self.post.id
        )
        self.assertEquals(
            self.post.title,
            data['title']
        )
        self.assertEquals(
            self.post.text,
            data['text']
        )

    def test_update_post(self):
        response = self.client.get(self.url)
        data = response.json()
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data['title'] = 'new mansour title'
        data['text'] = 'new mansour text'
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.post.refresh_from_db()
        self.assertEquals(
            self.post.title,
            data['title']
        )
        self.assertEquals(
            self.post.text,
            data['text']
        )

    def test_delete_post(self):
        self.assertEquals(
            Post.objects.count(),
            1
        )
        response = self.client.delete(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEquals(
            Post.objects.count(),
            0
        )