import argparse
import sys
import os
from PIL import Image
from colorama import Fore, Back, Style


class ArgumentOptions:
    parser = None
    options = None
    args = None
    filename = None
    output = None
    ext = None
    verbose = False
    show = False
    indexes = dict()
    order = []

    def __init__(self, args=sys.argv[1:]):
        self.parser = argparse.ArgumentParser(
            description="Image Converter Command Interface"
        )
        self.args = args
        self._set_execution_order()
        self._set_args_options()
        self.indexes["gray_scale"] = 0
        self.indexes["overlay"] = 0
        self.indexes["rotate"] = 0

    def _set_execution_order(self):
        order = list()
        index = 1
        for arg in self.args:
            # IF AN ARGUMENT
            if arg.startswith("--", 0, 2):
                argv = arg
                if "=" in arg:
                    argv = arg.split("=")[0]
                argv = argv.replace("--", "")
                order.append(argv)
        self.order = order

    def _set_args_options(self):
        group = self.parser.add_argument_group("image converter")
        group.add_argument(
            "--filename",
            dest="filename",
            help="Image name to be converted, with extention (jpg, png, jpeg).",
            type=str,
            default=None,
            required=True,
        )
        group.add_argument(
            "--output",
            dest="output",
            help="Output filename.",
            type=str,
            default=None,
            required=True,
        )
        group.add_argument(
            "--ext",
            dest="ext",
            choices=["png", "jpg"],
            help="Extention output file.",
            required=True,
        )
        group.add_argument(
            "--gray_scale",
            dest="gray_scale",
            choices=["bw1bp", "bw8bp"],
            help="Convert the image to black and white.",
            action="append",
        )
        group.add_argument(
            "--overlay",
            type=str,
            dest="overlay",
            default=None,
            help="Overlay a given image on top of the source.",
            action="append",
        )
        group.add_argument(
            "--rotate",
            type=int,
            dest="rotate",
            default=None,
            help="Rotate image N degrees.",
            action="append",
        )
        group.add_argument(
            "--show",
            dest="show",
            action="store_true",
            help="Show the image to the end.",
        )
        group.add_argument(
            "--verbose", dest="verbose", action="store_true", help="Verbose mode."
        )
        self.options = self.parser.parse_args(self.args)

    def gray_scale(self, value):
        try:
            try:
                image_file = Image.open("./temp/temp.png")
            except Exception as e:
                image_file = Image.open(f"./source/{self.filename}")
        except Exception as e:
            print(Fore.RED + f"[ CRITICAL EXCEPTION ] {e}")
            self.remove_temp()
            return
        if self.verbose:
            print(Fore.CYAN + f"[ B/W SCALYING ] with {value}")
        mode_convert = "1" if value == "bw1bp" else "L"
        # convert image (1-bit pixel or 8-bit pixels, black and white)
        image_file = image_file.convert(mode_convert)
        image_file.save("./temp/temp.png", format="png")

    def overlay(self, value):
        try:
            try:
                image_file = Image.open("./temp/temp.png")
            except Exception as e:
                image_file = Image.open(f"./source/{self.filename}")
        except Exception as e:
            print(Fore.RED + f"[ CRITICAL EXCEPTION ] {e}")
            self.remove_temp()
            return
        if self.verbose:
            print(Fore.MAGENTA + f"[ OVERLYING ] with {value}")
        # WATERMARK
        watermark = Image.open(f"./source/{value}").convert("RGBA")
        width, height = image_file.size
        transparent = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        transparent.paste(image_file, (0, 0))
        transparent.paste(watermark, (0, 0), mask=watermark)
        transparent.save("./temp/temp.png", format="png")

    def rotation(self, value):
        try:
            try:
                image_file = Image.open("./temp/temp.png")
            except Exception as e:
                image_file = Image.open(f"./source/{self.filename}")
        except Exception as e:
            print(Fore.RED + f"[ CRITICAL EXCEPTION ] {e}")
            self.remove_temp()
            return
        if self.verbose:
            print(Fore.YELLOW + f"[ ROTATION ] {value} degrees")
        image_file = image_file.rotate(value)
        image_file.save("./temp/temp.png", format="png")

    def show_image(self):
        image_file = Image.open(f"./output/{self.output}.{self.ext}")
        image_file.show()
        if self.verbose:
            print(Fore.GREEN + f"[ IMAGE SHOWED ]")

    def save_image(self):
        image_file = Image.open("./temp/temp.png")
        image_file.save(f"./output/{self.output}.{self.ext}", format="png")
        if self.verbose:
            print(Fore.GREEN + f"[ IMAGE SAVED ]")

    def remove_temp(self):
        os.remove("./temp/temp.png")
        if self.verbose:
            print(Fore.GREEN + f"[ TEMP IMAGE REMOVED ]")

    def execute(self):
        args = vars(self.options)
        self.filename = args["filename"]
        self.output = args["output"].replace(".", "")
        self.ext = args["ext"]
        self.verbose = args["verbose"]
        self.show = args["show"]
        if self.verbose:
            print(Fore.GREEN + "[ INITIALIZED ]")
        # VALIDATIONS
        for oe in self.order:
            if oe == "gray_scale":
                if isinstance(args[oe], list):
                    self.gray_scale(args[oe][self.indexes[oe]])
                    self.indexes[oe] = self.indexes[oe] + 1
            if oe == "overlay":
                if isinstance(args[oe], list):
                    self.overlay(args[oe][self.indexes[oe]])
                    self.indexes[oe] = self.indexes[oe] + 1
            if oe == "rotate":
                if isinstance(args[oe], list):
                    self.rotation(args[oe][self.indexes[oe]])
                    self.indexes[oe] = self.indexes[oe] + 1
        self.save_image()
        self.remove_temp()
        if self.show:
            self.show_image()


if __name__ == "__main__":
    command = ArgumentOptions()
    command.execute()
