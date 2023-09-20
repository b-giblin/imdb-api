import tkinter as tk
from tkinter import ttk, messagebox
from imdb import IMDb

class MovieComparerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IMDb Movie Comparer")
        self.geometry("400x200")
        
        self.imdb = IMDb()
        
        ttk.Label(self, text="Original Movie:").grid(row=0, column=0, padx=10, pady=5)
        self.original_entry = ttk.Entry(self)
        self.original_entry.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(self, text="Remake Movie:").grid(row=1, column=0, padx=10, pady=5)
        self.remake_entry = ttk.Entry(self)
        self.remake_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.compare_button = ttk.Button(self, text="Compare", command=self.compare_movies)
        self.compare_button.grid(row=2, column=0, columnspan=2, pady=20)
        
    def compare_movies(self):
        original_name = self.original_entry.get()
        remake_name = self.remake_entry.get()

        if not original_name or not remake_name:
            messagebox.showwarning("Warning", "Both movie names must be filled!")
            return
        
        original_movie = self.search_movie(original_name)
        remake_movie = self.search_movie(remake_name)

        if not original_movie or not remake_movie:
            messagebox.showerror("Error", "Couldn't find one or both movies.")
            return
        
        original_score = original_movie.get('rating', "N/A")
        remake_score = remake_movie.get('rating', "N/A")

        result = f"{original_name} Rating: {original_score}\n{remake_name} Rating: {remake_score}"
        messagebox.showinfo("Comparison Result", result)

    def search_movie(self, movie_name):
        results = self.imdb.search_movie(movie_name)
        return results[0] if results else None

if __name__ == "__main__":
    app = MovieComparerApp()
    app.mainloop()