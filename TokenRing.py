import random

class Token:
    def __init__(self, IPSource, IPDestination, message, ArrivedAtDestination):
        self.IPSource = IPSource
        self.IPDestination = IPDestination
        self.message = message
        self.ArrivedAtDestination = ArrivedAtDestination
        
    def setToken(self, IPSource, IPDestination, message, ArrivedAtDestination):
        self.IPSource = IPSource
        self.IPDestination = IPDestination
        self.message = message
        self.ArrivedAtDestination = ArrivedAtDestination
        
class Computer:
    def __init__(self, buffer, IPAddress):
        self.buffer = buffer
        self.IPAddress = IPAddress
        
    def getBuffer(self):
        return self.buffer
        
    def getIPAddress(self):
        return self.IPAddress
        
    def generateIPAddress(self):
        for i in range(4):
            self.IPAddress += str(random.randint(0, 255))
            if i < 3:
                self.IPAddress += "."
                
    def setMessage(self, token):
        self.buffer = token.message

def generateComputerIPAddresses():
    computers = []
    
    for i in range(10):
        computer = Computer("", "");
        computer.generateIPAddress()
        computers.append(computer)
        
    return computers

def generateSourceDestination(computers):
    indices = random.sample(range(10), 2)
    sourceIndex = indices[0]
    destinationIndex = indices[1]
        
    return sourceIndex, computers[sourceIndex].getIPAddress(), destinationIndex, computers[destinationIndex].getIPAddress()

def printComputersInformations(computers):
    for i in range(10):
        if not computers[i].getBuffer():
            print(f"Computer {i} -> null")
        else:
            print(f"Computer {i} -> {computers[i].getBuffer()}")

def tokenRing(computers):
    sourceIndex, computerSource, destinationIndex, computerDestination = generateSourceDestination(computers)
    token = Token(computerSource, computerDestination, "Visited", False)

    for i in range(0, 9):
        print(f"Starting from computer {computerSource}")
        print(f"Destination computer is {computerDestination}")
        print()
        print(f"Computer {computerSource}: Passing token to {computers[(sourceIndex + 1) % 10].getIPAddress()}")
        
        index = sourceIndex
        
        while not token.ArrivedAtDestination:
            index += 1
                
            if index % 10 == destinationIndex:
                computers[index % 10].setMessage(token)
                token.ArrivedAtDestination = True
                print(f"Computer {computers[index % 10].getIPAddress()}: is the destination")
                print("Token arrived at destination:", computers[index % 10].getIPAddress())
                break
            else:
                print(f"Computer {computers[index % 10].getIPAddress()}: is not the destination")
                print(f"Computer {computers[index % 10].getIPAddress()}: Passing token to {computers[(index + 1) % 10].getIPAddress()}")

        index = destinationIndex
        
        while index % 10 != sourceIndex:
            print(f"Computer {computers[index % 10].getIPAddress()}: Passing token to {computers[(index + 1) % 10].getIPAddress()}")
            index += 1
            
        copySourceIndex = sourceIndex
        sourceIndex, computerSource, destinationIndex, computerDestination = generateSourceDestination(computers)
        token.setToken(computerSource, computerDestination, "Visited", False)
        
        while copySourceIndex % 10 != sourceIndex:
            
            print(f"Computer {computers[copySourceIndex % 10].getIPAddress()}: Passing token to {computers[(copySourceIndex + 1) % 10].getIPAddress()}")
            copySourceIndex += 1

        print()
        printComputersInformations(computers)
        print()
         
def main():
    computers = generateComputerIPAddresses()

    print("Computers Generated IP Addresses:")
    print()

    for i in range(10):
        print(f"Computer {i}:", computers[i].IPAddress)
    print()
    
    print("Computers Information:")
    print()
    printComputersInformations(computers)
    print()
    
    tokenRing(computers)

main()