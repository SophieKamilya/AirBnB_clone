#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_crea_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().crea_at))

    def test_upd_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().upd_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_crea_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.crea_at, bm2.crea_at)

    def test_two_models_different_upd_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.upd_at, bm2.upd_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.crea_at = bm.upd_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'crea_at': " + dt_repr, bmstr)
        self.assertIn("'upd_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", crea_at=dt_iso, upd_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.crea_at, dt)
        self.assertEqual(bm.upd_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, crea_at=None, upd_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", crea_at=dt_iso, upd_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.crea_at, dt)
        self.assertEqual(bm.upd_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
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
        bm = BaseModel()
        sleep(0.05)
        first_upd_at = bm.upd_at
        bm.save()
        self.assertLess(first_upd_at, bm.upd_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_upd_at = bm.upd_at
        bm.save()
        second_upd_at = bm.upd_at
        self.assertLess(first_upd_at, second_upd_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_upd_at, bm.upd_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("crea_at", bm.to_dict())
        self.assertIn("upd_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["crea_at"]))
        self.assertEqual(str, type(bm_dict["upd_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.crea_at = bm.upd_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'crea_at': dt.isoformat(),
            'upd_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
