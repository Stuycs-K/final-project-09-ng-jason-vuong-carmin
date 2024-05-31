class Wheel {
  int cx, cy;
  String alphabet;
  int r = 500;

  Wheel(int cx, int cy, String alphabet) { // constructor
    this.cx = cx;
    this.cy = cy;
    this.alphabet = alphabet;
  }

  void drawSpokesAndLettersCW() {
    stroke(BG_COLOR);
    strokeWeight(4);
    for (int i = 0; i < alphabet.length(); i++) {
      int endx =  (int) (cx + cos(i*2*PI/26)*r/2);
      int endy = (int) (cy + sin(i*2*PI/26)*r/2);
      if (i == 0) { // zenith
        fill(255, 0, 0);
        textSize(40);
      } else {
        fill(255, 255, 255);
        textSize(30);
      }
      textAlign(CENTER, CENTER);
      text(alphabet.charAt(i), cx + cos(i*2*PI/26+PI/26-14*PI/26)*(r/2-25), cy + sin(i*2*PI/26+PI/26-14*PI/26)*(r/2-25));
      fill(WHEEL_COLOR);
      line(cx, cy, endx, endy);
    }
    noStroke();
  }
  
  void drawSpokesAndLettersCCW() {
    stroke(BG_COLOR);
    strokeWeight(4);
    for (int i = 0; i < alphabet.length(); i++) {
      int endx =  (int) (cx + cos(i*2*PI/26)*r/2);
      int endy = (int) (cy + sin(i*2*PI/26)*r/2);
      if (i == 0) { // zenith
        fill(255, 0, 0);
        textSize(40);
      } else {
        fill(255, 255, 255);
        textSize(30);
      }
      textAlign(CENTER, CENTER);
      text(alphabet.charAt(i), cx + cos(-i*2*PI/26+PI/26-14*PI/26)*(r/2-25), cy + sin(-i*2*PI/26+PI/26-14*PI/26)*(r/2-25));
      fill(WHEEL_COLOR);
      line(cx, cy, endx, endy);
    }
    noStroke();
  }
  

  void displayCW() {
    circle(cx, cy, r);
    fill(BG_COLOR);
    circle(cx, cy, r-100);
    fill(WHEEL_COLOR);
    drawSpokesAndLettersCW();
  }
  
  void displayCCW() {
    circle(cx, cy, r);
    fill(BG_COLOR);
    circle(cx, cy, r-100);
    fill(WHEEL_COLOR);
    drawSpokesAndLettersCCW();
  }

  void rotate_out() {
  }
}
