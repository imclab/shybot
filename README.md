Origin
======


Can a [robot](http://www.youtube.com/watch?v=3PMlDidyG_I "StarTrek: Measure of a Man") _like or dislike_ a person? How can a robot build a relationship with its _friends_? Can a robot think based on its relationship with human? Can a robot learn in an irreversible manner?
Shybot is here to explore these questions.
Shybot is an emotion-driven robot like a shy creature which recognizes friends or strangers and 
interacts with them differently. 

Shybot was a 
[research project](http://affect.media.mit.edu/projects.php?id=2306 "Affective Computing Group") 
originated from the Autism Theory and Technology class 
(co-taught by [Rosalind Picard](http://www.bbc.co.uk/news/technology-24652902?SThisFB), 
[Cynthia Breazeal](http://www.ted.com/talks/cynthia_breazeal_the_rise_of_personal_robots.html), and 
[Sherry Turkle](http://www.youtube.com/watch?v=Ikn-_myAfhQ)) at MIT Media Lab in 2007. 
Many of Shybot's features are inspired by [_The Uncanny_](https://github.com/jackylee0424/shybot/wiki/Uncanny "by Sigmund Freud (1919)").

[Short video from '07 (.m4v)](https://github.com/jackylee0424/shybot/blob/master/doc/shybot_07short.m4v?raw=true)

<img src="https://raw.github.com/jackylee0424/shybot/master/doc/shybot_07a.jpg" height=160 />
<img src="https://raw.github.com/jackylee0424/shybot/master/doc/shybot_07b.jpg" height=160 />
<img src="http://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Kou-Kou_by_Georgios_Iakovidis.jpg/200px-Kou-Kou_by_Georgios_Iakovidis.jpg" height=160 />



Roadmap
======

- _Peer-to-peer face learning_. It would be more efficient to accumulate the "learning" part so that this network of Shybots could keep improving themselves.
- _Companion_. The plan is to re-build it using some existing platform 
(e.g., [Romo](http://romotive.com/ "iPhone/iPod extension toy car")
or [SparkFun robotic car](https://www.sparkfun.com/products/10825)). 
This repository contains Shybot's work-in-progress prototype code based on Romo. For making it work as a consumer toy, 
we'll need durable design and robust sensors for basic safety concerns. 
Adding human detector (and danger detector) using non-contact temperature sensors 
([MLX90614](https://www.sparkfun.com/products/9570) 
or [MLX90620](http://www.melexis.com/Infrared-Thermometer-Sensors/Infrared-Thermometer-Sensors/MLX90620-776.aspx)). This part was paused because the software part seemed more important. We are also considering building Shybot on [Raspberry Pi](http://www.raspberrypi.org/) with camera, sensors, and motors.
- _Parents_. Shybot could help collect spoken words from kids (inspired by [Deb Roy](http://www.ted.com/talks/deb_roy_the_birth_of_a_word.html "Deb's Ted Talk")'s [research](http://dkroy.media.mit.edu/publications/)).


<img src="https://raw.github.com/jackylee0424/shybot/master/doc/shybot_v1.png" height=160 />
<img src="https://raw.github.com/jackylee0424/shybot/master/doc/shybot_13a.png" height=160 />


Citation
======

Lee, C.H., Kim, K., Breazeal, C., Picard, R.W. Shybot: Friend-Stranger Interaction for Children Living with Autism, _Work-In-Progress in the Extended Abstract of Computer-Human Interaction 2008_, April 5-10, 2008, Florence, Italy

[Download full-text PDF](https://github.com/jackylee0424/shybot/blob/master/reference/chi08_shybot-lee.pdf?raw=true)

<img src="https://raw.github.com/jackylee0424/shybot/master/doc/shybot_07c.jpg" height=160 />

Notes
======
- All codes are under MIT license.
- For Romo developers, to smoothly run it in debug mode, iPhone/iPod needs to be docked (on Romo) "before" connecting the charging wire to your Mac. "After" connected, Romo will try connecting its app, so click "ignore" then open Shybot app.


Contribute
======
This hasn't reached first stable master yet. 
However, we'll be following [a successful git branching model](http://nvie.com/posts/a-successful-git-branching-model/).
