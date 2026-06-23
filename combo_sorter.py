import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import re

class TextExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Messy Text Extractor")
        self.root.geometry("680x600")
        
        # --- Input Section ---
        tk.Label(root, text="Paste your messy text below or open a file:", font=("Arial", 11, "bold")).pack(pady=(10, 5))
        self.input_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=12)
        self.input_area.pack(pady=5, padx=15)

        # --- Button Frame ---
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        # Buttons mapped to their respective functions
        tk.Button(btn_frame, text="📁 Open File", command=self.load_file, bg="#FF9800", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="🧹 Clean Accounts", command=self.process_accounts, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="🎮 Extract Xbox Codes", command=self.process_codes, bg="#2196F3", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="🗑️ Clear Both", command=self.clear_all, bg="#f44336", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)

        # --- Output Section ---
        tk.Label(root, text="Extraction Results:", font=("Arial", 11, "bold")).pack(pady=(10, 5))
        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=15)
        self.output_area.pack(pady=5, padx=15)
        self.output_area.config(state=tk.DISABLED) # Make read-only by default

    def load_file(self):
        """Opens a file dialog and loads the text into the input area."""
        file_path = filedialog.askopenfilename(
            title="Select a Text File",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    self.input_area.delete("1.0", tk.END)
                    self.input_area.insert(tk.END, file_content)
            except Exception as e:
                self.display_output(f"❌ Error reading file:\n{str(e)}")

    def display_output(self, text):
        """Helper function to print text into the output box."""
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete("1.0", tk.END)
        self.output_area.insert(tk.END, text)
        self.output_area.config(state=tk.DISABLED)

    def clear_all(self):
        """Clears both the input and output boxes."""
        self.input_area.delete("1.0", tk.END)
        self.display_output("")

    def process_accounts(self):
        """Account cleaning logic."""
        messy_text = self.input_area.get("1.0", tk.END)
        count = 0
        results = []

        for line in messy_text.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            first_chunk = line.split(' ')[0]
            first_chunk = first_chunk.split('|')[0]
            
            if ':' in first_chunk and len(first_chunk) > 5:
                results.append(first_chunk)
                count += 1

        # Format the output string
        output_str = "=== 🧹 CLEANED ACCOUNTS 🧹 ===\n\n"
        output_str += "\n".join(results)
        output_str += "\n\n" + "="*30 + "\n"
        output_str += f"✅ Successfully cleaned {count} accounts!"
        
        self.display_output(output_str)

    def process_codes(self):
        """Xbox code extraction logic."""
        messy_text = self.input_area.get("1.0", tk.END)
        pattern = r'\b[A-Za-z0-9]{5}-[A-Za-z0-9]{5}-[A-Za-z0-9]{5}-[A-Za-z0-9]{5}-[A-Za-z0-9]{5}\b'
        
        matches = re.findall(pattern, messy_text)
        extracted_codes = [match.upper() for match in matches]

        # Format the output string
        output_str = f"Found {len(extracted_codes)} code(s):\n\n"
        output_str += "\n".join(extracted_codes)
        
        self.display_output(output_str)

if __name__ == "__main__":
    # Initialize and run the Tkinter application
    root = tk.Tk()
    app = TextExtractorApp(root)
    root.mainloop()