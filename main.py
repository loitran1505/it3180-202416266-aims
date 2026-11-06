from aims.dvd import DigitalVideoDisc
from aims.cart import Cart

cart = Cart()
dvd1 = DigitalVideoDisc("The Lion King", "Animation", 19.95)
dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", 24.95)
dvd3 = DigitalVideoDisc("Aladdin", "Animation", 18.99)

cart.add_digital_video_disc(dvd1)
cart.add_digital_video_disc(dvd2)
cart.add_digital_video_disc(dvd3)

print("=== AIMS PROGRAM VERSION 1.0 ===")
cart.print_cart()