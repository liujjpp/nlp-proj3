## intent:greet
- hey
- hello
- hi
- good morning
- good afternoon
- good evening
- hey there
- what's up

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- yes, please
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:gratitude
- thanks
- thanks again
- many thanks
- thank you
- appreciate it
- love it

## lookup:guide_action
data/test/lookup_tables/guide_action.txt

## intent:recipe_search
- [walk me through](guide_action) a recipe from AllRecipes.com
- [walk me through](guide_action) recipe from AllRecipes.com

## regex:recipe_lookup
- ^http
- ^www
- ^allrecipes

## intent:recipe_lookup
- https://www.allrecipes.com/
- https://allrecipes.com/
- http://www.allrecipes.com/
- http://allrecipes.com/
- www.allrecipes.com/
- allrecipes.com/

## regex:display_ingredients
- ^1$
- ^1\.$

## intent:display_ingredients
- 1
- 1.
- Show me the ingredients list
- [walk me through](guide_action) the ingredients list
- [walk me through](guide_action) ingredients list
- [walk me through](guide_action) the ingredients
- [walk me through](guide_action) ingredients

## regex:read_recipe
- ^2$
- ^2\.$

## intent:read_recipe
- 2
- 2.
- Show me the recipe steps
- [walk me through](guide_action) the recipe steps
- [walk me through](guide_action) recipe steps
- [walk me through](guide_action) the recipe
- [walk me through](guide_action) recipe

## lookup:number
data/test/lookup_tables/number.txt

## intent:prev_step
- go back to the previous step
- [walk me through](guide_action) the previous step
- go back one step
- go back [one](number) step
- back [one](number) step

## regex:next_step
- next

## intent:next_step
- show next step
- go to next step
- go to the next step
- [walk me through](guide_action) the next step
- [walk me through](guide_action) next step
- next [one](number) step
- next step

## lookup:count
data/test/lookup_tables/count.txt

## intent:index_step
- take me to the [1st](count) step
- take me to the [2nd](count) step
- take me to the [3rd](count) step
- [walk me through](guide_action) the [1st](count) step
- [walk me through](guide_action) [1st](count) step
- [1st](count) step

## regex:count
- ^[a-zA-Z0-9]{1,}th$

## regex:how_question
- how[^\\s]*
- how is[^\\s]*

## lookup:cook_action
data/test/lookup_tables/cook_action.txt

## intent:how_question
- how to
- how do i
- how do i [preheat](cook_action)
- how do i [preheat](cook_action) a [fish](food)
- how do i [preheat](cook_action) [pasta](food)
- how does
- how does the

## lookup:food
data/test/lookup_tables/food.txt

## regex:what_question
- what[^\\s]*
- what is[^\\s]*

## intent:what_question
- what is
- what is a
- what are