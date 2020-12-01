import argparse
import sys
from PIL import Image


class ArgumentOptions:
    parser = None
    options = None
    args = None
    filename = None
    order = []

    def __init__(self, args=sys.argv[1:]):
        self.parser = argparse.ArgumentParser(
            description="Image Converter Command Interface"
        )
        self.args = args
        self._set_execution_order()
        self._set_args_options()

    def _set_execution_order(self):
        order = list()
        index = 1
        for arg in self.args:
            # IF AN ARGUMENT
            if arg.startswith("--", 0, 2):
                order.append(arg.replace("--", ""))
        self.order = order

    def _set_args_options(self):
        group = self.parser.add_argument_group("image converter")
        group.add_argument(
            "--filename",
            dest="filename",
            help="Image name to be converted, with extention (jpg, png, jpeg)",
            type=str,
            default=None,
            required=True,
        )
        group.add_argument(
            "--gray_scale",
            action="store_true",
            dest="gray_scale",
            help="Convert the image to black and white",
        )
        group.add_argument(
            "--overlay",
            type=str,
            dest="overlay",
            default=None,
            help="Overlay a given image on top of the source.",
        )
        group.add_argument(
            "--rotate", type=int, dest="rotate", default=None, help="rotate N degrees."
        )
        group.add_argument(
            "--verbose", dest="verbose", action="store_true", help="verbose mode."
        )
        self.options = self.parser.parse_args(self.args)

    def gray_scale(self, value):
        print("hello", value)
        image_file = Image.open(f"./source/{self.filename}")
        image_file = image_file.convert(
            "L"
        )  # convert image (8-bit pixels, black and white)
        filename_output = self.filename.split(".")[0]
        image_file.save(f"./output/{filename_output}.png")

    def execute(self):
        args = vars(self.options)
        print(args)
        self.filename = args["filename"]
        for oe in self.order:
            if oe == "gray_scale":
                self.gray_scale(args[oe])


if __name__ == "__main__":
    command = ArgumentOptions()
    command.execute()
    if command.options.verbose:
        print("Verbose mode on")
    else:
        print("Verbose mode off")

    # if command.options.gray_scale:
    #     print(command.options.gray_scale)

    # if command.options.overlay:
    #     print(command.options.overlay)

    # if command.options.rotate:
    #     print(command.options.rotate)

    # print(vars(command.options))
