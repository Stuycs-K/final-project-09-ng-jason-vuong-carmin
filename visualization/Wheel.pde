class Wheel {
  int cx, cy;
  String alphabet;
  int r = 500;

  Wheel(int cx, int cy, String alphabet) { // constructor
    this.cx = cx;
    this.cy = cy;
    this.alphabet = alphabet;
  }
  
  
  void display() {
    circle(cx, cy, r);
    fill(BG_COLOR);
    circle(cx, cy, r-100);
    fill(WHEEL_COLOR);
  }

}
