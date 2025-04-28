from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder='templates')

fields = sorted([
    "Medicine/Healthcare",
    "Engineering/Technology",
    "Business/Finance",
    "Education",
    "Arts/Entertainment",
    "Law/Public Policy",
    "Science/Research",
    "Social Services",
    "Environmental Science"
])

majors = sorted([
    "Accounting", "Aerospace Engineering", "Astronomy", "Biochemistry", "Biology", 
    "Business Administration", "Chemistry", "Civil Engineering", "Computer Science", 
    "Creative Writing", "Criminal Justice", "Economics", "Education", "Electrical Engineering", 
    "Early Childhood Ed", "Entrepreneurship", "Environmental Science", "English", "Film Studies", 
    "Finance", "Fine Arts", "Geology", "Graphic Design", "International Relations", "Law", 
    "Marketing", "Mechanical Engineering", "Music", "Nursing", "Photography", "Physics", 
    "Political Science", "Pre-Med", "Public Health", "Public Policy", "Robotics Engineering", 
    "Social Work", "Sociology", "Special Education", "Theater Arts"
])

activities = sorted([
    "Acting", "Astronomy", "Birdwatching", "Budgeting", "Building Circuits", 
    "Building Models", "Chess", "Coding", "Creative Writing", "Debate", 
    "Digital Art", "Filmmaking", "Gardening", "Hiking", "Photography", 
    "Playing Guitar", "Public Speaking", "Reading", "Rock Collecting", 
    "Running", "Social Media", "Stargazing", "Stock Trading", "Swimming", 
    "Tutoring", "Video Games", "Volunteering", "Writing"
])

subjects = sorted([
    "Art", "Biology", "Chemistry", "Computer Science", "Economics", "English",
    "History", "Math", "Music", "Physics", "Psychology", "Sociology"
])

@app.route("/")
@app.route("/home")
def home():
    return render_template('startup.html', title='Future Focus')

@app.route("/unlock_insights", methods=["GET", "POST"])
def unlock_insights():
    if request.method == "POST":
        # Here you can process the form data
        field_of_interest = request.form.get("field_of_interest")
        first_major = request.form.get("first_major")
        second_major = request.form.get("second_major")
        first_hobby = request.form.get("first_hobby")
        second_hobby = request.form.get("second_hobby")
        first_subject = request.form.get("first_subject")
        second_subject = request.form.get("second_subject")

        # Example: just print (later you will pass it to your ML model)
        print(field_of_interest, first_major, second_major, first_hobby, second_hobby, first_subject, second_subject)

        # Redirect or render a success page later
        return redirect(url_for('unlock_insights'))  

    return render_template(
        "unlock_insights.html",
        fields=fields,
        majors=majors,
        activities=activities,
        subjects=subjects
    )

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

print("Hello")