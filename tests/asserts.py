# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>
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
import sys
from StringIO import StringIO
from nose.tools import assert_equals
from lettuce import CALLBACK_REGISTRY, STEP_REGISTRY

def prepare_stdout():
    CALLBACK_REGISTRY.clear()
    STEP_REGISTRY.clear()
    if isinstance(sys.stdout, StringIO):
        del sys.stdout
    std = StringIO()
    sys.stdout = std
def prepare_stderr():
    CALLBACK_REGISTRY.clear()
    STEP_REGISTRY.clear()
    if isinstance(sys.stderr, StringIO):
        del sys.stderr
    std = StringIO()
    sys.stderr = std

def assert_lines(one, other):
    lines_one = one.splitlines()
    lines_other = other.splitlines()
    for line1, line2 in zip(lines_one, lines_other):
        assert_equals(line1, line2)

    assert_equals(len(lines_one), len(lines_other))

def assert_stderr(expected):
    string = sys.stderr.getvalue()
    assert_equals(string, expected)
def assert_stdout(expected):
    string = sys.stdout.getvalue()
    assert_equals(string, expected)
def assert_stdout_lines(other):
    assert_lines(sys.stdout.getvalue(), other)
def assert_stderr_lines(other):
    assert_lines(sys.stderr.getvalue(), other)

