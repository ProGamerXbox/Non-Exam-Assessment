> [!IMPORTANT]
> Please note that it is the PROTOTYPE VERSION
> 
> However I will update this branch first for the README.md file

# 🔰 Non-Exam-Assessment :

- [🔰 Non-Exam-Assessment :](#-non-exam-assessment-)
- [1. 💠 Introduction :](#1--introduction-)
- [:gift: Implementation :](#gift-implementation-)
  - [Installation :](#installation-)
  - [How to make it available online :](#how-to-make-it-available-online-)
    - [How to access my router interface ?](#how-to-access-my-router-interface-)
  - [Port forwarding :](#port-forwarding-)
    - [How to port forwad an application](#how-to-port-forwad-an-application)
    - [How to add a firewall rule on Windows](#how-to-add-a-firewall-rule-on-windows)
- [2. :hammer: Creation :](#2-hammer-creation-)
  - [2.1. 🤔 Current problems ? :](#21--current-problems--)
  - [🤔 Why ? :](#-why--)
  - [2.2. Goal of the project :](#22-goal-of-the-project-)
- [3. :book: Analysis :](#3-book-analysis-)
- [4. ⚙️ Design :](#4-️-design-)
  - [4.1. interface :](#41-interface-)
- [⚙️ Plan:](#️-plan)
  - [3.1. interface :](#31-interface-)
- [5. 🚧 Progress :](#5--progress-)
  - [5.1 :moyai: interface :](#51-moyai-interface-)
  - [5.2 :computer: Code :](#52-computer-code-)
- [🚧 Progress :](#-progress-)
- [6. :test\_tube: Testing :](#6-test_tube-testing-)
- [interface :](#interface-)
- [7. :pencil: Evaluation :](#7-pencil-evaluation-)
- [Code](#code)


# 1. 💠 Introduction :

* Creation of a **web-based** **`chatroom`** using **client/server** infrastructure and implementating features such as:
    * sending :
        * vocals (if possible)
        * photos
        * messages
    * types of chats :
        * private
        * group
        * server (if possible)
    * calls (highly doubt it due to its difficulty to implement)
---

# :gift: Implementation :

## Installation :

* Download Python 3.10 or over **[Download here](https://www.python.org/downloads/)**
* Download ZIP
* Extract Archive
* Open cmd or powershell in the directory
* Run **`pip install -r requirements.txt`**

## How to make it available online :

> [!IMPORTANT]
> You will need admin access to your router web interface
### [How to access my router interface ?](https://youtu.be/UdQTr6N02QA?si=oBtPbmkP5mhEh5qt)

> [!NOTE]
> Every router brand has a different interface
## Port forwarding :

The default port for the `chatroom` server is port : `80` (which is the default port for websites)

- create a **firewall rule** to allow port `80`
- the rule must direct traffic to your local IP machine running the python script

### [How to port forwad an application](https://youtu.be/jfSLxs40sIw?si=18PmzbKOrmbS6r73&t=180)

> [!IMPORTANT]
> If you are on **Windows**, you NEED to add a **firewall rule** within the settings
### [How to add a firewall rule on Windows](https://youtu.be/GBUVyu69Qsk?si=vbLywG4Juixe4gGd&t=11)

---

# 2. :hammer: Creation :

> ### What problem does it solve ?
> What is the point of creating this type of application ?
## 2.1. 🤔 Current problems ? :
## 🤔 Why ? :

- **Privacy :**
    - nowdays most of big companies chat applications **steal personal data/informations**
    - most of the private conversations are not really 'private', they are kept and logged by big companies 

- **Security :**
    - some chat applications may use **weak encryption method**, which would result in data being able to be **intercepted**

## 2.2. Goal of the project :

- **Privacy :**
  - ensure a non-log policy

- **Security :**
  - ensure strong encryption method, preventing data from being intercepted

- **Accessibility :**
  - **open-source** script for anyone who wishes to host their own **`chatroom`** server and having full access to it
  - will be **customizable**


---

# 3. :book: Analysis :

- ask end user what thet think of the project

# 4. ⚙️ Design :

## 4.1. interface :
# ⚙️ Plan:

## 3.1. interface :
* Interface :
    - web browser


---

# 5. 🚧 Progress :

## 5.1 :moyai: interface :

<details>
<summary>Web Interface</summary>

- [ ] Web
    - [ ] message bubble
    - [ ] username display
    - [ ] font used
    - [ ] color design (black/grey)

</details>

## 5.2 :computer: Code :

<details>
<summary>Core Features</summary>

- [ ] Establish a connection
    - [ ] send/receive message
    - [ ] general chat
    - [ ] database

</details>

# 🚧 Progress :

# 6. :test_tube: Testing :
# interface :

# 7. :pencil: Evaluation :
# Code