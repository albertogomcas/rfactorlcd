#!/usr/bin/env python3

# rFactor Remote LCD
# Copyright (C) 2014 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import unittest
import rfactorlcd
import rfactorlcd.state


class rFactorLCDTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_loading_aspect(self):
        pass

    def test_rfactorState(self):
        state1 = rfactorlcd.state.rFactorState()
        data = state1.to_vracingDisplayPRO()
        state2 = rfactorlcd.state.rFactorState(data)
        self.assertEqual(state1.to_vracingDisplayPRO(),
                         state2.to_vracingDisplayPRO())


if __name__ == '__main__':
    unittest.main()


# EOF #
