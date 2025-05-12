import unittest
from url_shortener import create_app
from url_shortener.extensions import db
from url_shortener.models import Link

class TestURLShortener(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.app = create_app(config_dict={
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'SQLALCHEMY_TRACK_MODIFICATIONS': False,
            'SECRET_KEY': 'k)$2uP+dMLw+?|F',
        })
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
    
    def tearDown(self):
        """Clean up after tests."""
        with self.app.app_context():
            db.session.remove()
            db.engine.dispose()
            db.drop_all()

    def test_create_short_url(self):
        response = self.client.post('/create_link', data={
            'original_url': 'https://google.com', 'custom_id': 'gogo'
        })
        self.assertEqual(
            response.status_code,
            200,
            msg=f"Response status: {response.status_code}, Data: {response.data.decode()}"
        )
        with self.app.app_context():
            link = Link.query.filter_by(original_url='https://google.com').first()
            self.assertIsNotNone(link)

    def test_redirect_to_original_url(self):
        """Test redirection from short URL to original URL."""
        with self.app.app_context():
            
            link = Link(original_url="https://google.com")
            db.session.add(link)
            db.session.commit()

            link = Link.query.filter_by(original_url="https://google.com").first()

            response = self.client.get(f'/{link.short_url}')

            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, "https://google.com")

    def test_delete_url(self):
        with self.app.app_context():
            
            test_link = Link(original_url="https://google.com", short_url="exmpl")
            db.session.add(test_link)
            db.session.commit()

            response = self.client.post(f"/delete/{test_link.id}", follow_redirects=False)

            self.assertEqual(response.status_code, 302)

            redirect_response = self.client.get("/analytics", follow_redirects=True)
            self.assertIn(b"Short URL successfully removed.", redirect_response.data)

    def test_invalid_url(self):
        """Test handling of an invalid or non-existent short URL."""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
    
    def test_regenerate_short_url(self):
        with self.app.app_context():
            # Add a test link
            link = Link(original_url="https://google.com", short_url="exmpl")
            db.session.add(link)
            db.session.commit()

            old_short_url = link.short_url

            link = Link.query.filter_by(id=link.id).first()

            new_short_url = link.generate_short_link()
            link.short_url = new_short_url
            db.session.commit()

            updated_link = Link.query.filter_by(id=link.id).first()

             
            self.assertNotEqual(old_short_url, updated_link.short_url)
            self.assertEqual(updated_link.short_url, new_short_url)


if __name__ == '__main__':
    unittest.main()

