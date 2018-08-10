
var i = 0;
function changeimage(){
  // 1 = flowers >> ferris wheel
  // 2 = ferris wheel >> coke bottle
  // 3 = coke bottle >> night sky 2
  // 4 = night sky 2 >> flower lights
  // 5 = flower lights >> flowers

  i+=1;

  if(i==1) {
    document.getElementById("image_one").src = "ferriswheel.jpg";
  }
  else if (i == 2) {
    document.getElementById("image_one").src = "cokebottle.jpg";
  }
  else if (i == 3) {
    document.getElementById("image_one").src = "nightsky2.jpg";
  }
  else if (i == 4) {
    document.getElementById("image_one").src = "flowerlights.jpg";
  }
  else if (i == 5){
    i = 0;
    document.getElementById("image_one").src = "http://cdn3.balconygardenweb.com/wp-content/uploads/2015/08/most-poisonous-flowers-3_mini.jpg";
  }
}
