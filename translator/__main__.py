from os import environ
from pathlib import Path
from json import load
from .translation_manager import TranslationManager
from .translators import MessageTranslator
from .messages import CloudEvent

if __name__ == "__main__":
    SOURCE_FORMAT = environ.get('SOURCE_FORMAT', 'json')
    TARGET_FORMAT = environ.get('TARGET_FORMAT', 'xml')

    SOURCE_TOPIC = environ.get('SOURCE_TOPIC', 'test')
    TARGET_TOPIC = environ.get('TARGET_TOPIC', 'neu')
    KAFKA_BROKER = environ.get('KAFKA_BROKER', 'localhost:9092')

    print(f'Starting translation from "{SOURCE_FORMAT}" to "{TARGET_FORMAT}".')
    print(f'Subscribing to kafka broker "{KAFKA_BROKER}" topic "{SOURCE_TOPIC}".')
    print(f'Publishing translated messages on topic "{TARGET_TOPIC}"')

    translator = MessageTranslator.get_translator(SOURCE_FORMAT, TARGET_FORMAT)
    manager = TranslationManager([KAFKA_BROKER], SOURCE_TOPIC, TARGET_TOPIC, translator)
    try:
        manager.start_consuming()
    except KeyboardInterrupt:
        print('exiting program')
