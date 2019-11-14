# python-sockets
Simulation of communication between multiple nodes on a network using sockets in Python.

# Interworking Procols Assignment

Consider there are four nodes A, B, C and D and the physical connections are between A-B, C-B, and B-D. Implement this scenario by using process/thread for representing each node and physical connections through sockets. (i.e., there is a channel between A and B, C and B, and B and D).

Now, if a user at A wants to send a line of text to B, it sends it through the socket dedicated for B and B prints the line of text on the terminal. If the user at A wants to send a line of text to C, the process at A shall have to send it to B and B shall have to forward it to C, and C will print it on the terminal.

So each node shall have a user interface through which a user shall specify the name of the destination along with the line of text to be sent. Each node shall have a "routing table" from which it will decide depending on the destination, whether to print the line of text on the terminal, or forward it to another node.

Also allow a special input word by the user, eg. EXIT, to terminate each node. [You may write programs for one node and run them in parallel to represent the four nodes.]

Modify the program so that instead of typing a line of text to be sent to a specified node, the user will type the name of a local file that is to be sent to the specified node where it will be copied. If the file is large, it may have to be sent as multiple packets. [Include Network layer functions]
