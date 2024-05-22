#include "networking.h"

void clientLogic(int server_socket){
  while (1) {
    char * buff = malloc(sizeof(char) * BUFFER_SIZE); 
    printf("enter a string: ");
    fgets(buff, BUFFER_SIZE, stdin); 
    buff = strsep(&buff, "\n"); // pre-process the string

    int error = write(server_socket, buff, BUFFER_SIZE); 
    err(error, "could not write");
  
    error = read(server_socket, buff, BUFFER_SIZE);
    if (error < BUFFER_SIZE) {
      printf("lost connection with server\n"); 
      exit(1);  
    } 
    err(error, "could not read");
    printf("rot13'd string [%s]\n", buff); 
    free(buff);

  }
}

int main(int argc, char *argv[] ) {
  char* IP = "127.0.0.1";
  if(argc>1){
    IP = argv[1]; //connect with a different IP address
    // no route to host 
    // connection refused 
    //LOOK AT THE TEMPLATE REPO
    //149.89.161.100...35
  }
  int server_socket = client_tcp_handshake(IP);
  printf("client connected.\n");
  clientLogic(server_socket); 
}