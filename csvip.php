<?php
$accuracy = -1;
extract($_GET);
if ($accuracy == -1) {
  echo '
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <title>SAF 4.X</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      
      <link href="https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css?family=Vidaloka" rel="stylesheet">

      <link rel="stylesheet" href="css2/open-iconic-bootstrap.min.css">
      <link rel="stylesheet" href="css2/animate.css">
      
      <link rel="stylesheet" href="css2/owl.carousel.min.css">
      <link rel="stylesheet" href="css2/owl.theme.default.min.css">
      <link rel="stylesheet" href="css2/magnific-popup.css">

      <link rel="stylesheet" href="css2/aos.css">

      <link rel="stylesheet" href="css2/ionicons.min.css">

      <link rel="stylesheet" href="css2/bootstrap-datepicker.css">
      <link rel="stylesheet" href="css2/jquery.timepicker.css">

      
      <link rel="stylesheet" href="css2/flaticon.css">
      <link rel="stylesheet" href="css2/icomoon.css">
      <link rel="stylesheet" href="css2/style.css">

      <link rel="stylesheet" href="css1/style.css">

    </head>
    <body>

      <div class="page" >
      
      
      <div id="colorlib-page sticky" >
        <header>
          <div class="container" >
            <div class="colorlib-navbar-brand" style="position: fixed;">
              <a class="colorlib-logo" href="index.html" >S.A.F 4.X<br><span>HOME PAGE</span></a>
            </div>
          </div>
        </header>


      <!-- About Us Section Begin -->
      <section class="about-us-section spad">
          <div class="container">
              <div class="row">
                  <div class="col-lg-6">
                      <div class="as-pic">
                          <br><br>
                          <br><br>
                          <img src="img/hero/4.jpg" id = "output_img">
                      </div>
                  </div>
                  <div class="col-lg-6">
                      <div class="as-text">
                          <br><br>
                          <br><br>
                          <div class="section-title">
                              <span>SAF 4.X</span>
                              <h2>CSV Input</h2>
                          </div>
                          <div class="footer-widget">
                              <p>Upload a csv file below, the overall accuracy of which is to be found.</p>
                              <form class="news-form" action="upload.php" method="post" enctype="multipart/form-data"">
                                  <br><br>
                                  <input type="file" name="sentences" class="question" id="sentences" required autocomplete="off" accept=".csv">
                                  <br>
                                  <input type="submit" name="submit" style="background: #e32879; color: #ffffff;" value="CHECK ACCURACY"><br>
                              </form>
                          </div>
                          <div class="section-title">
                              <span id="accuracyop" >Please wait for a few minutes after submitting the csv. The result would be intimated to you as soon as it is available.</span>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </section>
      

      <script src="js2/jquery.min.js"></script>
      <script src="js2/jquery-migrate-3.0.1.min.js"></script>
      <script src="js2/popper.min.js"></script>
      <script src="js2/bootstrap.min.js"></script>
      <script src="js2/jquery.easing.1.3.js"></script>
      <script src="js2/jquery.waypoints.min.js"></script>
      <script src="js2/jquery.stellar.min.js"></script>
      <script src="js2/owl.carousel.min.js"></script>
      <script src="js2/jquery.magnific-popup.min.js"></script>
      <script src="js2/aos.js"></script>
      <script src="js2/jquery.animateNumber.min.js"></script>
      <script src="js2/scrollax.min.js"></script>
      <script src="js2/jquery.mb.YTPlayer.min.js"></script>
      <script src="js2/bootstrap-datepicker.js"></script>
      <script src="js2/jquery.timepicker.min.js"></script>
      <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBVWaKrjvy3MaE7SQ74_uJiULgl1JY0H2s&sensor=false"></script>
      <script src="js2/google-map.js"></script>
      <script src="js2/main.js"></script>
      
    </body>
  </html>';
}
else {
  echo '
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <title>SAF 4.X</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      
      <link href="https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css?family=Vidaloka" rel="stylesheet">

      <link rel="stylesheet" href="css2/open-iconic-bootstrap.min.css">
      <link rel="stylesheet" href="css2/animate.css">
      
      <link rel="stylesheet" href="css2/owl.carousel.min.css">
      <link rel="stylesheet" href="css2/owl.theme.default.min.css">
      <link rel="stylesheet" href="css2/magnific-popup.css">

      <link rel="stylesheet" href="css2/aos.css">

      <link rel="stylesheet" href="css2/ionicons.min.css">

      <link rel="stylesheet" href="css2/bootstrap-datepicker.css">
      <link rel="stylesheet" href="css2/jquery.timepicker.css">

      
      <link rel="stylesheet" href="css2/flaticon.css">
      <link rel="stylesheet" href="css2/icomoon.css">
      <link rel="stylesheet" href="css2/style.css">

      <link rel="stylesheet" href="css1/style.css">

    </head>
    <body>

      <div class="page" >
      
      
      <div id="colorlib-page sticky" >
        <header>
          <div class="container" >
            <div class="colorlib-navbar-brand" style="position: fixed;">
              <a class="colorlib-logo" href="index.html" >S.A.F 4.X<br><span>HOME PAGE</span></a>
            </div>
          </div>
        </header>


      <!-- About Us Section Begin -->
      <section class="about-us-section spad">
          <div class="container">
              <div class="row">
                  <div class="col-lg-6">
                      <div class="as-pic">
                          <br><br>
                          <br><br>
                          <img src="img/hero/4.jpg" id = "output_img">
                      </div>
                  </div>
                  <div class="col-lg-6">
                      <div class="as-text">
                          <br><br>
                          <br><br>
                          <div class="section-title">
                              <span>SAF 4.X</span>
                              <h2>CSV Input</h2>
                          </div>
                          <div class="footer-widget">
                              <p>Upload a csv file below, the overall accuracy of which is to be found.</p>
                              <form class="news-form" action="upload.php" method="post" enctype="multipart/form-data">
                                  <br><br>
                                  <input type="file" name="sentences" class="question" id="sentences" required autocomplete="off" accept=".csv">
                                  <br>
                                  <input type="submit" name="submit" style="background: #e32879; color: #ffffff;" value="CHECK ACCURACY"><br>
                              </form>
                          </div>
                          <div class="section-title">
                              <span id="accuracyop" style="font-size:20px;">ACCURACY: '.$accuracy.'</span><br>
                              <span>Please wait for a few minutes after submitting the csv. The result would be intimated to you as soon as it is available.</span>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </section>
      

      <script src="js2/jquery.min.js"></script>
      <script src="js2/jquery-migrate-3.0.1.min.js"></script>
      <script src="js2/popper.min.js"></script>
      <script src="js2/bootstrap.min.js"></script>
      <script src="js2/jquery.easing.1.3.js"></script>
      <script src="js2/jquery.waypoints.min.js"></script>
      <script src="js2/jquery.stellar.min.js"></script>
      <script src="js2/owl.carousel.min.js"></script>
      <script src="js2/jquery.magnific-popup.min.js"></script>
      <script src="js2/aos.js"></script>
      <script src="js2/jquery.animateNumber.min.js"></script>
      <script src="js2/scrollax.min.js"></script>
      <script src="js2/jquery.mb.YTPlayer.min.js"></script>
      <script src="js2/bootstrap-datepicker.js"></script>
      <script src="js2/jquery.timepicker.min.js"></script>
      <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBVWaKrjvy3MaE7SQ74_uJiULgl1JY0H2s&sensor=false"></script>
      <script src="js2/google-map.js"></script>
      <script src="js2/main.js"></script>
      
    </body>
  </html>';
}

?>