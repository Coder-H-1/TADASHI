import os, pyttsx3, sys,speech_recognition as sr, random,wikipedia,time,platform,webbrowser,datetime,pyautogui
from keyboard import press_and_release, write
from pyautogui import rightClick

try: import pywhatkit
except: 
    print("Please start it with Internet, Sir")
    sys.exit()

path = os.getcwd()


try: 
    os.makedirs(f"{path}//Custom_Set")
except:pass
try: 
    os.makedirs(f"{path}//Custom_Path")
except:pass

Attrib=[ 1 , 200 , 0 , 'Male' ] #format - [0]=volume, [1]=pace, [2]=voice, [3]=voice gender
def speak(audio): ### Speaks output
    "Output audio - Speech"
    numb = int(Attrib[2])
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[numb].id)
    engine.setProperty('rate' , 200)
    print(f"TADASHI : {audio}")
    engine.say(audio)
    engine.runAndWait()

def takecommand(): ### Takes query from user
    "Takes Command from User in string format return query" 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        os.system("title TADASHI - Listening...")
        r.pause_threshold = 1
        try:audio = r.listen(source, 7)
        except:pass

    try: 
        os.system("title TADASHI - Initializing...")
        query = r.recognize_google(audio)
    except:
        query = "none"
    query = str(query)
    return query.lower()

def __System__(): ## Checks Attributes of pc
    "Informations about user's pc"
    name = platform.system()
    print("Verifing the Operating System (OS)")
    if name != "Windows": 
        print("Verification could be done --> Error OS:Linux or Mac")
        speak("Sorry, not developed for other System, Only for Windows thankyou")
        sys.exit()

    elif 'Windows' in name: 
        print("Verification : Done")
        processor = platform.architecture()[0]
        other = platform.platform()
        print("OS : " + other, processor)
        print("")
        os.system("cls")

