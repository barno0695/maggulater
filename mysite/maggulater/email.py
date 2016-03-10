import sys
import telnetlib

HOST = "10.3.100.244"
PORT = 25

tn = telnetlib.Telnet(HOST, PORT)

# print tn.read_until("Postfix")
print tn.read_eager()
tn.write("HELO iitkgp.ernet.in\n")
print tn.read_until("ac.in")
tn.write("MAIL FROM: ppc@cse.iitkgp.ernet.in\n")
print tn.read_until("Ok")
tn.write("RCPT TO: any_user@gmail.com\n")
print tn.read_until("Ok")
tn.write("DATA\n")
print tn.read_until("<LF>")
tn.write("Subject: This is a python test \r\nIf this works we are almost done\r\n.\r\n")
print tn.read_all()
telnet.close()
