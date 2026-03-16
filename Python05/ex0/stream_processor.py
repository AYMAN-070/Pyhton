# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    stream_processor.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/06 17:40:34 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/07 11:41:41 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):
    """Base abstract class for all Nexus data processors."""
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data and return a statistical summary."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if the data is suitable for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Provide a default implementation for formatting output."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialized for list of numbers."""
    processor_name = "Numeric Processor"

    def process(self, data: Any) -> str:
        """Calculates sum and average of numeric data."""
        count = 0
        total = 0
        for x in data:
            count += 1
            total += x
        if count == 0:
            average = 0
        else:
            average = total / count
        return f"Processed {count} numeric values, sum={total}, avg={average}"

    def validate(self, data: Any) -> bool:
        """Checks if data is a list containing only numbers."""
        try:
            if not isinstance(data, list):
                raise ValueError
            for x in data:
                if isinstance(x, (int, float)) is False:
                    raise ValueError
            print("Validation: Numeric data verified")
            return True
        except ValueError:
            return False


class TextProcessor(DataProcessor):
    """Processor specialized for strings."""
    processor_name = "Text Processor"

    def process(self, data: Any) -> str:
        """Counts characters and words in a string."""
        num_chars = 0
        for x in data:
            num_chars += 1
        num_words = 0
        check = True
        for x in data:
            if check is True:
                if x != " ":
                    num_words += 1
                    check = False
            elif x == " ":
                check = True
        return f"Processed text: {num_chars} characters, {num_words} words"

    def validate(self, data: Any) -> bool:
        """Checks if data is a string."""
        try:
            if not isinstance(data, str):
                raise ValueError
            print("Validation: Text data verified")
            return True
        except ValueError:
            return False


class LogProcessor(DataProcessor):
    """Processor specialized for log-formatted strings (Level: Message)."""
    processor_name = "Log Processor"

    def process(self, data: Any) -> str:
        """Parses log level and message."""
        data_len = 0
        for char in data:
            data_len += 1
        i = 0
        for x in data:
            if x != ":":
                i += 1
            if x == ":":
                break
        if data[0:5] == "ERROR":
            return f"[ALERT] {data[0:i]} level detected:{data[i+1:data_len]}"
        elif data[0:4] == "INFO":
            return f"[INFO] {data[0:i]}:{data[i+1:data_len]}"
        else:
            return f"{data[0:i]} level detected:{data[i+1:data_len]}"

    def validate(self, data: Any) -> bool:
        """Verifies if the string contains a colon for log parsing."""
        if not isinstance(data, str):
            return False
        check = False
        for x in data:
            if x == ":":
                check = True
                break
        try:
            if check is False:
                raise ValueError
            print("Validation: Log entry verified")
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    processors = [NumericProcessor(), LogProcessor(), TextProcessor()]
    test_data = List[Union[List[int], str]]
    test_data = [[1, 2, 3, 4, 5], "Hello Nexus World",
                 "ERROR: Connection timeout",]
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    for data in test_data:
        print("Processing data: ", data)
        for processor in processors:
            if processor.validate(data) is True:
                print(f"Initializing {processor.processor_name}...")
                result = processor.process(data)
                print(processor.format_output(result))
                break
        print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    print()
    data_test = [[1, 2, 3], "Yooooooo Man", "INFO level detected: "
                 "System ready"]
    i = 0
    for data in data_test:
        i += 1
        for processor in processors:
            if processor.validate(data) is True:
                print(f"Result {i}: {processor.process(data)}")
                break
        print()
    print("Foundation systems online. Nexus ready for advanced streams.")
