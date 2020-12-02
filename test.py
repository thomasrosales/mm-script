import unittest
from app.image_converter import ConverterImage


class TestConverterImage(unittest.TestCase):
    def test_init(self):
        """
        Test the init of the ConverterImage class
        """
        command = ConverterImage(
            ["--filename", "input.jpg", "--output", "tt", "--ext", "png"]
        )
        self.assertIsInstance(command.args, list)
        self.assertFalse(command.verbose)
        self.assertEqual(command.ext, "png")
        self.assertEqual(command.filename, "input.jpg")
        self.assertEqual(command.output, "tt")

    def test_execution_order(self):
        command = ConverterImage(
            [
                "--filename",
                "input.jpg",
                "--output",
                "tt",
                "--ext",
                "png",
                "--rotate",
                "90",
                "--overlay",
                "python.png",
            ]
        )
        self.assertListEqual(
            command.order, ["filename", "output", "ext", "rotate", "overlay"]
        )

    def test_execution_order_repeat_args(self):
        command = ConverterImage(
            [
                "--filename",
                "input.jpg",
                "--output",
                "tt",
                "--ext",
                "png",
                "--rotate",
                "90",
                "--overlay",
                "python.png",
                "--rotate",
                "45",
                "--gray_scale",
                "bw8bp",
            ]
        )
        self.assertListEqual(
            command.order,
            ["filename", "output", "ext", "rotate", "overlay", "rotate", "gray_scale"],
        )

    def test_base_image(self):
        command = ConverterImage(
            [
                "--filename",
                "input_fake.jpg",
                "--output",
                "tt",
                "--ext",
                "png",
            ]
        )
        command.execute()
        self.assertIn("FileNotFoundError", command.errors)


if __name__ == "__main__":
    unittest.main()