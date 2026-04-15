# 💻 Project Setup Commands

## 🔧 Raspberry Pi Setup

| Task | Command |
|------|--------|
| Update system | `sudo apt update && sudo apt upgrade` |
| Install VLC | `sudo apt install vlc` |
| Install Python serial | `pip3 install pyserial --break-system-packages` |

---

## 📁 File Operations

| Task | Command |
|------|--------|
| Go to home directory | `cd ~` |
| Create project folder | `mkdir project` |
| Go inside folder | `cd project` |
| List files | `ls` |
| Copy video file | `cp /home/justbuild/Downloads/video.mp4 /home/justbuild/project/` |
| Move video file | `mv /home/justbuild/Downloads/video.mp4 /home/justbuild/project/` |

---

## ▶️ Running Video

| Task | Command |
|------|--------|
| Play video (GUI) | `vlc /home/justbuild/Downloads/video.mp4` |
| Play video (terminal) | `cvlc /home/justbuild/Downloads/video.mp4` |

---

## 🔌 Arduino Detection

| Task | Command |
|------|--------|
| Check Arduino port | `ls /dev/ttyACM*` |

---

## 🧠 Python Execution

| Task | Command |
|------|--------|
| Run Python script | `python3 play.py` |

---

## 📝 File Editing

| Task | Command |
|------|--------|
| Create/Edit Python file | `nano play.py` |

---

## 🔐 SSH (Optional)

| Task | Command |
|------|--------|
| Connect to Raspberry Pi | `ssh USERNAME@192.168.0.108` |

---

## ⚠️ Notes

- Ensure Arduino is connected before running Python script  
- Verify correct file paths before execution  
- Use `cvlc` for headless or terminal-based execution  
