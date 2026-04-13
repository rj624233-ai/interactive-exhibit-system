
# 🧩 Interactive Museum Exhibit System

A sensor-based interactive exhibit system built using **Raspberry Pi** and **Arduino**, designed to create real-time, user-driven experiences for museum installations.

---

## 🚀 Overview

This project enables visitors to interact with exhibits using **IR sensors**, triggering **video playback** on a display. The system uses a combination of **Arduino (for sensing)** and **Raspberry Pi (for processing & media control)**.

The interaction is designed to be **intentional and stable**, requiring continuous detection before triggering actions.

---

## 🎯 Key Features

- 🔹 Dual IR sensor-based interaction  
- 🔹 5-second continuous detection logic (prevents accidental triggers)  
- 🔹 Toggle-based video control (Play / Stop)  
- 🔹 Serial communication between Arduino and Raspberry Pi  
- 🔹 Fullscreen video playback using VLC  
- 🔹 Designed for real-world continuous operation 

---

    +------------------+
    |   IR Sensors     |
    | (2 Sensors)      |
    +--------+---------+
             |
             v
    +------------------+
    |    Arduino UNO   |
    |  (Signal Logic)  |
    +--------+---------+
             |
    Serial Communication (USB)
             |
             v
    +------------------+
    |  Raspberry Pi    |
    | (Python Script)  |
    +--------+---------+
             |
             v
    +------------------+
    |   Display + VLC  |
    |  Video Playback  |
    +------------------+


## 🧠 System Architecture


---

## ⚙️ Tech Stack

| Component        | Technology Used |
|----------------|----------------|
| Microcontroller | Arduino UNO |
| Processor       | Raspberry Pi |
| Programming     | Python, Embedded C |
| Communication   | Serial (USB) |
| Media Playback  | VLC (cvlc) |
| Sensors         | IR Sensors |


---

## 📌 Status

🟡 Ongoing Freelance Project  
Currently under development and testing phase.

---

## ⭐ Contribution

This is a freelance project. Suggestions and improvements are welcome.

