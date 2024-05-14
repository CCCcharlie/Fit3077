from abc import abstractmethod

class Subscriber():
    """
    Subscriber that listens to events by emitters

    Based on the observer pattern
    """
    @abstractmethod
    def notify(self):
        """
        Noify that this event has occured
        """
        raise NotImplementedError()
