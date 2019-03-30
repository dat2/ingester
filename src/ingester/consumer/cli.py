import logging
import os

from kafka import KafkaConsumer

import ingester.logging
from ingester.messages import Message, ExampleMessage

logger = logging.getLogger(__name__)


def main():
    consumer = KafkaConsumer(
        os.environ["KAFKA_TOPIC"],
        bootstrap_servers=os.environ["KAFKA_BOOTSTRAP_SERVERS"],
    )
    for record in consumer:
        logger.info(f"{Message.deserialize(ExampleMessage, record.value)}")
