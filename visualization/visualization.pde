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
  
   
}

String rotate(String string, char first) {
  while (string.charAt(0) != first) {
    // stub
  }  
  return string;
}


void draw() {
  wheel1.display();
  wheel2.display();
  
}
