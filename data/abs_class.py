from abc import ABC, abstractmethod


class Api(ABC):

    @abstractmethod
    def get_api(self):
        pass
