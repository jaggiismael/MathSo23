# Spread of an infectious disease
Cellular automata are used to model time-discrete processes with position-dependent state
variables. They are based on a space of cells of identical geometry that cover the spatial
domain.<br/>
In our case the cell space is a two-dimensional regular rectangular grid of size n × m
representing the beds in a dormitory. Initially one of the residents has contracted an infectious
disease. <br/><br/>

## The disease spreads from one time step to the next according to the following rules:<br/>
<ul>
<li>There are three states: (i) ill, (ii) healthy and infectable, and (iii) healthy and immune
(due to previous infection).</li>
<li>The neighbours in the beds at the head and foot end and to both sides of the infected
person’s bed can contract the disease. The probability of infection is 0 < p < 1.
Infection is instantaneous.</li>
<li>After k days of illness one is healthy and immune.</li>
</ul>  
  
## Work to do
Implement this cellular automat. The user should be able to enter the parameters of the
model, i.e. the size n×m of the dorimtory, the position of the ill person’s bed at the beginning
of the simulation, the probability of infection p and the duration k of the illness. An animation
of the spread of the disease should then be generated. Experiment with different parameters
and describe the different behaviour that may occur. Generate video files (in mpeg format)
for a few typical examples.<br/>
Now extend this model:
<ul>
<li>Every day a certain number of the healthy but infectable residents are vaccinated (assume that they are randomly distributed in the dormitory).</li>
<li>Every day a certain number of residents swap beds.</li>
<li>The disease has an incubation period of i days, during which one is not infectious.</li>
</ul>
<br/>Illustrate the influence of each of these extensions on the spread of the disease for a few
selected examples.

## How to run it
Once installed via GitHub, you can go in the folder of the project called "infectious_disease_project" and type "python main.py" in the terminal
Then, fill the questions that appear on the terminal by pressing a number + enter. 

There is also a library that we added in order to save files. You can just paste this command in the terminal : 
conda install -c conda-forge ffmpeg

## Work repartition
We both started to work, during class, on this project until we had the base of the project (the basic first spread and an animation that was not working really well).
Then, we separated the job like the following : Ismael was responsible of developing the vaccination, bed swao and the incubation methods and Theo was responsible of making the 
three different animation. Then, we have made the jupiter notebook. The repartition for it was like so : Ismael did the presentation of the first technical parts and Theo presented 
the simulation and the animation part. 

Overall, we think that we work the same amount of time on that project.
