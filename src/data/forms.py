from flask_wtf import FlaskForm
import wtforms


class ReviewForm(FlaskForm):
    text = wtforms.StringField("Введіть свій відгук", validators=[wtforms.validators.length(5, message="Відгук занадто короткий")])
    submit = wtforms.SubmitField("Зберегти")