class Main:
    "The Home for all Classes containing all functioning of TADASHI"
    class ApplicationsPaths: ### Home for coded paths
        taskmanager = "C:\\Windows\\System32\\Taskmgr.exe"
        DiskManagement  = "C:\\Windows\\System32\\Diskmgmt.msc"
        CMD = "C:\\Windows\\System32\\cmd.exe"
        Notepad  = "C:\\Windows\\notepad.exe"
        fileMGMT = "C:\\Windows\\explorer.exe"
        regEditor = "C:\\Windows\\regedit.exe"
        DeviceMGMT = "C:\\Windows\\System32\\Devmgmt.msc"
        DeviceInfo = "C:\\Windows\\System32\\dxdiag.exe"
        MSConfig = "C:\\Windows\\System32\\msconfig.exe"
        MSINFO = "C:\\Windows\\System32\\msinfo32.exe"
        Chrome_exe = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    
    class Chatbot: ### Replies the given query, Hence the name Chatbot
        def chat(_chat=None):
            if _chat != None:
                hellohi = [
                        'hi',
                        'hello',
                        'hello tadashi',
                        'oh hello',
                        'oh hello tadashi',
                        'hola',             
                        'hola amigo',
                        'bonjour'
                    ]
                
                hellohi_reply = [
                            'Oh hello Sir',
                            'Hello Sir',
                            'Oh hello sir, How are you Doing',
                            'Hello Sir, How are you?'
                            ]
                
                how_send = [
                        'how are you',
                        'how are you doing',
                        'how about you',
                        'how are you tadashi'
                        ]
                
                how_return = [
                        "I'm fine",
                        "I'm fine Sir",
                        "Fine Sir",
                        "I'm good",
                        "I'm good Sir",
                        "I'm very well Sir", 
                        "well Sir"
                            ]
                
                work_send = [
                'what are you doing',
                'what you doing'
                ]
                
                work_reply = [
                'Sir, I am listening and answering to you.', 
                'I am speaking to you'
                ]
                
                iam_send =  [
                "i am fine",
                "i am good",
                "mai theek hun",
                "not good"
                ]
                
                iam_reply = [
                        "That's good",
                        "That's Fine",
                        "Oh, Great!",
                        "Good To Hear That",
                        "Great!",
                        "Good."
                            ]
                
                iam2_send = [
                "i am not fine",
                "i am not good"
                ]      
                
                iam2_reply = [
                        "Oh?, What happened?",
                        "That's not good",
                        "OH!",
                        "Sorry to hear but what happened?",
                        "What happened?"
                        ]
                
                Nothing = [
                'nothing',
                "what can you do",
                'nothing at all'
                ]
                
                Nothing_reply = [
                'Nothing',
                'nothing at all',
                'Absolutely Nothing'
                ]

                query = str(_chat)
                if Main.SetNote.query_Request(query) == True: pass
                else:
                    if query in hellohi: 
                        speak(random.choice(hellohi_reply))

                    elif query in Nothing: 
                        speak(random.choice(Nothing_reply))

                    elif query in iam2_send: 
                        speak(random.choice(iam2_reply))

                    elif query in how_send: 
                        speak(random.choice(how_return))

                    elif query in work_send: 
                        speak(random.choice(work_reply))

                    elif 'jarvis' in query or 'friday' in query: 
                        speak("Sir, 'Tadashi' Here")

                    elif 'introduce yourself' in query: 
                        speak("Hello, I am Tadashi")
                        speak(f"An Artificial Intelligent, here to provide assistance with a variety of tasks")
                        speak("I am Coded to also for Online stuff")

                    elif '*' in query: 
                        speak("Please don't try to abuse")

                    elif 'who are you' in query or 'well by the way who are you' in query or 'who the heck are you' in query:
                        Main.Chatbot.chat('introduce yourself')

                    elif query in iam_send:
                        speak(random.choice(iam_reply))

                    else:
                        pass

    class Wiki: ### Searches query on Wikipedia
        def Search(query=None, condition=None):
            if condition == None: 
                condition = "According To Wikipedia"
            if query != None:
                query = str(query)
                try: 
                    results = wikipedia.summary(query, sentences=2)
                    speak(condition)
                    speak(results)
                except:
                    try: 
                        results = wikipedia.summary("who is " + query, sentences=2)
                        speak(condition)
                        speak(results)
                    except:
                        try: 
                            results = wikipedia.summary("defination of " + query, sentences=2)
                            speak(condition)
                            speak(results)
                        except:
                            try: 
                                results = wikipedia.summary("what is " + query, sentences=2)
                                speak(condition)
                                speak(results)
                            except:
                                try: 
                                    results = wikipedia.summary("where is " + query, sentences=2)
                                    speak(condition)
                                    speak(results)
                                except:
                                    try: 
                                        results = wikipedia.summary("define " + query, sentences=2)
                                        speak(condition)
                                        speak(results)
                                    except:
                                        if condition != "According to Internet":
                                            speak("Sir, Couldn't find anything about it.")

    class Google: ### Googles the given query
        def __init__(self, query):
            query = str(query)
            query = query.replace("google search " , "")
            query = query.replace("google " , "")
            query1= query.replace(' ' , "+")
            pywhatkit.search(query1)
            Main.Wiki.Search(query, 'According to Internet')

    class SystemCommand: ### All System Command lies here and also open|close commands
        def System(command=None):
            command= str(command)
            if 'restart the pc' in command or 'restart pc' in command or 'restart computer' in command or 'restart the computer' in command: 
                speak("Restarting the Computer")
                press_and_release("win + d")
                time.sleep(0.3)
                press_and_release("alt + f4")
                time.sleep(0.3)
                press_and_release("down")
                time.sleep(0.2)
                press_and_release("enter")
            
            elif 'shutdown computer' in command or 'shutdown pc' in command or 'shutdown my pc' in command or 'shutdown the computer' in command: 
                speak("Shutting down the computer")
                press_and_release("win+d")
                time.sleep(0.3)
                press_and_release("alt+f4")
                time.sleep(0.3)
                press_and_release("enter")
            
            elif 'computer to sleep' in command or 'pc to sleep' in command or 'put the computer to sleep' in command: 
                speak("Putting Computer to sleep")
                press_and_release("win + d")
                time.sleep(0.3)
                press_and_release("alt + f4")
                time.sleep(0.3)
                press_and_release("up")
                time.sleep(0.2)
                press_and_release("enter")
            
            elif 'open settings' in command: 
                press_and_release("win + i")
                speak("Opened System Settings")
            
            elif 'lock computer' in command or 'lock the computer' in command or 'lock my pc' in command or 'lock the pc' in command: 
                press_and_release("win + l")
            
            elif 'open run prompt' in command: 
                press_and_release("win + r")

            elif 'open search' in command: 
                press_and_release("win + s")

            elif 'refresh the computer' in command or 'refresh computer' in command or 'refresh pc' in command or 'refresh the pc' in command: 
                press_and_release("f5")
            
            elif 'open display settings' in command:
                if int(platform.release()) <= 10: 
                    speak("Sir, You are on windows version lower than windows 10 so its ease of access at that time, ?Operation aborted?")
                elif int(platform.release()) >= 10:
                    press_and_release("win + u")
            
            elif 'make a folder on desktop' in command:
                command = str(command)
                command = command.replace("make a folder on desktop" , "")
                press_and_release("win + d")
                time.sleep(0.2)
                rightClick(x=0,y=0)
                time.sleep(0.1)
                press_and_release("ctrl + shift + n")
                if 'of name ' in command:
                    command = command.replace("of name " , "")
                    write(command)
                    time.sleep(0.5)
                    press_and_release("enter")
                    
                else:
                    pass
                speak("Created folder on Desktop")

            else: 
                pass

        def Sys(command):
            command = str(command)
            command = command.lower()
            if 'open task manager' in command: 
                os.startfile(Main.ApplicationsPaths.taskmanager)
                speak("Opened Task manager")

            elif 'close task manager' in command: 
                os.system("taskkill /f /im taskmgr.exe")
                speak("Closed Task Manager")
                
            elif 'open disk management' in command: 
                os.startfile(Main.ApplicationsPaths.DiskManagement)
                speak("Opened Disk Management")

            elif 'close disk management' in command: 
                os.system("taskkill /f /im diskmgmt.msc")
                speak("Closed Disk Management")

            elif 'open cmd' in command or 'open terminal' in command: 
                os.startfile(Main.ApplicationsPaths.CMD)
                speak("Opened Command Prompt")

            elif 'close cmd' in command or 'close terminal' in command: 
                os.system("taskkill /f /im cmd.exe")

            elif 'open notepad' in command: 
                os.startfile(Main.ApplicationsPaths.Notepad)
                speak("Opened Notepad")

            elif 'close notepad' in command: 
                os.system("taskkill /f /im notepad.exe")
                speak("Closed Notepad")

            elif 'open file manager' in command or 'open file explorer' in command: 
                os.startfile(Main.ApplicationsPaths.fileMGMT)
                speak("Opened File Explorer")

            elif 'close file explorer' in command or 'close file manager' in command: 
                speak("Sorry, It cannot be done.")

            elif 'open registry editor' in command: 
                os.startfile(Main.ApplicationsPaths.regEditor)
                speak("Opened Registry Editor")

            elif 'close registry editor' in command: 
                os.system("taskkill /f /im regedit.exe")
                speak("Closed Registry Editor")

            elif 'open device manager' in command: 
                os.startfile(Main.ApplicationsPaths.DeviceMGMT)
                speak("Opened Device Manager")

            elif 'close device manager' in command: 
                os.system("taskkill /f /im devmgmt.msc")
                speak("Closed Device Manager")

            elif 'open device info' in command: 
                os.startfile(Main.ApplicationsPaths.DeviceInfo)
                speak("Opened System Information")

            elif 'close device info' in command: 
                os.system("taskkill /f /im msinfo32.exe")
                speak("Closed System Information")

            elif 'hostname' in command: 
                os.system("hostname")
                speak("Printed Hostname")

            elif 'ip address' in command: 
                os.system("ipconfig")
                speak("Printed IP Address")
            
            elif 'open system config' in command: 
                os.startfile(Main.ApplicationsPaths.MSConfig)
                speak("Opened Microsoft Configurations")

            elif 'close system config' in command: 
                os.system("taskkill /f /im msconfig.exe")
            
            elif 'open system info' in command: 
                os.startfile(Main.ApplicationsPaths.MSINFO)
                speak("Opened Microsoft Information")

            elif 'close system info' in command: 
                os.system("taskkill /f /im msinfo32.exe")
                speak("Closed Microsoft Information")
            
            elif 'take screenshot' in command or 'take a screenshot' in command: 
                press_and_release("win + PrtScn")
                speak("ScreenShot Taken")
                os.startfile("C:\\Users\\H\\Pictures\\Screenshots")

            elif 'clear screen' in command or 'cls' in command or 'clear the screen' in command: 
                os.system("cls")         
            
            elif 'go to desktop' in command: 
                press_and_release("win + d")
                speak("Done!, You're on Desktop now") 

            elif 'open chrome' in command:  
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                speak("Opened Chrome")

            elif 'close chrome' in command or 'shutdown chrome' in command: 
                os.system("Taskkill /f /im chrome.exe")
                speak("Closed Chrome")
                os.system("cls")
            
            elif 'open google' in command: 
                webbrowser.open("https://www.google.com/")
                speak("Opened Google")

            elif 'open youtube' in command: 
                webbrowser.open("https://www.youtube.com/")
                speak("Opened Youtube")

            elif 'open reddit' in command: 
                webbrowser.open("https://www.reddit.com/")
                speak("Opened Reddit")

            elif 'open instagram' in command: 
                webbrowser.open("https://www.instagram.com/")
                speak("Opened Instagram")

            elif 'open camera' in command: 
                os.startfile(f"C:\\Windows\\Camera\\Camera.exe")
                speak("Opened Camera")

            elif 'close camera' in command: 
                os.system("taskkill /f /im Camera.exe")
            
            elif 'open control panel' in command: 
                os.system("control.exe")

            elif 'close control panel' in command: 
                speak("[Operation Aborted!], You have to close it manually.")

            else:
                Main.SystemCommand.System(command)

    class Youtube: ### Searches query on YouTube
        def __init__(self, query): 
            query = str(query)
            query = query.replace("youtube " , "")
            query = query.replace("youtube search " , "")
            query1 = query.replace(" " , "+")
            if 'play+playlist' in query1: 
                webbrowser.open("https://www.youtube.com/watch?v=Ct5kU0w1Vgk&list=PLTnfJXRz5-KMLKqe93Pa0ddscbzZSWdoM")
            elif 'play+' in query1: 
                query1 = query1.replace("play+" , "")
                pywhatkit.playonyt(query1)
                query1 = query1.replace("+" , " ")
                speak(f"Played {query1} on YouTube")
            else: 
                webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={query1}") 
    
    class GetTime: ### Checks the Time if user asks
        def __ChangeSet__(hour):
            hour = int(hour)
            if hour == 13:
                return "1", "PM"
            elif hour == 14:
                return "2", "PM"
            elif hour == 15:
                return "3", "PM"
            elif hour == 16:
                return "4", "PM"
            elif hour == 17:
                return "5", "PM"
            elif hour == 18:
                return "6", "PM"
            elif hour == 19:
                return "7", "PM"
            elif hour == 20:
                return "8", "PM"
            elif hour == 21:
                return "9", "PM"
            elif hour == 22:
                return "10", "PM"
            elif hour == 23:
                return "11", "PM"
            elif hour == 24:
                return "12", "PM"
            else:
                return str(hour),"AM"

        def onlytime(): 
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute
            return hour, minute  

        def GiveTime():
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            Day = datetime.datetime.now().strftime("%d")
            month = datetime.datetime.now().strftime("%m")
            year = datetime.datetime.now().strftime("%y")
            hour = int(hour)
            _date_ = Main.GetTime.MonChanger(month)
            if hour <= 12:
                _get = "AM"
            elif hour >= 13: 
                hour,_get = Main.GetTime.__ChangeSet__(hour)

            return f"Time is {hour}:{minute} {_get} of date {Day}-{_date_}-{year}"

        def MonChanger(_time_=0):
            ### For month ###
            _time_ = int(_time_)
            if _time_ == 1: 
                return "January"
            elif _time_ == 2: 
                return "February"
            elif _time_ == 3: 
                return "March"
            elif _time_ == 4: 
                return "April"
            elif _time_ == 5: 
                return "May"
            elif _time_ == 6: 
                return "June"
            elif _time_ == 7: 
                return "July"
            elif _time_ == 8: 
                return "August"
            elif _time_ == 9: 
                return "September"
            elif _time_ == 10: 
                return "October"
            elif _time_ == 11: 
                return "November"
            elif _time_ == 12: 
                return "December"

            return f"{_time_}" ### Returns time in string format
    
    class Restarter: ### To restart this file
        def res():
            try: 
                os.startfile(f"{path}\\Main.py")
                sys.exit()
            except Exception as e:
                speak(f"Error - [{e}]")

    class PathExe: ### Reads Custom_files for paths
        def __find__(query):
            query = str(query)
            query = query.replace("start " , "")
            for files in os.listdir(f"{os.getcwd()}//Custom_Path"):
                for lines in open(f"{os.getcwd()}//Custom_Path//{files}", "r"):
                    lines = str(lines)
                    thing, execution = lines.split(" : ")
                    if query == thing: 
                        os.startfile(execution)

    class SetNote: ### Sets|Reads Custom chat |Sets - triggered by set chat
        def query_reset():
            for files in os.listdir(f"{path}\\Custom_Set"):
                if files == "speak_attrib.value":pass
                else:
                    try: 
                        os.remove(f"{path}\\Custom_Set\\{files}")
                    except Exception as e: 
                        print(f"Error : [ {e} ]")
        
        def query_Set(query):
            query = str(query)
            query = query.replace("set chat " , "")
            query = query.replace("if i say " , "")
            isay, ysay = query.split(" you say ")
            filesnumb = 0
            for files in os.listdir(f"{os.getcwd()}//Custom_Set"):
                filesnumb+=1

            with open(f"{os.getcwd()}//Custom_Set//Custom{filesnumb}.set_value", "w") as file1: 
                file1.write(f"{isay} : {ysay}\n")

            file1.close()
    
        def query_Request(query):
            query = str(query)
            toReturn = False
            for files in os.listdir(f"{os.getcwd()}//Custom_Set"):
                if files == "speak_attrib.value":pass
                else:
                    for lines in open(f"{os.getcwd()}//Custom_Set//{files}", "r"):
                        lines = str(lines)
                        isay, ysay = lines.split(" : ")
                        if query == isay: 
                            speak(ysay)
                            toReturn = True

            return toReturn

    class Maths_sol: ### Solves the simple maths problem in terminal
        def __maths__(query):
            query = str(query)
            reply = False
            if 'sum of' in query or '+' in query:
                if 'sum of ' in query: 
                    query = query.replace("sum of " , "")
                    d1,d2 = query.split(" and ")
                    sum = int(d1) + int(d2)

                elif '+' in query: 
                    d1,d2 = query.split(" + ")
                    sum = int(d1) + int(d2)

                speak(sum)
                reply = True

            elif 'subtract' in query or '-' in query:
                query = query.replace("subtract " , "")
                query = query.replace("sub " , "")

                if 'from' in query: 
                    d1,d2 = query.split(" from ")
                    sub = int(d2) - int(d1)

                elif 'minus' in query or '-' in query: 
                    d1,d2 = query.split(" - ")
                    sub = int(d1) - int(d2)

                speak(sub)
                reply = True

            elif 'multiply' in query or 'x' in query:
                if 'multiply' in query: 
                    query = query.replace("multiply" , "")
                    d1,d2 = query.split(" by ")
                    mut = int(d1) * int(d2)

                elif 'x' in query: 
                    d1,d2 = query.split(" x ")
                    mut = int(d1) * int(d2)

                speak(mut)
                reply = True

            elif 'divide' in query or '/' in query or 'divided by' in query:
                if 'divide' in query: 
                    query = query.replace("divide " , "")
                    d1,d2 = query.split(" by ")
                    div = int(d1) / int(d2)

                elif '/' in query: 
                    d1,d2 = query.split("/")
                    div = int(d1) / int(d2)

                elif 'divided by' in query: 
                    d1,d2 = query.split("divided by")
                    div = int(d1) / int(d2)

                speak(div)
                reply = True

            return reply

    class SetSpeakAttrib: ### Sets Attributes for Speak
        def __speakAttrib__():
            "You have to specify the old_pace and new_pace"
            default = [ 1 , 200 , 0 , 'Male']
            for lines in open(f"{os.getcwd()}\\Custom_Set\\speak_attrib.value" , "r"):
                if "set volume : " in lines:
                    lines = lines.replace("set volume : " , "")
                    if int(lines) <= 1:
                        Attrib[0] = lines
                    else: 
                        Attrib[0] = default[0]

                elif "set vol_pace : " in lines:
                    lines = lines.replace("set vol_pace : " , "")
                    if int(lines) <= 300:
                        Attrib[1] = lines
                    else: 
                        Attrib[1] = default[1]

                elif "set voice : " in lines:
                    lines = lines.replace("set voice : " , "")
                    if int(lines) <= 5:
                        Attrib[2] = lines
                    else: 
                        Attrib[2] = default[2]

                elif "set voice_gender : " in lines:
                    lines = lines.replace("set voice_gender : " , "")
                    Attrib[3] = f"{lines}"

    class SetVolume:
        def __init__(self, query):
            self.query = query

    class QUERY_EXTRA:
        def set_attributes():
            os.system("cls")
            print("Usage : [intype] | [type] | [value]")
            print("")
            print(" -- [intype] -- ")
            print("     1.) speak ")
            print("     only developed for speak, Yet. ")
            print("")
            print(" -- [type] -- ")
            print("     1.) volume              | Default = 0.5   | Max       = 1")
            print("     2.) vol_pace            | Default = 200   | Max       = 300")
            print("     3.) voice               | Default = 0     | Max       = [voices in system]")
            print("     4.) voice_gender        | Default = Male  | Change by = Female")
            print("")
            print(" -- value -- ")
            print("     -- Can be any value lower than Max settings")
            print("")
            print(" Sorry not fully developed yet.")

    class Responder: ### One word to describe Query Executor | Locator
        def res():
            query = takecommand().lower()
            if query != "none":
                print("User Said : " + query)
                if 'google search' in query: 
                    Main.Google(query)

                elif 'wikipedia ' in query or 'define ' in query: 
                    query = query.replace("wikipedia search " , "")
                    query=query.replace("wikipedia " , "")
                    Main.Wiki.Search(query) 

                elif 'what time is it' in query or 'tell me time' in query or 'tell time' in query: 
                    speak(Main.GetTime.GiveTime())

                elif 'youtube ' in query: 
                    Main.Youtube(query)

                elif 'system showdown' in query or 'exit system' in query or 'quit' in query: 
                    speak("Have a good day Sir")
                    sys.exit()

                elif 'restart yourself' in query or 'recharge yourself' in query:
                    speak("Restarting Myself")
                    Main.Restarter.res()

                elif 'start file ' in query: 
                    Main.PathExe.__find__(query)

                elif 'et chat ' in query: 
                    Main.SetNote.query_Set(query)

                elif 'reset chat' in query: 
                    Main.SetNote.query_reset()

                elif 'set attributes' in query:
                    Main.QUERY_EXTRA.set_attributes()

                else:
                    Main.SystemCommand.Sys(query)
                    Main.Chatbot.chat(query)
                    Main.Maths_sol.__maths__(query)

                   
if __name__=="__main__":
    os.system("title TADASHI - At your service")
    os.system("cls")
    Main.SetSpeakAttrib.__speakAttrib__()
    __System__()
    hour, minute = Main.GetTime.onlytime()
    if int(hour) > 0 and int(hour) <= 11 and int(minute) < 60: 
        speak("Good Morning, Sir")

    elif int(hour) > 11 and int(hour) <= 15 and int(minute) < 60: 
        speak("Good Afternoon, Sir")

    elif int(hour) > 15 and int(hour) <= 18 and int(minute) < 60: 
        speak("Good Evening, Sir")

    elif int(hour) > 18 and int(minute) < 60: 
        speak("Good Night, Sir")

    else: 
        speak("Welcome Sir")

    speak(Main.GetTime.GiveTime()) 
    while True:
        try: 
            Main.Responder.res()
        except Exception as e: 
            print(f"Error : [ {e} ]")
