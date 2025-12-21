## 1. Purpose of Logging

Logging is the practice of keeping a structured, permanent record of events that occur within an application. 

Unlike `print()`, which sends text to the console (standard output) and disappears, Logging sends data to files, databases, or monitoring tools (like Datadog or Splunk).

---

## 2. Why Logging is Relevant in OOP

In professional architecture, print() is considered a "code smell" (bad practice) for several reasons:

- **Persistence** : When a server crashes at 3 AM, you cannot see the console output. Logs are saved to files so you can investigate the "Crime Scene" later.

- **Granularity (Levels)** : `print()` treats everything as equal. Logging allows you to categorize messages by severity (e.g., "Just info" vs. "CRITICAL FAILURE").

- **Context** : A robust logging system automatically records when it happened (Timestamp), where it happened (Module/Line Number), and who did it (Thread/User ID).

---

## 3. How it Works Conceptually

The Python logging module operates on Levels. You configure your application to "listen" only to specific levels.

- **DEBUG:** Detailed information, typically of interest only when diagnosing problems.

- **INFO:** Confirmation that things are working as expected.

- **WARNING:** An indication that something unexpected happened, but the software is still working (e.g., "Disk space low").

- **ERROR:** Due to a more serious problem, the software has not been able to perform some function.

- **CRITICAL:** A serious error, indicating that the program itself may be unable to continue running.

---

## 4. When to Use Logging

- **Development:** Use DEBUG to trace variable values instead of print.

- **Auditing:** Use INFO to record user actions (e.g., "User X deleted File Y") for security.

- **Monitoring:** Use ERROR inside except blocks so that system administrators get alerted when things break.

---

## 5. Key Takeaway

- Logging is about Observability.

- It gives you "X-Ray Vision" into your running application without needing to stop it or modify the code.

- **Rule of Thumb:** If you are asking "What is the value of X?", use a Debugger. If you are asking "What happened yesterday?", use Logs.

---