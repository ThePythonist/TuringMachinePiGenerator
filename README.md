# Turing Machine Pi Generator

This repo contains code from my paper "Generating Pi With A Turing Machine".

## Using the simulator
The file `turing.py` is a turing machine simulator. It has no prerequisites other than pygame. To use it, simply call it from the command line, as pass as a paramater the path to the Turing machine program you want to run, e.g.

```
python3 turing.py pi.tur
```

If you would like to specify the initial contents of the tape, pass a string containing the contents as an additional parameter. Each character of the string will be written into a separate cell. (Note that space characters in the string will be treated as blank cells on the tape.)

```
python3 turing.pu pi.tur "12345"
```

The above will always carry the assumption that the read/write head starts over the first character in the string (position 0). If you would like to specify a different position for the read/write head, pass this as an additional parameter, e.g. running

```
python3 turing.pu pi.tur "12345" 2
```
would cause the read/write head to start over the cell containing the symbol "3".

Once the simulator is running, the controls are the following:
* Space: Toggle manual mode
* Enter: Run one step of the simulation (only works in manual mode)
* Left/Right arrow keys: Change speed
* T: Toggle between "static head" and "static tape" view
* Escape: Exit simulator


## Using the generator
The file `generate.py` is used to generate the file `pi.tur`, which will contain the set of rules for the Turing machine program described in my paper to generate approximations of pi. Its usage is as follows:

```
python3 generate.py
```
