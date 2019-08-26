
import os
import redis
from flask import Flask, render_template, redirect, request, url_for, make_response
import datetime
import requests
import json


r = redis.Redis(host='', port='', password='')



app = Flask(__name__)

@app.route('/')
def mainmenu():
    

    response = """
<!DOCTYPE html>
<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<body id="myPage">

<!-- Sidebar on click -->
<nav class="w3-sidebar w3-bar-block w3-white w3-card w3-animate-left w3-xxlarge" style="display:none;z-index:2" id="mySidebar">
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-bar-item w3-button w3-display-topright w3-text-teal">Close
    <i class="fa fa-remove"></i>
  </a>
  <a href="#" class="w3-bar-item w3-button">Link 1</a>
  <a href="#" class="w3-bar-item w3-button">Link 2</a>
  <a href="#" class="w3-bar-item w3-button">Link 3</a>
  <a href="#" class="w3-bar-item w3-button">Link 4</a>
  <a href="#" class="w3-bar-item w3-button">Link 5</a>
</nav>

<!-- Navbar -->
<div class="w3-top">
 <div class="w3-bar w3-theme-d2 w3-left-align">
  <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-hover-white w3-theme-d2" href="javascript:void(0);" onclick="openNav()"><i class="fa fa-bars"></i></a>
  <a href="#" class="w3-bar-item w3-button w3-teal"><i class="fa fa-pied-piper-alt w3-xlarge w3-margin-right"></i>Piper Project</a>
  <a href="#ourteam" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Our Team</a>
  <a href="lovelyhome.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Lovely Home</a>
  <a href="demo.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Demo</a>
  <a href="dashboard.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Dashboard</a>
  <a href="#" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-teal" title="Search"><i class="fa fa-search"></i></a>
 </div>

  <!-- Navbar on small screens -->
  <div id="navDemo" class="w3-bar-block w3-theme-d2 w3-hide w3-hide-large w3-hide-medium">
    <a href="#author" class="w3-bar-item w3-button">Author</a>
    <a href="#lovely home" class="w3-bar-item w3-button">Lovely Home</a>
    <a href="#demo" class="w3-bar-item w3-button">Demo</a>
    <a href="#dashboard" class="w3-bar-item w3-button">Dashboard</a>
    <a href="#" class="w3-bar-item w3-button">Search</a>
  </div>
</div>

<!-- Image Header -->
<div class="w3-display-container w3-animate-opacity">
  <img src="static/frontimage.jpg" alt="boat" style="width:100%;min-height:350px;max-height:1000px;">
  <br><br><br><br>
</div>

<!-- ourteam Container -->
<div class="w3-container w3-padding-64 w3-center" id="ourteam">
<h2>OUR TEAM</h2>
<p>Piped Piper</p>

<div class="w3-row"><br>

<div class="w3-half">
  <img src="static/Fiona_1.JPG" alt="Author" style="width:45%" class="w3-circle w3-hover-opacity">
  <h3>Fiona Liu</h3>
  <h4>Author</h4>
</div>

<div class="w3-half">
  <img src="static/Jonas_1.jpg" alt="Author" style="width:40%" class="w3-circle w3-hover-opacity">
  <h3>Jonas Werner</h3>
  <h4>Mentor</h4>
</div>


</div>
</div>

<!-- Footer -->
<footer class="w3-container w3-padding-32 w3-theme-d1 w3-center">
  <h4>Follow Us</h4>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Facebook"><i class="fa fa-facebook"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Twitter"><i class="fa fa-twitter"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-google-plus"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-instagram"></i></a>
  <a class="w3-button w3-large w3-teal w3-hide-small" href="javascript:void(0)" title="Linkedin"><i class="fa fa-linkedin"></i></a>
  <p>Powered by PipedPiper</p>

  <div style="position:relative;bottom:100px;z-index:1;" class="w3-tooltip w3-right">
    <span class="w3-text w3-padding w3-teal w3-hide-small">Go To Top</span>   
    <a class="w3-button w3-theme" href="#myPage"><span class="w3-xlarge">
    <i class="fa fa-chevron-circle-up"></i></span></a>
  </div>
</footer>

<script>
// Script for side navigation
function w3_open() {
  var x = document.getElementById("mySidebar");
  x.style.width = "300px";
  x.style.paddingTop = "10%";
  x.style.display = "block";
}

// Close side navigation
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
}

// Used to toggle the menu on smaller screens when clicking on the menu button
function openNav() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}
</script>
</body>
</html>
    """
    return response



