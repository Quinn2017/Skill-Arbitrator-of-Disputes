## Skill-Abitrator-of-Disputes
This skill is meant to give Mycroft the ability to arbitrate silly disputes using a very basic random python event. This random event simply chooses between 
two pre-parties set in the dialog folder. This setup works perfectly in our household as there is just two people to arbitrate. 

## Phase
WIP -- Work in progress.
Initial testing phase. 

## TO DO
* Add a mechanism where names of parties to the dispute can be taken by Mycroft. 
* Add a listen event where Mycroft would request and stt a dictated summary of the dispute, and save the text to a log file, with a time stamp. 
* Add Mycroft's random decision to the log file, time stamped, and email a record to the user account (similar to the skill-dictation).
* Add contexts
* Consider more sophisticate ways of settling disputes other than using a random event.

## Instructions
Basic MSM install. 
Simply edit the dialog files to replace names used, and that's it.

## Examples
"Mycroft, we need you to decide a dispute." 
"Mycroft, can you settle who is right in this dispute."
"Mycroft, we need you to arbitrate this dispute."

Any utterance with "settle/decide/arbitrate" and "dispute" words. 

Mycroft will follow-up if all parties consent, to which a "yes" must be provided to proceed, otherwise dispute resolution is terminated. 

## Credits
The skill is inspired and a basic reworking of Willem Ligtenberg's 'Flip a Coin' Skill.