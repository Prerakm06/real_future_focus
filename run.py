from flask import Flask, render_template

app = Flask(__name__,template_folder='templates')

@app.route("/")
@app.route("/home")
def home():
    return render_template('startup.html', title='Future Focus')

@app.route("/unlock_insights")
def unlock_insights():
    return render_template('unlock_insights.html', title='Unlock Insights')

@app.route("/testimonials")
def testimonials():
    testimonials_list=[
    {'name': 'Ms. Smith', 'pfp_url': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'quote': 'An exceptional student with a passion for innovation.','role':"Alloa Principal"},
    {'name': 'Mr. Johnson', 'pfp_url': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'quote': 'A dedicated learner who excels in problem-solving.','role':"Fletcher's Meadow Principal"},
    {'name': 'Ms. Smith', 'pfp_url': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'quote': 'An exceptional student with a passion for innovation.','role':"Alloa Principal"},
    ]
    return render_template('testimonials.html', title='Testimonials', testimonials_list=testimonials_list)


@app.route("/about_us")
def about_us():
    
    return render_template('about_us.html')


@app.route("/schools_visited")
def schools_visited():
    schools = [
        {'name': 'Alloa Public School', 'image_url': 'https://alloa.peelschools.org/images/324ee78d-1cae-41b4-b138-ad8c416cd763'},
        {'name': 'Cheyne Middle School', 'image_url': 'https://cheyne.peelschools.org/images/2c4d75c1-6919-421e-b9db-0f1ec78f06bd'}
    ]
    
    return render_template('schools_visited.html', title='Schools Visited', schools=schools)

if __name__ == '__main__':
    app.run()

print("Helolo")