@app.route('/lovelyhome.html')
def lovelyhome():
    

    response = """
<!DOCTYPE html>
<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<body id="myPage">

<!-- Sidebar on click -->
<nav class="w3-sidebar w3-bar-block w3-white w3-card w3-animate-left w3-xxlarge" style="display:none;z-index:2" id="mySidebar">
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-bar-item w3-button w3-display-topright w3-text-teal">Close
    <i class="fa fa-remove"></i>
  </a>
  <a href="#" class="w3-bar-item w3-button">Link 1</a>
  <a href="#" class="w3-bar-item w3-button">Link 2</a>
  <a href="#" class="w3-bar-item w3-button">Link 3</a>
  <a href="#" class="w3-bar-item w3-button">Link 4</a>
  <a href="#" class="w3-bar-item w3-button">Link 5</a>
</nav>

<!-- Navbar -->
<div class="w3-top">
 <div class="w3-bar w3-theme-d2 w3-left-align">
  <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-hover-white w3-theme-d2" href="javascript:void(0);" onclick="openNav()"><i class="fa fa-bars"></i></a>
  <a href="/" class="w3-bar-item w3-button w3-teal"><i class="fa fa-pied-piper-alt w3-xlarge w3-margin-right"></i>Piper Project</a>
  <a href="/#ourteam" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Our Team</a>
  <a href="lovelyhome.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Lovely Home</a>
  <a href="demo.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Demo</a>
  <a href="dashboard.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Dashboard</a>
  <a href="#" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-teal" title="Search"><i class="fa fa-search"></i></a>
 </div>

  <!-- Navbar on small screens -->
  <div id="navDemo" class="w3-bar-block w3-theme-d2 w3-hide w3-hide-large w3-hide-medium">
    <a href="#author" class="w3-bar-item w3-button">Author</a>
    <a href="#lovely home" class="w3-bar-item w3-button">Lovely Home</a>
    <a href="#demo" class="w3-bar-item w3-button">Demo</a>
    <a href="#dashboard" class="w3-bar-item w3-button">Dashboard</a>
    <a href="#" class="w3-bar-item w3-button">Search</a>
  </div>
</div>


<!-- Lovely Home Row -->
<div class="w3-row-padding w3-padding-64 w3-theme-l5" id="lovely home">

<div class="w3-quarter">
 <h2>"Lovely Home" Introduction</h2>
 <p>In this project, I am creating a smart Home AI, at the first sprint, there are 4 main functions:-</p>
 <p>1.User access web interface to tell AI "I am going home", ask AI to turn on light and ac via REST API </p>
 <p>2.User entering room, AI takes a photo, recognize owner and his/her mood, react with different actions </p>
 <p>3.IoT: sensor --> data --> EdgeX --> MQTT --> TurnON/OFF light and ac (REST API) according to the env </p>
 <p>4.Dashboard: presenting the data collected </p>
</div>

<div class="w3-quarter">
 <img src="static/flowchart2.jpg" style="width:100%;cursor:zoom-in" onclick="document.getElementById('modal01').style.display='block'" alt="Snow" >
</div>

<!-- Modal for full size images on click-->
<div id="modal01" class="w3-modal w3-black" style="padding-top:0" onclick="this.style.display='none'">
   <span class="w3-button w3-black w3-xxlarge w3-display-topright">x</span>
   <div class="w3-modal-content w3-animate-zoom w3-center w3-transparent w3-padding-64">
    <img src="static/flowchart2.jpg" style="width:100%">
   </div>
</div>

<div class="w3-quarter">
 <img src="static/flowchart2.jpg" style="width:100%;cursor:zoom-in" onclick="document.getElementById('modal02').style.display='block'" alt="Snow" >
</div>


<!-- Modal for full size images on click-->
<div id="modal02" class="w3-modal w3-black" style="padding-top:0" onclick="this.style.display='none'">
   <span class="w3-button w3-black w3-xxlarge w3-display-topright">x</span>
   <div class="w3-modal-content w3-animate-zoom w3-center w3-transparent w3-padding-64">
    <img src="static/flowchart2.jpg" style="width:100%">
   </div>
</div>



<div class="w3-quarter">
 <img src="static/flowchart2.jpg" style="width:100%;cursor:zoom-in" onclick="document.getElementById('modal03').style.display='block'" alt="Snow" >
</div>


<!-- Modal for full size images on click-->
<div id="modal03" class="w3-modal w3-black" style="padding-top:0" onclick="this.style.display='none'">
   <span class="w3-button w3-black w3-xxlarge w3-display-topright">x</span>
   <div class="w3-modal-content w3-animate-zoom w3-center w3-transparent w3-padding-64">
    <img src="static/flowchart2.jpg" style="width:100%">
   </div>
</div>

</div>

<!-- Container -->
<div class="w3-container" style="position:relative">
  <a onclick="w3_open()" class="w3-button w3-xlarge w3-circle w3-teal"
  style="position:absolute;top:-28px;right:24px">+</a>
</div>


<!-- Footer -->
<footer class="w3-container w3-padding-32 w3-theme-d1 w3-center">
  <h4>Follow Us</h4>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Facebook"><i class="fa fa-facebook"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Twitter"><i class="fa fa-twitter"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-google-plus"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-instagram"></i></a>
  <a class="w3-button w3-large w3-teal w3-hide-small" href="javascript:void(0)" title="Linkedin"><i class="fa fa-linkedin"></i></a>
  <p>Powered by PipedPiper</p>

  <div style="position:relative;bottom:100px;z-index:1;" class="w3-tooltip w3-right">
    <span class="w3-text w3-padding w3-teal w3-hide-small">Go To Top</span>   
    <a class="w3-button w3-theme" href="#myPage"><span class="w3-xlarge">
    <i class="fa fa-chevron-circle-up"></i></span></a>
  </div>
</footer>

<script>
// Script for side navigation
function w3_open() {
  var x = document.getElementById("mySidebar");
  x.style.width = "300px";
  x.style.paddingTop = "10%";
  x.style.display = "block";
}

// Close side navigation
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
}

// Used to toggle the menu on smaller screens when clicking on the menu button
function openNav() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}
</script>
</body>
</html>
    """

    return response
	


