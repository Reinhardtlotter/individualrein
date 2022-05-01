{% include navigation.html %}

<h1>Create Task Work</h1>

<h2>Written responses to questions</h2>

<p>Describes the overall purpose of the program:</p>

<p>The purpose of the project is for male gymnasts to be able to calculate the starting/base score of the routines they create. Skills are ranked by letter and add a different amount to each routine. Requirments also add extra points to start score.</p>

<p>Describes what functionality of the program is demonstrated in the video</p>

<p>The functionality shown is the program asking what the skill is worth however many times the user says there are skills and using the requirments met to create a start score and compare it to winning final scores from the olympics</p>

<p>Describes the input and output of the program demonstrated in the video</p>

<p>The input is the user saying the number of skills and requirements and the output is the users start score. The next input will be which event the routine is for and the output will be the Olympic winning score for that event and the difference between the two</p>

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
while count<=5:
  print (str(olyscores[count])+":"+event[count])
  count+=1
```
<p>3b iii: the name of the list is olyscores.

3b iv: The data is floats which are the olympic winning scores to be compared to the user's start scores.

3b v: With the list the scores are able to be used and called multiple times as in subtracting the user start score multiple times when they run the program more then once for multiple routines.</p>

<p>3c i:</p>

```
def skills(eventnum, skillcount,  letterval):    # Skillcount = number of skills in routine (max 8); letterval = skill's letter value
  if eventnum==4:  
    vaultcount=0
    while vaultcount < 8:
      print (str(vaultcount+1) + " " + str(vaults[vaultcount]))
      vaultcount += 1
    vaultstart=9
    while vaultstart > 8:
      vaultstarttext = input("What is your vault?  ")
      if not re.match("[1-8]", vaultstarttext):  #Checks to make sure the input is an integer 1-8#
        print("Enter a value from 1-8 only")
        vaultstart=9
      else:
        vaultstart = int(vaultstarttext)
        letterval=vaultscore[vaultstart-1]
  else:  
    execution = arr.array('u', ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'])
    inputcounter = 0
    while inputcounter < skillcount:
        execution[inputcounter] = (input("What is skill " + str(inputcounter+1) + " worth?(Please enter the letter value) "))
        if re.match("[a-i]", execution[inputcounter]):    #use regular expression to check for valid input
            inputcounter += 1
        else:
            print ("Error! Only letters a-i allowed!")   #if input is not valid, alert user
    for i in range(skillcount):        
        if execution[inputcounter] == "a":
            letterval += 0.1
        elif execution[inputcounter] == "b":
            letterval += 0.2
        elif execution[inputcounter] == "c":
            letterval += 0.3
        elif execution[inputcounter] == "d":
            letterval += 0.4
        elif execution[inputcounter] == "e":
            letterval += 0.5
        elif execution[inputcounter] == "f":
            letterval += 0.6
        elif execution[inputcounter] == "g":
            letterval += 0.7
        elif execution[inputcounter] == "h":
            letterval += 0.8
        else:
            letterval += 0.9
  return letterval
```
<p>3c ii:</p>

```
runagain = 1
#while loop is used so the user can run the program again for another routine
while runagain>0:
    #basic start of a routine with no skills or requirments
    letterval = 10.0
    #question to determine how any times function (skills) iterates
    skillcount = 9
    count = 0
    eventnum=7
    #prints all scores next to name
    while count <= 5:
      print (str(count+1) + str(event[count]))
      count += 1
    while eventnum > 6:
      eventnumtext = input("What event is your routine for?  ")
      if not re.match("[1-6]", eventnumtext):  #Checks to make sure the input is an integer 1-8#
          print("Enter a value from 1-6 only")
          eventnum=7
      else:
          eventnum = int(eventnumtext)
    if eventnum == 4:
      skillcount = 0
    while skillcount > 8:
      skillcounttext = input("How many skills do you have (max=8) ")
      if not re.match("[1-8]", skillcounttext):  #Checks to make sure the input is an integer 1-8#
          print("Enter a value from 1-8 only")
          skillcount=9
      else:
          skillcount = int(skillcounttext)
    #question to determine how many times the for i in range require will run
    requir=5
    if eventnum==4:
      requir=0
  
    while requir>4:
      requirtext = input("How many requirements did you fill? (max=4) ")
      if not re.match("[1-4]", requirtext):      #Checks to make sure that the input is an integer from 1-4
        print("Enter a value from 1-4 only")
        requir=5
      else:
        requir = int(requirtext)
    #function is assigned to a variable
    startscore=skills(eventnum,skillcount, letterval )
```
<p>3c iii: The procedure is used to calculate the value of what will be added to the start score based on the different skill values input by the user. The procedure allows for this value to be calculaed mutiple times as the user reruns the code. 3c iv: The algorithm takes the user input string value such as 'a' and then it is matched to the corresponding value with the conditional statements. This value will then be added to the letterval variable and the question will iterate again until it has repeated the user inputed amount of times. If the eventnum is 4 however, the procudure will display a few possible vaults which the user can select from which have a given startscore which will be assiged to letterval. Letterval will then be assigned to the startscore variable. </p>

<p>3d i: Call one is when eventnum is anything besides 4. The second call is when is equal to 4. 3d ii: The first call tests whether eventnum is not equal to 4 so the part of the algorithm which asks for individual score values will run. The second call tests that eventnum is equal to 4 so that the possible vaults can be dislayed for the user to select from. 3d iii: The result of the first call would be the sum of all of the values of the user's individual skills. The result of the second call would be the user's selected vault start score being assigned to the startscore variable. </p>

<p> The create Task must have an algorithm, procedure, list, and user input. There will also be a video with no sound of the code and answers to written questions.</p>
<p>For my create task I will create a program to calculate scores for gymnastics and compare them to olympians</p>
<p>List: list of an olympians score for comparing

  User Input: The user putting in the scores they would like to calculate

  Procedure: Fuctin to calculate and provide an end score t be compared

  Algorithm: the adding and subtaction of the scores to be used</p>


<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@ReinhardtLotter/Create-Task?lite=true#src/main.py">

