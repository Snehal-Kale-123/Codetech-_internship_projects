#!/usr/bin/env python3
"""
CUSTOMER SUPPORT CHATBOT v2.0 - Internship Ready
- Professional responses for company queries
- Logs all conversations to file
- Handles greetings, products, pricing, support
- Time responses & exit handling
- Clean professional interface
"""

import datetime           # For timestamps
import json              # For conversation logs
import os                # For file operations

def get_timestamp():
    """Get current time for logs"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def chatbot_response(user_input):
    """Main response logic - rule-based AI"""
    user_input = user_input.lower().strip()
    
    # Greetings
    if any(word in user_input for word in ['hello', 'hi', 'hey', 'good morning', 'good evening']):
        return "Hello! Welcome to Codec Technologies Customer Support 😊\nHow can I assist you today?"
    
    # Name/Introduction
    elif any(word in user_input for word in ['name', 'who are you', 'your name']):
        return "I'm CodecBot, your 24/7 customer support assistant at Codec Technologies!\nWhat can I help you with?"
    
    # Company Info
    elif any(word in user_input for word in ['company', 'about', 'codec', 'what you do']):
        return """Codec Technologies India Pvt Ltd
📍 211B, Saki Vihar Road, West Chandivali IT Park
💼 Software Development | IT Services | AI Solutions
🌐 www.codec.in | 📧 support@codec.in"""

    # Products/Services
    elif any(word in user_input for word in ['product', 'service', 'what you offer', 'solutions']):
        return """Our Services:
🔹 Custom Software Development
🔹 AI/ML Solutions  
🔹 Web & Mobile Apps
🔹 Cloud Services (AWS/Azure)
🔹 Data Analytics & Automation"""

    # Pricing
    elif any(word in user_input for word in ['price', 'cost', 'pricing', 'how much', 'rate']):
        return """Our Pricing Plans:
💎 Starter: ₹25,000/month (1 developer)
💰 Professional: ₹50,000/month (3 developers)  
🏆 Enterprise: Custom Quote

Contact sales@codec.in for detailed proposal!"""

    # Time/Date
    elif any(word in user_input for word in ['time', 'date', 'today']):
        now = datetime.datetime.now()
        return f"Current Time: {now.strftime('%H:%M:%S')}\nDate: {now.strftime('%Y-%m-%d %A')}"

    # Support/Help
    elif any(word in user_input for word in ['help', 'support', 'issue', 'problem', 'error']):
        return """How I can help:
📞 Technical Support
💰 Billing & Pricing  
🔧 Product Issues
📋 Account Management
❓ General Queries

Type your issue or ask anything!"""

    # Contact
    elif any(word in user_input for word in ['contact', 'phone', 'email', 'call', 'reach']):
        return """Contact Us:
📧 Email: support@codec.in
📞 Phone: +91 22-12345678
💬 WhatsApp: +91 9876543210
🌐 Website: www.codec.in/contact
⏰ Response: Within 2 hours (9AM-7PM IST)"""

    # Hours
    elif any(word in user_input for word in ['hours', 'timing', 'office time', 'working hours']):
        return "Office Hours: Monday-Friday 9:00 AM - 7:00 PM IST\n24/7 Emergency Support Available!"

    # Exit
    elif any(word in user_input for word in ['bye', 'exit', 'quit', 'goodbye', 'thank you']):
        return "Thank you for contacting Codec Technologies! Have a great day! 👋"
    
    # Default
    else:
        return """I understand you're asking about something specific.
Please try:
- "What are your services?"
- "What is pricing?"
- "Contact details"
- "Office hours"
- Or describe your issue! 😊"""

def log_conversation(user_msg, bot_response):
    """Save chat to JSON log file"""
    log_entry = {
        "timestamp": get_timestamp(),
        "user_message": user_msg,
        "bot_response": bot_response
    }
    
    log_file = "chat_logs.json"
    logs = []
    
    # Load existing logs
    if os.path.exists(log_file):
        try:
            with open(log_file, 'r') as f:
                logs = json.load(f)
        except:
            logs = []
    
    # Add new entry
    logs.append(log_entry)
    
    # Save back
    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=2)

def show_welcome():
    """Professional welcome screen"""
    print("="*60)
    print("🤖 CODEC TECHNOLOGIES CUSTOMER SUPPORT CHATBOT")
    print("📍 211B, Saki Vihar Road, West Chandivali IT Park")
    print("="*60)
    print("Type 'help' for options | 'bye' to exit")
    print("-"*60)

def main():
    """Main chatbot loop"""
    show_welcome()
    
    print("🤖 CodecBot: Hello! Type your message below:")
    
    while True:
        # Get user input
        user_input = input("\n👤 You: ").strip()
        
        if not user_input:
            print("🤖 CodecBot: Please type something! 😊")
            continue
        
        # Get bot response
        response = chatbot_response(user_input)
        print(f"🤖 CodecBot: {response}")
        
        # Log conversation
        log_conversation(user_input, response)
        
        # Check for exit
        if any(word in user_input.lower() for word in ['bye', 'exit', 'quit']):
            print("\n💾 Conversation logged to chat_logs.json")
            print("👋 Thank you for using CodecBot!")
            break

# Run chatbot
if __name__ == "__main__":
    main()
