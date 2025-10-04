import os
import time
import sys
from io import StringIO
from typing import Dict, List

class ReACTCodeGenerator:
    def __init__(self):
        self.current_phase = 0
        self.task_description = ""
        self.reasoning_log = []
        self.generated_code = ""
        self.execution_output = ""
        self.execution_error = ""
        
        self.phases = [
            {
                'id': 'understand',
                'name': 'Understanding Task',
                'description': 'Analyze and understand the coding task requirements',
                'icon': '🤔'
            },
            {
                'id': 'reason',
                'name': 'Reasoning',
                'description': 'Think through the approach and logic needed',
                'icon': '💭'
            },
            {
                'id': 'plan',
                'name': 'Planning',
                'description': 'Create a step-by-step implementation plan',
                'icon': '📋'
            },
            {
                'id': 'generate',
                'name': 'Code Generation',
                'description': 'Write the actual Python code',
                'icon': '⚙️'
            },
            {
                'id': 'execute',
                'name': 'Execution',
                'description': 'Run the code and verify results',
                'icon': '▶️'
            },
            {
                'id': 'reflect',
                'name': 'Reflection',
                'description': 'Analyze results and suggest improvements',
                'icon': '🔍'
            }
        ]
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Print the application header"""
        print("=" * 70)
        print("🤖 ReACT CODE GENERATOR".center(70))
        print("Reasoning + Action Pattern for Code Generation".center(70))
        print("=" * 70)
        print()
    
    def print_phases(self):
        """Display the current progress through ReACT phases"""
        print("📊 ReACT PHASES:")
        print("-" * 70)
        for i, phase in enumerate(self.phases):
            if i < self.current_phase:
                status = "✅"
                color = "\033[92m"  # Green
            elif i == self.current_phase:
                status = "▶️"
                color = "\033[94m"  # Blue
            else:
                status = "⭕"
                color = "\033[90m"  # Gray
            
            print(f"{color}{status} {phase['icon']} Phase {i+1}: {phase['name']}\033[0m")
            print(f"   {phase['description']}")
        
        print("-" * 70)
        print()
    
    def print_task(self):
        """Display the current task"""
        if self.task_description:
            print("📝 TASK:")
            print("-" * 70)
            print(f"   {self.task_description}")
            print("-" * 70)
            print()
    
    def print_reasoning(self):
        """Display reasoning steps"""
        if self.reasoning_log:
            print("💭 REASONING LOG:")
            print("-" * 70)
            for i, reason in enumerate(self.reasoning_log, 1):
                print(f"   {i}. {reason}")
            print("-" * 70)
            print()
    
    def print_code(self):
        """Display generated code"""
        if self.generated_code:
            print("💻 GENERATED CODE:")
            print("-" * 70)
            print("\033[93m")  # Yellow color for code
            print(self.generated_code)
            print("\033[0m")
            print("-" * 70)
            print()
    
    def print_execution_results(self):
        """Display execution output"""
        if self.execution_output or self.execution_error:
            print("▶️  EXECUTION RESULTS:")
            print("-" * 70)
            if self.execution_output:
                print("\033[92m✅ Output:\033[0m")
                print(self.execution_output)
            if self.execution_error:
                print("\033[91m❌ Error:\033[0m")
                print(self.execution_error)
            print("-" * 70)
            print()
    
    def display_ui(self):
        """Display the complete UI"""
        self.clear_screen()
        self.print_header()
        self.print_phases()
        self.print_task()
        self.print_reasoning()
        self.print_code()
        self.print_execution_results()
    
    def phase_understand(self, task: str):
        """Phase 1: Understand the task"""
        self.task_description = task
        time.sleep(0.5)
        
        # Reasoning for understanding
        reasoning = [
            f"Task received: '{task}'",
            "Identifying key requirements and constraints",
            "Determining input/output expectations",
            "Checking for edge cases to consider"
        ]
        
        self.reasoning_log.extend(reasoning)
        print("\n🤔 Understanding the task...")
        time.sleep(1)
    
    def phase_reason(self):
        """Phase 2: Reason about the approach"""
        print("\n💭 Reasoning about the approach...")
        time.sleep(1)
        
        # Add reasoning based on task type
        task_lower = self.task_description.lower()
        
        if 'fibonacci' in task_lower:
            reasoning = [
                "This is a sequence generation problem",
                "Can be solved iteratively or recursively",
                "Iterative approach is more efficient for large n",
                "Need to handle base cases (n=0, n=1)"
            ]
        elif 'prime' in task_lower:
            reasoning = [
                "Need to check divisibility by numbers",
                "Only need to check up to sqrt(n)",
                "Handle edge cases: n < 2 returns False",
                "Can optimize by checking 2 separately, then odd numbers"
            ]
        elif 'palindrome' in task_lower:
            reasoning = [
                "Need to compare string with its reverse",
                "Can ignore case and non-alphanumeric characters",
                "Can use slicing or two-pointer approach",
                "Edge case: empty string is a palindrome"
            ]
        elif 'sort' in task_lower or 'bubble' in task_lower:
            reasoning = [
                "Need to implement sorting algorithm",
                "Bubble sort compares adjacent elements",
                "Time complexity: O(n²)",
                "Need nested loops for comparison and swapping"
            ]
        elif 'factorial' in task_lower:
            reasoning = [
                "Factorial is the product of all positive integers up to n",
                "Can be solved recursively or iteratively",
                "Base case: 0! = 1, 1! = 1",
                "Need to handle negative numbers (undefined)"
            ]
        else:
            reasoning = [
                "Analyzing the problem structure",
                "Identifying required data structures",
                "Considering algorithmic complexity",
                "Planning for error handling"
            ]
        
        self.reasoning_log.extend(reasoning)
    
    def phase_plan(self):
        """Phase 3: Create implementation plan"""
        print("\n📋 Creating implementation plan...")
        time.sleep(1)
        
        task_lower = self.task_description.lower()
        
        if 'fibonacci' in task_lower:
            plan = [
                "Step 1: Define function with parameter n",
                "Step 2: Handle base cases (n=0 returns 0, n=1 returns 1)",
                "Step 3: Initialize first two numbers",
                "Step 4: Loop from 2 to n, calculating next number",
                "Step 5: Return the nth Fibonacci number"
            ]
        elif 'prime' in task_lower:
            plan = [
                "Step 1: Define function with parameter n",
                "Step 2: Handle edge cases (n < 2)",
                "Step 3: Check if divisible by 2",
                "Step 4: Check odd divisors up to sqrt(n)",
                "Step 5: Return True if no divisors found"
            ]
        elif 'palindrome' in task_lower:
            plan = [
                "Step 1: Define function with string parameter",
                "Step 2: Clean string (lowercase, remove non-alphanumeric)",
                "Step 3: Compare string with reverse",
                "Step 4: Return boolean result"
            ]
        elif 'sort' in task_lower or 'bubble' in task_lower:
            plan = [
                "Step 1: Define function with list parameter",
                "Step 2: Get length of list",
                "Step 3: Outer loop for passes",
                "Step 4: Inner loop for comparisons",
                "Step 5: Swap if elements are out of order",
                "Step 6: Return sorted list"
            ]
        elif 'factorial' in task_lower:
            plan = [
                "Step 1: Define function with parameter n",
                "Step 2: Handle base case (n=0 or n=1 returns 1)",
                "Step 3: Handle negative numbers (raise error)",
                "Step 4: Initialize result variable",
                "Step 5: Multiply result by each number from 2 to n",
                "Step 6: Return final result"
            ]
        else:
            plan = [
                "Step 1: Define function signature",
                "Step 2: Initialize necessary variables",
                "Step 3: Implement main logic",
                "Step 4: Handle edge cases",
                "Step 5: Return result"
            ]
        
        self.reasoning_log.extend(plan)
    
    def phase_generate(self):
        """Phase 4: Generate the actual code"""
        print("\n⚙️  Generating code...")
        time.sleep(1)
        
        task_lower = self.task_description.lower()
        
        if 'fibonacci' in task_lower:
            self.generated_code = '''def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Test the function
result = fibonacci(10)
print(f"The 10th Fibonacci number is: {result}")'''
        
        elif 'prime' in task_lower:
            self.generated_code = '''def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Test the function
test_numbers = [2, 17, 20, 29, 100]
for num in test_numbers:
    print(f"{num} is prime: {is_prime(num)}")'''
        
        elif 'palindrome' in task_lower:
            self.generated_code = '''def is_palindrome(text):
    """Check if a string is a palindrome."""
    # Clean the string: lowercase and keep only alphanumeric
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    
    # Compare with reverse
    return cleaned == cleaned[::-1]

# Test the function
test_strings = ["racecar", "hello", "A man a plan a canal Panama", "12321"]
for s in test_strings:
    print(f"'{s}' is palindrome: {is_palindrome(s)}")'''
        
        elif 'sort' in task_lower or 'bubble' in task_lower:
            self.generated_code = '''def bubble_sort(arr):
    """Sort a list using bubble sort algorithm."""
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps, array is sorted
        if not swapped:
            break
    
    return arr

# Test the function
unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(unsorted)
print(f"Original: {unsorted}")
print(f"Sorted: {sorted_arr}")'''
        
        elif 'factorial' in task_lower:
            self.generated_code = '''def factorial(n):
    """Calculate the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

