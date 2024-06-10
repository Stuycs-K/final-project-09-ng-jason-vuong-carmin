[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ecp4su41)
# THIS DOCUMENT IS REQUIRED

## Group Info

Group Members: <br>
Carmin Vuong and Jason Ng (period 9)

Group Name: <br>
<b>The Moggers</b>

## Overview
We implemented a cipher called the <b>chaocipher</b>. This is a cipher that doesn't need computers, however it is helpful to use a computer to perform the cipher quickly and do the visualizations. 

We decided to split the project up into three main parts: the cipher, the visualization, and the TryHackMe. After we finished the cipher part, we decided to create a program that takes in bytes for the key inputs. We decided to extrapolate the chaocipher to an arbitrary keylength, and that has become the basis for Task 2 of our THM. 


Note: 

## Instructions
In the ```ciphercode``` directory, you can find python code to use the chaocipher. It includes ```chaocipher.py```, which is used for the more traditional chaocipher (that only uses text encoding). To run, you should use this command: 

```
python3 chaocipher.py
```
This program takes in input from the terminal in order to perform the cipher. 

The program that uses bytes instead of just characters is called ```cipher2.py```. To use this program, you should either use 
```
python3 cipher2.py [CIPHER FILE] [PlAIN FILE] [INPUT FILE] [OUTPUT FILE] [encrypt/decrypt]
```

Note: the key files <b>have</b> to be greater than <b>two</b> characters in order for the cipher to work properly. 

There is an included makefile, however that makefile uses ```cipher.dat``` as the ```[CIPHER FILE]``` , ```plain.dat``` as the ```[PLAIN FILE]``` and ```output.dat``` as the ```[OUTPUT FILE]```. You can run ```make encrypt``` or ```make decrypt``` and set ```ARGS="[INPUT FILE]"```. 

The last file in the directory, ```generator.py```, serves as a generate key function for the bit operations.

The folders ```task1``` and ```task2``` contain all the material for the tasks in the THM. You can access those tasks by going to the [TryHackMe Room](https://tryhackme.com/jr/chaocipher) itself.

The folder ```visualization``` is a visualization of the traditional chaocipher built on processing. 
