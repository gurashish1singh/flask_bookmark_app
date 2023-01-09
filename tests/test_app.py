from __future__ import annotations

import os
from unittest import TestCase

# from flask_testing import TestCase
from parameterized import parameterized

from flask_bookmark_app import create_app


class TestApp(TestCase):
    @parameterized.expand(
        [
            ("dev", "dev", True),
            ("testing", "testing", True),
        ]
    )
    def test_app_environment(self, env, expected_env, expected_test_flag):
        os.environ["ENV"] = env
        app = create_app()
        self.assertEqual(app.config["ENV"], expected_env)
        self.assertEqual(app.config["TESTING"], expected_test_flag)
