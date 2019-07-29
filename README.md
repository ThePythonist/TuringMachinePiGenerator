# Turing Machine Pi Generator

This repo contains code from my paper "Generating Pi With A Turing Machine".

## Using the simulator
The file `turing.py` is a turing machine simulator. To use it, simply call it from the command line, as pass as a paramater the path to the Turing machine program you want to run, e.g.

```
python3 turing.py pi.tur
```

## Using the generator
The file `generate.py` is used to generate the file `pi.tur`, which will contain the set of rules for the Turing machine program described in my paper to generate approximations of pi. Its usage is as follows:

```
python3 generate.py
```
