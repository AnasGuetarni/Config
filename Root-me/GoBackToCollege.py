import socket, sys, time, math

server = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
botnick = "fuckingbot"
serverbot = "Candy"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting to:"+server
irc.connect((server, port))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n")
irc.send("NICK "+ botnick +"\n")
irc.send("PRIVMSG nickserv :iNOOPE\r\n")
irc.send("JOIN "+ channel +"\n")

i = 0
while 1:
	text = irc.recv(2040)
	print text

	if text.find('PING') != -1:
		irc.send('PONG ' + text.split() [1] + '\r\n')
	i += 1
	if i == 6:
		break

time.sleep(3)
irc.send('PRIVMSG '+serverbot+' :!ep1\r\n')
text = irc.recv(2040)
print text
if text.find(serverbot) != -1:
	text = text.split(' :')[1].strip().split(' / ')
	ans = math.sqrt(int(text[0]))*float(text[1])
	print '%.2f' % ans
	irc.send('PRIVMSG '+serverbot+' :!ep1 -rep %.2f\r\n' % ans)
text = irc.recv(2040)
print text
