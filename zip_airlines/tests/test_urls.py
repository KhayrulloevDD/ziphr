from django.test import SimpleTestCase
from django.urls import resolve, reverse
from zip_airlines import apis


class TestUrls(SimpleTestCase):

    def test_airplanes(self):
        url = reverse('airplanes')
        self.assertEquals(resolve(url).func.view_class, apis.AirplaneList)

    def test_airplane_detail(self):
        url = reverse('airplane_detail', args=[7])
        self.assertEquals(resolve(url).func.view_class, apis.AirplaneDetail)
