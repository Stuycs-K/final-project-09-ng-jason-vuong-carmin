[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ecp4su41)
# THIS DOCUMENT IS REQUIRED

## Group Info

Group Members: <br>
Carmin Vuong and Jason Ng (period 9)

Group Name: <br>
<b>The Moggers</b>

## Overview
We implemented a cipher called the <b>chaocipher</b>. In the ```ciphercode``` directory, you can find python code to use the chaocipher. It includes ```chaocipher.py```, which is used for the more traditional chaocipher (that only uses text encoding). To run, you should use this command: 

```
python3 chaocipher.py
```
This program takes in input from the terminal in order to perform the cipher. 

Then, we decided to create a program that takes in bytes as inputs. We extrapolated the chaocipher to an arbitrary keylength (but it <b>has</b> to be greater than <b>two</b> characters in order for the cipher to work properly). This program is ```cipher2.py```. To use this program, you should either use 
```
python3 cipher2.py [CIPHER FILE] [KEY FILE] [INPUT FILE] [OUTPUT FILE] [encrypt/decrypt]
```

There is an included makefile, however that makefile uses ```cipher.dat``` as the ```[CIPHER FILE]``` , ```plain.dat``` as the ```[KEY FILE]``` and ```output.dat``` as the ```[OUTPUT FILE]```. You can run ```make encrypt``` or ```make decrypt``` and set ```ARGS="[INPUT FILE]"```. 

Note: 

## Instructions
