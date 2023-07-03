// auto thumbnail generation script: https://timrodenbroeker.de/courses/sketching-with-code/thumbnails/
String sketchname = getClass().getName();

void setup(){
    size(1080,1080);
}

void draw(){

  if (frameCount ==  120) {
    saveFrame("../" + sketchname + ".png");
  }
}

