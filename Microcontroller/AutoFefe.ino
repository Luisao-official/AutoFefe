const int numOfInputs = 4;
const int InputPins[numOfInputs] = {2, 4, 7, 8};
int InputStates[numOfInputs] = {0, 0, 0, 0};
int InputStatesOld[numOfInputs] = {0, 0, 0, 0};
bool inputFlags[numOfInputs] = {false, false, false, false};
long LastDebounceTime[numOfInputs] = {0, 0, 0, 0};
long DebounceDelay = 10;

const int numOfTasks = 3;
int currentTask = 0;
String tasks[numOfTasks] = {"checkEvents", "testInternet", "sendMail"};

void setup()
{
  for (int i = 0; i < numOfInputs; i++)
  {
    pinMode(InputPins[i], INPUT_PULLUP);
  }
  Serial.begin(115200);
}

// ! Debouncing

void setInputFlags()
{
  for (int i = 0; i < numOfInputs; i++)
  {
    int reading = digitalRead(InputPins[i]);
    if (reading != InputStatesOld[i])
    {
      LastDebounceTime[i] = millis();
    }
    if ((millis() - LastDebounceTime[i]) > DebounceDelay)
    {
      if (InputStates[i] != reading)
      {
        InputStates[i] = reading;
        if (InputStates[i] == LOW)
        {
          inputFlags[i] = true;
        }
      }
    }
    InputStatesOld[i] = reading;
  }
}

void resolveInputFlags()
{
  for (int i = 0; i < numOfInputs; i++)
  {
    if (inputFlags[i] == true)
    {
      Serial.println("pressed");
      Serial.println(i);
      inputAction(i);
      inputFlags[i] = false;
    }
  }
}

void inputAction(int input)
{
  if (input == 0)
  {
    Serial.println("pressedHome");
    Serial.println(tasks[currentTask]);
    currentTask = 0;
  }
  else if (input == 1)
  {
    Serial.println("pressedLeft");
    currentTask = (currentTask - 1 + numOfTasks) % numOfTasks;
    Serial.print("currentTask.");
    Serial.println(tasks[currentTask]);
  }
  else if (input == 2)
  {
    Serial.println("pressedRight");
    currentTask = (currentTask + 1) % numOfTasks;
    Serial.print("currentTask.");
    Serial.println(tasks[currentTask]);
  }
  else if (input == 3)
  {
    Serial.print("execute.");
    Serial.println(tasks[currentTask]);
  }
}

void loop()
{
  setInputFlags();
  resolveInputFlags();
}