Wheel wheel1, wheel2;
color BG_COLOR = #D1D1D1;
color WHEEL_COLOR= #3ECEF7;
color GREEN = #1DD306;
color LIGHT_GREEN = color(0, 255, 0);
String encrypted;
String decrypted;

void setup() {
  size(1200, 800);
  background(BG_COLOR); // gray
  noStroke();
  
  fill(WHEEL_COLOR);
  wheel1 = new Wheel(345, 300, "QWERTYUIOPASDFGHJKLZXCVBNM");
  wheel2 = new Wheel(855, 300, "abcdefghijklmnopqrstuvwxyz".toUpperCase());
  
  encrypted = "";
  decrypted = "";
  
  
  //wheel2.alphabet = reverse_word(wheel2.alphabet); // for the reversed wheels
  
   
}

String rotate(String string) {
  //while (string.charAt(0) != first) {
   string = string.substring(1, string.length()) + string.substring(0, 1);
  //}  
  return string;
}

String unrotate(String string) {
  //while (string.charAt(0) != first) {
   string = string.substring(string.length()-1, string.length()) + string.substring(0, string.length()-1);
  //}  
  return string;
}

String permute(String string) {
    String newString = string.substring(0,13)+string.charAt(25)+string.substring(13,25);
    //println(string);
    //println(newString);
    return newString;
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
  wheel1.displayCW();
  wheel2.displayCCW();
  
  textAlign(CENTER, CENTER);
  textSize(50);
  fill(GREEN);
  text("ciphertext", 345, 300);
  fill(255, 0, 0);
  text("plaintext", 855, 300);
  fill(WHEEL_COLOR);
  
  //println(reverse_word("penis"));
  
  
}

void mousePressed() {
  if (mouseButton == RIGHT) {
    rotateIn();
  }
  else if (mouseButton == LEFT) {
    rotateOut();
  
  }
  
  
}

void keyPressed() {
  if (key == ' ') { // WHEN YOU FIND THE LETTER
    encrypted += wheel1.alphabet.charAt(0);
    decrypted += wheel2.alphabet.charAt(0);
    println(encrypted);
    println(decrypted);
    wheel1.alphabet = permute(wheel1.alphabet);
    wheel2.alphabet = permute(wheel2.alphabet);
  }
}
