import logging
import os
import time
import uuid

from kafka import KafkaProducer

import ingester.logging
from ingester.messages import Message, ExampleMessage

logger = logging.getLogger(__name__)


def main():
    logger.info("starting up")
    producer = KafkaProducer(
        bootstrap_servers=os.environ["KAFKA_BOOTSTRAP_SERVERS"],
        value_serializer=Message.serialize,
    )
    while True:
        logger.info("sending a message")
        producer.send(
            os.environ["KAFKA_TOPIC"], ExampleMessage(id=str(uuid.uuid4()), text="blah")
        )
        time.sleep(1)
