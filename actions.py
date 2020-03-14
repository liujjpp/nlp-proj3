# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from project_2.fetcher import RecipeFetcher

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

str_number_lookup = {
    1: "1st",
    2: "2nd",
    3: "3rd"
}

str_count_lookup = [
    ['1st', 'first'],
    ['2nd', 'second'],
    ['3rd', 'third'],
    ['4th', 'fourth'],
    ['5th', 'fifth'],
    ['6th', 'sixth'],
    ['7th', 'seventh'],
    ['8th', 'eighth'],
    ['9th', 'ninth'],
    ['10th', 'tenth']
]

def translate_number(num):
    if num < 4:
        return str_number_lookup[num]
    else:
        return str(num) + "th"

class ActionLookupRecipe(Action):
    def name(self) -> Text:
        return "action_lookup_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # print('tracker state', tracker.current_slot_values())

        try:
            # clean url
            inputUrl = tracker.latest_message['text'].strip()

            # fetch recipe from website
            rf = RecipeFetcher()
            recipe = rf.scrape_recipe(inputUrl)
            message = "Alright. So let's start working with \"" + recipe['title'] + "\". What do you want to do?"

            dispatcher.utter_message(text=message)
            return [SlotSet("recipe", recipe)]

        except:
            dispatcher.utter_message(text="Url failed. Please try another recipe url.")
            return []

class ActionReadRecipe(Action):
    def name(self) -> Text:
        return "action_read_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots = tracker.current_slot_values()
        if not slots['recipe']:
            dispatcher.utter_message(text="Please input a valid recipe url before going over recipe steps.")
            return []
        steps = slots['recipe']['directions']
        idx = 0
        dispatcher.utter_message(text="The 1st step is: " + steps[idx])
        return [SlotSet("current_step", idx)]

class ActionDisplayIngredients(Action):
    def name(self) -> Text:
        return "action_display_ingredients"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slots = tracker.current_slot_values()
        if not slots['recipe']:
            dispatcher.utter_message(text="Please input a valid recipe url before going over ingredients.")
            return []
        ingredients = slots['recipe']['ingredients']
        # transform ingredients dict to string
        ingredients_str = '\n\n'.join(ingredients)
        dispatcher.utter_message(text="Here are the ingredients for \"" + slots['recipe']['title'] + "\":\n\n" + ingredients_str)
        return []

class ActionReadNextStep(Action):
    def name(self) -> Text:
        return "action_read_next_step"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slots = tracker.current_slot_values()
        if not slots['recipe']:
            dispatcher.utter_message(text="Please input a valid recipe url before going over recipe steps.")
            return []
        steps = slots['recipe']['directions']
        idx = slots['current_step'] + 1
        if idx >= len(steps):
            dispatcher.utter_message(text="Last step has been reached. Resetting back to beginning step if asked again.")
            return [SlotSet("current_step", -1)]
        else:
            dispatcher.utter_message(text="The " + translate_number(idx+1) + " step is: " + steps[idx])
            return [SlotSet("current_step", idx)]

class ActionReadPrevStep(Action):
    def name(self) -> Text:
        return "action_read_prev_step"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slots = tracker.current_slot_values()
        if not slots['recipe']:
            dispatcher.utter_message(text="Please input a valid recipe url before going over recipe steps.")
            return []
        steps = slots['recipe']['directions']
        idx = slots['current_step'] - 1
        if idx < 0:
            dispatcher.utter_message(text="First step has been reached. Cannot go further backwards.")
            return []
        else:
            dispatcher.utter_message(text="The " + translate_number(idx+1) + " step is: " + steps[idx])
            return [SlotSet("current_step", idx)]

class ActionAskContinue(Action):
    def name(self) -> Text:
        return "action_ask_continue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slots = tracker.current_slot_values()
        if not slots['recipe']:
            dispatcher.utter_message(text="Please input a valid recipe url first!")
            return []
        idx = slots['current_step'] + 1

        dispatcher.utter_message(text="Should I continue to the " + translate_number(idx+1) + " step?")
        return []

class ActionReadNthStep(Action):
    def name(self) -> Text:
        return "action_read_nth_step"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slots = tracker.current_slot_values()
        print(tracker.latest_message['entities'])
        if not slots['recipe']:
            dispatcher.utter_message(text="Please input a valid recipe url before going over recipe steps.")
            return []
        try:
            idx = slots['current_step'] + 1
            steps = slots['recipe']['directions']
            if len(tracker.latest_message['entities']) > 0:
                nth_value = tracker.latest_message['entities'][0]['value'].lower()
                # parse step from latest message
                for i in range(len(str_count_lookup)):
                    if nth_value in str_count_lookup[i]:
                        idx = i
                        break

            dispatcher.utter_message(text="The " + translate_number(idx+1) + " step is: " + steps[idx])
            return [SlotSet("current_step", idx)]
        except:
            dispatcher.utter_message(text="The nth step is out of range for this recipe. The recipe has a maximum of " + str(len(slots['recipe']['directions'])) + " steps.")
            return []