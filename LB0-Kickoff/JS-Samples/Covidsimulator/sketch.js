/* 
  Covid-19 infection dynamics simulation with moving people
  ---------------------------------------------------------
  Library : p5.js
  
  V1.0 : April 2020 dbe - initial version
  
  to dos
  - reenter objects at the boundary of the canvas (bounce or mirror)
  - simulate clustering in movements
  - variation in individual object moving, add barriers and bottlenecks
  - infect depends on distance, time and age
  - add multiple health status (healthy, infected, recovered, dead)
  - ....
  
  Links/Ressources
  - https://www.covid19sim.org/documents/outbreak-methods

*/

var person = [];       						// array of person objects
var CmaxNoPerson = 500;           // max No of person to create for simulation
var CmaxSpeedX = 5;   						 // max horizontal speed of a person in a single move step
var CmaxSpeedY = 2;    						 // max vertical speed of a person in a single move step
var CmaxDiameter = 20;  					// max person diameter, equls person age
var CstartInfectionspread = 3000; // start infection spreading after 3 secs

/*
  Setup the canvas, create array of Person objects
*/
function setup() {
  createCanvas(1000, 600);
  // Create objects
  for (var i=0; i<CmaxNoPerson; i++) {
    person.push(new InitPerson());
  }
}

/*
  Execute the simulation
  - move each person object
  - check/update for infection
  - show the (in time) situation
*/

function draw() {
  background(50, 89, 100);
  randomSeed(0);
  for (var i=0; i<person.length; i++) {
    person[i].move();
    person[i].infection();
    person[i].display();
  }
}


/* 
  InitPerson class and functions
*/
function InitPerson() {
  this.x = random(width);
  this.y = random(height);
  this.diameter = random(5, CmaxDiameter);
  var zufall = random(0,100);
  if (zufall > 0.5) {this.health = 0} else {this.health = 1};
  // this.health = 0;
  
  this.infection = function() {
  	var currentTime = millis();
  	if (currentTime >= CstartInfectionspread) {
  	  if (this.health == 0) {if (random(0,100) <= 5) {this.health = 1}}
    }
  };

  this.move = function() {
    var speedX = random(0,CmaxSpeedX);
    var speedY = random(0,CmaxSpeedY);
    var nextX = this.x;
    var nextY = this.y;
    // this.x += random(-this.speed, this.speed);
    // this.y += random(-this.speed, this.speed);
    this.x += random(-speedX, speedX);
    // nextX += random(-speedX, speedX);
    // this.x = nextX;
    // if (nextX >= width){this.x = width - abs(nextX-width)};
    // if (nextX <=0) {this.x = abs(nextX)};
    this.y += random(-speedY, speedY);
    // nextY += random(-speedY, speedY);
    // this.y += nextY;
    // if (nextY >= width){this.y = width - abs(nextY-width)};
    // if (nextY <=0) {this.y = abs(nextY)};
    
  };

  this.display = function() {
  	// noFill();
  	fill(255,255,255);
  	if (this.health == 1){fill(255,0,0)};
  	ellipse(this.x, this.y, this.diameter, this.diameter);
  	// print(this.health);
  	
  };
}
