"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import PropertyForm
from app.models import Property
from werkzeug.utils import secure_filename
from app import db

###
# Routing for your application.
###

@app.route('/')
def home():
    print('Testing')
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""    
    return render_template('about.html')



# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/property', methods=['POST','GET'])
def property():
	print('propTest')
	myform = PropertyForm()
	print('propTest1')    
	if request.method == 'POST':
		print("method is post")
		if myform.validate_on_submit():
		    #Add data from form
			print('This is the true test')            	
			propTitle = myform.propTitle.data
			description = myform.description.data
			roomNum = myform.roomNum.data
			bathroomNum = myform.bathroomNum.data
			price = myform.price.data
			propType = myform.propType.data
			location = myform.location.data
			image = myform.file.data
			filename = secure_filename(image.filename)
			image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			
			newProp = Property(propTitle, description, roomNum, bathroomNum, price, propType, location, filename)          	
			db.session.add(newProp)
			db.session.commit()   

			flash('The property was added successfully!')            
			return redirect(url_for('home'))
	else:
		flash_errors(myform)	
	return render_template('property.html', form = myform)

@app.route('/properties', methods=["GET"])
def properties():
    """Render the website's about page."""    
    propList = db.session.query(Property).all()    
    return render_template('properties.html', properties = propList)

@app.route('/property/<propertyid>' , methods=["GET"])
def singleProperty(propertyid):
    """Render the website's about page."""
    prop = db.session.query(Property).filter(Property.id == propertyid).first()    
    return render_template('singleProperty.html', prop = prop)


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (
			    getattr(form, field).label.text,
			    error
			), 'danger')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
