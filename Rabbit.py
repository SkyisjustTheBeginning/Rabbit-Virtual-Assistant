from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3
import webbrowser
import random
commands = ["Covid Update - covid update for","Weather Updates - weather update for","News[Currently Offline]","Open Application - open","Open website - go to","Quotes - motivate me","Jokes - amuse me","Find Meaning - what is the meaning of","Sentiment Analysis - analyse sentiment","Sketching Images - sketch"]
chatbot = ChatBot('ChattyRoad')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings",
                  "chatterbot.corpus.english","chatterbot.corpus.french","chatterbot.corpus.chinese")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine. setProperty("rate", 160)
engine.setProperty('voice', voices[1].id)
while True:
    InputFromUser = str(input(""))
    if "covid update for" in InputFromUser:
        print("Working on it......")
        InputFromUser = InputFromUser.split("covid update for",1)
        from covid import *
        CovidHandle = Covid()
        Target = InputFromUser[1]
        InfoOnTarget = CovidHandle.get_status_by_country_name(Target[1:])
        print(">" + "Country:",str(InfoOnTarget.get("country")))
        print(">" +"Active Cases:"+ str(InfoOnTarget.get("active")))
        print(">" +"Deaths:",str(InfoOnTarget.get("deaths")))
        print(">" + "Confirmed:",str(InfoOnTarget.get("confirmed")))
        engine.say("Country" + str(InfoOnTarget.get("country")))
        engine.say("Number of Active cases" + str(InfoOnTarget.get("active")))
        engine.say("Number of Deaths" + str(InfoOnTarget.get("deaths")))
        engine.say("Number of Confirmed Cases" + str(InfoOnTarget.get("confirmed")))
        engine.runAndWait()
    elif "open" in InputFromUser:
        print("Working on it......")
        import os
        InputFromUser = InputFromUser.split("open",1)
        InputFromUser = InputFromUser[1]
        InputFromUser = InputFromUser[1:]
        FinalAppName = InputFromUser + ".exe"
        try:
            engine.say("Opening Application")
            os.system("start " + FinalAppName)
            engine.runAndWait()
        except:
            engine.say("Error! Please Try Again")
            engine.runAndWait()
    elif "go to" in InputFromUser:
        InputFromUser = InputFromUser.split("go to", 1)
        InputFromUser = InputFromUser[1]
        InputFromUser = InputFromUser[1:]
        engine.say("Opening " + InputFromUser)
        engine.runAndWait()
        webbrowser.open(InputFromUser)
    elif "news update" in InputFromUser:
        print("Working on it.....")
        import requests
        try:
             query_params = {
                "source": "bbc-news",
                "sortBy": "top",
                "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
              }
             main_url = " https://newsapi.org/v1/articles"
             res = requests.get(main_url, params=query_params)
             open_bbc_page = res.json()
             article = open_bbc_page["articles"]
             results = []
             for ar in article:
                 results.append(ar["title"])
             print("####Headlines####")
             x = 1
             for l in results:
                 print(str(x) + "." + " " + l)
                 engine.say(str(x) + "." + " " + l)
                 engine.runAndWait()
                 x += 1
        except KeyError:
            print("Oops...We faced an error")
            print("Please try again")
            engine.say("Oops We faced an error")
            engine.say("Please try again later")
            engine.runAndWait()

    elif "amuse me" in InputFromUser:
        joke_database = [
            "Why were the early days of history called The Dark Ages ? \nBecause there were so many knights",
            "Why did the scarecrow win an award?\nHe was outstanding in his field",
            "What's a snake's favourite subject in school ?\nHiss-tory",
            "Why don't eggs tell jokes ?\nThey'd crack each other up",
            "What do you call a funny mountain?\nHill-arious",
            "Where do cows go on Friday nights ?\nThey go to the moo-vies",
            "What do you give a sick lemon ? \n A Lemon Aid",
            "What did the ocean say to the shore ? \n Nothing , It just waved",
            "What kind of Shorts do clouds wear ? \n Thunderwear"]
        choice = random.choice(joke_database)
        print(">" + choice)
        engine.say(choice)
        engine.runAndWait()
    elif "motivate me" in InputFromUser:
        quote_database = [
            'Success is no final, Failure is not fatal, It is the courage to continue that counts - Winston Churchill\n',
            'To see what is right and not do it is a lack of courage - Confucius\n',
            'Tough Times don’t last , Tough people do\n', 'Do or do not.There is no try - Yoda\n',
            'A hero need not speak.When he is gone , The world will speak for him -The Master Chief , Halo\n',
            'The more we learn , The more we discover how much we don’t know -Yoda\n',
            'Don’t focus on the pain,Focus on the progress - Dwayne Johnson\n',
            'Work Hard in silence , Let success make the noise\n', 'Why follow when you can lead\n',
            'Fear kills more dreams than failure ever will - Suzy Kassem\n',
            'If you can dream it , you can Do it -Walt Disney\n', 'There is no excuse for not trying -Barack Obama\n',
            'When something is important enough , you do it even if the odds are not in your favour -Elon Musk\n',
            'The secret of success is to do the common things uncommonly well -John D. Rockefeller\n',
            'It is choice , not chance , that defines our destiny -Halo\n',
            'If you cannot do great things , do small things in a great way -Napoleon Hill\n',
            'Everybody is a genius.But if you judge a fish by its ability to climb a tree, It will live its whole life thinking that it is stupid. -Albert Einstein\n',
            'The true sign of intelligence is not knowledge but imagination. -Albert Einstein\n',
            'We are here to put a dent in the universe.Otherwise why would we be here ? -Steve Jobs\n',
            'The only way to do great work is to love what you do -Steve Jobs\n',
            'Courage is what it takes to stand up and speak, Courage is also what it takes to sit down and listen -Richard Branson\n',
            'When something is important enough , you do it even if the odds are not in your favour -Elon Musk\n',
            'Life is too short for long-term grudges. -Elon Musk\n',
            'Rich people believe “I create my life”.Poor people believe “Life happens to me” -T. Harv Eker\n',
            'Your brand is what people say about you when you are not in the room. -Jeff Bezos\n',
            'You see but you do not observe.The distinction is clear. -Sherlock Holmes\n',
            'Character is like a tree and reputation like a shadow.The shadow is what we think of it.The tree is the real thing. -Abraham Lincoln\n',
            'You cannot help men permanently by doing for them what they could and should do themselves. -Abraham Lincoln\n',
            'Whatever you are , be a good one. -Abraham Lincoln\n',
            'It is important to follow your dreams and heart.Do something that excites you. -Sundar Pichai\n',
            'Never share your secrets with anybody.It will destroy you. -Chanakya\n',
            'If your hate could be turned into electricity.It would light up the whole world. -Nikola Tesla\n',
            'Empathy grounds me and centers me. -Satya Nadella\n',
            'The view you adopt for yourself profoundly affects the way you lead your life. -Satya Nadella\n',
            'If you have been born poor it’s not your mistake, but if you die poor , It is your mistake. -Bill Gates\n',
            'The fear of being different prevents most people from seeking new ways to solve their problems -Robert T. Kiyosaki\n',
            'The primary difference between rich and poor people is how they handle fear. -Robert T. Kiyosaki\n',
            'Strong men don’t have attitude.They have standards.\n',
            'To truly live your life,You must enjoy it. -Daniel Craig\n',
            'Creativity is seeing the same thing but thinking differently. -Dr. APJ Abdul Kalam\n',
            'My pain may be the reason for someone’s laugh.But my laugh must never be the reason for somebody’s pain. -Charlie Chaplin\n',
            'I believe it’s better to be prepared for an illness than to wait for a cure -Roger Moore\n',
            'In life , Don’t react , Always respond. -Sundar Pichai\n',
            'Wear your failure as a badge of honour. -Sundar Pichai\n',
            'The best way to predict your future is to create it. -Abraham Lincoln\n',
            'In the end it’s not the years in your life that count.It’s the life in your years. -Abraham Lincoln\n',
            'The harder the conflict , the greater the triumph. -George Washington\n',
            'It is far better to be alone than to be in Bad Company. -George Washington\n',
            'Good Things take time -John Wooden\n',
            'I have no special talent.I am only passionately curious. -Albert Einstein\n',
            'Life isn’t about finding yourself.Life is about creating yourself. -George Bernard Shaw\n',
            'The purpose of our lives is to be happy. -Dalai Lama\n',
            'In the middle of difficulty lies opportunity. -Albert Einstein\n', 'The best fighter is never angry.\n',
            'It always seems impossible until it’s done. -Nelson Mandela\n',
            'Our history is not our destiny -Alan Cohen\n',
            'Don’t follow the crowd.Let the crowd follow you. -Margaret Thatcher\n',
            'There is a limit to what one can do if people are themselves limited. -Margaret Thatcher\n',
            'You may have to fight a battle more than once to win it. -Margaret Thatcher',
            'You won’t fail unless and until you stop trying', 'Don’t stop when you’re tired.Stop when you are done',
            'A meaningful silence is always better than meaningless words',
            "The most difficult thing is the decision to act.The rest is merely tenacity.-Amelia Earhart",
            "Education is the passport to the future,for tomorrow belongs to those who prepare for it today\n-Malcolm X",
            "The roots of education are bitter,but the fruit is sweet \n - Aristotle",
            "Be a game-changer.The world is already full of players.\n ~Anonymous"]
        choice = random.choice(quote_database)
        print(">" + choice)
        engine.say(choice)
        engine.runAndWait()
    elif "analyse sentiment" in InputFromUser:
        print("Working on it......")
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        InputFromUser = InputFromUser.split("analyse sentiment",1)
        SentenceToAnalyse = InputFromUser
        SentenceToAnalyse = SentenceToAnalyse[1:]
        sentence = SentenceToAnalyse
        sid_obj = SentimentIntensityAnalyzer()
        sentiment_dict = sid_obj.polarity_scores(sentence)
        y = sentiment_dict['neg'] * 100
        string = str(round(y)) + "% Negative"
        print(">"+string)
        engine.say(string)
        engine.runAndWait()
        y = sentiment_dict['neu'] * 100
        string = str(round(y)) + "% Neutral"
        print(">"+string)
        engine.say(string)
        engine.runAndWait()
        string = str(round(sentiment_dict['pos'] * 100)) + "% Positive"
        print(">" + string)
        engine.say(string)
        engine.runAndWait()
        if sentiment_dict['compound'] >= 0.05:
            string = "Conclusion:Positive"
            print(">"+string)
            engine.say(string)
            engine.runAndWait()
        elif sentiment_dict['compound'] <= - 0.05:
            string = "Conclusion:Negative"
            print(">" + string)
            engine.say(string)
            engine.runAndWait()
        else:
            string = "Conslucion:Neutral"
            print(">" + string)
            engine.say(string)
            engine.runAndWait()
    elif "weather update" in InputFromUser:
        print("Working on it.....")
        import requests
        InputFromUser = InputFromUser.split("weather update for",1)
        InputFromUser = InputFromUser[1]
        WeatherTarget = InputFromUser[1:]
        api_key = "65825486e9c1aefba2408ed97a7dfb9b"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + WeatherTarget

        response = requests.get(complete_url)

        x = response.json()
        if x["cod"] != "404":
            y = x["main"]

            current_temperature = y["temp"]
            current_pressure = y["pressure"]

            current_humidiy = y["humidity"]

            z = x["weather"]
            weather_description = z[0]["description"]
            current_temperature = current_temperature - 273.15
            Status = "Weather update for " + WeatherTarget + "\n" " Current Temperature:" + str(
                round(current_temperature)) + "\n" + " Current Humidity:" + str(
                round(current_humidiy)) + "\n" + " Current Pressure:" + str(
                round(current_pressure)) + "\n" + " Weather Description:" + str(weather_description)
            print(">" + Status)
            engine.say(Status)
            engine.runAndWait()
    elif "google" in InputFromUser:
        print("Working on it......")
        InputFromUser = InputFromUser.split("google",1)
        InputFromUser = InputFromUser[1]
        query = InputFromUser[1:]
        from googlesearch import search
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            print("I found this on the Internet....")
            engine.say("I found this on the Internet")
            engine.runAndWait()
            print(j)
    elif "what is the meaning of" in InputFromUser:
        print("Working on it......")
        from PyDictionary import *
        InputFromUser = InputFromUser.split("what is the meaning of", 1)
        InputFromUser = InputFromUser[1]
        query = InputFromUser[1:]
        dict = PyDictionary()
        meaning = dict.meaning(query)
        Compiled_Meanings = meaning.get("Noun")
        print("I found this")
        for i in Compiled_Meanings:
            i = str(i)
            print(i.title())
            engine.say(i.title())
            engine.runAndWait()
        print(">" +"That's all I found")
        engine.say("That's all I found")
        engine.runAndWait()
    elif "make a note" in InputFromUser:
        engine.say("I am going to make a quick note.Please enter name of the note")
        nameofnote = input("Name of Note:")
        Control = open(nameofnote,"w")
        engine.say("What should I write?")
        content = input("")
        Control.write(content)
        Control.close()
        name = "I have saved the note file as " + nameofnote
        content = "The Content saved" + content
        engine.say(name+content)
        engine.runAndWait()
    elif "sketch" in InputFromUser:
        import cv2
        import os
        filetosketch = input("File Name(without format)")
        outputfilename = input("Output File Name:")
        outputfilename = outputfilename + ".jpg"
        filetosketch = filetosketch + ".jpg"
        img = cv2.imread(filetosketch)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_invert = cv2.bitwise_not(img_gray)
        img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
        def dodge(x, y):
            return cv2.divide(x, 255 - y, scale=256)
        final_img = dodge(img_gray, img_smoothing)
        cv2.imwrite(outputfilename, final_img)
        print(">" + "Image has been sketched.Opening......")
        os.open(outputfilename)
    elif "who are you" in InputFromUser:
        print(">" + "My name is Rabbit , A virtual assistant.Pleased to meet you !")
        engine.say("My name is Rabbit , A virtual assistant Pleased to meet you !")
        engine.runAndWait()
    elif "who created you" in InputFromUser:
        print("I was created by SkyIsJustTheBeginning, A Python Programmer.He toiled day and night for my creation")
        engine.say("I was created by SkyIsJustTheBeginning , A Python Programmer ,, He toiled day and night for my creation")
        engine.runAndWait()
    elif InputFromUser == "help":
        print("> Here is a list of all commands - ")
        engine.say("Here is a list of all commands")
        engine.runAndWait()
        for i in commands:
            print(">" + i)
            engine.say(i)
            engine.runAndWait()
    elif InputFromUser == "stop":
        print("> I am going to terminate")
        engine.say("I am going to terminate")
        engine.runAndWait()
        destiny = input("Are you sure?[Y/N]")
        if destiny == "Y":
            print("> So long , partner....")
            engine.say("So long , partner")
            engine.runAndWait()
            exit()
        elif destiny == "N":
            print("> Termination Process Stopped.It's good to be alive")
            engine.say("Termination process stopped.it is good to be alive")
    else:
        response = chatbot.get_response(InputFromUser)
        print(">" + str(response))
        engine.say(str(response))
        engine.runAndWait()



