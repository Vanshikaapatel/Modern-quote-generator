import tkinter as tk
from tkinter import messagebox, ttk
import random
import json
import os
from matplotlib import text
import pyttsx3
import pyperclip
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import threading
import time
import webbrowser
import subprocess
import sys
import urllib.parse

# ------------------ QUOTES ------------------ #
motivational_quotes = [
    "The best way to predict the future is to create it.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Don't watch the clock; do what it does. Keep going.",
    "Believe you can and you're halfway there.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Dream it. Wish it. Do it.",
    "Great things never come from comfort zones.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Doubt kills more dreams than failure ever will.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Don't stop when you're tired. Stop when you're done.",
    "Little things make big days.",
    "It's going to be hard, but hard does not mean impossible."
]

life_quotes = [
    "Life is what happens when you're busy making other plans.",
    "Get busy living, or get busy dying.",
    "In the end, we only regret the chances we didn't take.",
    "Life is really simple, but we insist on making it complicated.",
    "Life isn't about finding yourself. It's about creating yourself.",
    "Difficult roads often lead to beautiful destinations.",
    "Enjoy the little things in life, for one day you may look back and realize they were the big things.",
    "Life is short, and it is up to you to make it sweet.",
    "To live is the rarest thing in the world. Most people exist, that is all.",
    "Live as if you were to die tomorrow. Learn as if you were to live forever.",
    "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.",
    "The purpose of our lives is to be happy.",
    "Life is either a daring adventure or nothing at all.",
    "Life has no limitations, except the ones you make.",
    "Live your life and forget your age."
]

love_quotes = [
    "Love the one you're with.",
    "The greatest thing you'll ever learn is just to love and be loved in return.",
    "Love is composed of a single soul inhabiting two bodies.",
    "Love is a many-splendored thing.",
    "You know you're in love when you can't fall asleep because reality is finally better than your dreams.",
    "Love doesn't make the world go round. Love is what makes the ride worthwhile.",
    "Where there is love there is life.",
    "To love and be loved is to feel the sun from both sides.",
    "Love is not about how many days, months, or years you've been together. Love is about how much you love each other every single day.",
    "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.",
    "True love stories never have endings.",
    "Love is when the other person's happiness is more important than your own.",
    "I saw that you were perfect, and so I loved you. Then I saw that you were not perfect and I loved you even more.",
    "Love is the bridge between you and everything.",
    "Love recognizes no barriers. It jumps hurdles, leaps fences, penetrates walls to arrive at its destination full of hope."
]

friendship_quotes = [
    "Friendship is the only cement that will ever hold the world together.",
    "A real friend is one who walks in when the rest of the world walks out.",
    "Friends are the siblings God never gave us.",
    "Friendship isn't about who you've known the longest, it's about who walked into your life and said 'I'm here for you'.",
    "A single rose can be my garden… a single friend, my world.",
    "Friendship is born at that moment when one person says to another, 'What! You too? I thought I was the only one.'",
    "There is nothing on this earth more to be prized than true friendship.",
    "Good friends are like stars. You don't always see them, but you know they're always there.",
    "A friend is someone who knows all about you and still loves you."
]

success_quotes = [
    "Success is not in what you have, but who you are.",
    "Don't be afraid to give up the good to go for the great.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "The road to success and the road to failure are almost exactly the same.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Don't aim for success if you want it; just do what you love and believe in, and it will come naturally.",
    "To succeed in life, you need two things: ignorance and confidence."
]

happiness_quotes = [
    "Happiness is not something ready-made. It comes from your own actions.",
    "For every minute you are angry you lose sixty seconds of happiness.",
    "Happiness depends upon ourselves.",
    "The most important thing is to enjoy your life—to be happy—it's all that matters.",
    "Happiness is a warm puppy.",
    "If you want to be happy, be.",
    "Happiness is not a goal… it's a by-product of a life well-lived.",
    "The purpose of our lives is to be happy."
]

