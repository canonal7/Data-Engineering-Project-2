from kafka import KafkaProducer
import json


def kafka_python_producer_sync(producer, msg, topic):
    producer.send(topic, json.dumps(msg).encode("utf-8"))
    print("Sending " + str(msg))
    producer.flush(timeout=60)


def success(metadata):
    print(metadata.topic)


def error(exception):
    print(exception)


def kafka_python_producer_async(producer, msg, topic):
    producer.send(topic, json.dumps(msg).encode("utf-8")).add_callback(
        success
    ).add_errback(error)
    producer.flush()


if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers="35.232.232.195:9092"
    )  # use your VM's external IP Here!
    with open(
        "/Users/canonal/Desktop/Assignment-2/data/mock_dataset.json"
    ) as f:  # change this path to the path in your laptop
        data = json.load(f)

    for item in data:
        kafka_python_producer_sync(producer, item, "flight")

    f.close()