@app.route('/demo.html')
def demo():
    

    response = """
<!DOCTYPE html>
<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<body id="myPage">

<!-- Sidebar on click -->
<nav class="w3-sidebar w3-bar-block w3-white w3-card w3-animate-left w3-xxlarge" style="display:none;z-index:2" id="mySidebar">
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-bar-item w3-button w3-display-topright w3-text-teal">Close
    <i class="fa fa-remove"></i>
  </a>
  <a href="#" class="w3-bar-item w3-button">Link 1</a>
  <a href="#" class="w3-bar-item w3-button">Link 2</a>
  <a href="#" class="w3-bar-item w3-button">Link 3</a>
  <a href="#" class="w3-bar-item w3-button">Link 4</a>
  <a href="#" class="w3-bar-item w3-button">Link 5</a>
</nav>

<!-- Navbar -->
<div class="w3-top">
 <div class="w3-bar w3-theme-d2 w3-left-align">
  <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-hover-white w3-theme-d2" href="javascript:void(0);" onclick="openNav()"><i class="fa fa-bars"></i></a>
  <a href="/" class="w3-bar-item w3-button w3-teal"><i class="fa fa-pied-piper-alt w3-xlarge w3-margin-right"></i>Piper Project</a>
  <a href="/#ourteam" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Our Team</a>
  <a href="lovelyhome.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Lovely Home</a>
  <a href="demo.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Demo</a>
  <a href="dashboard.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Dashboard</a>
  <a href="#" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-teal" title="Search"><i class="fa fa-search"></i></a>
 </div>

  <!-- Navbar on small screens -->
  <div id="navDemo" class="w3-bar-block w3-theme-d2 w3-hide w3-hide-large w3-hide-medium">
    <a href="#author" class="w3-bar-item w3-button">Author</a>
    <a href="#lovely home" class="w3-bar-item w3-button">Lovely Home</a>
    <a href="#demo" class="w3-bar-item w3-button">Demo</a>
    <a href="#dashboard" class="w3-bar-item w3-button">Dashboard</a>
    <a href="#" class="w3-bar-item w3-button">Search</a>
  </div>
</div>

<!-- Demo Row -->
<div class="w3-row-padding w3-center w3-padding-64" id="demo">
    <h2>DEMO</h2>
    <p>Choose a DEMO you would like to see.</p><br>
    <div class="w3-third w3-margin-bottom">
      <ul class="w3-ul w3-border w3-hover-shadow">
        <li class="w3-theme">
          <p class="w3-xlarge">
            <a href="http://127.0.0.1:5000" class="w3-xlarge">I'm Going Home</a>
          </p>
        </li>
      </ul>
    </div>

    <div class="w3-third w3-margin-bottom">
      <ul class="w3-ul w3-border w3-hover-shadow">
        <li class="w3-theme-l2">
          <p class="w3-xlarge">Entering Room</p>
        </li>
      </ul>
    </div>

    <div class="w3-third w3-margin-bottom">
      <ul class="w3-ul w3-border w3-hover-shadow">
        <li class="w3-theme">
          <p class="w3-xlarge">Light & AC Auto Adjust</p>
        </li>
      </ul>
    </div>
</div>


<!-- Footer -->
<footer class="w3-container w3-padding-32 w3-theme-d1 w3-center">
  <h4>Follow Us</h4>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Facebook"><i class="fa fa-facebook"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Twitter"><i class="fa fa-twitter"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-google-plus"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-instagram"></i></a>
  <a class="w3-button w3-large w3-teal w3-hide-small" href="javascript:void(0)" title="Linkedin"><i class="fa fa-linkedin"></i></a>
  <p>Powered by PipedPiper</p>

  <div style="position:relative;bottom:100px;z-index:1;" class="w3-tooltip w3-right">
    <span class="w3-text w3-padding w3-teal w3-hide-small">Go To Top</span>   
    <a class="w3-button w3-theme" href="#myPage"><span class="w3-xlarge">
    <i class="fa fa-chevron-circle-up"></i></span></a>
  </div>
</footer>

<script>
// Script for side navigation
function w3_open() {
  var x = document.getElementById("mySidebar");
  x.style.width = "300px";
  x.style.paddingTop = "10%";
  x.style.display = "block";
}

// Close side navigation
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
}

// Used to toggle the menu on smaller screens when clicking on the menu button
function openNav() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}
</script>
</body>
</html>
    """

    return response
	