# Enhanced color schemes with maximum contrast for all buttons
quote_colors = {
    "Motivational": {
        "light": {
            "bg": "#f5eff1",  # Blue
            "text": "#0d0d0d",  # White
            "hover": "#2980b9"  # Darker blue
        },
        "dark": {
            "bg": "#2980b9",  # Darker blue
            "text": "#090909",  # White
            "hover": "#0bcd45"  # Even darker blue
        },
        "buttons": {
            "generate": {"bg": "#3498db", "text": "#000000", "hover": "#2980b9"},
            "copy": {"bg": "#2ecc71", "text": "#000000", "hover": "#27ae60"},  # Green with black text
            "speak": {"bg": "#e67e22", "text": "#000000", "hover": "#d35400"},  # Orange with black text
            "favorites": {"bg": "#e74c3c", "text": "#000000", "hover": "#c0392b"},  # Red with white text
            "view_favorites": {"bg": "#9b59b6", "text": "#0C0101", "hover": "#8e44ad"},  # Purple with white text
            "image": {"bg": "#1abc9c", "text": "#000000", "hover": "#16a085"},  # Teal with black text
            "share": {"bg": "#34495e", "text": "#000000", "hover": "#2c3e50"},  # Dark gray with white text
            "auth": {"bg": "#95a5a6", "text": "#000000", "hover": "#7f8c8d"}  # Light gray with black text
        }
    },
    "Life": {
        "light": {
            "bg": "#9b59b6",  # Purple
            "text": "#000000",
            "hover": "#8e44ad"
        },
        "dark": {
            "bg": "#8e44ad",
            "text": "#000000",
            "hover": "#6c3483"
        },
        "buttons": {
            "generate": {"bg": "#9b59b6", "text": "#000000", "hover": "#8e44ad"},
            "copy": {"bg": "#2ecc71", "text": "#000000", "hover": "#27ae60"},
            "speak": {"bg": "#e67e22", "text": "#000000", "hover": "#d35400"},
            "favorites": {"bg": "#e74c3c", "text": "#000000", "hover": "#c0392b"},
            "view_favorites": {"bg": "#3498db", "text": "#000000", "hover": "#2980b9"},
            "image": {"bg": "#1abc9c", "text": "#000000", "hover": "#16a085"},
            "share": {"bg": "#34495e", "text": "#000000", "hover": "#2c3e50"},
            "auth": {"bg": "#95a5a6", "text": "#000000", "hover": "#7f8c8d"}
        }
    },
    "Love": {
        "light": {
            "bg": "#e74c3c",  # Red
            "text": "#000000",
            "hover": "#c0392b"
        },
        "dark": {
            "bg": "#c0392b",
            "text": "#000000",
            "hover": "#922b21"
        },
        "buttons": {
            "generate": {"bg": "#FE2C15", "text": "#000000", "hover": "#c0392b"},
            "copy": {"bg": "#13F170", "text": "#000000", "hover": "#27ae60"},
            "speak": {"bg": "#e67e22", "text": "#000000", "hover": "#d35400"},
            "favorites": {"bg": "#9b59b6", "text": "#0b0b0b", "hover": "#8e44ad"},
            "view_favorites": {"bg": "#3498db", "text": "#060000", "hover": "#2980b9"},
            "image": {"bg": "#1abc9c", "text": "#000000", "hover": "#16a085"},
            "share": {"bg": "#34495e", "text": "#030303", "hover": "#2c3e50"},
            "auth": {"bg": "#95a5a6", "text": "#000000", "hover": "#7f8c8d"}
        }
    },
    "Friendship": {
        "light": {
            "bg": "#1abc9c",  # Teal
            "text": "#000000",  # Black for better contrast
            "hover": "#16a085"
        },
        "dark": {
            "bg": "#16a085",
            "text": "#0b0b0b",  # White in dark mode
            "hover": "#117a65"
        },
        "buttons": {
            "generate": {"bg": "#1abc9c", "text": "#000000", "hover": "#16a085"},
            "copy": {"bg": "#2ecc71", "text": "#000000", "hover": "#27ae60"},
            "speak": {"bg": "#e67e22", "text": "#000000", "hover": "#d35400"},
            "favorites": {"bg": "#e74c3c", "text": "#000000", "hover": "#c0392b"},
            "view_favorites": {"bg": "#9b59b6", "text": "#000000", "hover": "#8e44ad"},
            "image": {"bg": "#3498db", "text": "#090707", "hover": "#2980b9"},
            "share": {"bg": "#34495e", "text": "#030101", "hover": "#2c3e50"},
            "auth": {"bg": "#95a5a6", "text": "#000000", "hover": "#7f8c8d"}
        }
    },
    "Success": {
        "light": {
            "bg": "#f39c12",  # Orange
            "text": "#000000",  # Black for better contrast
            "hover": "#e67e22"
        },
        "dark": {
            "bg": "#e67e22",
            "text": "#090909",  # White in dark mode
            "hover": "#d35400"
        },
        "buttons": {
            "generate": {"bg": "#f39c12", "text": "#000000", "hover": "#e67e22"},
            "copy": {"bg": "#2ecc71", "text": "#000000", "hover": "#27ae60"},
            "speak": {"bg": "#9b59b6", "text": "#040303", "hover": "#8e44ad"},
            "favorites": {"bg": "#e74c3c", "text": "#070707", "hover": "#c0392b"},
            "view_favorites": {"bg": "#3498db", "text": "#040404", "hover": "#2980b9"},
            "image": {"bg": "#1abc9c", "text": "#000000", "hover": "#16a085"},
            "share": {"bg": "#34495e", "text": "#070606", "hover": "#2c3e50"},
            "auth": {"bg": "#16d51a", "text": "#000000", "hover": "#b7b3b4"}
        }
    },
    "Happiness": {
        "light": {
            "bg": "#2ecc71",  # Green
            "text": "#000000",  # Black for better contrast
            "hover": "#27ae60"
        },
        "dark": {
            "bg": "#27ae60",
            "text": "#060606",  # White in dark mode
            "hover": "#219653"
        },
        "buttons": {
            "generate": {"bg": "#2ecc71", "text": "#000000", "hover": "#27ae60"},
            "copy": {"bg": "#3498db", "text": "#060505", "hover": "#2980b9"},
            "speak": {"bg": "#e67e22", "text": "#000000", "hover": "#d35400"},
            "favorites": {"bg": "#e74c3c", "text": "#030303", "hover": "#c0392b"},
            "view_favorites": {"bg": "#9b59b6", "text": "#080808", "hover": "#8e44ad"},
            "image": {"bg": "#1abc9c", "text": "#000000", "hover": "#16a085"},
            "share": {"bg": "#34495e", "text": "#050505", "hover": "#2c3e50"},
            "auth": {"bg": "#95a5a6", "text": "#000000", "hover": "#7f8c8d"}
        }
    }
}

# ------------------ DATA HANDLERS ------------------ #
def save_data(data, filename="users_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_data(filename="users_data.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}

