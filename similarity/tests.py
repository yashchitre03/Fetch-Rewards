from django.test import TestCase, Client

from .forms import TextForm


class ResponseTest(TestCase):
    """
    Tests whether the requests return the appropriate status code in response.
    """

    def setUp(self) -> None:
        """
        Creates a dummy client used for getting response.
        :return: None
        """
        self.client = Client()

    def test_get(self) -> None:
        """
        Tests the GET request.
        :return: None
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, msg='GET request failed.')

    def test_post(self) -> None:
        """
        Tests the POST request.
        :return: None
        """
        dummy_form_data = {'t1': 'hello',
                           't2': 'world',
                           'algo': 'dice'}
        response = self.client.post('/', {'form': TextForm(dummy_form_data)})
        self.assertEqual(response.status_code, 200, msg='POST request failed.')
