#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_crea_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().crea_at))

    def test_upd_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().upd_at))

    def test_name_is_public_class_attribute(self):
        st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(st))
        self.assertNotIn("name", st.__dict__)

    def test_two_states_unique_ids(self):
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_two_states_different_crea_at(self):
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.crea_at, st2.crea_at)

    def test_two_states_different_upd_at(self):
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.upd_at, st2.upd_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        st = State()
        st.id = "123456"
        st.crea_at = st.upd_at = dt
        ststr = st.__str__()
        self.assertIn("[State] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'crea_at': " + dt_repr, ststr)
        self.assertIn("'upd_at': " + dt_repr, ststr)

    def test_args_unused(self):
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        st = State(id="345", crea_at=dt_iso, upd_at=dt_iso)
        self.assertEqual(st.id, "345")
        self.assertEqual(st.crea_at, dt)
        self.assertEqual(st.upd_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, crea_at=None, upd_at=None)


class TestState_save(unittest.TestCase):
    """Unittests for testing save method of the State class."""

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
        st = State()
        sleep(0.05)
        first_upd_at = st.upd_at
        st.save()
        self.assertLess(first_upd_at, st.upd_at)

    def test_two_saves(self):
        st = State()
        sleep(0.05)
        first_upd_at = st.upd_at
        st.save()
        second_upd_at = st.upd_at
        self.assertLess(first_upd_at, second_upd_at)
        sleep(0.05)
        st.save()
        self.assertLess(second_upd_at, st.upd_at)

    def test_save_with_arg(self):
        st = State()
        with self.assertRaises(TypeError):
            st.save(None)

    def test_save_updates_file(self):
        st = State()
        st.save()
        stid = "State." + st.id
        with open("file.json", "r") as f:
            self.assertIn(stid, f.read())


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        st = State()
        self.assertIn("id", st.to_dict())
        self.assertIn("crea_at", st.to_dict())
        self.assertIn("upd_at", st.to_dict())
        self.assertIn("__class__", st.to_dict())

    def test_to_dict_contains_added_attributes(self):
        st = State()
        st.middle_name = "Holberton"
        st.my_number = 98
        self.assertEqual("Holberton", st.middle_name)
        self.assertIn("my_number", st.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        st = State()
        st_dict = st.to_dict()
        self.assertEqual(str, type(st_dict["id"]))
        self.assertEqual(str, type(st_dict["crea_at"]))
        self.assertEqual(str, type(st_dict["upd_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        st = State()
        st.id = "123456"
        st.crea_at = st.upd_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'crea_at': dt.isoformat(),
            'upd_at': dt.isoformat(),
        }
        self.assertDictEqual(st.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        st = State()
        self.assertNotEqual(st.to_dict(), st.__dict__)

    def test_to_dict_with_arg(self):
        st = State()
        with self.assertRaises(TypeError):
            st.to_dict(None)


if __name__ == "__main__":
    unittest.main()