@app.route('/dashboard.html')
def dashboard():
    

    response = """
<!DOCTYPE html>
<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<body id="myPage">

<!-- Sidebar on click -->
<nav class="w3-sidebar w3-bar-block w3-white w3-card w3-animate-left w3-xxlarge" style="display:none;z-index:2" id="mySidebar">
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-bar-item w3-button w3-display-topright w3-text-teal">Close
    <i class="fa fa-remove"></i>
  </a>
  <a href="#" class="w3-bar-item w3-button">Link 1</a>
  <a href="#" class="w3-bar-item w3-button">Link 2</a>
  <a href="#" class="w3-bar-item w3-button">Link 3</a>
  <a href="#" class="w3-bar-item w3-button">Link 4</a>
  <a href="#" class="w3-bar-item w3-button">Link 5</a>
</nav>

<!-- Navbar -->
<div class="w3-top">
 <div class="w3-bar w3-theme-d2 w3-left-align">
  <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-hover-white w3-theme-d2" href="javascript:void(0);" onclick="openNav()"><i class="fa fa-bars"></i></a>
  <a href="/" class="w3-bar-item w3-button w3-teal"><i class="fa fa-pied-piper-alt w3-xlarge w3-margin-right"></i>Piper Project</a>
  <a href="/#ourteam" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Our Team</a>
  <a href="lovelyhome.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Lovely Home</a>
  <a href="demo.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Demo</a>
  <a href="dashboard.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Dashboard</a>
  <a href="#" class="w3-bar-item w3-button w3-hide-small w3-right w3-hover-teal" title="Search"><i class="fa fa-search"></i></a>
 </div>

  <!-- Navbar on small screens -->
  <div id="navDemo" class="w3-bar-block w3-theme-d2 w3-hide w3-hide-large w3-hide-medium">
    <a href="#author" class="w3-bar-item w3-button">Author</a>
    <a href="#lovely home" class="w3-bar-item w3-button">Lovely Home</a>
    <a href="#demo" class="w3-bar-item w3-button">Demo</a>
    <a href="#dashboard" class="w3-bar-item w3-button">Dashboard</a>
    <a href="#" class="w3-bar-item w3-button">Search</a>
  </div>
</div>



<!-- Dashboard Container -->
<div class="w3-container w3-padding-64 w3-theme-l5" id="dashboard">
  <!-- Header -->
  <header class="w3-container" style="padding-top:22px">
    <h5><b><i class="fa fa-dashboard"></i> My Dashboard</b></h5>
  </header>

  <div class="w3-row-padding w3-margin-bottom">
    <div class="w3-quarter">
      <div class="w3-container w3-red w3-padding-16">
        <div class="w3-left"><i class="fa fa-building-o w3-xxxlarge"></i></div>
        <div class="w3-right">
"""
    item = len(r.keys('*'))
    response += "<h3>" + str(item) + "</h3>"
    response += """
        </div>
        <div class="w3-clear"></div>
        <h4>Entries</h4>
      </div>
    </div>
    <div class="w3-quarter">
      <div class="w3-container w3-blue w3-padding-16">
        <div class="w3-left"><i class="fa fa-frown-o w3-xxxlarge"></i></div>
        <div class="w3-right">
"""
    t = t = datetime.datetime.now()
    t2 = t.strftime("%Y-%m")
    print t2
    sadface = 0
    for eachtimestamp in r.keys(t2+'*'):
        if r.hget(eachtimestamp, 'MODE') == "SAD":
            sadface += 1
    response += "<h3>" + str(sadface) + "</h3>"
    response += """
        </div>
        <div class="w3-clear"></div>
        <h4>Sad Mood in This Month</h4>
      </div>
    </div>
    <div class="w3-quarter">
      <div class="w3-container w3-teal w3-padding-16">
        <div class="w3-left"><i class="fa fa-bomb w3-xxxlarge"></i></div>
        <div class="w3-right">
"""
    t = t = datetime.datetime.now()
    t2 = t.strftime("%Y-%m")
    print t2
    angryface = 0
    for eachtimestamp in r.keys(t2+'*'):
        if r.hget(eachtimestamp, 'MODE') == "ANGRY":
            angryface += 1
    response += "<h3>" + str(angryface) + "</h3>"
    response += """
        </div>
        <div class="w3-clear"></div>
        <h4>Angry Mood in This Month</h4>
      </div>
    </div>
    <div class="w3-quarter">
      <div class="w3-container w3-orange w3-text-white w3-padding-16">
        <div class="w3-left"><i class="fa fa-users w3-xxxlarge"></i></div>
        <div class="w3-right">
          <h3>50</h3>
        </div>
        <div class="w3-clear"></div>
        <h4>Users</h4>
      </div>
    </div>
  </div>


</div>




<!-- Footer -->
<footer class="w3-container w3-padding-32 w3-theme-d1 w3-center">
  <h4>Follow Us</h4>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Facebook"><i class="fa fa-facebook"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Twitter"><i class="fa fa-twitter"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-google-plus"></i></a>
  <a class="w3-button w3-large w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-instagram"></i></a>
  <a class="w3-button w3-large w3-teal w3-hide-small" href="javascript:void(0)" title="Linkedin"><i class="fa fa-linkedin"></i></a>
  <p>Powered by PipedPiper</p>

  <div style="position:relative;bottom:100px;z-index:1;" class="w3-tooltip w3-right">
    <span class="w3-text w3-padding w3-teal w3-hide-small">Go To Top</span>   
    <a class="w3-button w3-theme" href="#myPage"><span class="w3-xlarge">
    <i class="fa fa-chevron-circle-up"></i></span></a>
  </div>
</footer>

<script>
// Script for side navigation
function w3_open() {
  var x = document.getElementById("mySidebar");
  x.style.width = "300px";
  x.style.paddingTop = "10%";
  x.style.display = "block";
}

// Close side navigation
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
}

// Used to toggle the menu on smaller screens when clicking on the menu button
function openNav() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}
</script>
</body>
</html>
    """

    return response
	

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5001')))
