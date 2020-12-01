import argparse
import sys


class ArgumentOptions:
    parser = None
    options = None

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Image Converter Command Interface"
        )

    def set_args_options(self, args=sys.argv[1:]):

        self.parser.add_argument(
            "-v", "--verbose", dest="verbose", help="verbose mode."
        )
        self.options = self.parser.parse_args(args)


if __name__ == "__main__":
    print(sys.argv[1:])
    command = ArgumentOptions()
    command.set_args_options(sys.argv[1:])
    if command.options.verbose:
        print("Verbose mode on")
    else:
        print("Verbose mode off")
