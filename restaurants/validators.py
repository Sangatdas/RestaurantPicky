from django.core.exceptions import ValidationError

def validate_even(value):
	if value % 2 != 0:
		raise ValidationError(
				'%(value)s is not an even number',
				params={'value':value},
			)

def clean_location(value):
	location = self.cleaned_data.get("location")
	if location == "Hello":
		raise ValidationError("Not a valid location")
	return location

CATEGORIES = ["Indian", "Chinese", "Italian", "American", "Mexican", "Thai"]

def validate_category(value):
	cat = value.capitalize()
	if value not in CATEGORIES and cat not in CATEGORIES:
		raise ValidationError(F'{value} is not a valid category')