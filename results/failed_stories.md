## happy path 1 (C:\Users\15378\AppData\Local\Temp\tmp1bvje2b0\f981fbfa8a074575a8c56d50f87b5a87_conversation_tests.md)
* greet: hello there!   <!-- predicted: bot_challenge: hello there! -->
    - utter_greet   <!-- predicted: utter_iamabot -->
* mood_great: amazing   <!-- predicted: affirm: amazing -->
    - utter_happy


## happy path 2 (C:\Users\15378\AppData\Local\Temp\tmp1bvje2b0\f981fbfa8a074575a8c56d50f87b5a87_conversation_tests.md)
* greet: hello there!   <!-- predicted: bot_challenge: hello there! -->
    - utter_greet   <!-- predicted: utter_iamabot -->
* mood_great: amazing   <!-- predicted: affirm: amazing -->
    - utter_happy
* goodbye: bye-bye!   <!-- predicted: bot_challenge: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_iamabot -->


## sad path 1 (C:\Users\15378\AppData\Local\Temp\tmp1bvje2b0\f981fbfa8a074575a8c56d50f87b5a87_conversation_tests.md)
* greet: hello   <!-- predicted: affirm: hello -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_unhappy: not good   <!-- predicted: bot_challenge: not good -->
    - utter_cheer_up   <!-- predicted: utter_iamabot -->
    - utter_did_that_help
* affirm: yes
    - utter_happy


## sad path 2 (C:\Users\15378\AppData\Local\Temp\tmp1bvje2b0\f981fbfa8a074575a8c56d50f87b5a87_conversation_tests.md)
* greet: hello   <!-- predicted: affirm: hello -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_unhappy: not good   <!-- predicted: bot_challenge: not good -->
    - utter_cheer_up   <!-- predicted: utter_iamabot -->
    - utter_did_that_help
* deny: not really   <!-- predicted: bot_challenge: not really -->
    - utter_goodbye   <!-- predicted: utter_iamabot -->


## sad path 3 (C:\Users\15378\AppData\Local\Temp\tmp1bvje2b0\f981fbfa8a074575a8c56d50f87b5a87_conversation_tests.md)
* greet: hi   <!-- predicted: affirm: hi -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_unhappy: very terrible   <!-- predicted: bot_challenge: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_iamabot -->
    - utter_did_that_help
* deny: no   <!-- predicted: affirm: no -->
    - utter_goodbye   <!-- predicted: utter_happy -->


## say goodbye (C:\Users\15378\AppData\Local\Temp\tmp1bvje2b0\f981fbfa8a074575a8c56d50f87b5a87_conversation_tests.md)
* goodbye: bye-bye!   <!-- predicted: bot_challenge: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_iamabot -->


