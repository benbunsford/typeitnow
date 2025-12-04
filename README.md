
# type-it

type-it is a terminal-based game inspired by Bop It.
As the player, you're tasked with typing in the words presented
to you before the timer runs out.
It has multiple difficulties, and can be played for fun
or to practice touch-typing.
The initial idea was to have the player press a single key,
which is more similar to Bop It.
That idea was more fun to implement, but less fun to play(to me).
Maybe I'll add it back as an option. Hope you have fun! :)

## OS

type-it works on Linux. It should work on Mac and Windows as well,
but has not been tested.

## Installation

1. FluidSynth (2.0.0 or later) is required. You can find instructions on how
to install it here: [FluidSynth Download](https://github.com/FluidSynth/fluidsynth/wiki/Download)
2. Install type-it with pip.

    ```sh
    pip install type-it
    ```

3. Add the .sf2 file so the audio sounds right.
    - Download `undertale.sf2` from the latest Github Release page in this
repository - [release page](https://github.com/benbunsford/type-it/releases/tag/v0.1.0-alpha)
    - Put it in `type-it/src/music`
4. Run type-it in your terminal.

    ```sh
    type-it
    ```

## TODO

- add high score tracking
- re-implement single-key mode
