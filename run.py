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
    {'name': 'Ms. Smith', 'pfp_url': 'https://preview.redd.it/oqhs74f166511.png?width=640&crop=smart&auto=webp&s=e768a28eb87cd18177ca17d08daeb3317ae7d3f4', 'quote': 'An exceptional student with a passion for innovation.','role':"Alloa Principal"},
    {'name': 'Mr. Johnson', 'pfp_url': 'https://media.licdn.com/dms/image/v2/D5612AQHV7OQuC-dRvQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1709355461942?e=1732147200&v=beta&t=U3Ktgrlt7Yuq-sbwsBHWhlKIY8KdHJXcZCRcc_6AbYQ', 'quote': 'A dedicated learner who excels in problem-solving.','role':"Fletcher's Meadow Principal"},
    {'name': 'Ms. Smith', 'pfp_url': 'https://preview.redd.it/oqhs74f166511.png?width=640&crop=smart&auto=webp&s=e768a28eb87cd18177ca17d08daeb3317ae7d3f4', 'quote': 'An exceptional student with a passion for innovation.','role':"Alloa Principal"},
    ]
    return render_template('testimonials.html', title='Testimonials', testimonials_list=testimonials_list)


@app.route("/about_us")
def about_us():
    
    return render_template('about_us.html')


@app.route("/schools_visited")
def schools_visited():
    schools = [
        {'name': 'Alloa Public School', 'image_url': 'https://alloa.peelschools.org/images/324ee78d-1cae-41b4-b138-ad8c416cd763'},
    
    ]
    return render_template('schools_visited.html', title='Schools Visited', schools=schools)

if __name__ == '__main__':
    app.run()

print("Helolo")