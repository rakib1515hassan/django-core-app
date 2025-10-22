import uuid
from django.utils.text import slugify


def generate_unique_slug(instance, name_field, slug_field_name="slug"):
    """
    Generate a unique slug for any model instance.
    :param instance: Model instance (self)
    :param name_field: string to generate slug from (ex: instance.name)
    :param slug_field_name: name of the slug field (default='slug')
    
    :#* Directly Create Slug
    if not self.slug:
        base_slug = slugify(self.name)
        slug = base_slug
        counter = 1
        while SubscriptionPlan.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        self.slug = slug
    """
    ModelClass = instance.__class__
    base_slug = slugify(name_field)
    slug = base_slug
    counter = 1

    # loop until unique slug found
    while ModelClass.objects.filter(**{slug_field_name: slug}).exclude(pk=instance.pk).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug


def generate_unique_code(model_class, prefix="CMP", field_name="code_no", padding=4):
    """
    Generate a unique incremental code like CMP0001, CMP0002, etc.
    :param model_class: Model class (not instance)
    :param prefix: Prefix for the code (ex: 'CMP', 'SHOP', 'PRD')
    :param field_name: Field name of code (default='code_no')
    :param padding: Number of digits (default=4) padding=4 শুধু minimum width নির্ধারণ করে এটা কোনো maximum cap নয়
    
    :#* Directly Create Code
    if not self.code_no:
        prefix = "CMP"
        last_obj = Company.objects.order_by("id").last()
        next_id = (last_obj.id + 1) if last_obj else 1
        self.code_no = f"{prefix}{str(next_id).zfill(4)}"

        # Ensure code_no uniqueness
        while Company.objects.filter(code_no=self.code_no).exclude(pk=self.pk).exists():
            next_id += 1
            self.code_no = f"{prefix}{str(next_id).zfill(4)}"
    """
    last_obj = model_class.objects.order_by("id").last()
    next_id = (last_obj.id + 1) if last_obj else 1
    code = f"{prefix}{str(next_id).zfill(padding)}"

    # Ensure uniqueness
    while model_class.objects.filter(**{field_name: code}).exists():
        next_id += 1
        code = f"{prefix}{str(next_id).zfill(padding)}"

    return code
