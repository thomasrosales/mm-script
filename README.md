### Python coding challenge

This exercise is not related to web development. This is on purpose because frameworks like Django and Flask
dictate a common way of working. For this reason we use this test to see more generic programming skills
and creativity.

### Exercise

Create a commandline script that applies 1 or more filters to an image and saves it as a new file.

The filters should be:

1. `gray_scale` convert the image to black and white.
2. `overlay` overlay a given image on top of the source.
3. `rotate` rotate N degrees. (no need for resizing/cropping)
4. Optionally, make up your own filter. Not required.

Other requirements:

- (x) All parameters should be given in one line. (no interactive approach using `input()`)
- (x) Each filter should be optional.
- (x) The order of filters is important since we want to be able to control if the overlay will become black and white or not.
- (x) The source image should be given as a filename on the command line.
- (x) The overlay image should also be given as a filename on the command line and should be a transparent png.
- (x) The number of degrees should be given on the command line.
- (x) The output file should be given as a filename on the command line. (Support saving as png and jpg)
- (x) Allow applying a filter more than once. (for example: gray_scale > rotate > overlay > rotate)
- Think about extensibility. How can you make it easy (for future you) to allow adding a new filter without changing a lot of code.
- Add unittests to test individual components of your program. Add instructions on how to run the tests.
- Follow PEP8 guidelines.

Images input.jpg and overlay.png are provided to save you a little time.

Provide a zip file with the script and a README with instructions on how to use it.
Also include how much time you spent on it.
