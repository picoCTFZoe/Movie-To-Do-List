#Zoe
#01/12/24
#To Do List

#Initialize
#Greets Users
movieList = []
print("Welcome to Movie List!")
print("Menu:")

movieCount = 0
#Functions
#Allows users to imput a movie, and adds it to the list
def addMovie():
    global movieCount
    movie = input("Insert Name of Movie ")
    movieList.append(movie)
    print(movie + " has been added! \n")
    movieCount = movieCount + 1

#Displays list
def viewList():
    print("Movie List:")
    print(movieList)
    print("")

#Marks a specified movie as watched
def watched():
    viewList()
    movieWatched = (input("Which movie do you want to mark as watched? "))
    i = movieList.index(movieWatched)
    movieList[i] = movieWatched + " (Watched!)"
    print(movieWatched + " has been marked as watched!\n ")

#removes a specified movie from list
def remove():
    viewList()
    global movieCount
    removeMovie = input("What movie would you like to remove? Be sure to type the whole movie, including the watched marking if present. ")
    i = movieList.index(removeMovie)
    movieList.pop(i)
    print(removeMovie + " has been removed from list!\n ")
    movieCount = movieCount - 1

#edits a specified movie
def editMovie():
    viewList()
    editMovie = input("What movie would you like to edit? Make sure to type the whole movie, including the watched marking if present. ")
    editedMovie = input("What would you like to change it to? ")
    i = movieList.index(editMovie)
    movieList[i] = editedMovie
    print(editMovie + " has been changed to " + editedMovie + "!\n ")
    
#clears the list
def clearMovies():
    global movieCount
    movieList.clear()
    print("Your list has been cleared\n ")
    movieCount = 0

#Sort the list in alphabetical order
def sortAlphabetically():
    movieList.sort()
    print("Your list has been sorted alphabetically!\n ")

#Prints the number of movies currently in list
def numOfMovies():
    global movieCount
    if movieCount == 1:
        print("There is 1 movie on your list \n")
    else:
        print("There are " + str(movieCount) + " movies on your list!\n ")

#Main
while True:
    #Options
    print("(1) Add Movie \n(2) View Movie List\n(3) Mark Movie as Watched \n(4) Remove Movie from Watched List \n(5) Edit a Movie \n(6) Clear List \n(7) Sort List Alphabetically \n(8) Display the number of items currently on the movie list \n(9) Quit \n ")
    #Input Menu
    menu = int(input("What do you want to do? "))
    if menu == 1:
        addMovie()
    elif menu == 2:
        viewList()
    elif menu == 3:
        watched()
    elif menu == 4:
        remove()
    elif menu ==5:
        editMovie()
    elif menu == 6:
        clearMovies()
    elif menu == 7:
        sortAlphabetically()
    elif menu == 8:
        numOfMovies()
    elif menu == 9:
        print("Bye Bye!")
        break
    else:
        print("Uh Oh! Invalid Number Added! Please Try Again!")

