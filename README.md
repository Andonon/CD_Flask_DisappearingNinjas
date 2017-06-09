# CD_Flask_DisappearingNinjas

Troy Center troycenter1@gmail.com	
June 2017

Coding Dojo Flask Fundamentals. Disappearing Ninjas Assignment. 

Assignment: Disappearing Ninja
Build a flask application with the below functionality.

This exercise will help you practice URL routing, using views, and rendering static content.



These are the routes that you need to set up:

On the default page ('localhost:5000'), it should display a view that says "No ninjas here"
When user visits /ninja, it should display all four Ninja Turtles (Leonardo, Michelangelo, Raphael, and Donatello)
/ninja/[ninja_color], should display the corresponding Ninja Turtle (grab the color parameter out of the requested URL)
If user visits /ninja/blue, it should only display the Ninja Turtle Leonardo.
/ninja/orange - Ninja Turtle Michelangelo.
/ninja/red - Ninja Turtle Raphael
/ninja/purple - Ninja Turtle Donatello
If a user tries to hack into your web app by specifying a color or string combination other than the colors (Blue, Orange, Red, and Purple), example: /ninja/black or /ninja/123, then display the image notapril.jpg
You'll need to remember how to use static files for this assignment. Take a minute to refresh your memory back to the static files section if you need to :)
Click here to download the image files.


http://s3.amazonaws.com/General_V88/boomyeah/company_209/chapter_3677/handouts/chapter3677_7470_Ninjas.zip

<img src="http://s3.amazonaws.com/General_V88/boomyeah/company_209/chapter_2392/handouts/chapter2392_2694_tmnt.png" style="width: 504px;">