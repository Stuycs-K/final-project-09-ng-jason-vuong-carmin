[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ecp4su41)
# THIS DOCUMENT IS REQUIRED

## Group Info

Group Members: <br>
Carmin Vuong and Jason Ng (period 9)

Group Name: <br>
<b>The Moggers</b>

## Overview
We implemented a cipher called the <b>chaocipher</b> (a further explanation of the chaocipher will be provided in ```PRESENTATION.md```). This is a cipher that doesn't need computers, however it is helpful to use a computer to perform the cipher quickly and do the visualizations. 

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

### Visualization

The folder ```visualization``` is a visualization of the traditional chaocipher built on processing.

To run the program, open the processing file ```visualization.pde``` and click the run button in the top left. This program offers a <b>manual</b> experience of encoding / decoding text, allowing the user to see how inner workings of how the Chaocipher works.

#### Controls:
```LEFT-CLICK``` - rotates the disks OUTWARDS (left disk CCW right disk CW)

```RIGHT-CLICK``` - rotates the disks INWARDS (left disk CW right disk CCW)

```SPACE``` - choose the desired letter at the zenith + permutes both disks

```R``` - reset everything

As the plaintext / ciphertext is being exhausted, the encrypted and decrypted letters will be recorded at the bottom of the screen as the user manually chooses letters.

# [Presentation Link](https://drive.google.com/drive/folders/11QtJvnoM9cA_z2xoLuF2V6FjH790Enbj?usp=sharing)
