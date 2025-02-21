from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, URLField
from wtforms.validators import DataRequired, Optional, NumberRange, URL

class ElectronicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    price = FloatField('Price ($)', validators=[
        DataRequired(),
        NumberRange(min=0, message="Price must be positive")
    ])
    stock = IntegerField('Stock', validators=[
        DataRequired(),
        NumberRange(min=0, message="Stock must be positive")
    ])
    image = StringField('Image URL', validators=[Optional()])

    # ProductModel.py specification paragraph
    specification = TextAreaField('Additional Specifications', validators=[Optional()]) 
    
    # ElectronicModel.py technical specifications
    power_rating = IntegerField('Power Rating (W)', validators=[Optional()])
    battery_life = IntegerField('Battery Life (hours)', validators=[Optional()])
    energy_efficiency_rating = StringField('Energy Rating', validators=[Optional()])
    operating_system = StringField('Operating System', validators=[Optional()])
    processor = StringField('Processor', validators=[Optional()])
    ram = StringField('RAM', validators=[Optional()])
    storage = StringField('Storage', validators=[Optional()])
    
    # ElectronicModel.py physical specifications
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    warranty_period = IntegerField('Warranty (months)', validators=[DataRequired()])
    dimensions = StringField('Dimensions', validators=[DataRequired()])
    weight = StringField('Weight', validators=[DataRequired()])
    