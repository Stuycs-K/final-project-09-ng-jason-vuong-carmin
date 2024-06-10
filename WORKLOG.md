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
- finished encryption and decryption 
- wrote helper methods 
- refactored some code 

### 5/29/2024
Added a way to take in inputs for the cipher 
- made checks to ensure that the keys were of the same length
- made sure to reject the plain key if they did not contain the proper set of characters 

### 5/30/2024
Trying to reformat the cipher to accept files as inputs 
- want to make this cipher available for byte data, not just chars 
- attempted to make a bytearray, but this did not work

### 5/31/2024 
Worked on getting byte data to work
- make a makefile to speed up the workflow
- figured out a way to open files using the "wb"/"rb" modes

### 6/03/2024 
Finally got the bytes to go from one thing to another
- still doesn't not display properly
- nevermind, figured out it was an issue with .upper in the decrypt method
Started work on the TryHackMe. Looked at a video about VMs and quickly realized that yes, this would be way harder than I thought. 
- updated the TryHackMe to have two different tasks 

### 6/05/2024 
Working on the THM 

### 6/07/2024 
- Refactored some code that was wrong 
- Tested some more code to see if something breaks
- used a base58 calculator for the code 

### 6/09/2024
Finished the Tryhackme 
- tested all the cases 
- made the folders for each task
Updated Readme


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

# References/Resources Used
- [Wikipedia article for Chaocipher](https://en.wikipedia.org/wiki/Chaocipher)
- [Dcode.fr](https://www.dcode.fr/chao-cipher)
- Mr. K
- [Medium article for creating THM Rooms](https://medium.com/@cykn0x/so-you-wanna-create-a-room-on-tryhackme-95e6c64543ca)