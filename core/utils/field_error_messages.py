from django.utils.translation import gettext_lazy as _

def get_field_error_messages(field_name, field_type='default'):
    """
    Generate consistent error messages for all serializer field types
    Args:
        field_name (str): Human-readable field name (e.g., "Supplier", "Air way bill")
        field_type (str): Type of serializer field (e.g., "CharField", "PrimaryKeyRelated", "EmailField")
    Returns:
        dict: Complete error messages dictionary for the field
    """
    
    # Common base messages for all field types
    base_messages = {
        'required' : _('%(field_name)s is required.'),
        'null'     : _('%(field_name)s cannot be null.'),
        'blank'    : _('%(field_name)s cannot be blank.'),
        'invalid'  : _('Invalid %(field_name_lower)s value.')
    }
    
    # Field type specific additional messages
    type_specific = {
        'PrimaryKeyRelated': {
            'does_not_exist' : _('%(field_name)s does not exist.'),
            'incorrect_type' : _('%(field_name)s must be a valid ID.')
        },
        'CharField': {
            'max_length' : _('%(field_name)s cannot exceed %(max_length)s characters.'),
            'min_length' : _('%(field_name)s must be at least %(min_length)s characters.')
        },
        'EmailField': {
            'invalid': _('Enter a valid %(field_name_lower)s address.')
        },
        'IntegerField': {
            'max_value' : _('%(field_name)s cannot be greater than %(max_value)s.'),
            'min_value' : _('%(field_name)s cannot be less than %(min_value)s.')
        },
        'DecimalField': {
            'max_value'          : _('%(field_name)s cannot be greater than %(max_value)s.'),
            'min_value'          : _('%(field_name)s cannot be less than %(min_value)s.'),
            'max_digits'         : _('%(field_name)s cannot have more than %(max_digits)s digits.'),
            'max_decimal_places' : _('%(field_name)s cannot have more than %(max_decimal_places)s decimal places.'),
            'max_whole_digits'   : _('%(field_name)s cannot have more than %(max_whole_digits)s whole digits.')
        },
        'DateField': {
            'invalid': _('Enter a valid %(field_name_lower)s date.')
        },
        'DateTimeField': {
            'invalid': _('Enter a valid %(field_name_lower)s date/time.')
        },
        'BooleanField': {
            'invalid': _('%(field_name)s must be either true or false.')
        },
        'ChoiceField': {
            'invalid_choice': _('Invalid %(field_name_lower)s selection.')
        },
        'FileField': {
            'invalid': _('Invalid %(field_name_lower)s file.'),
            'empty': _('%(field_name)s file cannot be empty.'),
            'max_length': _('%(field_name)s file name too long.')
        },
        'ImageField': {
            'invalid_image': _('Upload a valid %(field_name_lower)s image.')
        },
        'URLField': {
            'invalid': _('Enter a valid %(field_name_lower)s URL.')
        },
        'UUIDField': {
            'invalid': _('Enter a valid %(field_name_lower)s UUID.')
        },
        'ListField': {
            'empty': _('%(field_name)s cannot be empty.'),
            'invalid': _('Invalid %(field_name_lower)s list.')
        },
        'DictField': {
            'empty': _('%(field_name)s cannot be empty.'),
            'invalid': _('Invalid %(field_name_lower)s dictionary.')
        },
        'JSONField': {
            'invalid': _('Invalid %(field_name_lower)s JSON data.')
        },
        'default': {}
    }
    
    # Merge base messages with type specific messages
    return {**base_messages, **type_specific.get(field_type, {})}


"""#! Example: Uses of this, 
from .utils.error_utils import get_field_error_messages

# প্রাইমারি কী সম্পর্কিত ফিল্ড
supplier_id = serializers.PrimaryKeyRelatedField(
    queryset=Supplier.objects.all(),
    error_messages=get_field_error_messages('Supplier', 'PrimaryKeyRelated')
)

# চার ফিল্ড
awb_number = serializers.CharField(
    max_length=100,
    error_messages=get_field_error_messages('Air way bill', 'CharField')
)

# ইমেইল ফিল্ড
email = serializers.EmailField(
    error_messages=get_field_error_messages('Email', 'EmailField')
)

# তারিখ ফিল্ড
delivery_date = serializers.DateField(
    error_messages=get_field_error_messages('Delivery date', 'DateField')
)
"""