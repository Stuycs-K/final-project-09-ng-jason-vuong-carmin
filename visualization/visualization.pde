Wheel wheel1, wheel2;
color BG_COLOR = #D1D1D1;
color WHEEL_COLOR= #3ECEF7;
color GREEN = #1DD306;
color LIGHT_GREEN = color(0, 255, 0);
String encrypted;
String decrypted;
String a1, a2;

void setup() {
  size(1200, 800);
  background(BG_COLOR); // gray
  noStroke();

  fill(WHEEL_COLOR);
  a1 = "QWERTYUIOPASDFGHJKLZXCVBNM".toUpperCase();
  a2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toUpperCase();
  wheel1 = new Wheel(345, 300, a1);
  wheel2 = new Wheel(855, 300, a2);

  encrypted = "";
  decrypted = "";


  //wheel2.alphabet = reverse_word(wheel2.alphabet); // for the reversed wheels
}

String rotate(String string) { // ABCDE --> BCDEA
  //while (string.charAt(0) != first) {
  string = string.substring(1, string.length()) + string.substring(0, 1);
  //}
  return string;
}

String rot(String string) {
  string = string.substring(0, 1)+string.substring(2, 14)+string.substring(1, 2)+string.substring(15,string.length());
  return "";
}

String unrotate(String string) { // ABCDE --> EABCD
  //while (string.charAt(0) != first) {
  string = string.substring(string.length()-1, string.length()) + string.substring(0, string.length()-1);
  //}
  return string;
}

String permuteLeft(String string) {
  string = string.substring(0, 1)+string.substring(2, 14)+string.substring(1, 2)+string.substring(14,string.length());
  return string;
}

String permuteRight(String string) {
  string = rotate(string);
  string = string.substring(0, 2)+string.substring(3, 14)+string.substring(2, 3)+string.substring(14,string.length());
  //println(string);
  //println(newString);
  return string;
}


void rotateIn() {
  wheel1.alphabet = unrotate(wheel1.alphabet);
  wheel2.alphabet = unrotate(wheel2.alphabet);
}

void rotateOut() {
  wheel1.alphabet = rotate(wheel1.alphabet);
  wheel2.alphabet = rotate(wheel2.alphabet);
}

String reverse_word(String word) {
  String newWord = "";
  for (int i = word.length()-1; i >= 0; i--) {
    newWord += word.charAt(i);
  }
  return newWord;
}

void draw() {
  background(BG_COLOR);
  wheel1.displayCW();
  wheel2.displayCCW();

  textAlign(CENTER, CENTER);
  textSize(50);
  fill(GREEN);
  text("ciphertext", 345, 300);
  fill(255, 0, 0);
  text("plaintext", 855, 300);
  fill(WHEEL_COLOR);
  
  // words
  fill(0);
  text("encrypted: "+encrypted, width/2, height-50);
  text("decrypted: "+decrypted, width/2, height-150);
  fill(WHEEL_COLOR);

}

void mousePressed() {
  if (mouseButton == RIGHT) {
    rotateIn();
  } else if (mouseButton == LEFT) {
    rotateOut();
  }
}

void keyPressed() {
  if (key == ' ') { // WHEN YOU FIND THE LETTER
    encrypted += wheel1.alphabet.charAt(0);
    decrypted += wheel2.alphabet.charAt(0);
    //println(encrypted);
    //println(decrypted);
   
    wheel1.alphabet = permuteLeft(wheel1.alphabet);
    wheel2.alphabet = permuteRight(wheel2.alphabet);
    //println(wheel1.alphabet);
    //println(wheel2.alphabet);
  }
  else if (key == 'r') {
    wheel1.alphabet = a1;
    wheel2.alphabet = a2;

    encrypted = "";
    decrypted = "";  
  }
}