# ------------------ MAIN CLASS ------------------ #
class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Modern Quote Generator ✨")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # Initialize theme and category_var first
        self.theme = "dark"
        self.category_var = tk.StringVar(value="Motivational")
        
        # Initialize style before creating widgets
        self.style = ttk.Style()
        self.configure_styles()
        
        self.users_data = load_data()
        self.logged_in_user = None
        self.favorite_quotes = []
        self.engine = pyttsx3.init()
        
        # Create widgets
        self.create_widgets()
        self.display_quote()
        self.schedule_daily_notification()
        
        # Bind theme change to category change for dynamic color updates
        self.category_var.trace_add("write", self.update_theme_colors)

    def configure_styles(self):
        # Configure main styles
        self.style.configure("TFrame", background=self.get_bg_color())
        self.style.configure("TLabel", background=self.get_bg_color(), 
                           font=("Helvetica", 12))
        
        # Configure button styles with better padding and font
        self.style.configure("TButton", 
                            font=("Helvetica", 12, "bold"), 
                            padding=10, 
                            borderwidth=0,
                            relief="raised",
                            focuscolor=self.get_bg_color())  # Remove focus highlight
        
        # Configure custom styles
        self.style.configure("Title.TLabel", 
                           font=("Helvetica", 24, "bold"),
                           foreground=self.get_fg_color())
        
        self.style.configure("Quote.TLabel", 
                           font=("Georgia", 24, "italic"),
                           wraplength=700,
                           justify="center",
                           padding=20,
                           foreground=self.get_fg_color())
        
        # Configure individual button styles
        self.configure_button_styles()
        
        # Enhanced OptionMenu styling
        self.style.configure("TMenubutton", 
                           font=("Helvetica", 14, "bold"),  # Bold font for better readability
                           padding=10,
                           relief="raised",
                           background=self.get_button_color(),
                           foreground=self.get_button_text_color(),
                           arrowcolor=self.get_button_text_color(),
                           bordercolor=self.get_button_color(),
                           highlightthickness=0,
                           highlightbackground=self.get_button_color(),
                           highlightcolor=self.get_button_color())
        
        self.style.map("TMenubutton",
                      background=[("active", self.get_button_hover_color()),
                                 ("!active", self.get_button_color())],
                      foreground=[("active", self.get_button_text_color()),
                                 ("!active", self.get_button_text_color())],
                      relief=[("pressed", "sunken"), ("!pressed", "raised")],
                      bordercolor=[("active", self.get_button_hover_color()),
                                  ("!active", self.get_button_color())])
        
        # Configure menu style (dropdown items)
        self.style.configure("TMenu",
                           font=("Helvetica", 12, "bold"),  # Bold font for dropdown items
                           background=self.get_bg_color(),
                           foreground=self.get_fg_color(),
                           activebackground=self.get_button_color(),
                           activeforeground=self.get_button_text_color(),
                           borderwidth=0,
                           relief="flat")
        
        # Configure scrollbar style
        self.style.configure("Vertical.TScrollbar", 
                           gripcount=0,
                           background="#25d1da",
                           darkcolor="#160303",
                           lightcolor="#7aa7b8",
                           troughcolor=self.get_bg_color(),
                           bordercolor=self.get_bg_color(),
                           arrowcolor="#981cdb")

    def configure_button_styles(self):
        """Configure styles for all individual buttons with maximum contrast"""
        category = self.category_var.get()
        btn_colors = quote_colors[category]["buttons"]
        
        # Base button style with better padding and rounded corners
        self.style.configure("TButton",
                           padding={'left': 20, 'right': 20, 'top': 10, 'bottom': 10},
                           relief="raised",
                           borderwidth=2,
                           focusthickness=0,
                           focuscolor=self.get_bg_color(),
                           font=("Helvetica", 12, "bold"))  # Bold and slightly larger font
        
        # Generate button style - Now with high contrast like Copy button
        self.style.configure("Generate.TButton",
                           foreground=btn_colors["generate"]["text"],
                           background=btn_colors["generate"]["bg"],
                           font=("Helvetica", 12, "bold"),
                           padding={'left': 20, 'right': 20, 'top': 10, 'bottom': 10})
        self.style.map("Generate.TButton",
                      background=[("active", btn_colors["generate"]["hover"]), 
                                 ("!active", btn_colors["generate"]["bg"])],
                      foreground=[("active", btn_colors["generate"]["text"]),
                                 ("!active", btn_colors["generate"]["text"])],
                      relief=[("pressed", "sunken"), ("!pressed", "raised")])
        
        # Copy button style - High contrast maintained
        self.style.configure("Copy.TButton",
                           foreground=btn_colors["copy"]["text"],
                           background=btn_colors["copy"]["bg"],
                           font=("Helvetica", 12, "bold"),
                           padding={'left': 20, 'right': 20, 'top': 10, 'bottom': 10})
        self.style.map("Copy.TButton",
                      background=[("active", btn_colors["copy"]["hover"]), 
                                 ("!active", btn_colors["copy"]["bg"])],
                      foreground=[("active", btn_colors["copy"]["text"]),
                                 ("!active", btn_colors["copy"]["text"])],
                      relief=[("pressed", "sunken"), ("!pressed", "raised")])
        
        # Speak button style - Enhanced contrast like Copy
        self.style.configure("Speak.TButton",
                           foreground=btn_colors["speak"]["text"],
                           background=btn_colors["speak"]["bg"],
                           font=("Helvetica", 12, "bold"),
                           padding={'left': 20, 'right': 20, 'top': 10, 'bottom': 10})
        self.style.map("Speak.TButton",
                      background=[("active", btn_colors["speak"]["hover"]), 
                                 ("!active", btn_colors["speak"]["bg"])],
                      foreground=[("active", btn_colors["speak"]["text"]),
                                 ("!active", btn_colors["speak"]["text"])],
                      relief=[("pressed", "sunken"), ("!pressed", "raised")])
        
        # Favorites button style - Enhanced contrast
        self.style.configure("Favorites.TButton",
                           foreground=btn_colors["favorites"]["text"],
                           background=btn_colors["favorites"]["bg"],
                           font=("Helvetica", 12, "bold"),
                           padding={'left': 20, 'right': 20, 'top': 10, 'bottom': 10})
        self.style.map("Favorites.TButton",
                      background=[("active", btn_colors["favorites"]["hover"]), 
                                 ("!active", btn_colors["favorites"]["bg"])],
                      foreground=[("active", btn_colors["favorites"]["text"]),
                                 ("!active", btn_colors["favorites"]["text"])],
                      relief=[("pressed", "sunken"), ("!pressed", "raised")])
        
        # View Favorites button style - Enhanced contrast
        self.style.configure("ViewFavorites.TButton",
                           foreground=btn_colors["view_favorites"]["text"],
                           background=btn_colors["view_favorites"]["bg"],
                           font=("Helvetica", 12, "bold"),
                           padding={'left': 20, 'right': 20, 'top': 10, 'bottom': 10})
        self.style.map("ViewFavorites.TButton",
                      background=[("active", btn_colors["view_favorites"]["hover"]), 
                                 ("!active", btn_colors["view_favorites"]["bg"])],
                      foreground=[("active", btn_colors["view_favorites"]["text"]),
                                 ("!active", btn_colors["view_favorites"]["text"])],
                      relief=[("pressed", "sunken"), ("!pressed", "raised")])
        
        # Image button style - Enhanced contrast like Copy
        self.style.configure("Image.TButton",
                           foreground=btn_colors["image"]["text"],
                           background=btn_colors["image"]["bg"],
                           font=("Helvetica", 12, "bold"),
                           padding={'left': 20, 'right': 20, 'top': 10, 'bottom': 10})
        self.style.map("Image.TButton",
                      background=[("active", btn_colors["image"]["hover"]), 
                                 ("!active", btn_colors["image"]["bg"])],
                      foreground=[("active", btn_colors["image"]["text"]),
                                 ("!active", btn_colors["image"]["text"])],
                      relief=[("pressed", "sunken"), ("!pressed", "raised")])
        
        # Share button style - Enhanced contrast
        self.style.configure("Share.TButton",
                           foreground=btn_colors["share"]["text"],
                           background=btn_colors["share"]["bg"],
                           font=("Helvetica", 12, "bold"),
                           padding={'left': 20, 'right': 20, 'top': 10, 'bottom': 10})
        self.style.map("Share.TButton",
                      background=[("active", btn_colors["share"]["hover"]), 
                                 ("!active", btn_colors["share"]["bg"])],
                      foreground=[("active", btn_colors["share"]["text"]),
                                 ("!active", btn_colors["share"]["text"])],
                      relief=[("pressed", "sunken"), ("!pressed", "raised")])
        
        # Auth button style - Enhanced contrast like Copy
        self.style.configure("Auth.TButton",
                           foreground=btn_colors["auth"]["text"],
                           background=btn_colors["auth"]["bg"],
                           font=("Helvetica", 12, "bold"),
                           padding={'left': 20, 'right': 20, 'top': 10, 'bottom': 10})
        self.style.map("Auth.TButton",
                      background=[("active", btn_colors["auth"]["hover"]), 
                                 ("!active", btn_colors["auth"]["bg"])],
                      foreground=[("active", btn_colors["auth"]["text"]),
                                 ("!active", btn_colors["auth"]["text"])],
                      relief=[("pressed", "sunken"), ("!pressed", "raised")])
        
        # Toggle button style (uses category color)
        self.style.configure("Toggle.TButton",
                           foreground=self.get_button_text_color(),
                           background=self.get_button_color(),
                           font=("Helvetica", 12, "bold"),
                           padding={'left': 20, 'right': 20, 'top': 10, 'bottom': 10})
        self.style.map("Toggle.TButton",
                      background=[("active", self.get_button_hover_color()), 
                                 ("!active", self.get_button_color())],
                      foreground=[("active", self.get_button_text_color()),
                                 ("!active", self.get_button_text_color())],
                      relief=[("pressed", "sunken"), ("!pressed", "raised")])

    def get_bg_color(self):
        return "#03031A" if self.theme == "light" else "#eaeff5"
    
    def get_fg_color(self):
        return "#d3dbe2" if self.theme == "light" else "#0b0b0b"
    
    def get_button_color(self):
        category = self.category_var.get()
        return quote_colors[category]["light"]["bg"] if self.theme == "light" else quote_colors[category]["dark"]["bg"]
    
    def get_button_text_color(self):
        category = self.category_var.get()
        return quote_colors[category]["light"]["text"] if self.theme == "light" else quote_colors[category]["dark"]["text"]
    
    def get_button_hover_color(self):
        category = self.category_var.get()
        return quote_colors[category]["light"]["hover"] if self.theme == "light" else quote_colors[category]["dark"]["hover"]
    
    def darken_color(self, hex_color, amount):
        """Darken a hex color by the specified amount (0-100)"""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        rgb = tuple(max(0, min(255, int(channel * (1 - amount/100)))) for channel in rgb)
        return "#{:02x}{:02x}{:02x}".format(*rgb)
    
    def lighten_color(self, hex_color, amount):
        """Lighten a hex color by the specified amount (0-100)"""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        rgb = tuple(max(0, min(255, int(channel + (255 - channel) * amount/100))) for channel in rgb)
        return "#{:02x}{:02x}{:02x}".format(*rgb)
    
    def update_theme_colors(self, *args):
        """Update all colors based on current theme and category"""
        # Update background colors
        bg_color = self.get_bg_color()
        fg_color = self.get_fg_color()
        
        self.root.configure(bg=bg_color)
        self.style.configure(".", background=bg_color, foreground=fg_color)
        self.style.configure("TFrame", background=bg_color)
        self.style.configure("TLabel", background=bg_color, foreground=fg_color)
        self.style.configure("Title.TLabel", foreground=fg_color)
        self.style.configure("Quote.TLabel", foreground=fg_color)
        
        # Update quote frame border color
        border_color = self.get_button_color()
        self.quote_frame.configure(style="Quote.TFrame")
        self.style.configure("Quote.TFrame", 
                           background=bg_color, 
                           bordercolor=border_color,
                           relief="solid",
                           borderwidth=2)
        
        # Update all button styles
        self.configure_button_styles()
        
        # Update status bar
        self.status_bar.configure(background=bg_color, foreground=fg_color)
        
        # Update option menu with enhanced styling
        btn_color = self.get_button_color()
        btn_text_color = self.get_button_text_color()
        hover_color = self.get_button_hover_color()
        
        self.style.configure("TMenubutton", 
                           background=btn_color,
                           foreground=btn_text_color,
                           arrowcolor=btn_text_color,
                           bordercolor=btn_color,
                           highlightthickness=0)
        self.style.map("TMenubutton",
                      background=[("active", hover_color),
                                 ("!active", btn_color)],
                      foreground=[("active", btn_text_color),
                                 ("!active", btn_text_color)],
                      bordercolor=[("active", hover_color),
                                  ("!active", btn_color)])
        
        # Update menu style
        self.style.configure("TMenu",
                           background=bg_color,
                           foreground=fg_color,
                           activebackground=btn_color,
                           activeforeground=btn_text_color,
                           borderwidth=0)
        
        # Update toggle button text
        self.toggle_button.config(text="🌙 Dark Mode" if self.theme == "light" else "☀️ Light Mode")

    def display_quote(self):
        category = self.category_var.get()
        quotes = {
            "Motivational": motivational_quotes,
            "Life": life_quotes,
            "Love": love_quotes,
            "Friendship": friendship_quotes,
            "Success": success_quotes,
            "Happiness": happiness_quotes
        }
        quote = random.choice(quotes.get(category, motivational_quotes))
        self.quote_label.config(text=quote)
        
        # Update status
        self.status_var.set(f"Displayed new {category} quote")
        
        # Update colors based on new category
        self.update_theme_colors()

    def create_widgets(self):
        # Main container frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        
        # Header frame
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill="x", pady=(0, 20))
        
        # Title label
        self.title_label = ttk.Label(self.header_frame, 
                                   text="✨ Modern Quote Generator ✨",
                                   style="Title.TLabel")
        self.title_label.pack(side="left")
        
        # Theme toggle button
        self.toggle_button = ttk.Button(self.header_frame, 
                                      text="🌙 Dark Mode" if self.theme == "light" else "☀️ Light Mode",
                                      command=self.toggle_theme,
                                      style="Toggle.TButton")
        self.toggle_button.pack(side="right")
        
        # Quote display frame with enhanced border
        self.quote_frame = ttk.Frame(self.main_frame, 
                                   style="Quote.TFrame",
                                   relief="solid",
                                   borderwidth=2)
        self.quote_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        # Quote label with action indicators
        self.quote_label = ttk.Label(self.quote_frame, 
                                   text="",
                                   style="Quote.TLabel")
        self.quote_label.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Action indicator label below the quote
        self.action_indicator = ttk.Label(self.quote_frame,
                                        text="",
                                        font=("Helvetica", 12),
                                        foreground="#F6F6F6")
        self.action_indicator.pack(side="bottom", pady=(0, 10))
        
        # Controls frame
        self.controls_frame = ttk.Frame(self.main_frame)
        self.controls_frame.pack(fill="x", pady=(0, 20))
        
        # Category selection with enhanced OptionMenu
        self.category_label = ttk.Label(self.controls_frame, text="Category:")
        self.category_label.pack(side="left", padx=(0, 10))
        
        self.category_menu = ttk.OptionMenu(
            self.controls_frame, 
            self.category_var, 
            "Motivational",
            *["Motivational", "Life", "Love", "Friendship", "Success", "Happiness"],
            style="TMenubutton"
        )
        self.category_menu.pack(side="left", fill="x", expand=True)
        
        # Buttons frame
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.pack(fill="x")
        
        # First row of buttons
        self.button_row1 = ttk.Frame(self.buttons_frame)
        self.button_row1.pack(fill="x", pady=(0, 10))
        
        self.generate_button = ttk.Button(self.button_row1, 
                                       text="Generate Quote", 
                                       command=self.generate_quote_with_feedback,
                                       style="Generate.TButton")
        self.generate_button.pack(side="left", expand=True, fill="x", padx=5)
        
        self.copy_button = ttk.Button(self.button_row1, 
                                    text="Copy", 
                                    command=self.copy_quote_with_feedback,
                                    style="Copy.TButton")
        self.copy_button.pack(side="left", expand=True, fill="x", padx=5)
        
        self.speak_button = ttk.Button(self.button_row1, 
                                     text="Speak", 
                                     command=self.speak_quote_with_feedback,
                                     style="Speak.TButton")
        self.speak_button.pack(side="left", expand=True, fill="x", padx=5)
        
        # Second row of buttons
        self.button_row2 = ttk.Frame(self.buttons_frame)
        self.button_row2.pack(fill="x", pady=(0, 10))
        
        self.favorites_button = ttk.Button(self.button_row2, 
                                         text="Save to Favorites", 
                                         command=self.save_to_favorites_with_feedback,
                                         style="Favorites.TButton")
        self.favorites_button.pack(side="left", expand=True, fill="x", padx=5)
        

        self.view_favorites_button = ttk.Button(self.button_row2, 
                                              text="View Favorites", 
                                              command=self.view_favorites_with_feedback,
                                              style="ViewFavorites.TButton")
        self.view_favorites_button.pack(side="left", expand=True, fill="x", padx=5)
        
        # Third row of buttons
        self.button_row3 = ttk.Frame(self.buttons_frame)
        self.button_row3.pack(fill="x", pady=(0, 10))
        
        self.image_button = ttk.Button(self.button_row3, 
                                     text="Save as Image", 
                                     command=self.save_quote_as_image_with_feedback,
                                     style="Image.TButton")
        self.image_button.pack(side="left", expand=True, fill="x", padx=5)
        
        self.share_button = ttk.Button(self.button_row3, 
                                     text="Share Quote", 
                                     command=self.share_quote_with_feedback,
                                     style="Share.TButton")
        self.share_button.pack(side="left", expand=True, fill="x", padx=5)
        
        # Login/register buttons
        self.auth_frame = ttk.Frame(self.main_frame)
        self.auth_frame.pack(fill="x", pady=(20, 0))
        
        self.login_button = ttk.Button(self.auth_frame, 
                                    text="Login", 
                                    command=self.show_login,
                                    style="Auth.TButton")
        self.login_button.pack(side="left", expand=True, fill="x", padx=5)
        
        self.register_button = ttk.Button(self.auth_frame, 
                                       text="Register", 
                                       command=self.show_register,
                                       style="Auth.TButton")
        self.register_button.pack(side="left", expand=True, fill="x", padx=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.main_frame, 
                                  textvariable=self.status_var,
                                  relief="sunken",
                                  anchor="center")
        self.status_bar.pack(fill="x", pady=(10, 0))
        
        # Update colors based on initial theme
        self.update_theme_colors()

    # Enhanced button functions with visual feedback in the quote area
    def generate_quote_with_feedback(self):
        self.action_indicator.config(text="Generating new quote...")
        self.root.update()
        self.display_quote()
        self.action_indicator.config(text="New quote generated!")
        self.root.after(2000, lambda: self.action_indicator.config(text=""))

    def copy_quote_with_feedback(self):
        quote = self.quote_label.cget("text")
        self.action_indicator.config(text="Copying to clipboard...")
        self.root.update()
        pyperclip.copy(quote)
        self.action_indicator.config(text="Quote copied to clipboard!")
        self.root.after(2000, lambda: self.action_indicator.config(text=""))
        self.status_var.set("Quote copied to clipboard!")

    def speak_quote_with_feedback(self):
        quote = self.quote_label.cget("text")

        if not quote:
            return

        self.action_indicator.config(text="Speaking quote...")
        self.status_var.set("Speaking quote...")

        self.speak_external(quote)

        self.root.after(2000, lambda: self.action_indicator.config(text=""))



    def save_to_favorites_with_feedback(self):
        quote = self.quote_label.cget("text")
        self.action_indicator.config(text="Saving to favorites...")
        self.root.update()
        self.save_to_favorites()
        self.action_indicator.config(text="Saved to favorites!")
        self.root.after(2000, lambda: self.action_indicator.config(text=""))

    def view_favorites_with_feedback(self):
        self.action_indicator.config(text="Loading favorites...")
        self.root.update()
        self.view_favorites()
        self.action_indicator.config(text="Favorites displayed!")
        self.root.after(2000, lambda: self.action_indicator.config(text=""))

    def save_quote_as_image_with_feedback(self):
        self.action_indicator.config(text="Creating image...")
        self.root.update()
        self.save_quote_as_image()
        self.action_indicator.config(text="Image saved!")
        self.root.after(2000, lambda: self.action_indicator.config(text=""))

    def share_quote_with_feedback(self):
        self.action_indicator.config(text="Preparing to share...")
        self.root.update()
        self.share_quote()
        self.action_indicator.config(text="Share options ready!")
        self.root.after(2000, lambda: self.action_indicator.config(text=""))

    def copy_quote(self):
        quote = self.quote_label.cget("text")
        pyperclip.copy(quote)
        self.status_var.set("Quote copied to clipboard!")
        messagebox.showinfo("Copied", "Quote copied to clipboard!")

    def speak_in_thread(self, quote):
        try:
            engine = pyttsx3.init()   # ✅ NEW engine every time
            engine.say(quote)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print("Speech Error:", e)
        
    def speak_external(self, text):
        subprocess.Popen(
        [sys.executable, "-c",
        f"import pyttsx3; e=pyttsx3.init(); e.say({text!r}); e.runAndWait()"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        )


    def save_to_favorites(self):
        quote = self.quote_label.cget("text")
        if self.logged_in_user:
            if quote not in self.users_data[self.logged_in_user].get("favorites", []):
                self.users_data[self.logged_in_user].setdefault("favorites", []).append(quote)
                save_data(self.users_data)
                self.status_var.set("Quote added to favorites!")
                messagebox.showinfo("Saved", "Quote added to favorites!")
            else:
                self.status_var.set("Quote already in favorites")
                messagebox.showwarning("Exists", "Quote already in favorites!")
        else:
            self.status_var.set("Login required to save favorites")
            messagebox.showwarning("Login Required", "Please login to save favorites.")

    def view_favorites(self):
        if self.logged_in_user:
            favs = self.users_data[self.logged_in_user].get("favorites", [])
            if favs:
                window = tk.Toplevel(self.root)
                window.title("Your Favorite Quotes")
                window.geometry("800x600")
                
                # Create scrollable frame
                canvas = tk.Canvas(window, bg=self.get_bg_color())
                scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
                scrollable_frame = ttk.Frame(canvas)
                
                scrollable_frame.bind(
                    "<Configure>",
                    lambda e: canvas.configure(
                        scrollregion=canvas.bbox("all")
                    )
                )
                
                canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                canvas.configure(yscrollcommand=scrollbar.set)
                
                # Add quotes
                for i, quote in enumerate(favs):
                    frame = ttk.Frame(scrollable_frame, padding=10)
                    frame.pack(fill="x", pady=5, padx=10)
                    
                    # Quote number
                    ttk.Label(frame, text=f"{i+1}.", font=("Helvetica", 12, "bold")).pack(side="left")
                    
                    # Quote text
                    ttk.Label(frame, text=quote, wraplength=600, font=("Georgia", 14)).pack(side="left", padx=10)
                    
                    # Delete button
                    ttk.Button(frame, text="❌", 
                              command=lambda q=quote: self.delete_favorite(q, window),
                              style="Favorites.TButton").pack(side="right")
                
                canvas.pack(side="left", fill="both", expand=True)
                scrollbar.pack(side="right", fill="y")
                
                self.status_var.set(f"Displaying {len(favs)} favorite quotes")
            else:
                self.status_var.set("No favorite quotes found")
                messagebox.showinfo("No Favorites", "You have no favorite quotes.")
        else:
            self.status_var.set("Login required to view favorites")
            messagebox.showwarning("Login Required", "Please login to view favorites.")
    
    def delete_favorite(self, quote, window):
        if self.logged_in_user and quote in self.users_data[self.logged_in_user].get("favorites", []):
            self.users_data[self.logged_in_user]["favorites"].remove(quote)
            save_data(self.users_data)
            self.status_var.set(f"Removed quote from favorites")
            messagebox.showinfo("Removed", "Quote removed from favorites")
            window.destroy()
            self.view_favorites()  # Refresh the favorites window

    def save_quote_as_image(self):
        quote = self.quote_label.cget("text")
        category = self.category_var.get()
        colors = quote_colors[category]
        
        # Create image with gradient background
        width, height = 1000, 500
        img = Image.new("RGB", (width, height), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        # Draw gradient background
        for i in range(height):
            r = int(int(colors["light"]["bg"][1:3], 16) * (height - i) / height + 
                 int(colors["dark"]["bg"][1:3], 16) * i / height)
            g = int(int(colors["light"]["bg"][3:5], 16) * (height - i) / height + 
                 int(colors["dark"]["bg"][3:5], 16) * i / height)
            b = int(int(colors["light"]["bg"][5:7], 16) * (height - i) / height + 
                 int(colors["dark"]["bg"][5:7], 16) * i / height)
            draw.line([(0, i), (width, i)], fill=(r, g, b))
        
        # Add quote text
        try:
            font = ImageFont.truetype("arial.ttf", 32)
        except:
            font = ImageFont.load_default()
        
        # Calculate text size and position
        lines = []
        line = ""
        for word in quote.split():
            test_line = line + word + " "
            if draw.textlength(test_line, font=font) <= width - 100:
                line = test_line
            else:
                lines.append(line)
                line = word + " "
        if line:
            lines.append(line)
        
        text_height = len(lines) * 40
        y = (height - text_height) // 2
        
        for line in lines:
            text_width = draw.textlength(line, font=font)
            x = (width - text_width) // 2
            draw.text((x, y), line, font=font, fill="#896a6a")
            y += 40
        
        # Add category and app name at bottom
        small_font = ImageFont.truetype("arial.ttf", 16) if font != ImageFont.load_default() else font
        draw.text((20, height - 40), f"Category: {category}", font=small_font, fill="#ffffff")
        draw.text((width - 200, height - 40), "Modern Quote Generator", font=small_font, fill="#ffffff")
        
        # Save image
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"quote_{category.lower()}_{timestamp}.png"
        img.save(filename)
        
        self.status_var.set(f"Quote saved as image: {filename}")
        messagebox.showinfo("Saved", f"Quote saved as image: {filename}")

  
    def share_quote(self):
        quote = self.quote_label.cget("text")
        category = self.category_var.get()

        share_text = f"{quote}\n\n— {category} quote from Modern Quote Generator"
        pyperclip.copy(share_text)

        encoded_text = urllib.parse.quote(share_text)

        twitter_url = f"https://twitter.com/intent/tweet?text={encoded_text}"
        webbrowser.open(twitter_url)

        self.status_var.set("Quote copied! Share on Twitter.")
        messagebox.showinfo(
            "Share Quote",
            "Quote copied to clipboard!\n\n"
            "Twitter: Browser opened\n"
        )


    def toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self.update_theme_colors()
        self.status_var.set(f"Switched to {self.theme} mode")

    def show_login(self):
        win = tk.Toplevel(self.root)
        win.title("Login")
        win.geometry("400x300")
        win.resizable(False, False)
        
        # Center the window
        self.center_window(win)
        
        # Main frame
        main_frame = ttk.Frame(win, padding=20)
        main_frame.pack(fill="both", expand=True)
        
        # Title
        ttk.Label(main_frame, text="Login", font=("Helvetica", 18, "bold")).pack(pady=10)
        
        # Username
        ttk.Label(main_frame, text="Username:").pack(pady=(10, 0))
        user_entry = ttk.Entry(main_frame)
        user_entry.pack(fill="x", pady=5)
        
        # Password
        ttk.Label(main_frame, text="Password:").pack(pady=(10, 0))
        pass_entry = ttk.Entry(main_frame, show="*")
        pass_entry.pack(fill="x", pady=5)
        
        # Login button
        login_button = ttk.Button(main_frame, text="Login", 
                                command=lambda: self.login_action(user_entry.get(), pass_entry.get(), win),
                                style="Auth.TButton")
        login_button.pack(pady=20, fill="x")
        
        # Focus on username field
        user_entry.focus_set()

    def login_action(self, username, password, window):
        if username in self.users_data and self.users_data[username]["password"] == password:
            self.logged_in_user = username
            self.status_var.set(f"Welcome back, {username}!")
            messagebox.showinfo("Welcome", f"Welcome back, {username}!")
            window.destroy()
            
            # Update UI to show logged in state
            self.login_button.config(text="Logout", command=self.logout)
            self.register_button.config(state="disabled")
        else:
            self.status_var.set("Login failed - invalid credentials")
            messagebox.showerror("Error", "Invalid credentials")

    def logout(self):
        self.logged_in_user = None
        self.status_var.set("Logged out successfully")
        self.login_button.config(text="Login", command=self.show_login)
        self.register_button.config(state="normal")

    def show_register(self):
        win = tk.Toplevel(self.root)
        win.title("Register")
        win.geometry("400x350")  # Slightly increased height to accommodate the button
        win.resizable(False, False)
        
        # Center the window
        self.center_window(win)
        
        # Main frame
        main_frame = ttk.Frame(win, padding=20)
        main_frame.pack(fill="both", expand=True)
        
        # Title
        ttk.Label(main_frame, text="Register", font=("Helvetica", 18, "bold")).pack(pady=10)
        
        # Username frame
        user_frame = ttk.Frame(main_frame)
        user_frame.pack(fill="x", pady=5)
        ttk.Label(user_frame, text="Username:").pack(side="left", padx=(0, 10))
        user_entry = ttk.Entry(user_frame)
        user_entry.pack(side="right", expand=True, fill="x")
        
        # Password frame
        pass_frame = ttk.Frame(main_frame)
        pass_frame.pack(fill="x", pady=5)
        ttk.Label(pass_frame, text="Password:").pack(side="left", padx=(0, 10))
        pass_entry = ttk.Entry(pass_frame, show="*")
        pass_entry.pack(side="right", expand=True, fill="x")
        
        # Confirm Password frame
        confirm_frame = ttk.Frame(main_frame)
        confirm_frame.pack(fill="x", pady=5)
        ttk.Label(confirm_frame, text="Confirm Password:").pack(side="left", padx=(0, 10))
        confirm_pass_entry = ttk.Entry(confirm_frame, show="*")
        confirm_pass_entry.pack(side="right", expand=True, fill="x")
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=(20, 0))
        
        # Register button - now properly styled and visible
        register_button = ttk.Button(button_frame, 
                                   text="Register", 
                                   command=lambda: self.register_action(
                                       user_entry.get(), 
                                       pass_entry.get(), 
                                       confirm_pass_entry.get(), 
                                       win),
                                   style="Auth.TButton")
        register_button.pack(fill="x", pady=10)
        
        # Focus on username field
        user_entry.focus_set()

    def register_action(self, username, password, confirm_password, window):
        if not username or not password:
            self.status_var.set("Registration failed - empty fields")
            messagebox.showerror("Error", "Username and password cannot be empty")
            return
            
        if password != confirm_password:
            self.status_var.set("Registration failed - passwords don't match")
            messagebox.showerror("Error", "Passwords don't match")
            return
            
        if username not in self.users_data:
            self.users_data[username] = {"password": password, "favorites": []}
            save_data(self.users_data)
            self.status_var.set(f"Account created for {username}")
            messagebox.showinfo("Success", "Account created successfully!")
            
            # Automatically log in the new user
            self.logged_in_user = username
            self.login_button.config(text="Logout", command=self.logout)
            self.register_button.config(state="disabled")
            
            window.destroy()
        else:
            self.status_var.set("Registration failed - username exists")
            messagebox.showerror("Exists", "Username already exists")

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def schedule_daily_notification(self, notify_time="09:00"):
        def notifier():
            while True:
                now = datetime.now().strftime("%H:%M")
                if now == notify_time:
                    self.display_quote()
                    messagebox.showinfo("Quote of the Day", self.quote_label.cget("text"))
                    time.sleep(60)
                time.sleep(10)

        thread = threading.Thread(target=notifier, daemon=True)
        thread.start()

# ------------------ RUN APP ------------------ #
if __name__ == "__main__":
    root = tk.Tk()
    
    # Set window icon (optional)
    try:
        root.iconbitmap("quote_icon.ico")  # Provide this file in the same directory
    except:
        pass
    
    app = QuoteApp(root)
    root.mainloop()