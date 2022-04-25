{% include navigation.html %}

<h1>Create Task Work</h1>

<h2>Written responses to questions</h2>

<p>Describes the overall purpose of the program:</p>

<p>The purpose of the project is for male gymnasts to be able to calculate the starting/base score of the routines they create. SKills are ranked by letter and add a different amont to each routine. Requirments also add extra point to start score as well.</p>

<p>Describes what functionality of the program is demonstrated in the video</p>

<p>The functionality shown is the program asking what the skill is worth however many times the user says there are skills and using the requirments met to create a start score and compare it to winning final scores from the olympics</p>

<p>Describes the input and output of the program demonstrated in the video</p>

<p>The input is the user saying the number of skills and requirments and the output is the users start score. The next input will be whic hevent the routine is for and the output will be the Olympic winning score for that event and the difference between the two</p>

<p>3b i:</p>

```
olyscores = [
    15.200,
    14.900,
    15.300,
    14.866,
    16.166,
    15.033
]
```
<p>3b ii:</p>

```
if event == "floor":
  difference=olyscores[0]-startscore
  print("The winning Floor score in the 2020 Olympics was "+str(olyscores[0])+" which was "+str(round(difference,3)) + " higher than your START. Isnt that crazy??")
```
<p>3b iii: the name of the list is olyscores.

3b iv: The data is floats which are the olympic winning scores to be compared to the users starts

3b v: with the list the scores are able to be used and called without having to put them in everytime</p>

<p>3c i:</p>

```
def skills(skillcount,startscores):
  for i in range(skillcount):
      execution = (input("What is the "+str(i+1)+ " skill worth?(Please enter the letter value) "))
      if execution == "a":
          startscores += 0.1
      elif execution == "b":
        startscores += 0.2
      elif execution == "c":
        startscores += 0.3
      elif execution == "d":
        startscores += 0.4
      elif execution == "e":
        startscores += 0.5
      elif execution == "f":
        startscores += 0.6
      elif execution == "g":
        startscores += 0.7
      elif execution == "h":
        startscores += 0.8
      elif execution == "i":
        startscores += 0.9
      else:
        startscores="Please enter the LETTER value(a-i)"
  return startscores
```
<p>3c ii:</p>

```
startscore=skills(skillcount,startscores)
#adds 0.5 for each requirment
for i in range(requir):
  startscore += 0.5
#prints start score and rounds it to 2 decimals
print("Your start score is: "+str(round(startscore,2)))
```
<p>3c iii: The procedure is used to calculate how much is being added to the start score based on the different skill values input by the user. 3c iv: The string uses skill count as a number and iterates i number of times. Each time it asks how much is the skill worth. if the input is a it adds 0.1 to startscores. If it is b it adds 0.2, c 0.3 and so on to i adding 0.9. If it is not a letter a-i it gives a message saying please input a letter value a-i. </p>

<p> The create Task must have an algorithm, procedure, list, and user input. There will also be a video with no sound of the code and answers to written questions.</p>
<p>For my create task I will create a program to calculate scores for gymnastics and compare them to olympians</p>
<p>List: list of an olympians score for comparing

  User Input: The user putting in the scores they would like to calculate

  Procedure: Fuctin to calculate and provide an end score t be compared

  Algorithm: the adding and subtaction of the scores to be used</p>


<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@ReinhardtLotter/Create-Task?lite=true#src/main.py">

