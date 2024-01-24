
## TCP/IP
TCP (Transfer Control Protocol) is a protocol used when sending data across a network. It is the most commonly used protocol, as it prioritises data integrity over speed and latency, making it most suitable for webpages, and other largely static content. For this reason, it is not used in *live* applications such as livestreaming, VoIP and online videogames. It would be better to use [UDP](#udpip) in this situation.

To start a TCP connection, a 'handshake' must first take place between the recipient and the sender. This allows for the agreement of formats and protocols to be used before the transmission of the data.

## Sending Some Data (TCP/IP)
To send a packet using the TCP/IP stack (after initial handshake and connection is opened), the following steps are used:

##### 1. Application Layer  
Format the HTTP request to the destination server. As data is being sent, the POST/UPDATE request will also contain a copy of the data to be sent. 
##### 2. Transport Layer  
Split the payload into packets, giving each a number, as well as any checksums on the payload. The required protocols to interpret the data are added here as well as an expiration date (Time-To-Live Protocols)
##### 3. Network Layer  
Add metadata to the packets, including source and destination IPs. Also, the physical route for the packet to take is determined
##### 4. Link Layer  
Enables the transfer of packets between the sender and recipient. This often comes in the form of a network driver for a specific NIC.

## Receiving Some Data (TCP/IP)
When receiving data using the TCP/IP stack, the stack is traversed in reverse order.

##### 1. Link Layer
Interprets the electronic signal into a readable file or buffer
##### 2. Network Layer
Strip metadata from the packets, as well as check for checksum integrity. 
##### 3. Transport Layer
Re-order the packets and re-assemble the received data
##### 4. Application Layer
Interpret the received data and use it.

## Requesting Data (TCP/IP)
To request data, such as a webpage from a webserver, there are several steps to getting that page. Below is an overview of the steps:
1. Send request to DNS server for IP of webserver from URL
2. Receive IP of webserver from DNS server
3. Send request to webserver IP for webpage
4. Receive webpage from webserver

## Packet Switching and Lost Data
When a packet has been sent, it must be routed through the physical internet to get to it's destination. To do this, it is sent through various devices called *routers* which can send the packet on to the next router or to its final destination.

If, during the process of getting from its source to its destination, the packet is lost in some way, or otherwise corrupted, the packet is resent. It will always be resent unless the sender receives an ACK from the recipient. **NOTE:** This only applies to [TCP](#tcpip) connections, and will not happen with [UDP](#udpip) connections, where lost packets are left lost.

## UDP/IP
UDP (User Datagram Protocol) is another protocol, much like TCP, except that it is built to prioritise latency and speed over data integrity. It functions in a fundamentally similar way, but has some major differences:
- Lack of support for packet ordering
- Lack of support for packet retransmission (Recovery of lost packets)
- Minimal error checking / correction
- Much, much faster than TCP
- One-To-Many Connections are possible (Many Clients / One Server)
- No connection / 'handshake' required to start sending / recieving data. It is up to the recipient to make sense of the data in the packets sent. 

