from abc import ABCMeta, abstractmethod


# Subject
class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latest_news = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.__latest_news = news

    def get_news(self):
        return 'Got News:', self.__latest_news


# Observer
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


# ConcreteObserver
class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscribers(news_publisher)
    print('Subscribers:', news_publisher.subscribers())

    news_publisher.add_news('Jo Kook')
    news_publisher.notify_subscribers()

    print('Detached:', type(news_publisher.detach()).__name__)
    print('Subscribers:', news_publisher.subscribers())

    news_publisher.add_news('Sun sil')
    news_publisher.notify_subscribers()
