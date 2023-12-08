#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def setUp(self):
        """Set up method to prepare test environment"""
        self.review = Review()

    def tearDown(self):
        """Tear down method to clean up test environment"""
        del self.review

    def test_place_id_attribute(self):
        """Test the existence and type of place_id attribute"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertIsInstance(self.review.place_id, str)
        self.assertEqual(self.review.place_id, "")

    def test_user_id_attribute(self):
        """Test the existence and type of user_id attribute"""
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertIsInstance(self.review.user_id, str)
        self.assertEqual(self.review.user_id, "")

    def test_text_attribute(self):
        """Test the existence and type of text attribute"""
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertIsInstance(self.review.text, str)
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Test if Review class inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_init_method(self):
        """Test the __init__ method"""
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict() method"""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('__class__', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(datetime.strptime(review_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertIsInstance(datetime.strptime(review_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertEqual(review_dict['place_id'], "")
        self.assertEqual(review_dict['user_id'], "")
        self.assertEqual(review_dict['text'], "")


if __name__ == '__main__':
    unittest.main()
