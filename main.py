from website import create_app 
# website is python patckge so can call anything from init.py file

app = create_app()

# to run web server
if __name__ == "__main__": # if main is run then app.run will be executed
    app.run(debug=True) # automatcially rerun webserver if files are edited