from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import time

value = {"/?choice=rock": ("/?choice=scissors", "/?choice=lizard"),
         "/?choice=paper": ("/?choice=rock", "/?choice=spock"),
         "/?choice=scissors": ("/?choice=paper", "/?choice=lizard"),
         "/?choice=lizard": ("/?choice=paper", "/?choice=spock"),
         "/?choice=spock": ("/?choice=scissors", "/?choice=rock")}

class stats:
    wins = 0
    losses = 0
    ties = 0
    def __init__(self, wins, losses, ties):
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def stattrack(self):
        print("<p>You have %s</p>" % self.wins, "<p> wins,%s</p> " % self.ties, "<p> tied games, and %s</p>" % self.losses, "<p> losses.%s</p>", "utf-8")
    def incrementwins(self):
        self.wins += 1
        #self.stattrack()
    def incrementlosses(self):
        self.losses += 1
        #self.stattrack()
    def incrementties(self):
        self.ties += 1
        #self.stattrack()

s1 = stats(0,0,0)

compin = random.choice(["/?choice=rock", "/?choice=paper", "/?choice=scissors", "/?choice=lizard", "/?choice=spock"])

def rand():
    global compin
    compin = random.choice(["/?choice=rock", "/?choice=paper", "/?choice=scissors", "/?choice=lizard", "/?choice=spock"])

f = open("newAccount.txt", "w")
f.write('''self.wfile.write(bytes("<p>Type a username.</p>", "utf-8"))
        self.wfile.write(bytes("<textarea id=new_user name=new_user_name rows=1 cols=20></textarea>", "utf-8"))
        self.wfile.write(bytes("<button type=submit>Done</button>", "utf-8"))''')
f.close()


hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def newAccount(self):
        self.wfile.write(bytes("<p>Type a username.</p>", "utf-8"))
        self.wfile.write(bytes("<textarea id=new_user name=new_user_name rows=1 cols=20></textarea>", "utf-8"))
        self.wfile.write(bytes("<button type=submit>Done</button>", "utf-8"))
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Rock_Paper_Scissors_Lizard_Spock</title></head>", "utf-8"))
        self.wfile.write(bytes("""<form method=get class=input autocomplete=off><div class=input><lable for=choice>Type your choice:
        </lable><input type=text name=choice id=choice %s></div><div class=input><input type=submit value=Submit>
        </div></form>""" % self.path, "utf-8"))
        #self.wfile.write(bytes("", "utf-8"))
        #self.wfile.write(bytes("<button form=submit name=choice>Done</button>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        if self.path == compin:
            self.wfile.write(bytes("<p>You tied. The computer picked: %s</p>" % compin, "utf-8"))
            rand()
            s1.incrementties()
            self.wfile.write(bytes("<p>Wins: %s</p>" % s1.wins, "utf-8"))
            self.wfile.write(bytes("<p>Ties: %s</p>" % s1.ties, "utf-8"))
            self.wfile.write(bytes("<p>Losses: %s</p>" % s1.losses, "utf-8"))
        elif compin in value[self.path]:
            self.wfile.write(bytes("<p>You win! The computer picked %s</p>" % compin, "utf-8"))
            rand()
            s1.incrementwins()
            self.wfile.write(bytes("<p>Wins: %s</p>" % s1.wins, "utf-8"))
            self.wfile.write(bytes("<p>Ties: %s</p>" % s1.ties, "utf-8"))
            self.wfile.write(bytes("<p>Losses: %s</p>" % s1.losses, "utf-8"))
        else:
            self.wfile.write(bytes("<p>You lose. The computer picked %s</p>" % compin, "utf-8"))
            rand()
            s1.incrementlosses()
            self.wfile.write(bytes("<p>Wins: %s</p>" % s1.wins, "utf-8"))
            self.wfile.write(bytes("<p>Ties: %s</p>" % s1.ties, "utf-8"))
            self.wfile.write(bytes("<p>Losses: %s</p>" % s1.losses, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))



if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % ("127.0.0.1", serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


valid_input = False
a = 0


#s1 = stats(0, 0, 0)
in1 = MyServer
while valid_input == False:
    compin = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
#0=rock 1=paper 2=scissors
    w = ". You win!"
    t = ". You tied."
    L = ". You lose."
    if a == 0:
        in1.path = input("Welcome to rock, paper, scissors, lizard, spock! Please type your choice:").lower()
    elif a == 1:
        in1.path = input("If you would like to play again, please type your choice. If not, type stop.").lower()
    elif a == 2:
        in1.path = input("Try again.").lower()
    else:
        in1.path = input("I have no idea how you got this prompt, but if you want to input your choice I won't stop you.").lower()
    try:
        if in1.path == compin:
            print("The computer picked "+compin+t)
            #s1.incrementties()
            a = 1
        elif in1.path == "stop":
            break
        elif compin in value[in1.path]:
            print("The computer picked "+compin+w)
            #s1.incrementwins()
            a = 1
        else:
            print("The computer picked "+compin+L)
            #s1.incrementlosses()
            a = 1
    except:
        print("Error: the tool you picked does not exist")
        a = 2
