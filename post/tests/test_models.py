from django.test import TestCase
from post.models import BlogPost as Post, Tag


class PostTestCase(TestCase):
    def test_post(self):
        self.assertEquals(
            Post.objects.count(),
            0
        )
        Post.objects.create(
            title='active', text='text', is_active=True
        )
        Post.objects.create(
            title='another active', text='another text', is_active=True
        )
        self.assertEquals(
            Post.objects.count(),
            2
        )
        active_posts = Post.objects.filter(is_active=True)
        self.assertEquals(
            active_posts.count(),
            2
        )
        Post.objects.create(
            title='active', text='text', is_active=False
        )
        Post.objects.create(
            title='another active', text='another text', is_active=False
        )
        inactive_posts = Post.objects.filter(is_active=False)
        self.assertEquals(
            inactive_posts.count(),
            2
        )
        self.assertEquals(
            Post.objects.count(),
            4
        )


class TagTestCase(TestCase):
    def test_tag(self):
        self.assertEquals(
            Tag.objects.count(),
            0
        )
        Tag.objects.create(
            name='django rest frameworks'
        )
        Tag.objects.create(
            name='python best tutorial'
        )
        self.assertEquals(
            Tag.objects.count(),
            2
        )