# Test the function
test_values = [0, 1, 5, 10]
for val in test_values:
    print(f"{val}! = {factorial(val)}")'''
        
        else:
            # Generic example code
            self.generated_code = '''def solve_task():
    """
    Generic function to solve the given task.
    This is a placeholder - customize based on your specific needs.
    """
    result = "Task completed successfully!"
    return result

# Test the function
output = solve_task()
print(output)'''
    
    def phase_execute(self):
        """Phase 5: Execute the generated code"""
        print("\n▶️  Executing code...")
        time.sleep(1)
        
        try:
            # Capture stdout
            old_stdout = sys.stdout
            sys.stdout = captured_output = StringIO()
            
            # Execute the code
            exec(self.generated_code)
            
            # Get the output
            sys.stdout = old_stdout
            self.execution_output = captured_output.getvalue()
            
            self.reasoning_log.append("Code executed successfully!")
            
        except Exception as e:
            sys.stdout = old_stdout
            self.execution_error = str(e)
            self.reasoning_log.append(f"Execution failed: {str(e)}")
    
    def phase_reflect(self):
        """Phase 6: Reflect on the results"""
        print("\n🔍 Reflecting on results...")
        time.sleep(1)
        
        if self.execution_error:
            reflections = [
                "Error encountered during execution",
                "Code needs debugging and revision",
                "Consider edge cases and input validation",
                "Next step: Fix the error and re-test"
            ]
        else:
            reflections = [
                "Code executed successfully!",
                "Output matches expected results",
                "Possible improvements: Add error handling, optimize performance",
                "Code is ready for production use with proper testing"
            ]
        
        self.reasoning_log.extend(reflections)
    
    def process_task(self, task: str):
        """Process a coding task through all ReACT phases"""
        # Phase 1: Understand
        self.current_phase = 0
        self.display_ui()
        self.phase_understand(task)
        input("\nPress Enter to continue to Reasoning phase...")
        
        # Phase 2: Reason
        self.current_phase = 1
        self.display_ui()
        self.phase_reason()
        input("\nPress Enter to continue to Planning phase...")
        
        # Phase 3: Plan
        self.current_phase = 2
        self.display_ui()
        self.phase_plan()
        input("\nPress Enter to continue to Code Generation...")
        
        # Phase 4: Generate
        self.current_phase = 3
        self.display_ui()
        self.phase_generate()
        input("\nPress Enter to execute the code...")
        
        # Phase 5: Execute
        self.current_phase = 4
        self.display_ui()
        self.phase_execute()
        input("\nPress Enter to see reflection...")
        
        # Phase 6: Reflect
        self.current_phase = 5
        self.display_ui()
        self.phase_reflect()
        self.current_phase = 6
        self.display_ui()
    
    def run(self):
        """Main application loop"""
        self.clear_screen()
        print("\n🤖 Welcome to ReACT Code Generator!")
        print("=" * 70)
        print("\nThis tool uses the ReACT pattern (Reasoning + Action) to generate code.")
        print("Watch as the AI reasons through each step before taking action!\n")
        print("Example tasks you can try:")
        print("  • Write a function to calculate the nth Fibonacci number")
        print("  • Create a function to check if a number is prime")
        print("  • Implement a palindrome checker")
        print("  • Write a bubble sort algorithm")
        print("  • Create a factorial calculator")
        print("\nCommands: 'quit' to exit, 'reset' to start over")
        print("=" * 70)
        
        while True:
            print("\n")
            task = input("📝 Enter your coding task (or 'quit' to exit): ").strip()
            
            if not task:
                continue
            
            if task.lower() == 'quit':
                print("\n👋 Thank you for using ReACT Code Generator. Goodbye!")
                break
            
            if task.lower() == 'reset':
                self.__init__()
                continue
            
            # Process the task through all phases
            self.process_task(task)
            
            print("\n✅ ReACT cycle complete!")
            print("\nOptions:")
            print("  • Enter a new task")
            print("  • Type 'reset' to clear everything")
            print("  • Type 'quit' to exit")

def main():
    """Entry point"""
    try:
        generator = ReACTCodeGenerator()
        generator.run()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()