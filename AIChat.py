from interpreter import interpreter

interpreter.llm.model = "gpt-3.5-turbo"
interpreter.auto_run = True  # Don't require user confirmation

interpreter.chat("Open Keynote, if not already open")

interpreter.chat("With the keynote window open, Select new document")
interpreter.chat("Select Minimalist Light Template")