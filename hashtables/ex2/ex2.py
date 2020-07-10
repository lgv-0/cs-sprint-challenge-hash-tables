#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []

    NoneTicket = None
    for ticket in tickets:
        if ticket.source == "NONE":
            NoneTicket = ticket
            break

    def Climb(thisTicket):
        if thisTicket.source != "NONE":
            route.append(thisTicket.source)
        if thisTicket.destination == "NONE":
            route.append(thisTicket.destination)
            return
        
        for ticket in tickets:
            if ticket.source == thisTicket.destination:
                return Climb(ticket)

    Climb(NoneTicket)

    return route