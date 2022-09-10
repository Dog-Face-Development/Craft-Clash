#!/usr/bin/env python
"""Tests immediate drawing using indexed data.
"""
import unittest

import pyglet

from graphics_common import GraphicsIndexedGenericTestCase, get_feedback, GL_TRIANGLES

__noninteractive = True


class GraphicsIndexedImmediateTestCase(GraphicsIndexedGenericTestCase, unittest.TestCase):
    def get_feedback(self, data):
        return get_feedback(lambda: pyglet.graphics.draw_indexed(self.n_vertices,
                                                                 GL_TRIANGLES,
                                                                 self.index_data,
                                                                 *data))

if __name__ == '__main__':
    unittest.main()
