import unittest
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter


class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rect_area(2, 3), 6)
    def test_area_zero(self):
        self.assertEqual(rect_area(0, 8), 0)
    def test_area_negative(self):
        self.assertEqual(rect_area(5, -10), 0)


    def test_perimeter(self):
        self.assertEqual(rect_perimeter(2, 3), 12)
    def test_perimetr_zero(self):
        self.assertEqual(rect_perimeter(0, 10), 0)
        



class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(4), 16)
    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)


    def test_perimeter(self):
        self.assertEqual(square_perimeter(10), 40)
    def test_perimetr_zero(self):
        self.assertEqual(square_perimeter(0), 0)



class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle_area(10, 10), 50)
    def test_area_zero(self):
        self.assertEqual(triangle_area(0, 4), 0)
    def test_area_negative(self):
        self.assertEqual(triangle_area(-3 ,-4), 0)


    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
    def test_perimetr_zero(self):
        self.assertEqual(triangle_perimeter(0, 4, 0), 0)
    def test_perimetr_negative(self):
        self.assertEqual(triangle_perimeter(-3, 4, 0), 0)



class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), 3.14, places=2)
    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)
    def test_area_negative(self):
        self.assertEqual(circle_area(-5), 0)


    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(5), 31.4, places=1)
    def test_perimetr_negative(self):
        self.assertEqual(circle_perimeter(-5), 0)  
    def test_area_zero(self):
        self.assertEqual(circle_perimeter(0), 0)


if name == "__main__":
    unittest.main()
