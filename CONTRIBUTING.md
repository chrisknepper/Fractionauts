Contributing to Fractionauts
=================
Interested in contributing to the development of Fractionauts?
Awesome! You'd be helping children learn math and further solidfying your place in the free and open source development community.

Submitting Code
-----------------
All work on this project is done via this Github repository. If you'd like to squash a bug or implement a new feature, consider making it an issue in the Github issue tracker. This way, all contributors are aware of bugs/feature requests and work is less likely to be duplicated.

When you're ready to submit code, submit a pull request with your changes. Patches are welcome!

Technical Inner-Workings
-----------------
Fractionauts is written in Python 2. It uses the excellent [PyGame](http://www.pygame.org/news.html) library and is designed to run on the One Laptop Per Child XO-PC.

### Running The Game
It is highly recommended to use a Linux distribution when running or developing Fractionauts. The game requires Python and some dependencies and has not been tested to work on Windows or OSX, though it might be possible.

### Level File Format
Levels in Fractionauts are represented by JSON files. They are titled sequentially, numerically, starting at 0 (0.json, 1.json, etc...)

The JSON files have a relatively simple structure, consisting of three main parts:
* *type*, which is the type of fraction math the question involves. This can be addition, subtraction, multiplication, or division
* *options*, which is an array of answers the user can select
* *answer*, which is the correct or goal answer the user should arrive at