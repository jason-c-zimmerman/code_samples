from simple_chat import *

def main():
		server = ChatServer(PORT, NAME)
		session1 = ChatSession(server, '5005')

if __name__=='__main__':
	main()