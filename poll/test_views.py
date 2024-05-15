import json

from django.test import TestCase

from .models import Poll

class pollViewTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        
        number_of_polls = 7

        for poll_id in range(number_of_polls):
            Poll.objects.create(
                title = f'title {poll_id}',
                description = f'description {poll_id}',
            )
        
        return super().setUpTestData()
    
    def test_list(self):
        response = self.client.get('/poll')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 7)