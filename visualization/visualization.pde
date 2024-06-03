Wheel wheel1, wheel2;
color BG_COLOR = #D1D1D1;
color WHEEL_COLOR = #3CC1F0;

void setup() {
  size(1200, 800);
  background(BG_COLOR); // gray
  noStroke();
  
  fill(WHEEL_COLOR);
  wheel1 = new Wheel(345, 400, "QWERTYUIOPASDFGHJKLZXCVBNM");
  wheel2 = new Wheel(855, 400, "abcdefghijklmnopqrstuvwxyz".toUpperCase());
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
    println(string.substring(0, 14));
    return "hi";
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
  
  //println(reverse_word("penis"));
  
  
}

void mousePressed() {
  if (mouseButton == RIGHT) rotateIn();
  else if (mouseButton == LEFT) rotateOut();
  
  println(permute(wheel2.alphabet));
  
}
