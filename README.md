# 📲 WhatsApp Message Scheduler using Python and Twilio

This Python project allows you to schedule WhatsApp messages to be sent at a specific time using the Twilio API.

---

## 🚀 Features

- Send WhatsApp messages to any verified number.
- Schedule messages for a future date and time.
- Simple command-line interface.
- Error handling for incorrect date/time input.

---

## 🔧 Requirements

- Python 3.x
- Twilio Account (with WhatsApp sandbox enabled)
- `twilio` Python library

---

## 🧠 How It Works

1. User inputs:
   - Recipient name and number
   - Message content
   - Date and time to send the message
2. The program calculates the delay.
3. It waits until the scheduled time and sends the message using Twilio's WhatsApp API.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/whatsapp-twilio-scheduler.git
cd whatsapp-twilio-scheduler
