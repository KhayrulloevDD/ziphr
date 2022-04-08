import json
import pdb

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class TestAirplaneAPI(APITestCase):

    def setUp(self):
        super().setUp()
        self.airplanes_url = reverse("airplanes")
        self.airplane_detail_url = reverse("airplane_detail", args=[3])

        self.valid_airplane_data = {
            "id": 3,
            "passengers": 20
        }

        self.valid_airplane_data_with_the_same_id = {
            "id": 3,
            "passengers": 20
        }

        self.invalid_airplane_data1 = {
            "id": 0,
            "passengers": 20
        }

        self.invalid_airplane_data2 = {
            "id": 3,
            "passengers": -2
        }

    def test_post_method_for_valid_airplane_data(self):
        response = self.client.post(self.airplanes_url, data=json.dumps(self.valid_airplane_data),
                                    content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data, {
            "id": 3,
            "passengers": 20,
            "capacity": 600,
            "consumption_per_minute": 0.92,
            "able_to_fly": 652.17
        })

    def test_post_method_for_invalid_airplane_data1(self):
        response = self.client.post(self.airplanes_url, data=json.dumps(self.invalid_airplane_data1),
                                    content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data, {
            "id": [
                "Ensure this value is greater than or equal to 2."
            ]
        })

    def test_post_method_for_invalid_airplane_data2(self):
        response = self.client.post(self.airplanes_url, data=json.dumps(self.invalid_airplane_data2),
                                    content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data, {
            "passengers": [
                "Ensure this value is greater than or equal to 0."
            ]
        })

    def test_post_method_for_invalid_airplane_data_with_the_same_id(self):
        response1 = self.client.post(self.airplanes_url, data=json.dumps(self.valid_airplane_data),
                                     content_type='application/json')

        response2 = self.client.post(self.airplanes_url, data=json.dumps(self.valid_airplane_data),
                                     content_type='application/json')

        self.assertEquals(response1.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response1.data, {
            "id": 3,
            "passengers": 20,
            "capacity": 600,
            "consumption_per_minute": 0.92,
            "able_to_fly": 652.17
        })
        self.assertEquals(response2.data, {
            "id": [
                "airplane with this ID already exists."
            ]
        })

    def test_put_airplane(self):
        self.test_post_method_for_valid_airplane_data()
        response = self.client.put(self.airplane_detail_url, data=json.dumps({
            "id": 10,
            "passengers": 10,
        }), content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, {
            "id": 10,
            "passengers": 10,
            "capacity": 2000,
            "consumption_per_minute": 1.86,
            "able_to_fly": 1075.27
        })

    def test_get_airplane(self):
        self.test_post_method_for_valid_airplane_data()
        response = self.client.get(self.airplane_detail_url, content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, {
            "id": 3,
            "passengers": 20,
            "capacity": 600,
            "consumption_per_minute": 0.92,
            "able_to_fly": 652.17
        })

    def test_get_un_existed_airplane(self):
        response = self.client.get(self.airplane_detail_url, content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(response.data, {
            "detail": "Not found."
        })

    def test_delete_post(self):
        self.test_post_method_for_valid_airplane_data()
        response = self.client.delete(self.airplane_detail_url, content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(response.data, {
            "status": "success",
            "message": "Airplane with id=3 has been deleted successfully!"
        })
