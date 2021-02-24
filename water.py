# this is the welcome message to the user
greeting = "Hello Welcome to the shower spendage calculator program "

# this is where the welcome message is shown to the user
print(greeting)

# in this line the program will ask the user to input their name
name = str(input('May I take your name please?\n'))

# in this line it will ask the user to input their time spent in the shower in minutes
showertime = int(input('How much time did you spent in the shower (input your answer in minutes)? \n'))

# in this line the program will make the necessary calculations to give the user the results
results = showertime * 10

# in this line the program will show the results to the user
print(name + ' you have spent', results, 'litres in the shower')
