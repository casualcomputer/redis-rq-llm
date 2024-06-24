import subprocess
import requests
import time

# List of 100 philosophy questions: https://philosophy.hku.hk/think/phil/101q.php
questions = [
    "Is the mind the same as the brain, or do we have souls?",
    "Can computers think, or fall in love?",
    "Can computers be creative?",
    "What is consciousness?",
    "Can we really know what it feels like to be a bat?",
    "When you have a toothache, is the pain in your mouth or in your brain?",
    "What is an emotion?",
    "Is love just a feeling?",
    "How is love different from passion or sexual desire?",
    "Are emotions irrational?",
    "Which would you rather be - an unhappy human being or a happy dog?",
    "What is the meaning of life?",
    "Is happiness the most important purpose in life?",
    "Is it always better to have more choices?",
    "Does freewill really exist?",
    "If there is no freewill, should we punish people at all?",
    "If God knows what you will do tomorrow, do you still have freewill?",
    "Does God exist?",
    "If God exists, why is there so much evil in the world?",
    "Can God create a stone so heavy that he cannot lift?",
    "Can there be two almighty Gods?",
    "Can there be morality without God?",
    "Is morality relative?",
    "Is it objectively wrong to torture innocent babies just for fun?",
    "Is abortion ever permissible?",
    "Is it wrong to have children, if you don't know whether they want to be born?",
    "What is wrong with incest?",
    "What is friendship and why do we need it?",
    "What is art?",
    "Is there progress in art?",
    "Can food be art?",
    "Is it wrong to spend money on expensive food when people are dying of hunger?",
    "If someone is drowning and you refuse to help, are you responsible for his death?",
    "Why do we punish people?",
    "Is it alright to torture terrorists to extract information?",
    "When is it ok, if ever, to disobey the law?",
    "Is it the main purpose of law to promote morality?",
    "Should governments penalize people for unhealthy lifestyles?",
    "Why ban drugs and not alcohol or trans-fat?",
    "Should prostitution be made legal?",
    "Is there such a thing as sexual perversion?",
    "What is wrong with having sex with animals?",
    "How much freedom should people have?",
    "Are people free to sell themselves into slavery?",
    "Why think there are universal human rights?",
    "Is democracy the same as decision by the majority?",
    "Should people who pay more taxes get more votes?",
    "Is democracy suitable for all countries?",
    "When should governments intervene in the market?",
    "Is there a difference between free trade and fair trade?",
    "What is wrong, if anything, about protectionism?",
    "Is patriotism irrational?",
    "Can wars ever be just?",
    "Should people have the right to live in any country they wish?",
    "Is the preservation of culture a good reason to limit immigration?",
    "Is race a biological category or a social construct?",
    "Are you the same person you were ten years ago?",
    "What is a person? Is it the mind, or the body?",
    "Do we think with language or pictures?",
    "Why do we dream?",
    "Can animals reason?",
    "What about fish, oysters and tomatoes?",
    "Do animals have rights?",
    "If we eat chickens, why not dogs, dolphins, or babies?",
    "If super-intelligent aliens want to eat humans, are they wrong?",
    "If meat can be grown using stem cells, is there any reason not to eat meat?",
    "Should we let people commit suicide when they are terminally ill?",
    "Should we kill coma patients on life support to provide more resources to others?",
    "Should organ donation be made compulsory?",
    "Should organ donors be financially compensated?",
    "Is it wrong to grow brain dead babies to harvest their organs?",
    "Why should we respect the dead?",
    "Should we fear death?",
    "Is life meaningless if we can live forever?",
    "What are numbers and do they really exist?",
    "Does Sherlock Holmes exist?",
    "Why is there something rather than nothing?",
    "What is time?",
    "Does time flow? How fast does it flow?",
    "Can something be at two places at the same time?",
    "Is time travel possible?"]


url = "http://localhost:8000/query"

# Iterate through each question in the list
for index, question in enumerate(questions, start=1):
    # Record the start time
    start_time = time.time()

    # Send the POST request to the FastAPI server
    response = requests.post(url, json={"question": question})

    # Record the end time
    end_time = time.time()

    # Calculate the duration taken to get the response
    duration = end_time - start_time

    # Print the response and timing information
    print(f"Question {index}: '{question}'")
    print("Response:", response.text)
    print(f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
    print(f"End Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
    print(f"Duration: {duration:.2f} seconds")
    print("-" * 60)  # Print a separator line for clarity

