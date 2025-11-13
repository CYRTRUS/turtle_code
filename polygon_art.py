import turtle
import random


class ShapeGenerator:
    def __init__(self):
        self.screen = turtle.Screen()
        self.artist = turtle.Turtle()
        self.setup_screen()

    def setup_screen(self):
        self.screen.bgcolor("black")
        self.screen.colormode(255)
        self.artist.speed(0)
        self.artist.hideturtle()
        self.screen.tracer(0)

    def clear_board(self):
        self.artist.clear()
        self.artist.penup()
        self.artist.home()
        self.artist.pendown()
        self.screen.update()

    def get_new_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)

    def reposition(self, reduction_ratio, location, size):
        self.artist.penup()
        self.artist.forward(size*(1-reduction_ratio)/2)
        self.artist.left(90)
        self.artist.forward(size*(1-reduction_ratio)/2)
        self.artist.right(90)
        location[0] = self.artist.pos()[0]
        location[1] = self.artist.pos()[1]

    def draw_base_shape(self, size, orientation, location, color, border_size, num_side):
        self.artist.penup()
        self.artist.goto(location[0], location[1])
        self.artist.setheading(orientation)
        self.artist.color(color)
        self.artist.pensize(border_size)
        self.artist.pendown()
        for _ in range(num_side):
            self.artist.forward(size)
            self.artist.left(360 / num_side)
        self.artist.penup()

    def draw_shape(self, num_shape, num_side, num_layer):
        for _ in range(num_shape):
            # Generate new random values for each shape
            reduction_ratio = 0.6
            size = random.randint(50, 150)
            orientation = random.randint(0, 360)
            location = [random.randint(-300, 300),
                        random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 6)

            # Loop drawing in smaller version
            for _ in range(num_layer):
                self.draw_base_shape(
                    size, orientation, location, color, border_size, num_side)

                self.reposition(reduction_ratio, location, size)
                size *= reduction_ratio
                self.screen.update()

    def run(self):
        while True:
            choice = input(
                "Which art do you want to generate? Enter a number between 1 to 9 inclusive (or 'q' to quit): ")

            self.clear_board()

            num_shape = random.randint(20,30)  # num shape range: 20-30 shapes

            if choice == "1":
                self.draw_shape(num_shape, 3, 1)  # triangles, 1 layer each

            elif choice == "2":
                self.draw_shape(num_shape, 4, 1)  # squares, 1 layer each

            elif choice == "3":
                self.draw_shape(num_shape, 5, 1)  # pentagons, 1 layer each

            elif choice == "4":
                # Mix: triangles, squares, pentagons, 1 layer each
                self.draw_shape(round(num_shape / 3), 3, 1)
                self.draw_shape(round(num_shape / 3), 4, 1)
                self.draw_shape(round(num_shape / 3), 5, 1)

            elif choice == "5":
                self.draw_shape(num_shape, 3, 3)  # triangles, 3 layers each

            elif choice == "6":
                self.draw_shape(num_shape, 4, 3)  # squares, 3 layers each

            elif choice == "7":
                self.draw_shape(num_shape, 5, 3)  # pentagons, 3 layers each

            elif choice == "8":
                # Mix with layers: all shapes, 3 layers each
                self.draw_shape(round(num_shape / 3), 3, 3)
                self.draw_shape(round(num_shape / 3), 4, 3)
                self.draw_shape(round(num_shape / 3), 5, 3)

            elif choice == "9":
                # All mix: 2 of each shape with 1, 2, and 3 layers
                for side in range(3, 6):  # triangle, square, pentagon
                    for layer in range(1, 4):
                        self.draw_shape(round(num_shape / 10), side, layer)

            elif choice.lower() == "q":
                break

            else:
                print("Invalid choice.")


art_gen = ShapeGenerator()
art_gen.run()
