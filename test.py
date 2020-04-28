from unittest import TestCase
from rover import RoverSim, Direction


class TestRoverSim(TestCase):

    def test_valid_sim_config(self):
        sim = RoverSim(0, 0, Direction.S, 10, 10)
        self.assertEqual(str(sim), "0 0 Direction.S")

    def test_invalid_sim_config1(self):
        with self.assertRaises(ValueError):
            RoverSim(0, 0, Direction.N, -5, 10)

    def test_invalid_sim_config2(self):
        with self.assertRaises(ValueError):
            RoverSim(-6, 0, Direction.N, 10, 10)

    def test_rover_jams_against_walls(self):
        sim = RoverSim(0, 0, Direction.S, 10, 10)
        self.assertEqual(str(sim), "0 0 Direction.S")
        sim.command("MMMMM")  # Move 5 spaces in the negative y direction
        self.assertEqual(str(sim), "0 0 Direction.S")

    def test_rover_move(self):
        sim = RoverSim(0, 0, Direction.N, 10, 10)
        self.assertEqual(str(sim), "0 0 Direction.N")
        sim.command("MMMMM")  # Move 5 spaces in the positive y direction
        self.assertEqual(str(sim), "0 5 Direction.N")

    def test_smallest_grid(self):
        # This config dissallows the rover from moving
        sim = RoverSim(0, 0, Direction.N, 0, 0)
        self.assertEqual(str(sim), "0 0 Direction.N")
        sim.command("MMMMM")  # Move 5 spaces in the positive y direction
        self.assertEqual(str(sim), "0 0 Direction.N")
