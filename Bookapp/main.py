import tkinter as tk
from tkinter import simpledialog
from tkinter import font as tkFont  # Import the font module
from PIL import Image, ImageTk  # Correct import

#Tkinter set up
class BookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book App")
        self.root.geometry("600x400")

       
        #change the favicon
        self.root.iconbitmap("Ben.ico")

        # Create a Helvetica font
        self.helvetica_font = tkFont.Font(family="Helvetica", size=12)

        self.label = tk.Label(root, text="Your Genre Book",font=self.helvetica_font)  # Use the Helvetica font
        self.label.pack(pady=10)

        self.book_listbox = tk.Listbox(root, font=self.helvetica_font, bg="black", fg="white")  # Use the Helvetica font
        self.book_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.genres_entry = tk.Entry(root, font=self.helvetica_font,bg="black", fg="white")  # Use the Helvetica font
        self.genres_entry.pack(padx=10, pady=5, fill=tk.X)

        self.add_genres_button = tk.Button(root, text="Search genres", font=self.helvetica_font,command=self.search_genres)  # Use the Helvetica font
        self.add_genres_button.pack(padx=10, pady=5, fill=tk.X)

        # Genres and book data for each genre
        self.genre_books = {
            "Business": [
                "Rich Dad Poor Dad by Robert Kiyosaki",
                "Shoe Dog by Phil Knight",
                "The Hard Thing About Hard Things by Ben Horowitz",
                "Deep Work by Cal Newport",
                "How to Win Friends and Influence People by Dale Carnegie",
            ],
            "Sales": [
                "Inbound Selling by Brian Signorelli",
                "New Sales. Simplified. by Mike Weinberg",
                "The Sales Acceleration Formula by Mark Roberge",
                "To Sell Is Human by Daniel H. Pink",
                "Secrets of Closing the Sales by Zig Ziglar",
            ],
            "Marketing": [
                "Selling the Invisible by Harry Beckwith",
                "Positioning by Al Ries & Jack Trout",
                "The Psychology of Influence and Persuasion by Robert B. Cialdini",
                "Permission Marketing by Seth Godin",
                "The Tipping Point by Malcolm Gladwell",
            ],

            "Real estate": [
                "Real Estate Investment & Financial Analysis by Gaurav Jain",
                "What Every Real Estate Investor Needs to Know About Cash Flow by Frank Gallinelli",
                "The ABCs of Real Estate Investing by Ken McElroy",
                "Long-distance Real Estate Investing by David Greene",
                "How a Second Home can be your Best Investment by Tom Kelly"
            ],

            "Fitness": [
                "Bigger Leaner Stronger by Michael Matthews",
                "The 4-Hour Body by Timothy Ferriss",
                "Born to Run by Christopher McDougall",
                "Starting Strength by Mark Rippetoe",
            "StrongLifts 5x5 by Mehdi Hadim"

            ],

            "Farming": [
                "The Market Gardener: by Jean-Martin Fortier",
                "The Lean Farm:  by Ben Hartman",
                "The New Organic Grower, 3rd Edition:by Eliot Coleman",
                "You Can Farm:  by Joel Salatin",
                "Farm Anatomy: by Julia Rothman"

            ],

            

        }
        

    def search_genres(self):
        user_genre = self.genres_entry.get().strip()
        if user_genre in self.genre_books:
            books = self.genre_books[user_genre]
            self.update_listbox(books)
        else:
            self.update_listbox([])

    def update_listbox(self, books):
        self.book_listbox.delete(0, tk.END)
        for book in books:
            self.book_listbox.insert(tk.END, book)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()


