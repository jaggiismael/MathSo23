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
