from faker import Faker

class DataGenerator:
    def __init__(self):
        self.fake = Faker()
    
    def generate_post_data(self, user_id=None, **overrides):
        """Generate random post data"""
        post_data = {
            "title": self.fake.sentence(nb_words=6),
            "body": self.fake.paragraph(nb_sentences=3),
            "userId": user_id or self.fake.random_int(min=1, max=10)
        }
        post_data.update(overrides)
        return post_data
    
    def generate_user_data(self, **overrides):
        """Generate random user data"""
        user_data = {
            "name": self.fake.name(),
            "username": self.fake.user_name(),
            "email": self.fake.email(),
            "address": {
                "street": self.fake.street_address(),
                "suite": self.fake.building_number(),
                "city": self.fake.city(),
                "zipcode": self.fake.zipcode(),
                "geo": {
                    "lat": self.fake.latitude(),
                    "lng": self.fake.longitude()
                }
            },
            "phone": self.fake.phone_number(),
            "website": self.fake.domain_name(),
            "company": {
                "name": self.fake.company(),
                "catchPhrase": self.fake.catch_phrase(),
                "bs": self.fake.bs()
            }
        }
        user_data.update(overrides)
        return user_data
    
    def generate_comment_data(self, post_id=None, **overrides):
        """Generate random comment data"""
        comment_data = {
            "name": self.fake.name(),
            "email": self.fake.email(),
            "body": self.fake.paragraph(nb_sentences=2),
            "postId": post_id or self.fake.random_int(min=1, max=100)
        }
        comment_data.update(overrides)
        return comment_data