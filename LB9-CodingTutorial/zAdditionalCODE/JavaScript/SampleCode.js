// PS5JS Sample Code
// https://p5js.org/tutorials/setting-up-your-environment/

function setup() {
  createCanvas(800, 400);
}
function draw() {
  //when mouse button is pressed, circles turn black
  if (mouseIsPressed === true) {
    fill(0);
  } else {
    fill(255);
  }

  //white circles drawn at mouse position
  circle(mouseX, mouseY, 100);
}