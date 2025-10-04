import os
import time
from typing import Dict, List

class SelfReflectionAI:
    def __init__(self):
        self.current_iteration = 0
        self.max_iterations = 3
        self.original_text = ""
        self.summaries = []
        self.critiques = []
        self.improvements = []
        
        self.reflection_criteria = [
            "Clarity - Is the summary easy to understand?",
            "Completeness - Does it cover all key points?",
            "Conciseness - Is it brief without losing meaning?",
            "Accuracy - Does it faithfully represent the original?",
            "Structure - Is it well-organized?"
        ]
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Print the application header"""
        print("=" * 80)
        print("🔄 SELF-REFLECTION AI - ITERATIVE IMPROVEMENT".center(80))
        print("Critique and Improve Summaries Through Self-Reflection".center(80))
        print("=" * 80)
        print()
    
    def print_iteration_progress(self):
        """Display current iteration progress"""
        print("📊 ITERATION PROGRESS:")
        print("-" * 80)
        for i in range(self.max_iterations):
            if i < self.current_iteration:
                status = "✅"
                color = "\033[92m"  # Green
            elif i == self.current_iteration:
                status = "▶️"
                color = "\033[94m"  # Blue
            else:
                status = "⭕"
                color = "\033[90m"  # Gray
            
            print(f"{color}{status} Iteration {i+1}: ", end="")
            if i < len(self.summaries):
                print(f"Summary → Critique → Improvement\033[0m")
            else:
                print(f"Pending\033[0m")
        
        print("-" * 80)
        print()
    
    def print_original_text(self):
        """Display the original text"""
        if self.original_text:
            print("📄 ORIGINAL TEXT:")
            print("-" * 80)
            print(self.original_text)
            print("-" * 80)
            print()
    
    def print_current_summary(self):
        """Display the current summary"""
        if self.summaries and self.current_iteration > 0:
            idx = self.current_iteration - 1
            print(f"📝 SUMMARY (Iteration {self.current_iteration}):")
            print("-" * 80)
            print(self.summaries[idx])
            print("-" * 80)
            print()
    
    def print_critique(self):
        """Display the critique"""
        if self.critiques and self.current_iteration > 0:
            idx = self.current_iteration - 1
            print(f"🔍 SELF-CRITIQUE (Iteration {self.current_iteration}):")
            print("-" * 80)
            for key, value in self.critiques[idx].items():
                icon = "✅" if "good" in value.lower() or "clear" in value.lower() else "⚠️"
                print(f"{icon} {key}: {value}")
            print("-" * 80)
            print()
    
    def print_improvements(self):
        """Display identified improvements"""
        if self.improvements and self.current_iteration > 0:
            idx = self.current_iteration - 1
            print(f"💡 IDENTIFIED IMPROVEMENTS (Iteration {self.current_iteration}):")
            print("-" * 80)
            for i, improvement in enumerate(self.improvements[idx], 1):
                print(f"   {i}. {improvement}")
            print("-" * 80)
            print()
    
    def print_comparison(self):
        """Display side-by-side comparison of all summaries"""
        if len(self.summaries) > 1:
            print("📊 SUMMARY EVOLUTION:")
            print("=" * 80)
            for i, summary in enumerate(self.summaries, 1):
                print(f"\n🔹 Version {i}:")
                print("-" * 80)
                print(summary)
            print("=" * 80)
            print()
    
    def display_ui(self):
        """Display the complete UI"""
        self.clear_screen()
        self.print_header()
        self.print_iteration_progress()
        self.print_original_text()
        self.print_current_summary()
        self.print_critique()
        self.print_improvements()
    
    def generate_initial_summary(self, text: str) -> str:
        """Generate the initial summary"""
        # Simple extractive summary - take first few sentences and key points
        sentences = text.split('. ')
        
        # For demo purposes, create a deliberately improvable summary
        if len(sentences) > 3:
            summary = '. '.join(sentences[:2]) + '.'
        else:
            summary = text
        
        return summary
    
    def generate_critique(self, summary: str, iteration: int) -> Dict[str, str]:
        """Generate self-critique based on reflection criteria"""
        critique = {}
        
        # Simulate different critiques based on iteration
        if iteration == 1:
            critique = {
                "Clarity": "Somewhat clear but could be more direct",
                "Completeness": "Missing some important details from the original",
                "Conciseness": "Good length but could be more focused",
                "Accuracy": "Accurate but lacks specific examples",
                "Structure": "Basic structure, could improve logical flow"
            }
        elif iteration == 2:
            critique = {
                "Clarity": "Much clearer with better word choice",
                "Completeness": "Better coverage but still missing minor points",
                "Conciseness": "Well-balanced length",
                "Accuracy": "More accurate with added specifics",
                "Structure": "Improved flow and organization"
            }
        else:
            critique = {
                "Clarity": "Excellent clarity and readability",
                "Completeness": "Comprehensive coverage of all key points",
                "Conciseness": "Perfectly concise without sacrificing meaning",
                "Accuracy": "Highly accurate with precise details",
                "Structure": "Well-structured and logically organized"
            }
        
        return critique
    
    def generate_improvements(self, critique: Dict[str, str], iteration: int) -> List[str]:
        """Generate list of improvements based on critique"""
        improvements = []
        
        if iteration == 1:
            improvements = [
                "Add more specific details and examples from the original text",
                "Improve sentence structure for better flow",
                "Include key points that were omitted",
                "Use more precise vocabulary",
                "Better organize information hierarchically"
            ]
        elif iteration == 2:
            improvements = [
                "Fine-tune word choices for maximum clarity",
                "Ensure all secondary points are captured",
                "Polish transitions between ideas",
                "Verify consistency in tone and style"
            ]
        else:
            improvements = [
                "Summary has reached optimal quality",
                "All major improvement areas addressed",
                "Ready for final use"
            ]
        
        return improvements
    
    def improve_summary(self, previous_summary: str, improvements: List[str]) -> str:
        """Generate improved summary based on identified improvements"""
        # For demo purposes, progressively improve the summary
        
        if self.current_iteration == 1:
            # First improvement - add more details
            improved = previous_summary + " This includes additional context and specific examples that were initially overlooked, providing a more comprehensive overview."
        elif self.current_iteration == 2:
            # Second improvement - refine and polish
            improved = "A well-structured and comprehensive summary that captures all essential information from the original text. " + previous_summary + " The content is now organized logically with clear connections between ideas, maintaining accuracy while achieving optimal conciseness."
        else:
            improved = previous_summary
        
        return improved
    
    def reflection_cycle(self):
        """Execute one complete reflection cycle"""
        print(f"\n{'='*80}")
        print(f"🔄 ITERATION {self.current_iteration}")
        print(f"{'='*80}\n")
        
        # Step 1: Generate/Improve Summary
        if self.current_iteration == 1:
            print("📝 Generating initial summary...")
            time.sleep(1)
            summary = self.generate_initial_summary(self.original_text)
        else:
            print("📝 Generating improved summary based on feedback...")
            time.sleep(1)
            previous_summary = self.summaries[-1]
            previous_improvements = self.improvements[-1]
            summary = self.improve_summary(previous_summary, previous_improvements)
        
        self.summaries.append(summary)
        self.display_ui()
        input("\nPress Enter to generate self-critique...")
        
        # Step 2: Generate Critique
        print("\n🔍 Analyzing summary and generating critique...")
        time.sleep(1)
        critique = self.generate_critique(summary, self.current_iteration)
        self.critiques.append(critique)
        self.display_ui()
        input("\nPress Enter to identify improvements...")
        
        # Step 3: Identify Improvements
        print("\n💡 Identifying areas for improvement...")
        time.sleep(1)
        improvements = self.generate_improvements(critique, self.current_iteration)
        self.improvements.append(improvements)
        self.display_ui()
        
        # Check if we should continue
        if self.current_iteration < self.max_iterations:
            response = input(f"\nPress Enter to continue to Iteration {self.current_iteration + 1} (or type 'stop' to finish): ").strip().lower()
            if response == 'stop':
                return False
        
        return True
    
    def run(self):
        """Main application loop"""
        self.clear_screen()
        print("\n🔄 Welcome to Self-Reflection AI!")
        print("=" * 80)
        print("\nThis tool demonstrates how AI can critique and improve its own outputs")
        print("through iterative self-reflection.\n")
        print("How it works:")
        print("  1. Generate initial summary")
        print("  2. Critique the summary (self-reflection)")
        print("  3. Identify improvements")
        print("  4. Generate improved version")
        print("  5. Repeat until optimal\n")
        print("Commands: 'quit' to exit, 'reset' to start over")
        print("=" * 80)
        
        while True:
            print("\n")
            print("📄 Enter the text you want to summarize (or 'quit' to exit):")
            print("(You can paste multiple lines. Type 'END' on a new line when done)\n")
            
            lines = []
            while True:
                line = input()
                if line.strip().lower() == 'quit':
                    print("\n👋 Thank you for using Self-Reflection AI. Goodbye!")
                    return
                if line.strip().upper() == 'END':
                    break
                lines.append(line)
            
            text = ' '.join(lines).strip()
            
            if not text:
                print("\n⚠️  No text provided. Please try again.")
                continue
            
            # Reset for new text
            self.__init__()
            self.original_text = text
            
            # Run reflection cycles
            self.current_iteration = 1
            while self.current_iteration <= self.max_iterations:
                continue_reflection = self.reflection_cycle()
                
                if not continue_reflection:
                    break
                
                self.current_iteration += 1
            
            # Show final comparison
            self.display_ui()
            self.print_comparison()
            
            print("\n" + "="*80)
            print("✅ REFLECTION PROCESS COMPLETE!")
            print("="*80)
            print(f"\nFinal Summary (Version {len(self.summaries)}):")
            print("-" * 80)
            print(self.summaries[-1])
            print("-" * 80)
            
            print("\n💡 Key Improvements Made:")
            all_improvements = []
            for imp_list in self.improvements:
                all_improvements.extend(imp_list)
            unique_improvements = list(set(all_improvements))
            for i, imp in enumerate(unique_improvements[:5], 1):
                print(f"   {i}. {imp}")
            
            print("\n" + "="*80)
            choice = input("\nEnter new text, type 'reset', or 'quit': ").strip().lower()
            if choice == 'quit':
                print("\n👋 Thank you for using Self-Reflection AI. Goodbye!")
                break
            elif choice == 'reset':
                self.__init__()
                continue

def main():
    """Entry point"""
    try:
        tool = SelfReflectionAI()
        tool.run()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()