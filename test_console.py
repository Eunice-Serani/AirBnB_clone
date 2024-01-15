#!/usr/bin/python3

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

class TestConsole(unittest.TestCase):
    def setUp(self):
        """ Set up for the tests """
        self.console = HBNBCommand()
        storage.reload()

    def tearDown(self):
        """ Clean up after each test """
        del self.console
        storage.reset()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """ Test create command """
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        obj_key = "BaseModel.{}".format(obj_id)
        self.assertTrue(obj_key in storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """ Test show command """
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd("show BaseModel {}".format(obj_id))
        expected_output = "[BaseModel] ({})".format(obj_id)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class(self, mock_stdout):
        """ Test show command with missing class """
        self.console.onecmd("show")
        expected_output = "** class name missing **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_id(self, mock_stdout):
        """ Test show command with missing ID """
        self.console.onecmd("show BaseModel")
        expected_output = "** instance id missing **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_nonexistent_instance(self, mock_stdout):
        """ Test show command with nonexistent instance """
        self.console.onecmd("show BaseModel 12345")
        expected_output = "** no instance found **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """ Test destroy command """
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        obj_key = "BaseModel.{}".format(obj_id)
        self.assertTrue(obj_key in storage.all())
        self.console.onecmd("destroy BaseModel {}".format(obj_id))
        self.assertFalse(obj_key in storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_class(self, mock_stdout):
        """ Test destroy command with missing class """
        self.console.onecmd("destroy")
        expected_output = "** class name missing **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_id(self, mock_stdout):
        """ Test destroy command with missing ID """
        self.console.onecmd("destroy BaseModel")
        expected_output = "** instance id missing **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_nonexistent_instance(self, mock_stdout):
        """ Test destroy command with nonexistent instance """
        self.console.onecmd("destroy BaseModel 12345")
        expected_output = "** no instance found **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """ Test update command """
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        obj_key = "BaseModel.{}".format(obj_id)
        self.assertTrue(obj_key in storage.all())
        self.console.onecmd("update BaseModel {} name 'New Name'".format(obj_id))
        obj = storage.all()[obj_key]
        self.assertEqual(obj.name, "New Name")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_class(self, mock_stdout):
        """ Test update command with missing class """
        self.console.onecmd("update")
        expected_output = "** class name missing **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_id(self, mock_stdout):
        """ Test update command with missing ID """
        self.console.onecmd("update BaseModel")
        expected_output = "** instance id missing **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_nonexistent_instance(self, mock_stdout):
        """ Test update command with nonexistent instance """
        self.console.onecmd("update BaseModel 12345")
        expected_output = "** no instance found **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_attribute(self, mock_stdout):
        """ Test update command with missing attribute """
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        obj_key = "BaseModel.{}".format(obj_id)
        self.assertTrue(obj_key in storage.all())
        self.console.onecmd("update BaseModel {}".format(obj_id))
        expected_output = "** attribute name missing **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_value(self, mock_stdout):
        """ Test update command with missing value """
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        obj_key = "BaseModel.{}".format(obj_id)
        self.assertTrue(obj_key in storage.all())
        self.console.onecmd("update BaseModel {} name".format(obj_id))
        expected_output = "** value missing **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """ Test all command """
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create State")
        self.console.onecmd("all")
        expected_output = "[BaseModel] ({}) [State] ({})".format(
            list(storage.all().keys())[0], list(storage.all().keys())[1]
        )
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_with_class(self, mock_stdout):
        """ Test all command with class specified """
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create State")
        self.console.onecmd("create City")
        self.console.onecmd("all State")
        expected_output = "[State] ({})".format(list(storage.all().keys())[1])
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_with_nonexistent_class(self, mock_stdout):
        """ Test all command with nonexistent class """
        self.console.onecmd("all NonExistentClass")
        expected_output = "** class doesn't exist **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """ Test quit command """
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """ Test EOF command """
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

if __name__ == "__main__":
	unittest.main()
