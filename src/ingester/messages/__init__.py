import attr
import json


class Message:
    def serialize(self):
        return json.dumps(attr.asdict(self)).encode()

    @staticmethod
    def deserialize(msg_class, value):
        return msg_class(**json.loads(value.decode("utf8")))


@attr.s
class ExampleMessage(Message):
    id = attr.ib(str)
    text = attr.ib(str)
