import os
import time
from typing import Dict, List

class CustomerSupportAI:
    def __init__(self):
        self.current_step = 0
        self.chat_history = []
        self.collected_data = {
            'issue': '',
            'category': '',
            'urgency': '',
            'details': '',
            'solution': ''
        }
        
        self.steps = [
            {
                'id': 'greeting',
                'name': 'Greeting',
                'prompt': 'Greet the customer and ask what issue they need help with.',
                'system_prompt': 'You are a friendly customer support agent. Greet the customer warmly and ask them to describe their issue briefly.'
            },
            {
                'id': 'categorize',
                'name': 'Categorize',
                'prompt': 'Categorize the issue into: Technical, Billing, Account, or General.',
                'system_prompt': "Based on the customer's issue, categorize it as Technical, Billing, Account, or General. Confirm the category with the customer."
            },
            {
                'id': 'urgency',
                'name': 'Urgency',
                'prompt': 'Determine urgency level: Low, Medium, or High.',
                'system_prompt': 'Ask clarifying questions to determine if this is Low (can wait), Medium (needs attention soon), or High (urgent) priority.'
            },
            {
                'id': 'details',
                'name': 'Details',
                'prompt': 'Gather detailed information about the problem.',
                'system_prompt': 'Ask specific questions to gather all necessary details to resolve the issue effectively.'
            },
            {
                'id': 'solution',
                'name': 'Solution',
                'prompt': 'Provide a solution or next steps.',
                'system_prompt': 'Based on all the information gathered, provide a clear solution or escalation path. Confirm the customer is satisfied.'
            }
        ]
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Print the application header"""
        print("=" * 60)
        print("🤖 CUSTOMER SUPPORT AI - PROMPT CHAIN DEMO".center(60))
        print("=" * 60)
        print()
    
    def print_steps(self):
        """Display the current progress through the chain"""
        print("📋 PROMPT CHAIN STEPS:")
        print("-" * 60)
        for i, step in enumerate(self.steps):
            if i < self.current_step:
                status = "✅"
                color = "\033[92m"  # Green
            elif i == self.current_step:
                status = "▶️"
                color = "\033[94m"  # Blue
            else:
                status = "⭕"
                color = "\033[90m"  # Gray
            
            print(f"{color}{status} Step {i+1}: {step['name']}\033[0m")
            print(f"   {step['prompt']}")
        
        print("-" * 60)
        print()
    
    def print_chat_history(self):
        """Display the chat conversation"""
        print("💬 CHAT CONVERSATION:")
        print("-" * 60)
        
        if not self.chat_history:
            print("   No messages yet. Start the conversation!")
        else:
            for msg in self.chat_history:
                if msg['role'] == 'user':
                    print(f"\n👤 YOU: {msg['content']}")
                else:
                    print(f"\n🤖 AGENT: {msg['content']}")
        
        print()
        print("-" * 60)
        print()
    
    def print_collected_data(self):
        """Display collected customer information"""
        if any(self.collected_data.values()):
            print("📊 COLLECTED INFORMATION:")
            print("-" * 60)
            for key, value in self.collected_data.items():
                if value:
                    print(f"   {key.capitalize()}: {value}")
            print("-" * 60)
            print()
    
    def generate_response(self, user_input: str) -> str:
        """Generate AI response based on current step"""
        step = self.current_step
        
        if step == 0:  # Greeting
            return "Hello! Thank you for contacting our support team. I'm here to help you today. Could you please describe the issue you're experiencing?"
        
        elif step == 1:  # Categorize
            categories = ['technical', 'billing', 'account', 'general']
            detected_category = next((cat for cat in categories if cat in user_input.lower()), 'Technical')
            return f"I understand. This sounds like a {detected_category.capitalize()} issue. Is that correct?"
        
        elif step == 2:  # Urgency
            return "Thank you for confirming. To help prioritize your request, could you tell me if this is preventing you from using our service completely, or is it something that can wait a bit?"
        
        elif step == 3:  # Details
            return "I appreciate those details. To help resolve this quickly, could you provide any error messages you're seeing, or when you first noticed this issue?"
        
        elif step == 4:  # Solution
            import random
            ticket_number = random.randint(1000, 9999)
            return f"Based on everything you've shared, here's what I recommend: [Solution tailored to your issue]. I'll also create a ticket (#{ticket_number}) for our team to follow up. Is there anything else I can help you with today?"
        
        return "Thank you for your response."
    
    def update_collected_data(self, user_input: str):
        """Update collected data based on current step"""
        step_keys = ['issue', 'category', 'urgency', 'details', 'solution']
        if self.current_step < len(step_keys):
            self.collected_data[step_keys[self.current_step]] = user_input
    
    def display_ui(self):
        """Display the complete UI"""
        self.clear_screen()
        self.print_header()
        self.print_steps()
        self.print_chat_history()
        self.print_collected_data()
    
    def process_message(self, user_input: str):
        """Process user message and generate response"""
        # Add user message
        self.chat_history.append({'role': 'user', 'content': user_input})
        
        # Update collected data
        self.update_collected_data(user_input)
        
        # Generate AI response
        time.sleep(0.5)  # Simulate thinking
        ai_response = self.generate_response(user_input)
        self.chat_history.append({'role': 'assistant', 'content': ai_response})
        
        # Move to next step
        if self.current_step < len(self.steps) - 1:
            time.sleep(0.5)
            self.current_step += 1
    
    def run(self):
        """Main application loop"""
        print("\n🚀 Welcome to Customer Support AI!")
        print("Type your messages to interact with the AI agent.")
        print("Commands: 'reset' to restart, 'quit' to exit\n")
        input("Press Enter to start...")
        
        # Initial greeting
        greeting = self.generate_response("")
        self.chat_history.append({'role': 'assistant', 'content': greeting})
        
        while True:
            self.display_ui()
            
            # Check if conversation is complete
            if self.current_step >= len(self.steps):
                print("✅ Support session complete!")
                print("\nOptions: Type 'reset' to start over or 'quit' to exit")
            
            # Get user input
            user_input = input("💬 Your message: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == 'quit':
                print("\n👋 Thank you for using Customer Support AI. Goodbye!")
                break
            
            if user_input.lower() == 'reset':
                self.__init__()
                greeting = self.generate_response("")
                self.chat_history.append({'role': 'assistant', 'content': greeting})
                continue
            
            # Process the message
            if self.current_step < len(self.steps):
                self.process_message(user_input)
            else:
                print("\n⚠️  Conversation is complete. Type 'reset' to start over.")
                time.sleep(2)

def main():
    """Entry point"""
    try:
        app = CustomerSupportAI()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()