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
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    processor_name = "Numeric Processor"

    def process(self, data: Any) -> str:
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
        try:
            if isinstance(data, list) is False:
                raise ValueError
            for x in data:
                if isinstance(x, (int, float)) is False:
                    raise ValueError
            print("Validation: Numeric data verified")
            return True
        except ValueError:
            return False


class TextProcessor(DataProcessor):
    processor_name = "Text Processor"

    def process(self, data: Any) -> str:
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
        try:
            if isinstance(data, str) is False:
                raise ValueError
            print("Validation: Text data verified")
            return True
        except ValueError:
            return False


class LogProcessor(DataProcessor):
    processor_name = "Log Processor"

    def process(self, data: Any) -> str:
        len = 0
        for char in data:
            len += 1
        i = 0
        for x in data:
            if x != ":":
                i += 1
            if x == ":":
                break
        if data[0:5] == "ERROR":
            return f"[ALERT] {data[0:i]} level detected:{data[i+1:len]}"
        elif data[0:4] == "INFO":
            return f"[INFO] {data[0:i]}:{data[i+1:len]}"
        else:
            return f"{data[0:i]} level detected:{data[i+1:len]}"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) is False:
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
