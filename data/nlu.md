## intent:greet
- hey
- hello
- hi
- good morning
- good afternoon
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
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

## lookup:guide_action
data/test/lookup_tables/guide_action.txt

## intent:recipe_search
- [walk me through](guide_action) a recipe from
- [walk me through](guide_action) recipe from

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
- [walk me through](guide_action) the ingredients
- [walk me through](guide_action) ingredients

## regex:read_recipe
- ^2$
- ^2\.$

## intent:read_recipe
- 2
- 2.
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

## intent:next_step
- go to the next step
- [walk me through](guide_action) the next step
- [walk me through](guide_action) next step
- next [one](number) step
- next step

## lookup:count
data/test/lookup_tables/count.txt

## intent:index_step
- take me to the [1st](count) step
- [walk me through](guide_action) the [1st](count) step
- [walk me through](guide_action) [1st](count) step
- [1st](count) step

## regex:how_question
- how[^\\s]*

## lookup:count
data/test/lookup_tables/cook_action.txt

## intent:how_question
- how to
- how do i
- how do i [preheat](cook_action)
- how does
- how does the

## regex:what_question
- what[^\\s]*

## intent:what_question
- what is
- what is a
- what are