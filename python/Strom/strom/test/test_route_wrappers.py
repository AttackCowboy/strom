import unittest
from time import sleep

from strom.route_wrappers import *


class TestWrappers(unittest.TestCase):
    def setUp(self):
        self.data_dir = 'demo_data/'
        self.dstream = json.load(open(self.data_dir + 'demo_template_unit_test.txt'))

    def test_post_template(self):
        resp = post_template(url, self.dstream)
        self.assertEqual(resp[0], 200)
        self.assertEqual(len(resp[1]), 36)

        bad_resp = post_template(url, "blep")
        self.assertEqual(bad_resp[0], 400)

    def test_send_data(self):
        resp = send_data(url, self.dstream)
        self.assertEqual(resp, (202, 'Success.'))

        bad_resp = post_template(url, "blep")
        self.assertEqual(bad_resp[0], 400)

    def test_engine_status(self):
        resp = engine_status(url)
        self.assertEqual(resp[0], 200)
        self.assertTrue(resp[1]["running"])
        self.assertIn("time_running", resp[1].keys())

    def test_zesty_stop_engine(self):
        resp = stop_engine(url)
        self.assertEqual(resp[0], 200)
        self.assertTrue(resp[1]["engine_stopped"])
        sleep(1)
        r = engine_status(url)
        self.assertFalse(r[1]["running"])
        self.assertIn("time_stopped", r[1].keys())