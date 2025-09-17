from django.contrib.auth import get_user_model
from django.test import TestCase

class UsersManagerTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',    
            email='testuser@example.com',
            password='testpass123',
            phone='1234567890'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertEqual(user.phone, '1234567890')
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser) 
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='adminuser',   
            email='testsuperuser@example.com',
            password='adminpass123',
            phone='0987654321'
        )
        self.assertEqual(admin_user.username, 'adminuser')
        self.assertEqual(admin_user.email, 'testsuperuser@example.com')
        self.assertTrue(admin_user.check_password('adminpass123'))
        self.assertEqual(admin_user.phone, '0987654321')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)    
