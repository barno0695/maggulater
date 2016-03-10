import sys
import telnetlib
import unicodedata

def remove_non_ascii_1(text):
	return ''.join(i for i in text if ord(i)<128)

def sendEmail(sender, recipients, subject, body):
	HOST = "10.3.100.244"
	PORT = 25

	# reload(sys)
	# sys.setdefaultencoding('utf8')

	tn = telnetlib.Telnet(HOST, PORT)

	# print tn.read_until("Postfix")
	print tn.read_eager()

	tn.write("HELO iitkgp.ernet.in\n")
	print tn.read_until("ac.in")

	text = "MAIL FROM: " + sender + "\n"
	# print text
	text = unicodedata.normalize('NFKD',text).encode('ascii', 'ignore')
	# text = remove_non_ascii_1(text)
	# print text
	tn.write(text)
	print tn.read_until("Ok")

	for recipient in recipients:
		text = "RCPT TO: " + recipient + "\n"
		text = unicodedata.normalize('NFKD',text).encode('ascii', 'ignore')
		tn.write(text)
		print tn.read_until("Ok")

	tn.write("DATA\r\n")
	print tn.read_until("<LF>")

	text = "Subject: " + subject + " \r\n\r\n" + body +"\r\n.\r\n"
	text = unicodedata.normalize('NFKD',text).encode('ascii', 'ignore')
	tn.write(text)
	print tn.read_all()

	telnet.close()
	return
