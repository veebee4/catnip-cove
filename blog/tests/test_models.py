from django.test import TestCase
from blog.models import Category, Post, Comment


class CategoryModelTests(TestCase):

    def setUp(self):
        """ Set up a category instance for testing """
        self.category_name = 'Test Category'
        self.category = Category.objects.create(name=self.category_name)

    def test_category_str_method(self):
        """Test that the string representation
        of a category returns the category name"""
        self.assertEqual(str(self.category), self.category_name)


class PostModelTests(TestCase):

    def setUp(self):
        """ Set up a post instance for testing """
        self.category = Category.objects.create(name='Test Category')
        self.post_title = 'Test Post'
        self.post_body = 'This is the body of the test post.'
        self.post = (
            Post.objects.create(
                title=self.post_title,
                body=self.post_body
                )
        )
        self.post.categories.add(self.category)

    def test_post_str_method(self):
        """Test that the string representation
        of a post returns the post title"""
        self.assertEqual(str(self.post), self.post_title)

    def test_post_creation(self):
        """Test that the post is correctly created and saved"""
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.title, self.post_title)

        self.assertEqual(post.body, self.post_body)
        self.assertEqual(post.categories.count(), 1)
        self.assertEqual(post.categories.first(), self.category)

    def test_post_ordering(self):
        """Test that posts are ordered
        by the created_on field in descending order"""
        post_1 = Post.objects.create(title='Post 1', body='Body 1')
        post_2 = Post.objects.create(title='Post 2', body='Body 2')
        post_3 = Post.objects.create(title='Post 3', body='Body 3')

        posts = Post.objects.all()
        self.assertEqual(posts[0], post_3)  # Newest post should come first
        self.assertEqual(posts[1], post_2)
        self.assertEqual(posts[2], post_1)


class CommentModelTests(TestCase):

    def setUp(self):
        """ Set up a comment instance for testing """
        self.category = Category.objects.create(name='Test Category')
        self.post = (
            Post.objects.create(
                title='Test Post',
                body='This is a test post body.'
                )
        )
        self.comment_author = 'John Doe'
        self.comment_body = 'This is a test comment.'
        self.comment = (
            Comment.objects.create(
                author=self.comment_author,
                body=self.comment_body,
                post=self.post
                )
        )

    def test_comment_str_method(self):
        """Test that the string representation
        of a comment is in the format 'author on post'"""
        self.assertEqual(
            str(self.comment),
            f"{self.comment_author} on '{self.post}'"
        )

    def test_comment_creation(self):
        """Test that the comment is correctly created and saved"""
        comment = Comment.objects.get(id=self.comment.id)
        self.assertEqual(comment.author, self.comment_author)
        self.assertEqual(comment.body, self.comment_body)
        self.assertEqual(comment.post, self.post)
