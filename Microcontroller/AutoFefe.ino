// Define the pin for low state detection
const int actionPin = 2;
const int leftSwitch = 4;
const int rightSwitch = 7;
boolean actionDetected = false;

const char* commands[] = {
  "checkEvents",
  "testInternet",
  "sendMail"
};

int currentCommandIndex = 0;

void setup()
{
  // Initialize Serial communication with .1 timeout
  Serial.begin(115200);
  Serial.setTimeout(10);
  pinMode(actionPin, INPUT_PULLUP); // Enable internal pull-up resistor
  pinMode(rightSwitch, INPUT_PULLUP);
  pinMode(leftSwitch, INPUT_PULLUP);

}

// Define the pin for low state detection

void loop() {
  if (!actionDetected && digitalRead(actionPin) == HIGH) {
    actionDetected = true; // Set the actionDetected flag
    
    // Action detected, send the "time" command
    // Serial.println("events");
    Serial.println("pressedHome");
    while (actionPin != HIGH)
    {
      delay(5);
    }.
    
    
    do {
      if (digitalRead(rightSwitch) == LOW) {
        currentCommandIndex = (currentCommandIndex + 1) % (sizeof(commands) / sizeof(commands[0]));
        Serial.println("right");
        Serial.println(commands[currentCommandIndex]);
      } else if (digitalRead(leftSwitch) == LOW) {
        currentCommandIndex = (currentCommandIndex - 1 + (sizeof(commands) / sizeof(commands[0]))) % (sizeof(commands) / sizeof(commands[0]));
        Serial.println("pressedLeft");
        Serial.println(commands[currentCommandIndex]);
      }
      
      // Consider using millis() for non-blocking timing
      delay(1000);
      
    } while (digitalRead(actionPin) == HIGH);
    
    // Print the final selected command
    Serial.print("execute.");
    Serial.println(commands[currentCommandIndex]);
  }


  

  if (actionDetected)
  {
    // Wait for a response from Python
    if (Serial.available() > 0)
    {
      String response = Serial.readStringUntil('\n');
      // Process the response here
      // Serial.println("Received: " + response);
      actionDetected = false; // Reset the flag
    }
  }
}
