# Name: Daniel Masters
# Spring 2022
# Section: 31883
# ITP 216 Homework 03

def file_reader(file_name): #created file reader function
    f_in = open(file_name, 'r')
    header = f_in.readline()    #read in the header
    data = []
    for line in f_in:       #reading the lines of data
        data.append(line)       #appending the data to a list
    f_in.close()
    return header, data     #returns both the header and rest of the data

def calculate_mean(integers):                   #calculating the mean function
    average = sum(integers) / len(integers)     #simply sum the integers and divide by length
    return average                              #return the avg

def find_movies_above_score(movies, score): #takes in movie list and score (avg score) as parameters
    list_of_movies = []
    for movie in movies:                        #loops through the movie list provided in parameter
        if movie.strip() != "":                     #accounts for the space at the end of the csv
            line = movie.strip().split(", ")        #strips whitespace and splits by commas
            if int(line[1].strip()) > score:       #if the score is greater than avg score than append the movie to list
                list_of_movies.append(line)
    return list_of_movies                        #return the list of movies

def main():
    my_file_name = "deniro.csv"                 #file name
    header, data = file_reader(my_file_name)    #using file reader returns two values
    integers = []           #integers list to append to
    for i in data:              #for each data point
        if i.strip() != "":               #to prevent error thrown from extra line at end of csv file
            line = i.strip().split(", ")    #getting all scores
            numbers = line[1].strip()
            integers.append(int(numbers))   #appending all scores to list
    mean = calculate_mean(integers)     #calculating mean
    movies_above_avg = find_movies_above_score(data, mean)  #list of movies above the avg score
    above_avg_count = len(movies_above_avg)     #num of above avg movies
    print("I love Robert Deniro!")      #print statements from assignment
    print("The average Rotten Tomatoes score for his movies is "+str(mean)+".")
    print("Of 87 movies, "+str(above_avg_count)+" are above average.")
    print("Here they are: ")
    header = header.split()     #taking whitespace out of header
    print("\t" + header[0].replace('"', "").replace(',', "") + "\t" + header[1].replace('"', "").replace(',', "") +
          "\t" + header[2].replace('"', "").replace(',', "")) #printing the header
    for movies in movies_above_avg: #printing the data, making sure to print entire title
        print("\t"+str(movies[0])+"\t"+str(movies[1].strip())+"\t\t"+str(' '.join(movies[2:]).replace('"', "")))

if __name__ == '__main__':
    main()