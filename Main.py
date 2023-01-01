import os, pyttsx3, sys,speech_recognition as sr, random,wikipedia,time,platform,webbrowser,datetime,pyautogui

from keyboard import press_and_release, write
try: import pywhatkit
except: print("Please start it with Internet, Sir"); sys.exit()


###
os.system("title TADASHI - At your service")
os.system("cls")
###

path = os.getcwd()
extras = []

def speak(audio): engine = pyttsx3.init('sapi5'); voices = engine.getProperty('voices'); engine.setProperty('voice', voices[0].id);  engine.setProperty('rate' , 215);  print(f"TADASHI : {audio}");  engine.say(audio);  engine.runAndWait()

def takecommand(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        os.system("title Listening...")
        r.pause_threshold = 1
        try: audio = r.listen(source, 7)
        except:pass
    try: 
        os.system("title Initializing...")
        query = r.recognize_google(audio)
    except: 
        query = "none"

    query = str(query)
    return query.lower()

def __System__():
    name = platform.system()
    print("Verifing the Operating System (OS)")
    if name != "Windows":
        print("Verification could be done --> Error OS:Linux or Mac")
        speak("Sorry, not developed for other System, Only developed for Windows thankyou")
        sys.exit()
    elif 'Windows' in name:
        print("Verification : Done")
        processor = platform.architecture()[0]
        other = platform.platform()
        print("OS : " + other, processor)
        

__System__()
class Main:
    class ApplicationsPaths: 
        taskmanager = "C:\\Windows\\System32\\Taskmgr.exe"; DiskManagement  = "C:\\Windows\\System32\\Diskmgmt.msc"; CMD = "C:\\Windows\\System32\\cmd.exe"; Notepad  = "C:\\Windows\\notepad.exe"; fileMGMT = "C:\\Windows\\explorer.exe"; regEditor = "C:\\Windows\\regedit.exe"; DeviceMGMT = "C:\\Windows\\System32\\Devmgmt.msc"; DeviceInfo = "C:\\Windows\\System32\\dxdiag.exe"; MSConfig = "C:\\Windows\\System32\\msconfig.exe"; MSINFO = "C:\\Windows\\System32\\msinfo32.exe"; Chrome_exe = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    
    class Chatbot:
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
                if query in hellohi: speak(random.choice(hellohi_reply))
                elif query in Nothing: speak(random.choice(Nothing_reply))
                elif query in iam2_send: speak(random.choice(iam2_reply))
                elif query in how_send: speak(random.choice(how_return))
                elif query in work_send: speak(random.choice(work_reply))
                elif 'jarvis' in query or 'friday' in query: speak("Sir, 'Tadashi' Here")
                elif 'introduce yourself' in query: speak("Hello, I am Tadashi"); speak(f"An Artificial Intelligent, here to provide assistance with a variety of tasks"); speak("I am Coded to also for Online stuff")
                elif '*' in query: speak("Please don't try to abuse")
                elif 'who are you' in query or 'well by the way who are you' in query or 'who the heck are you' in query: Main.Chatbot.chat('introduce yourself')
                elif query in iam_send: speak(random.choice(iam_reply))
                else:pass

    class Wiki:
        def Search(query=None, condition=None):
            if condition == None: condition = "According To Wikipedia"
            if query != None:
                query = str(query)
                try: results = wikipedia.summary(query, sentences=2); speak(condition); speak(results)
                except:
                    try: results = wikipedia.summary("who is " + query, sentences=2); speak(condition); speak(results)
                    except:
                        try: results = wikipedia.summary("defination of " + query, sentences=2); speak(condition); speak(results)
                        except:
                            try: results = wikipedia.summary("what is " + query, sentences=2); speak(condition); speak(results)
                            except:
                                try: results = wikipedia.summary("where is " + query, sentences=2); speak(condition); speak(results)
                                except:
                                    try: results = wikipedia.summary("define " + query, sentences=2); speak(condition); speak(results)
                                    except: speak("Sir, Couldn't find anything about it.")

    class Google: 
        def __init__(self, query): query = str(query); query = query.replace("google search " , ""); query = query.replace("google " , ""); query1= query.replace(' ' , "+"); pywhatkit.search(query1); Main.Wiki.Search(query, 'According to Internet')

    class SystemCommand:
        def __System__(command):
            if 'shutdown computer' in command or 'shutdown pc' in command or 'shutdown my pc' in command or 'shutdown the computer' in command: speak("Shutting down the computer"); press_and_release("win+d"); time.sleep(0.3); press_and_release("alt+f4"); time.sleep(0.3); press_and_release("enter")
            
            elif 'restart my pc' in command or 'restart pc' in command or 'get my pc a restart' in command or 'get my pc a fresh restart' in command or 'restart the computer' in command: speak("Restarting the Computer"); press_and_release("win + d"); time.sleep(0.3); press_and_release("alt + f4"); time.sleep(0.3); press_and_release("down"); time.sleep(0.2); press_and_release("enter")
            
            elif 'computer to sleep' in command or 'pc to sleep' in command or 'put the computer to sleep' in command: speak("Putting Computer to sleep"); press_and_release("win + d"); time.sleep(0.3); press_and_release("alt + f4"); time.sleep(0.3); press_and_release("up"); time.sleep(0.2); press_and_release("enter")
            
            elif 'open settings' in command: press_and_release("win + i"); speak("Opened System Settings")
            
            elif 'lock computer' in command or 'lock the computer' in command or 'lock my pc' in command or 'lock the pc' in command: press_and_release("win + l")
            
            elif 'open run prompt' in command: press_and_release("win + r")

            elif 'open search' in command: press_and_release("win + s")

            elif 'refresh the computer' in command or 'refresh computer' in command or 'refresh pc' in command or 'refresh the pc' in command: press_and_release("f5")
            
            elif 'open display settings' in command:
                if int(platform.release()) <= 10: speak("Sir, You are on windows version lower than windows 10 so its ease of access at that time, ?Operation aborted?")
                elif int(platform.release()) >= 10: press_and_release("win + u")
            
            elif 'make a file on desktop' in command: press_and_release("win + d"); time.sleep(0.5); pyautogui.rightClick(x=1, y=1); time.sleep(0.2); pyautogui.leftClick(x=141, y=158); time.sleep(0.2); pyautogui.leftClick(x=237, y=297); write("File1"); time.sleep(0.1); press_and_release("enter")
            else: pass

        def Sys(command):
            command = str(command)
            command = command.lower()
            if 'open task manager' in command: os.startfile(Main.ApplicationsPaths.taskmanager); speak("Opened Task manager")
            elif 'close task manager' in command: os.system("taskkill /f /im taskmgr.exe"); speak("Closed Task Manager")

            elif 'open disk management' in command: os.startfile(Main.ApplicationsPaths.DiskManagement); speak("Opened Disk Management")
            elif 'close disk management' in command: os.system("taskkill /f /im diskmgmt"); speak("Closed Disk Management")
            
            elif 'open cmd' in command: os.startfile(Main.ApplicationsPaths.CMD); speak("Opened Command Prompt")
            elif 'close cmd' in command: os.system("taskkill /f /im cmd.exe")

            elif 'open notepad' in command: os.startfile(Main.ApplicationsPaths.Notepad); speak("Opened Notepad")
            elif 'close notepad' in command: os.system("taskkill /f /im notepad.exe"); speak("Closed Notepad")

            elif 'open file manager' in command: os.startfile(Main.ApplicationsPaths.fileMGMT); speak("Opened File Explorer")
            elif 'close file explorer' in command: speak("Sorry, It cannot be done.")

            elif 'open registry editor' in command: os.startfile(Main.ApplicationsPaths.regEditor); speak("Opened Registry Editor")
            elif 'close registry editor' in command: os.system("taskkill /f /im regedit.exe"); speak("Closed Registry Editor")

            elif 'open device manager' in command: os.startfile(Main.ApplicationsPaths.DeviceMGMT); speak("Opened Device Manager")
            elif 'close device manager' in command: os.system("taskkill /f /im devmgmt.exe"); speak("Closed Device Manager")
            
            elif 'open device info' in command: os.startfile(Main.ApplicationsPaths.DeviceInfo); speak("Opened System Information")
            elif 'close device info' in command: os.system("taskkill /f /im msinfo32.exe"); speak("Closed System Information")
            
            elif 'hostname' in command: os.system("hostname"); speak("Printed Hostname")
            
            elif 'ip address' in command: os.system("ipconfig"); speak("Printed IP Address")
            
            elif 'open system config' in command: os.startfile(Main.ApplicationsPaths.MSConfig); speak("Opened Microsoft Configurations")
            elif 'close system config' in command: os.system("taskkill /f /im msconfig.exe")
            
            elif 'system info' in command: os.startfile(Main.ApplicationsPaths.MSINFO); speak("Opened Microsoft Information")

            elif 'take screenshot' in command or 'take a screenshot' in command: press_and_release("win + PrtScn"); speak("ScreenShot Taken")

            elif 'clear screen' in command or 'cls' in command or 'clear the screen' in command: os.system("cls")         
            
            elif 'go to desktop' in command: press_and_release("win + d"); speak("Done!, You're on Desktop now") 

            elif 'open chrome' in command:  os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"); speak("Opened Chrome")
            elif 'close chrome' in command or 'shutdown chrome' in command: os.system("Taskkill /f /im chrome.exe"); speak("Closed Chrome"); os.system("cls")
            
            elif 'open google' in command: webbrowser.open("https://www.google.com/"); speak("Opened Google")
            elif 'open youtube' in command: webbrowser.open("https://www.youtube.com/"); speak("Opened YouTube")
            elif 'open reddit' in command: webbrowser.open("https://www.reddit.com/"); speak("Opened Reddit")
            elif 'open instagram' in command: webbrowser.open("https://www.instagram.com/"); speak("Opened Instagram")

            elif 'open camera' in command: os.startfile(f"C:\\Windows\\Camera\\Camera.exe"); speak("Opened Camera")
            elif 'close camera' in command: os.system("taskkill /f /im Camera.exe")
            
            elif 'open control panel' in command: os.system("control.exe")
            elif 'close control panel' in command: speak("Error : [Operation Aborted!], You have to close it manually.")
            else: 
                pass

    class Youtube: 
        def __init__(self, query): 
            query = str(query); query = query.replace("youtube " , ""); query = query.replace("youtube search " , ""); query1 = query.replace(" " , "+")
            if 'play+playlist' in query1: webbrowser.open("https://www.youtube.com/watch?v=Ct5kU0w1Vgk&list=PLTnfJXRz5-KMLKqe93Pa0ddscbzZSWdoM")
            elif 'play+' in query1: query1 = query1.replace("play+" , ""); pywhatkit.playonyt(query1)
            else: webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={query1}") 
    
    class GetTime:
        def __ChangeSet__(hour):
            hour = int(hour)
            if hour == 13:return "1", "PM"
            elif hour == 14:return "2", "PM"
            elif hour == 15:return "3", "PM"
            elif hour == 16:return "4", "PM"
            elif  hour == 17:return "5", "PM"
            elif hour == 18:return "6", "PM"
            elif hour == 19:return "7", "PM"
            elif hour == 20:return "8", "PM"
            elif hour == 21:return "9", "PM"
            elif hour == 22:return "10", "PM"
            elif hour == 23:return "11", "PM"
            elif hour == 24:return "12", "PM"
            else:return str(hour),"AM"

        def GiveTime():
            hour = datetime.datetime.now().strftime("%H"); minute = datetime.datetime.now().strftime("%M"); Day = datetime.datetime.now().strftime("%d"); month = datetime.datetime.now().strftime("%m"); year = datetime.datetime.now().strftime("%y")
            hour = int(hour)
            if hour <= 12: _get = "AM"
            elif hour >= 13: hour,_get = Main.GetTime.__ChangeSet__(hour)
            return f"Time is {hour}:{minute} {_get} of date {Day} : {month} : {year}"

    class Restarter:
        def res():
            try: os.startfile(f"{path}\\Main.exe"); sys.exit()
            except Exception as e: speak(f"Error - [{e}]")

    class Responder:
        def res():
            query = takecommand().lower()
            if query != "none":
                print("User Said : " + query)
                if 'google search' in query: Main.Google(query)
                elif 'wikipedia search' in query: query = query.replace("wikipedia search " , ""); Main.Wiki.Search(query) 
                elif 'what time is it' in query or 'tell me time' in query or 'tell time' in query or 'speak time' in query: speak(Main.GetTime.GiveTime())
                elif 'youtube' in query: Main.Youtube(query)
                elif 'sum of' in query or '+' in query:
                    if 'sum of ' in query: query = query.replace("sum of " , ""); d1,d2 = query.split(" and "); sum = int(d1) + int(d2)
                    elif '+' in query: d1,d2 = query.split(" + "); sum = int(d1) + int(d2)
                    print(sum)
                elif 'subtract' in query or '-' in query:
                    query = query.replace("subtract " , "");query = query.replace("sub " , "")
                    if 'from' in query: d1,d2 = query.split(" from "); sub = int(d2) - int(d1)
                    elif 'minus' in query or '-' in query: d1,d2 = query.split(" - "); sub = int(d1) - int(d2)
                    print(sub)
                elif 'multiply' in query or 'x' in query:
                    if 'multiply' in query: query = query.replace("multiply" , ""); d1,d2 = query.split(" by "); mut = int(d1) * int(d2)
                    elif 'x' in query: d1,d2 = query.split(" x ");mut = int(d1) * int(d2)
                    print(mut)
                elif 'divide' in query or '/' in query or 'divided by' in query:
                    if 'divide' in query: query = query.replace("divide " , ""); d1,d2 = query.split(" by "); div = int(d1) / int(d2)
                    elif '/' in query: d1,d2 = query.split("/"); div = int(d1) / int(d2)
                    elif 'divided by' in query: d1,d2 = query.split("divided by"); div = int(d1) / int(d2)
                    print(div)
                elif 'shutdown system' in query or 'quit' in query: 
                    speak("Have a good day Sir")
                    sys.exit()
                    
                elif 'restart yourself' in query or 'recharge yourself' in query: 
                    Main.Restarter.res()

                else: 
                    Main.SystemCommand.Sys(query)
                    Main.SystemCommand.__System__(query)
                    Main.Chatbot.chat(query)
      
while True:
    try: Main.Responder.res()
    except Exception as e: print(f"Error : [ {e} ]")
