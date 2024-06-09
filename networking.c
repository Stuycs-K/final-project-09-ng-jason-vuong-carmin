#include "networking.h"

/*Connect to the server
 *return the to_server socket descriptor
 *blocks until connection is made.*/
int client_tcp_handshake(char * server_address) {

  //getaddrinfo
  struct addrinfo * hints, * results; 
  hints = calloc(1, sizeof (struct addrinfo));
  hints->ai_family = AF_INET; 
  hints->ai_socktype = SOCK_STREAM; 

  int error = getaddrinfo(server_address, PORT, hints, &results);
  err(error, "getaddrinfo failed"); 

  //create the socket
  int serverd = socket(AF_INET, SOCK_STREAM, 0);
  err(serverd, "could not connect to server socket"); 

  //connect to the server
  error = connect (serverd, results->ai_addr, results->ai_addrlen);
  err(error, "could not connect to the server"); 

  //free info 
  free(hints);
  freeaddrinfo(results);

  return serverd;
}

/*Accept a connection from a client
 *return the to_client socket descriptor
 *blocks until connection is made.
 */
int server_tcp_handshake(int listen_socket){
    int client_socket;

    //accept the client connection
    socklen_t sock_size;
    struct sockaddr_storage client_address;
    sock_size = sizeof(client_address);
    client_socket = accept(listen_socket,(struct sockaddr *)&client_address, &sock_size);
    err(client_socket, "could not accept client socket");
    return client_socket;
}

/*Create and bind a socket.
* Place the socket in a listening state.
*/
int server_setup() {

  //setup structs for getaddrinfo
  struct addrinfo * hints, * results;
  hints = calloc(1,sizeof(struct addrinfo));
  hints->ai_family = AF_INET;
  hints->ai_socktype = SOCK_STREAM; //TCP socket
  hints->ai_flags = AI_PASSIVE; //only needed on server

  int error = getaddrinfo(NULL, PORT, hints, &results);  //Server sets node to NULL
  err(error, "could not getaddrinfo"); 

  //create the socket
  int clientd = socket(results->ai_family, results->ai_socktype, results->ai_protocol);
  //this code should get around the address in use error
  int yes = 1;
  int sockOpt =  setsockopt(clientd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(yes));
  err(sockOpt,"sockopt error");

  //client d would be the return value of the client socket descriptor
  //bind the socket to address and port
  error = bind(clientd, results->ai_addr, results->ai_addrlen);

  err (error, "failed to bind"); 

  //set socket to listen state
  error = listen(clientd, 10); 
  err (error, "failed to listen"); 

  //free the structs used by getaddrinfo
  free(hints);
  freeaddrinfo(results);
  
  return clientd;
}

void err(int i, char* message){
  if(i < 0){
	  printf("Error: %s - %s\n", message, strerror(errno));
  	exit(1);
  }
}