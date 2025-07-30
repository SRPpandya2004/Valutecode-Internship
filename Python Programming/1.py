# 1)
# def add_num(a,b)
#     return a+b
# print(add_num(5,10))

# 2)   
# name= 'Alice'
# print("Hello, "+name)    

# 3)
# for i in range(5):
#     print("Number:", i)

# 4)
# my_list = [1, 2, 3, 4, 5]
# print("The fifth element is: " + str(my_list[4]))

# 5)
# def greet(name):
#     print("Hello " + name)
# greet("Bob")

# 6)
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# 7)
# def multiply(a, b):
#     result = a * b
#     return result
# print(multiply(4, 5))

# 8)
# count = 10
# while count > 0:
#     print(count)
#     count -= 1
# print("Countdown !")

from fpdf import FPDF

# Define the presentation content
slides = [
    {
        "title": "Introduction to Python",
        "content": (
            "Python is a high-level, interpreted programming language known for its simplicity and readability. "
            "It supports multiple programming paradigms, including procedural, object-oriented, and functional programming."
        )
    },
    {
        "title": "History of Python",
        "content": (
            "• Developed by Guido van Rossum in the late 1980s.\n"
            "• First released in 1991 as Python 0.9.0.\n"
            "• Python 2.0 released in 2000 with new features like list comprehensions.\n"
            "• Python 3.0 released in 2008 with improvements and breaking changes.\n"
            "• Widely used today in web development, data science, AI, and automation."
        )
    },
    {
        "title": "Why Use Python?",
        "content": (
            "• Easy to learn and use\n"
            "• Extensive standard libraries\n"
            "• Large community support\n"
            "• Cross-platform compatibility\n"
            "• Ideal for rapid development and prototyping"
        )
    },
    {
        "title": "What are Functions?",
        "content": (
            "Functions are reusable blocks of code that perform a specific task.\n"
            "They help in organizing code, avoiding repetition, and improving readability.\n\n"
            "Syntax:\n"
            "def function_name(parameters):\n"
            "    # function body"
        )
    },
    {
        "title": "Function Example",
        "content": (
            "def greet(name):\n"
            "    return f\"Hello, {name}!\"\n\n"
            "print(greet(\"Alice\"))\n"
            "# Output: Hello, Alice!"
        )
    },
    {
        "title": "Types of Functions",
        "content": (
            "• Built-in Functions: Provided by Python (e.g., len(), print(), type())\n"
            "• User-defined Functions: Created by users using 'def'\n"
            "• Lambda Functions: Anonymous functions using 'lambda'"
        )
    },
    {
        "title": "What are Modules?",
        "content": (
            "Modules are files containing Python code (functions, variables, classes).\n"
            "They allow code organization and reuse.\n\n"
            "Example:\n"
            "import math\n"
            "print(math.sqrt(16))  # Output: 4.0"
        )
    },
    {
        "title": "Creating Your Own Module",
        "content": (
            "You can create your own module by saving functions in a .py file.\n\n"
            "Example:\n"
            "# mymodule.py\n"
            "def add(a, b):\n"
            "    return a + b\n\n"
            "# main.py\n"
            "import mymodule\n"
            "print(mymodule.add(2, 3))  # Output: 5"
        )
    },
    {
        "title": "Conclusion",
        "content": (
            "Python is a versatile language suitable for beginners and professionals alike.\n"
            "Understanding functions and modules is essential for writing efficient, reusable code.\n"
            "Keep exploring Python's vast ecosystem!"
        )
    }
]

# Create PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, "Python Presentation", 0, 1, "C")
        self.ln(5)

    def add_slide(self, title, content):
        self.set_font("Arial", "B", 14)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, title, 0, 1)
        self.ln(2)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 10, content)
        self.ln()

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

for slide in slides:
    pdf.add_page()
    pdf.add_slide(slide["title"], slide["content"])

# Save PDF
pdf.output("Python_Presentation_8_9_Slides.pdf")
