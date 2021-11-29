from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import time

value = {"/rock": ("/scissors", "/lizard"),
         "/paper": ("/rock", "/spock"),
         "/scissors": ("/paper", "/lizard"),
         "/lizard": ("/paper", "/spock"),
         "/spock": ("/scissors", "/rock")}



compin = random.choice(["/rock", "/paper", "/scissors", "/lizard", "/spock"])

def rand():
    global compin
    compin = random.choice(["/rock", "/paper", "/scissors", "/lizard", "/spock"])

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Type your choice: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        if self.path == compin:
            self.wfile.write(bytes("<p>You tied. The computer picked: %s</p>" % compin, "utf-8"))
            rand()
        elif compin in value[self.path]:
            self.wfile.write(bytes("<p>You win! The computer picked %s</p>" % compin, "utf-8"))
            rand()
        else:
            self.wfile.write(bytes("<p>You lose. The computer picked %s</p>" % compin, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        rand()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


class stats:
    wins = 0
    losses = 0
    ties = 0
    def __init__(self, wins, losses, ties):
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def stattrack(self):
        print("You have ", self.wins, " wins, ", self.ties, " tied games, and ", self.losses, " losses.")
    def incrementwins(self):
        self.wins += 1
        self.stattrack()
    def incrementlosses(self):
        self.losses += 1
        self.stattrack()
    def incrementties(self):
        self.ties += 1
        self.stattrack()


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
