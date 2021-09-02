import tkinter as tk
import random
import pyttsx3 as ts
from genre import genre_anime
from tkinter import messagebox as mb

def new(speak):
    #create the instance for python text to speech first
    anime = random.choice(genre_anime[speak])  #let machine speak out the recommended aniime before displaying message
    engine.say(anime)
    engine.runAndWait()
    return anime

def recommend(genre_recommend):
    watched = True
    #check if the user as watched the given anime, if he as watched, display next anime and continue
    while watched:
        anime = new(genre_recommend)
        answer = mb.askquestion("Recommendation","{}\nHave you watched it?".format(anime))
        if answer.lower().startswith('y'):
            continue
        else:
            #user didn't watch the anime, so display another message to tell him to watch
            mb.showinfo("To Watch","You Need Watch it")
            watched = False

#create different function for different genre to trigger the button
def action():
    recommend("Action")

def slice():
    recommend("Slice of Life")

def shounen():
    recommend("Shounen")

def romance():
    recommend("Romance")

def crime():
    recommend("Crime")

def adventure():
    recommend("Adventure")

def fantasy():
    recommend("Fantasy")

def movies():
    recommend("Anime Movies")

def horror():
    recommend("Horror")

def comedy():
    recommend("Comedy")

def scifi():
    recommend("Sci-Fi")

def thriller():
    recommend("Thriller")

def main():
    root = tk.Tk()
    root.geometry("375x345+450+200")  #fit gui in centre of screen
    root.minsize(375,345)
    root.maxsize(375,345)
    root.title("Anime Recommendation")
    #for background and neat gui use canva
    canva = tk.Canvas(bg="tan")
    canva.place(width=455,height=455)
    choose = tk.Label(text="Choose a Genre",font=("arial",25,"bold")).place(x=60,y=5)
    foot = tk.Label(text="written by:Tarun R Jain",bg="black",fg="white").place(x=220,y=320)

    #create different button with different color and command

    action_btn = tk.Button(text="Action",font=("arial",13,"bold"),command=action,bg="red").place(x=30,y=80,width=100,height=50)
    slice_btn = tk.Button(text="Slice of Life",font=("arial",12,"bold"),command=slice,bg="green",fg="white").place(x=140,y=80,width=100,height=50)
    shounen_btn = tk.Button(text="Shounen",font=("arial",13,"bold"),command=shounen,bg="yellow").place(x=250,y=80,width=100,height=50)
    romance_btn = tk.Button(text="Romance",font=("arial",13,"bold"),command=romance,bg="deeppink").place(x=30,y=140,width=100,height=50)
    comedy_btn = tk.Button(text="Comedy",font=("arial",13,"bold"),command=comedy,bg="aqua").place(x=140,y=140,width=100,height=50)
    fantasy_btn = tk.Button(text="Fantasy",font=("arial",13,"bold"),command=fantasy,bg="black",fg="white").place(x=250,y=140,width=100,height=50)
    scifi_btn = tk.Button(text="Sci Fi",font=("arial",13,"bold"),command=scifi,bg="blue",fg="white").place(x=30,y=200,width=100,height=50)
    adventure_btn = tk.Button(text="Adventure",font=("arial",13,"bold"),command=adventure,bg="violet").place(x=140,y=200,width=100,height=50)
    thriller_btn = tk.Button(text="Mystery",font=("arial",13,"bold"),command=thriller,bg="brown",fg="white").place(x=250,y=200,width=100,height=50)
    horror_btn = tk.Button(text="Horror",font=("arial",13,"bold"),command=horror,bg="purple",fg="white").place(x=30,y=260,width=100,height=50)
    movie_btn = tk.Button(text="Anime Movie",font=("arial",12,"bold"),command=movies,bg="orange").place(x=140,y=260,width=100,height=50)
    crime_btn = tk.Button(text="Detective",font=("arial",13,"bold"),command=crime,bg="grey",fg="white").place(x=250,y=260,width=100,height=50)

    root.mainloop()

if __name__ == '__main__':
    engine = ts.init()
    main()
