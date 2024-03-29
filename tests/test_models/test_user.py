#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_crea_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().crea_at))

    def test_upd_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().upd_at))

    def test_usrEmail_is_public_str(self):
        self.assertEqual(str, type(User.usrEmail))

    def test_usrPassword_is_public_str(self):
        self.assertEqual(str, type(User.usrPassword))

    def test_firstName_is_public_str(self):
        self.assertEqual(str, type(User.firstName))

    def test_lastName_is_public_str(self):
        self.assertEqual(str, type(User.lastName))

    def test_two_users_unique_ids(self):
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_different_crea_at(self):
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.crea_at, us2.crea_at)

    def test_two_users_different_upd_at(self):
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.upd_at, us2.upd_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.crea_at = us.upd_at = dt
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'crea_at': " + dt_repr, usstr)
        self.assertIn("'upd_at': " + dt_repr, usstr)

    def test_args_unused(self):
        us = User(None)
        self.assertNotIn(None, us.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", crea_at=dt_iso, upd_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.crea_at, dt)
        self.assertEqual(us.upd_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, crea_at=None, upd_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        us = User()
        sleep(0.05)
        first_upd_at = us.upd_at
        us.save()
        self.assertLess(first_upd_at, us.upd_at)

    def test_two_saves(self):
        us = User()
        sleep(0.05)
        first_upd_at = us.upd_at
        us.save()
        second_upd_at = us.upd_at
        self.assertLess(first_upd_at, second_upd_at)
        sleep(0.05)
        us.save()
        self.assertLess(second_upd_at, us.upd_at)

    def test_save_with_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_save_updates_file(self):
        us = User()
        us.save()
        usid = "User." + us.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("crea_at", us.to_dict())
        self.assertIn("upd_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())

    def test_to_dict_contains_added_attributes(self):
        us = User()
        us.middle_name = "Holberton"
        us.my_number = 98
        self.assertEqual("Holberton", us.middle_name)
        self.assertIn("my_number", us.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["crea_at"]))
        self.assertEqual(str, type(us_dict["upd_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.crea_at = us.upd_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'crea_at': dt.isoformat(),
            'upd_at': dt.isoformat(),
        }
        self.assertDictEqual(us.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_with_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)


if __name__ == "__main__":
    unittest.main()
