## default path
* recipe_search
  - utter_search
* recipe_lookup
  - action_lookup_recipe
  - utter_commands
> check_selected_command

## thanking path 1
* gratitude
  - utter_continue
* affirm
  - action_read_next_step
> change_step

## thanking path 2
* gratitude
  - utter_continue
* deny
  - utter_question
  - utter_commands
> check_selected_command

## display ingredients
> check_selected_command
* display_ingredients
  - action_display_ingredients
> check_selected_command

## read recipe
> check_selected_command
* read_recipe
  - action_read_recipe
> check_selected_command
> change_step

## prev step
> change_step
* prev_step
  - action_read_prev_step
> change_step
  
## next step
> change_step
* next_step
  - action_read_next_step
> change_step
  
## index step
> change_step
* index_step
  - action_read_nth_step
> change_step
  
## how question
* how_question
  - utter_how
  
## what question
* what_question
  - utter_what
  
## say hello
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye
