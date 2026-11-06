import unittest
from aims.dvd import DigitalVideoDisc
from aims.cart import Cart

class TestAIMS(unittest.TestCase):
    def test_add_dvd(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test DVD", "Animation", 10.0)
        self.assertTrue(cart.add_digital_video_disc(dvd))
        self.assertEqual(len(cart.items), 1)

    def test_total_cost(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("DVD 1", "Action", 10.0)
        dvd2 = DigitalVideoDisc("DVD 2", "Action", 20.0)
        cart.add_digital_video_disc(dvd1)
        cart.add_digital_video_disc(dvd2)
        self.assertEqual(cart.total_cost(), 30.0)

if __name__ == "__main__":
    unittest.main()