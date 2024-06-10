# Work Log

## Jason Ng

### 5/22/2024 

Worked on getting everything set up 
- networking files
- encrypt & decrypt
- did some research on RSA/blowfish/other algorithms
- set up the THM

### 5/23/2024

Pivoted ideas so worked on researching primarily 
- coded encrypt and decrypt 
- encrypt and decrypt aren't entirely accurate, however; need to go back and fix that 

### 5/28/2024
Mostly worked on coding the algorithm
- finished encryption and encryption 
- wrote helper methods 
- refactored some code 

## Carmin Vuong

### 5/23/2024
Found new idea of Chaociphers <br>
Worked on visualization part of this project using Processing
- made 2 wheels (Wheel class)
- added spokes for visual appeal
- added letters

### 5/28/2024
work on rotation of the cipher wheel
- allowed CCW rotation of left wheel + CW rotation of the right wheel


### 5/29/2024
make other rotation possible + control using mouse buttons
- make zenith position RED and BIG and on the top
- tell Jason chaocipher's alphabet is generated reversed

### 5/30/2024
attempt to implement the reversed order of the wheels
- doesn't work
- better implementation could be make 2 separate methods todisplay the letters
- one is CW and one is CCW (starts at zenith)

### 5/31/2024
make code cleaner with more methods
- added displayCW and displayCCW methods inside Wheel class
- need to add permutatation

### 6/3/2024
start permute function
- use substrings

### 6/5/2024
finish permute function
- for left and right wheel
- manual control using space bar agfter choosing a letter

add nadir and fix coloring
- added labels for both wheels

test out encoding and decoding but it doesn't work
- need to confirm with dcode.fr if my implementation is correct

### 6/9/2024
- added reset button + displays on screen
- fix permuting using dcode.fr
