Origin
======

Can a [robot](http://www.youtube.com/watch?v=3PMlDidyG_I "StarTrek: Measure of a Man") _like or dislike_ a person? How can a robot build a relationship with its _friends_? 
Shybot is here to explore these questions.
Shybot is an emotion-driven robot like a shy creature which recognizes friends or strangers and 
interacts with them differently. Shybot was a 
[research project](http://affect.media.mit.edu/projects.php?id=2306 "Affective Computing Group") 
originated from the Autism Theory and Technology class 
(co-taught by [Rosalind Picard](http://www.bbc.co.uk/news/technology-24652902?SThisFB), 
[Cynthia Breazeal](http://www.ted.com/talks/cynthia_breazeal_the_rise_of_personal_robots.html), and 
[Sherry Turkle](http://www.youtube.com/watch?v=Ikn-_myAfhQ)) at MIT Media Lab in 2007. 

[Short video from '07 (.m4v)](https://github.com/jackylee0424/shybot/blob/master/doc/shybot_07short.m4v?raw=true)

<img src="https://raw.github.com/jackylee0424/shybot/master/doc/shybot_07a.jpg" height=240 />
<img src="https://raw.github.com/jackylee0424/shybot/master/doc/shybot_07b.jpg" height=240 />
<img src="https://raw.github.com/jackylee0424/shybot/master/doc/shybot_07c.jpg" height=240 />


Roadmap
======

<img src="https://raw.github.com/jackylee0424/shybot/master/doc/shybot_13a.png" height=200 />
<img src="http://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Kou-Kou_by_Georgios_Iakovidis.jpg/200px-Kou-Kou_by_Georgios_Iakovidis.jpg" height=200 />

- _Resurrection_. The plan is to re-build it using some existing platform (e.g., [Romo](http://romotive.com/ "iPhone/iPod extension toy car")
or [SparkFun robotic car](https://www.sparkfun.com/products/10825)). 
We will start from implementing its emotion-familiarity model using face recognition techniques on an iPod touch 4th.
This repository contains Shybot's work-in-progress prototype code based on Romo. 
- _Companion_. For making it work as a consumer toy, we'll need durable design and robust sensors for basic safety concerns.
- _Parents_. Shybot could help collect spoken words from kids (inspired by [Deb Roy](http://www.ted.com/talks/deb_roy_the_birth_of_a_word.html "Deb's Ted Talk")'s [research](http://dkroy.media.mit.edu/publications/)).
We'll start exploring using [OpenEars](http://www.politepix.com/openears/).


Citation
======
Lee, C.H., Kim, K., Breazeal, C., Picard, R.W. Shybot: Friend-Stranger Interaction for Children Living with Autism, _Work-In-Progress in the Extended Abstract of Computer-Human Interaction 2008_, April 5-10, 2008, Florence, Italy

[Download full-text PDF](https://github.com/jackylee0424/shybot/blob/master/reference/chi08_shybot-lee.pdf?raw=true)


Notes
======
- All codes are under MIT license.
- For Romo developers, to smoothly run it in debug mode, iPhone/iPod needs to be docked (on Romo) "before" connecting the charging wire to your Mac. "After" connected, Romo will try connecting its app, so click "ignore" then open Shybot app.

