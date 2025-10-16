# responses for time/date queries
city_time_success = [
    "In {city}, it is {date} and the time is {time}.",
    "Right now in {city}, it's {date} and the time is {time}.",
    "The local time in {city} is {time} on {date}.",
    "Currently in {city}, it's {time} on {date}.",
    "{city}: {date}, {time} local time.",
]

city_time_fail = [
    "Sorry, I couldn't get the local time for {city}.",
    "I wasn't able to find the time for {city}.",
    "I couldn't retrieve the time for {city} right now.",
    "No time information available for {city}.",
    "I can't get the current time for {city} at the moment.",
]

local_time_success = [
    "In {city}, it is {date} and the time is {time} ({tz}).",
    "Right now in {city}, it's {date} and the time is {time} ({tz}).",
    "The local time here in {city} is {time} on {date} ({tz}).",
    "Currently in {city}, it's {time} on {date} ({tz}).",
    "{city}: {date}, {time} local time ({tz}).",
]

system_time_success = [
    "Today is {date} and the time is {time}.",
    "It's {date} and the time is {time} right now.",
    "The current date is {date} and the time is {time}.",
    "Right now, it's {time} on {date}.",
    "{date}, {time} local system time.",
]
# negative response for query that is not understandable
cannot_understand_user = [
    "Sorry, I didn't catch that",
    "I'm not sure if i understand",
    "Could you rephrase that?",
    "Hmm, I don't know about that",
    "I don't understand what you mean",
    "Im sorry, can you clarify?",
    "I didn't get that. Can you say it again?",
    "I’m not sure how to respond to that",
    "Sorry, I cannot process that request",
    "I don’t quite get it. Can you try again?",
]

# response when query is false in youtube search
cannot_understand_youtube = [
    "Sorry, I couldn't find that video on YouTube",
    "Hmm, I didn't understand which video to play",
    "I couldn't figure out what to play on YouTube",
    "Oops! That video doesn't seem to exist",
    "Sorry, I can't play that video right now",
    "I didn't get the video title, can you try again?",
    "Hmm, that request is unclear, please repeat",
    "I couldn't process your YouTube request",
    "That video seems unavailable or invalid",
    "Sorry, I don't know which video you mean",
]

cannot_find_app = [
    "Sorry, I couldn't find {app} in my database. Please check if it's added to the system",
    "I don't recognize the app '{app}'",
    "'{app}' is not available. Try another app or update my system commands",
    "I can't open '{app}' because it's not in my list",
]

cannot_understand_app_name = [
    "Sorry, which app did you mean?",
    "Could you repeat the app name for me?",
    "I didn’t quite catch the application you said",
    "What app should I open?",
    "Mind saying the app name again?",
]

cannot_find_whatsapp_contact = [
    "Sorry, I couldn't find a contact in your message. Please try again",
    "I wasn't able to identify a contact. Could you repeat the name or number?",
    "No contact found. Please specify who you want to message or call",
    "I need a contact name or number to proceed. Please try again",
]

cannot_send_whatsapp_message = [
    "Sorry, I couldn't send the WhatsApp message",
    "I was unable to deliver your WhatsApp message",
    "There was a problem sending your WhatsApp message",
    "I couldn't complete your WhatsApp request. Please try again",
]

welcome_back_user = [
    "Welcome back! Ivy is here to assist you 24/7 and 7 days a week",
    "Good to see you again. How can I help you today?",
    "Welcome back! Ready when you are",
]

ask_message_prompt_user = [
    "What message should I send?",
    "What would you like to say?",
    "Please tell me the message.",
    "What do you want to send?",
    "Okay, what's the message?",
    "Tell me the message to send.",
    "What should the message say?",
    "I'm ready. What's the message?",
]

city_not_found_user = [
    "Sorry, I couldn't find details for {city}. You can check the map: {map_url}",
    "I couldn't locate {city}. Try another city or see this map: {map_url}",
    "I couldn't get weather info for {city} right now. Map might help: {map_url}",
    "I can't find {city}. Would you like to open the map? {map_url}",
    "No results for {city}. Here's a map search you can use: {map_url}",
]

cannot_calculate = [
    "Sorry, I couldn't calculate that. {error}",
    "Hmm, I'm having trouble with that calculation. {error}",
    "I wasn't able to solve that math problem. {error}",
    "Oops, something went wrong with the calculation. {error}",
    "I can't figure out that math. {error}",
    "That calculation didn't work. {error}",
    "I'm unable to process that math expression. {error}",
    "Sorry, I encountered an error with that calculation. {error}",
]

error_in_allcommands = [
    "Oops, something went wrong on my end. Let's try that again!",
    "Unexpected error, I'm sorry we can try again",
    "Sorry, there was a I.V.Y. error, pleaste try again later",
    "Ivy will fix herself shortly, I.V.Y. system errored, my apologies for this"
    "It appears that I.V.Y. had a issue, please try again..."
    "I.V.Y. system malfunction, id: 8-4f6-9e6a-dasw5bc2",
    "Ivy Error id: 83196b-f063-4ff6-9e6a",
]
