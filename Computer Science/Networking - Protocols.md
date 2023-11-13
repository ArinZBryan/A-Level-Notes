## The internet vs WWW
Originally, the internet was first established in 1969 under the name of '*arcanet*' by the US military. The public world wide web was established by Sir Tim Burnes Leigh in 1991.

- The term *internet* refers to the physical hardware that makes up the network.
- The term *World Wide Web* refers to the software that drives the network.

## Protocols
A protocol is a set of instructions / rules that are used for the transmission of data between two systems / machines. 

For network protocols, they are used in the transmission of packets between machines. The protocols that are currently used were made standard in 1981 by the OSI.

The protocols used by the internet are called the 'TCP/IP stack'. It is made up from the following [layers](Networking%20-%20How%20Data%20Moves):
1. [Application](Networking%20-%20How%20Data%20Moves#application-layer)  
    (HTTP, HTTPS, FTP, SMTP, etc.)
2. [Transport](Networking%20-%20How%20Data%20Moves#transport-layer)  
    (TCP/UDP)
3. [Network](Networking%20-%20How%20Data%20Moves#network-layer)  
    (IP)
4. [Link](Networking%20-%20How%20Data%20Moves#link-layer)  
    (Ethernet)

## Uses for protocols

| Protocol | Stands For                         | What It Does                                                 | Layer       |
|:-------- |:---------------------------------- |:------------------------------------------------------------ |:----------- |
| IP       | Internet Protocol                  | Routing packets on the internet                              | Network     |
| TCP      | Transmission Control Protocol      | Handling lost packets sent over the internet                 | Transport   |
| UDP      | User Datagram Protocol             | Packet transmission in time critical applications            | Transport   |
| DNS      | Domain Name Service                | Translates domain names into IP addresses                    | Application |
| SSH      | Secure SHell                       | Encrypted terminal access on a remote computer               | Application |
| FTP      | File Transfer Protocol             | Remote file transfers                                        | Application |
| SMTP     | Simple Mail Transfer Protocol      | Email                                                        | Application |
| IMAP     | Internet Message Access Protocol   | Email                                                        | Application |
| POP3     | Post Office Protocol v3            | Email                                                        | Application |
| HTTP     | HyperText Transfer Protocol        | Website requests / Foreign web API calls                     | Application |
| HTTPS    | HyperText Transfer Protocol Secure | Encrypted website requests / Encrypted foreign web API calls | Application |
| Telnet   | Telephone Network                  | Physical Telephone Routing                                   | Link        |
| VOIP     | Voice Over Internet Protocol       | Video conferencing applications                              | Application |

## UDP vs TCP
UDP is used when real-time, fully duplex (two way) communication is required, and the the speed of the data being sent is critical. Thus, packets are not re-ordered, and are thus processed and in the order they are received.  
TCP on the other hand, TCP ensures that packets are processed in the correct order, and thus that data is always received as it was sent.

See [Networking Processes](Networking%20-%20How%20Data%20Moves#UDP/IP) for a more detailed explanation of UDP.