#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_crea_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().crea_at))

    def test_upd_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().upd_at))

    def test_city_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_idUser_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.idUser))
        self.assertIn("idUser", dir(pl))
        self.assertNotIn("idUser", pl.__dict__)

    def test_name_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_descpt_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.descpt))
        self.assertIn("descpt", dir(pl))
        self.assertNotIn("desctiption", pl.__dict__)

    def test_roomNumber_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.roomNumber))
        self.assertIn("roomNumber", dir(pl))
        self.assertNotIn("roomNumber", pl.__dict__)

    def test_bathroomsNumber_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.bathroomsNumber))
        self.assertIn("bathroomsNumber", dir(pl))
        self.assertNotIn("bathroomsNumber", pl.__dict__)

    def test_maxGuest_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.maxGuest))
        self.assertIn("maxGuest", dir(pl))
        self.assertNotIn("maxGuest", pl.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_lati_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.lati))
        self.assertIn("lati", dir(pl))
        self.assertNotIn("lati", pl.__dict__)

    def test_long_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.long))
        self.assertIn("long", dir(pl))
        self.assertNotIn("long", pl.__dict__)

    def test_Amenity_ids_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(list, type(Place.Amenity_ids))
        self.assertIn("Amenity_ids", dir(pl))
        self.assertNotIn("Amenity_ids", pl.__dict__)

    def test_two_places_unique_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_places_different_crea_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.crea_at, pl2.crea_at)

    def test_two_places_different_upd_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.upd_at, pl2.upd_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        pl = Place()
        pl.id = "123456"
        pl.crea_at = pl.upd_at = dt
        plstr = pl.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'crea_at': " + dt_repr, plstr)
        self.assertIn("'upd_at': " + dt_repr, plstr)

    def test_args_unused(self):
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        pl = Place(id="345", crea_at=dt_iso, upd_at=dt_iso)
        self.assertEqual(pl.id, "345")
        self.assertEqual(pl.crea_at, dt)
        self.assertEqual(pl.upd_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, crea_at=None, upd_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

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
        pl = Place()
        sleep(0.05)
        first_upd_at = pl.upd_at
        pl.save()
        self.assertLess(first_upd_at, pl.upd_at)

    def test_two_saves(self):
        pl = Place()
        sleep(0.05)
        first_upd_at = pl.upd_at
        pl.save()
        second_upd_at = pl.upd_at
        self.assertLess(first_upd_at, second_upd_at)
        sleep(0.05)
        pl.save()
        self.assertLess(second_upd_at, pl.upd_at)

    def test_save_with_arg(self):
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)

    def test_save_updates_file(self):
        pl = Place()
        pl.save()
        plid = "Place." + pl.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        pl = Place()
        self.assertIn("id", pl.to_dict())
        self.assertIn("crea_at", pl.to_dict())
        self.assertIn("upd_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())

    def test_to_dict_contains_added_attributes(self):
        pl = Place()
        pl.middle_name = "Holberton"
        pl.my_number = 98
        self.assertEqual("Holberton", pl.middle_name)
        self.assertIn("my_number", pl.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["crea_at"]))
        self.assertEqual(str, type(pl_dict["upd_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.crea_at = pl.upd_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'crea_at': dt.isoformat(),
            'upd_at': dt.isoformat(),
        }
        self.assertDictEqual(pl.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        pl = Place()
        self.assertNotEqual(pl.to_dict(), pl.__dict__)

    def test_to_dict_with_arg(self):
        pl = Place()
        with self.assertRaises(TypeError):
            pl.to_dict(None)


if __name__ == "__main__":
    unittest.main()
