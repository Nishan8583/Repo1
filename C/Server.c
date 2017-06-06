/*NOTE: THE CODE ONLY RUNS ON LINUX MACHINE, BOTH THE GCC AND G++ COMPILER CAN BE USED, 
CONNECT TO THIS SERVER WITH TARGET IP AND PORT=30001*/
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>

int main()
{
	int socket_fd = socket(PF_INET,SOCK_STREAM,0);  // PF_INET is protocol family, SOCK_STREAM signals a TCP socket,0 is protocol number, usually 0

	// Checking if an error was recived
	if (socket_fd == -1)
	{
		printf("An error has occured while creating a socket\n");
		return 1;
	}
	printf("Socket Creation successful\n");  //If everything goes according to plan

	// Making the port and IP address combo reusable
	int reuse = 1;
	if (setsockopt(socket_fd, SOL_SOCKET, SO_REUSEADDR, (char *)&reuse, sizeof(int)) == -1)
	{
		printf("Can't set the reuse option on the socket");
		return 1;
	}

	//Creating structure to hold socket info
	struct sockaddr_in name;
	name.sin_family = PF_INET;
	name.sin_port = (in_port_t)htons(30001);  // POrt no used 30000
	name.sin_addr.s_addr = htonl(INADDR_ANY);  // Our own IP

	//Binding the sokcet to the port and IP address
	int c = bind(socket_fd,(struct sockaddr *)&name, sizeof(name));

	//If an error was recieved during binding
	if(c == -1)
	{
		printf("An error occured while binding the addresses to the socket\n");
		return 1;
	}
	printf("Binding to socket successful\n");

	//COntinously loop
	while(1)
	{
		//Listeing for connection
		if (listen(socket_fd,10) == -1) // -1 is returned if an error occured
		{
			printf("Error while listening\n");
			return 1;
		}

		//Need a structure for storing client info
		struct sockaddr_storage client_addr;
		unsigned int address_size = sizeof(client_addr);

		//Accepting connection
		int connection = accept(socket_fd, (struct sockaddr *)&client_addr, &address_size);

		if (connection == -1)//If an error was recieved during accepting an connection
		{
			printf("Error accepting connection\n");
			return 1;
		}

		printf("A connection was recieved\n");

		char msg[] = "Hello Friend\n";
		send(connection,msg,strlen(msg),0); // Sending the message

		char s[50];
		int fill = 0;
		size_t n = 50;
		memset(s,fill,n); // Empyting the array of characters whith null
		while(1)
		{
			int c = recv(connection,s,50,0); // Recieving message from the esatblished connection
			if(c == -1)// If error while recieving message
			{
				printf("Error recieveing msg\n");
				break;
			}
			if(c <= 0) // If an empty string was recieved
			{
				break;
			}
			printf("The message recieved is : %s\n",s);
			memset(s,fill,n); // Again emptying the array of string
		}
		printf("The previous connection was closed so making new connection\n");

	}
}
//Reference: Let Us C
