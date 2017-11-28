import unittest
import json
from Strom.strom.database.mongo_management import MongoManager


class TestMongoManager(unittest.TestCase):
    def setUp(self):
        demo_data_dir = "Strom/demo_data/"
        self.manager = MongoManager()
        self.dstream_template = json.load(open(demo_data_dir + "demo_template.txt"))
        self.dstream_template["stream_token"] = "abc123"
        self.derived = {"stream_name": "driver_data", "version": 0, "stream_token": "abc123", "sources": {},'storage_rules': {}, 'ingest_rules': {}, 'engine_rules': {}, "timestamp": [1510603538107, 1510603538108, 1510603538109], "derived_measures":{"location": {"val": [[-122.69081962885704, 45.52110054870811], [-132.69081962885704, 55.52110054870811], [-142.69081962885704, 65.52110054870811]], "dtype": "float"}, "measure2": {"val": [13, 9, 4], "dtype": "int"}}, "fields": {"region-code": ["PDX", "PDX", "PDX"]}, "user_ids": {"driver-id": ["Molly Mora", "Molly Mora", "Molly Mora"], "id": [0, 0, 0]}, "tags": {"mood": ["chill", "big mood", "the last big mood"]}, "foreign_keys": [], "filters": [], "dparam_rules": [], "event_rules": {}, "template_id": "chadwick666"}
        self.events = {"stream_name": "driver_data", "version": 0, "stream_token": "abc123", "sources": {},'storage_rules': {}, 'ingest_rules': {}, 'engine_rules': {}, "timestamp": [1510603538107, 1510603538108, 1510603538109], "events":{"location": {"val": [[-122.69081962885704, 45.52110054870811], [-132.69081962885704, 55.52110054870811], [-142.69081962885704, 65.52110054870811]], "dtype": "float"}, "measure2": {"val": [13, 9, 4], "dtype": "int"}}, "fields": {"region-code": ["PDX", "PDX", "PDX"]}, "user_ids": {"driver-id": ["Molly Mora", "Molly Mora", "Molly Mora"], "id": [0, 0, 0]}, "tags": {"mood": ["chill", "big mood", "the last big mood"]}, "foreign_keys": [], "filters": [], "dparam_rules": [], "event_rules": {}, "template_id": "chadwick666"}

    def test_insert_retrieve(self):
        token = self.dstream_template["stream_token"]

        inserted_id = self.manager.insert(self.dstream_template, 'template')
        queried = self.manager.get_by_id(inserted_id, 'template')

        inserted_id2 = self.manager.insert(self.derived, 'derived')
        queried2 = self.manager.get_by_id(inserted_id2, 'derived', token)

        inserted_id3 = self.manager.insert(self.events, 'event')
        queried3 = self.manager.get_by_id(inserted_id3, 'event', token)

        self.assertEqual(inserted_id, queried["_id"])
        self.assertEqual(inserted_id2, queried2["_id"])
        self.assertEqual(inserted_id3, queried3["_id"])

        all_derived = self.manager.get_all_coll('derived', 'abc123')
        all_events = self.manager.get_all_coll('event', 'abc123')
        print(all_events)
        self.assertTrue(len(all_derived[0]["derived_measures"]) >= 2)
        self.assertTrue(len(all_events[0]["events"]) >= 2)



if __name__ == "__main__":
    unittest.main()