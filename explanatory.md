# Beginner Explanatory Guide: OPS-401: Build Structured Logging System

> **Task Type**: Product Task  
> **Domain/Focus**: Logging and Observability in Python

---

## 1. The Goal (In-Depth Beginner Explanation)

### The Core Problem
In modern software applications, understanding the flow of operations and diagnosing issues is crucial for maintaining performance and reliability. Currently, the logging system in our application outputs logs in plain text, which makes it difficult to parse and analyze programmatically. This lack of structure means that when developers or system administrators look at the logs, they have to sift through unformatted text, making it hard to identify issues quickly or trace requests through the system.

The task at hand is to build a structured logging system that outputs logs in JSON format. JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. By implementing structured logging, we can include essential metadata such as timestamps, log levels, messages, and correlation IDs. This will not only enhance the readability of logs but also facilitate better monitoring and debugging of the application, ultimately improving the user experience and system reliability.

### Jargon Buster (Key Terms Explained)
* **Structured Logging**: This refers to the practice of logging data in a consistent format, typically as key-value pairs in a structured format like JSON. For example, instead of a log entry that says "User logged in", a structured log might look like this: `{"timestamp": "2023-10-01T12:00:00Z", "level": "INFO", "message": "User logged in", "user_id": 123}`. This structure allows for easier searching and filtering of logs.

* **Correlation ID**: A unique identifier that is used to trace a request across various services or components in a system. For instance, if a user makes a request that goes through multiple services, each log entry related to that request can include the same correlation ID, making it easier to follow the request's path through the system.

* **Log Levels**: These are categories that indicate the severity or importance of log messages. Common log levels include DEBUG (for detailed information), INFO (for general information), WARN (for potential issues), and ERROR (for serious problems). For example, a log entry with level ERROR indicates that something has gone wrong that needs immediate attention.

* **JSON (JavaScript Object Notation)**: A lightweight data format that is easy for humans to read and write and easy for machines to parse and generate. It is often used for transmitting data in web applications. An example of JSON format is: `{"name": "John", "age": 30}`.

### Expected Outcome
After implementing the structured logging system, the application should output logs in JSON format instead of plain text. 

**Before**: 
```
User logged in
```

**After**: 
```json
{
  "timestamp": "2023-10-01T12:00:00Z",
  "level": "INFO",
  "message": "User logged in",
  "correlation_id": "req-123"
}
```

This structured output will allow developers to easily filter, search, and analyze logs, improving the overall observability of the application.

---

## 2. Related Coding Concepts & Syntax (50% Theory, 50% Practice)

### Concept 1: Object-Oriented Programming (OOP)
#### 📘 Theoretical Overview (50%)
* **Why it exists**: Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to represent data and methods to manipulate that data. OOP helps in organizing complex programs into manageable sections, making code reusable and easier to maintain. Without OOP, code can become tangled and difficult to follow, especially in larger applications.

* **Key Mechanisms**: OOP is built around four main principles: encapsulation (bundling data and methods that operate on that data), inheritance (creating new classes based on existing ones), polymorphism (using a single interface to represent different underlying forms), and abstraction (hiding complex implementation details). These principles help in creating a clear structure in code.

#### 💻 Syntax & Practical Examples (50%)
* **Language Syntax**:
  ```python
  class Animal:
      def __init__(self, name):
          self.name = name
      
      def speak(self):
          return "Some sound"
  
  class Dog(Animal):
      def speak(self):
          return "Woof!"
  
  my_dog = Dog("Buddy")
  print(my_dog.speak())  # Output: Woof!
  ```

* **Real-World Application**:
  ```python
  class StructuredLogger:
      def __init__(self, service_name='app', min_level='INFO'):
          self.service_name = service_name
          self.min_level = min_level
          self.logs = []
      
      def info(self, message):
          log_entry = {
              "timestamp": datetime.now().isoformat(),
              "level": "INFO",
              "message": message
          }
          self.logs.append(log_entry)
  ```

---

## 3. Step-by-Step Logic & Walkthrough

1. **Step 1: Locate and Analyze the Target File**
   * Navigate to the `structuredLogger.py` file in the `p-w12-task-03` folder. This file contains the `StructuredLogger` class where we will implement the logging functionality.
   * Focus on the methods: `set_correlation_id`, `_format_entry`, `_should_log`, `debug`, `info`, `warn`, and `error`. These methods will need to be modified or implemented to meet the acceptance criteria.

2. **Step 2: Input Verification & Validation**
   * Ensure that the `message` parameter in the logging methods is not empty or null. This is important to avoid logging meaningless entries.
   * Check if the `level` provided is one of the defined log levels (DEBUG, INFO, WARN, ERROR).

3. **Step 3: Core Implementation / Modification**
   * Implement the `set_correlation_id` method to store a correlation ID that can be used in all log entries.
   * Implement the `_format_entry` method to create a structured log entry in JSON format, including the timestamp, level, message, and correlation ID.
   * Modify the logging methods (`debug`, `info`, `warn`, `error`) to call `_format_entry` and add the formatted log entry to the `logs` list only if the log level meets the minimum level set.

4. **Step 4: Output Verification & Testing**
   * Run the tests in `test_logger.py` using pytest to ensure that all functionalities work as expected. This will verify that logs are being created correctly, that correlation IDs are propagated, and that the minimum log level filtering works.

---

## 4. Detailed Walkthrough of Test Cases

### Test Case 1: Standard / Success Case
* **Description**: This test checks if the `info` method correctly creates a log entry.
* **Inputs**:
  ```json
  {
    "message": "User logged in",
    "user_id": 123
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The `info` method is called with the message "User logged in" and an additional parameter `user_id`.
  2. The method checks if the log level (INFO) is above the minimum level set (default is INFO).
  3. The `_format_entry` method is called to create a structured log entry.
  4. The log entry is appended to the `logs` list.
* **Expected Output**: 
  ```json
  {
    "level": "INFO",
    "message": "User logged in",
    "timestamp": "2023-10-01T12:00:00Z"
  }
  ```

### Test Case 2: Edge Case / Validation Fail
* **Description**: This test checks if the logger correctly ignores messages below the minimum log level.
* **Inputs**:
  ```json
  {
    "message": "This debug message should be ignored"
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The `debug` method is called with a message.
  2. The method checks if the log level (DEBUG) is above the minimum level set (WARN).
  3. Since DEBUG is lower than WARN, the method does not create a log entry.
  4. The execution is halted early, and no log entry is added.
* **Expected Output**: 
  ```json
  []
  ```
This indicates that no logs were created, as expected.