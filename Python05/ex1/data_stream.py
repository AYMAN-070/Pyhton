# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    data_stream.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/09 12:00:50 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/09 14:15:10 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract Base Class representing a data stream within the Nexus."""
    def __init__(self, stream_id: str):
        """Initializes the stream with a unique identifier and counter."""
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Abstract method to process a batch of data. Must be overridden."""
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] =
                    None) -> List[Any]:
        """filters data based on criteria."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Returns diagnostic statistics for the current stream."""
        return {'stream_id': self.stream_id}


class SensorStream(DataStream):
    """Specialized stream for processing environmental sensor data."""
    def process_batch(self, data_batch: List[Any]) -> str:
        """Calculates the average temperature from the data batch."""
        count = 0
        total = 0
        for x in data_batch:
            if isinstance(x, dict) and x.get("id") == "temp":
                count += 1
                total += x["value"]
        if count == 0:
            return "Sensor analysis: NO reading processed"
        average = total / count
        return (f"Sensor analysis: {count} readings processed, avg temp: "
                f"{average}°C")

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] =
                    None) -> List[Any] | None:
        """Overrides filter_data to handle critical temperature alerts."""
        if criteria == "critical":
            filtered_sensor_list = [x["value"] for x in data_batch if
                                    x["id"] == "temp" and x["value"] > 22]
            return filtered_sensor_list
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    """Specialized stream for financial transaction processing."""
    def process_batch(self, data_batch: List[Any]) -> str:
        """Calculates net flow (buys - sells) from the batch."""
        count = 0
        total = 0
        for x in data_batch:
            if isinstance(x, dict):
                count += 1
                if x["type"] == "buy":
                    total += x["value"]
                if x["type"] == "sell":
                    total -= x["value"]
        if count == 0:
            return "Transaction analysis: NO reading processed"
        return (f"Transaction analysis: {count} operations, net flow: "
                f"{total} units")

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] =
                    None) -> List[Any]:
        """Filters for high-value transactions (> 100)."""
        if criteria == "critical":
            filtered_transaction_list = [x["value"] for x in data_batch if
                                         x["value"] > 100]
            return filtered_transaction_list
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    """Specialized stream for system event logging."""
    def process_batch(self, data_batch: List[Any]) -> str:
        """Counts events and detects system errors."""
        count = 0
        error = 0
        for x in data_batch:
            count += 1
            if x == "error":
                error += 1
        if count == 0:
            return "Event analysis: NO reading processed"
        return (f"Event analysis: {count} events, {error} error detected")


class StreamProcessor:
    """Orchestrates different stream types polymorphically."""
    def process_stream(self, stream: DataStream, data: List[Any]) -> str:
        """Processes any DataStream subtype using its polymorphic interface."""
        try:
            result = stream.process_batch(data)
            return (result)
        except Exception:
            return ("Error porcessing stream")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()
    processor = StreamProcessor()
    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")
    sensor_data = [
        {'id': 'temp', 'value': 22.5},
        {'id': 'temp', 'value': 23},
        {'id': 'temp', 'value': 22},
        {'id': 'humidity', 'value': 65},
        {'id': 'pressure', 'value': 1013}
    ]
    transaction_data = [
        {'type': 'buy', 'value': 100},
        {'type': 'sell', 'value': 150},
        {'type': 'buy', 'value': 75}
    ]
    even_data = ["login", "error", "logout"]
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor_stream.stream_id}, Type: Environmental Data")
    print_list_ = [f"{x['id']}:{x['value']}" for x in sensor_data]
    print(f"Processing sensor batch: {print_list_}")
    print(processor.process_stream(sensor_stream, sensor_data))
    print()
    print_list = [f"{x['type']}:{x['value']}" for x in transaction_data]
    print("Initializing Transaction Stream...")
    print(f"Stream ID: {transaction_stream.stream_id}, Type: Financial Data")
    print(f"Processing transaction batch: {print_list}")
    print(processor.process_stream(transaction_stream, transaction_data))
    print()
    print("Initializing Event Stream...")
    print(f"Stream ID: {event_stream.stream_id}, Type: System Events")
    print(f"Processing transaction batch: {even_data}")
    print(processor.process_stream(event_stream, even_data))
    print()
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()
    print("Batch 1 Results:")
    streams = [sensor_stream, transaction_stream, event_stream]
    all_data = [sensor_data, transaction_data, even_data]
    for stream, data in zip(streams, all_data):
        print("- ", processor.process_stream(stream, data))
    print()
    print("Stream filtering active: High-priority data only")
    critical_sensor = sensor_stream.filter_data(sensor_data, "critical")
    critical_transaction = transaction_stream.filter_data(transaction_data,
                                                          "critical")
    count_sensor = 0
    count_transaction = 0
    for x in critical_sensor:
        count_sensor += 1
    for x in critical_transaction:
        count_transaction += 1
    print(f"Filtered results: {count_sensor} critical sensor alerts, "
          f"{count_transaction} large transaction")
