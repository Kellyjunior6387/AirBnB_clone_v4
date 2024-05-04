#!/usr/bin/python3
import unittest
from flask import Flask, jsonify
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from api.v1.views.places import places_search

class TestPlaces(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True
        self.client = self.app.test_client()

    def test_empty_search(self):
        response = self.client.post('/api/v1/places_search', json={})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), len(storage.all(Place)))

    def test_search_by_state(self):
        state = State(name="Test State")
        city = City(name="Test City", state_id=state.id)
        place = Place(name="Test Place", city_id=city.id)
        storage.new(state)
        storage.new(city)
        storage.new(place)
        storage.save()

        response = self.client.post('/api/v1/places_search', json={'states': [state.id]})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Test Place")

    # Add more tests for other cases

if __name__ == '__main__':
    unittest.main()