#! /usr/bin/env python
"""
Unit tests for landlab.components.flexure.flexure
"""

import unittest
import numpy as np

from landlab.components.flexure import Flexure


(_SHAPE, _SPACING, _ORIGIN) = ((20, 20), (10e3, 10e3), (0., 0.))
_ARGS = (_SHAPE, _SPACING, _ORIGIN)


class TestFlexureInfo(unittest.TestCase):
    def setUp(self):
        self.flex = Flexure(*_ARGS)

    def test_name(self):
        self.assertEqual(self.flex.name, 'Flexure')

    def test_input_var_names(self):
        self.assertEqual(sorted(self.flex.input_var_names),
                         ['lithosphere__elevation',
                          'lithosphere__overlying_pressure'])

    def test_output_var_names(self):
        self.assertEqual(sorted(self.flex.output_var_names),
                         ['lithosphere__elevation',
                          'lithosphere__elevation_increment'])

    def test_var_units(self):
        self.assertEqual(set(self.flex.input_var_names) |
                         set(self.flex.output_var_names),
                         set(self.flex.units))

        self.assertEqual(self.flex.units['lithosphere__elevation'], 'm')
        self.assertEqual(self.flex.units['lithosphere__elevation_increment'],
                         'm')
        self.assertEqual(self.flex.units['lithosphere__overlying_pressure'],
                         'Pa')


class TestFlexureGrid(unittest.TestCase):
    def setUp(self):
        self.flex = Flexure(_SHAPE, _SPACING, _ORIGIN)

    def test_grid_shape(self):
        self.assertEqual(self.flex.get_count_of_rows(), _SHAPE[0])
        self.assertEqual(self.flex.get_count_of_cols(), _SHAPE[1])

    def test_grid_xdimension(self):
        self.assertEqual(self.flex.get_grid_xdimension(),
                         _SHAPE[1] * _SPACING[1])

    def test_grid_ydimension(self):
        self.assertEqual(self.flex.get_grid_xdimension(),
                         _SHAPE[0] * _SPACING[0])


class TestFlexureFields(unittest.TestCase):
    def setUp(self):
        self.flex = Flexure(*_ARGS)

    def test_field_getters(self):
        for name in self.flex:
            field = self.flex[name]
            self.assertIsInstance(field, np.ndarray)
            self.assertEqual(field.shape, (self.flex.get_count_of_rows(),
                                           self.flex.get_count_of_cols()))

        with self.assertRaises(KeyError):
            self.flex['not_a_var_name']

    def test_field_initialized_to_zero(self):
        for name in self.flex:
            field = self.flex[name]
            self.assertTrue(np.all(field == 0.))


if __name__ == '__main__':
    unittest.main()