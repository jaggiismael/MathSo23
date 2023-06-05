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
Then, fill the questions that appear on the terminal by pressing a number + enter 

## Where the project is, what we need to do
Now, the spray of the disease works, now we need to go further by having multiple parameters per bed : 
The grid is now a table of a table, but that is not enough to store multiple values. We have two solutions : 
First one, we keep it like that and we change the numbers accordingly (which is bad if we increase the complexity later)
Second option is to make an other layer of table so that we can have multiple parameters per bed. Ex : status, number of days ill, vaccinated, dead, etc.

(of course the second is better but it's more complex to work with).

The next job will be to introduce the numbers of days that the patient is ill, and, at the end, that he can enter in a "immune" state (he can't have the disease anymore). 