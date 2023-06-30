from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    registration_date = models.DateField(auto_now_add=True)

class AuthorizedTrainingPartner(models.Model):
    partner_id = models.AutoField(primary_key=True)
    partner_name = models.CharField(max_length=100)
    partner_description = models.TextField()

class Footer(models.Model):
    footer_id = models.AutoField(primary_key=True)
    social_media_icons = models.CharField(max_length=100)
    join_us_link = models.URLField()
    locations_link = models.URLField()
    contact_us_link = models.URLField()
    disclaimer = models.TextField()

class MainContent(models.Model):
    content_id = models.AutoField(primary_key=True)
    banner_search_keyword = models.CharField(max_length=100)
    authorized_training_partners = models.TextField()
    why_choose_vinsys = models.TextField()
    vinsys_portfolio = models.TextField()
    news_title = models.CharField(max_length=100)
    news_content = models.TextField()
    news_date = models.DateField()

class Header(models.Model):
    header_id = models.AutoField(primary_key=True)
    header_logo = models.ImageField(upload_to='header_logos/')
from django.db import models

class Domain(models.Model):
    domain_id = models.AutoField(primary_key=True)
    domain_name = models.CharField(max_length=100)

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)

class IndividualTraining(models.Model):
    training = models.ForeignKey('Training', on_delete=models.CASCADE)
    introduction_content = models.TextField()
    instructor_section = models.TextField()
    skill_gaps_section = models.TextField()

class GroupPrivateTraining(models.Model):
    training = models.ForeignKey('Training', on_delete=models.CASCADE)
    introduction_content = models.TextField()
    group_private_training_benefits_section = models.TextField()

class CorporateTraining(models.Model):
    training = models.ForeignKey('Training', on_delete=models.CASCADE)
    introduction_content = models.TextField()
    learning_pass_section = models.TextField()
    soft_skills_section = models.TextField()
    domain_brand_training_section = models.TextField()
    authorizations_section = models.TextField()
    locations_section = models.TextField()
    corporate_training_benefits_section = models.TextField()

class GovernmentTraining(models.Model):
    training = models.ForeignKey('Training', on_delete=models.CASCADE)
    introduction_content = models.TextField()
    government_solutions_section = models.TextField()

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    domain_id = models.ForeignKey(Domain, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Enrollments(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

class DeliveryFormat(models.Model):
    delivery_format_id = models.AutoField(primary_key=True)
    delivery_format_name = models.CharField(max_length=100)
    delivery_format_description = models.TextField()

class Training(models.Model):
    training_id = models.AutoField(primary_key=True)
    training_name = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    delivery_format_id = models.ForeignKey(DeliveryFormat, on_delete=models.CASCADE)

class WhatIsNew(models.Model):
    news_id = models.AutoField(primary_key=True)
    news_title = models.CharField(max_length=100)
    news_content = models.TextField()
    news_date = models.DateField()

class VinsysPortfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    portfolio_item = models.TextField()

class WhyChooseVinsys(models.Model):
    choose_id = models.AutoField(primary_key=True)
    choose_title = models.CharField(max_length=100)
    choose_description = models.TextField()

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)

class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)

class SubCategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=100)

class SubSubCategory(models.Model):
    subsubcategory_id = models.AutoField(primary_key=True)
    subsubcategory_name = models.CharField(max_length=100)

class ForeignLanguageServices(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)

class Industries(models.Model):
    industry_id = models.AutoField(primary_key=True)
    industry_name = models.CharField(max_length=100)

class ServiceCategory(models.Model):
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

class SubCategoryCategory(models.Model):
    subcategory_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    subsubcategory_id = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE)

class ProductCategory(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

class Quotes(models.Model):
    quote_id = models.AutoField(primary_key=True)
    document = models.TextField()
    pricing = models.TextField()
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

class Enquiries(models.Model):
    enquiry_id = models.AutoField(primary_key=True)
    message = models.TextField()
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

class PressReleases(models.Model):
    press_release_id = models.AutoField(primary_key=True)
    press_release_title = models.CharField(max_length=100)
    press_release_date = models.DateField()
    press_release_content = models.TextField()

class Whitepapers(models.Model):
    whitepaper_id = models.AutoField(primary_key=True)
    whitepaper_title = models.CharField(max_length=100)
    whitepaper_description = models.TextField()
    whitepaper_url = models.URLField()

class CaseStudies(models.Model):
    case_study_id = models.AutoField(primary_key=True)
    case_study_title = models.CharField(max_length=100)
    case_study_description = models.TextField()
    case_study_url = models.URLField()

class WebinarRegistrations(models.Model):
    registration_id = models.AutoField(primary_key=True)
    webinar_id = models.ForeignKey('Webinars', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    registration_date = models.DateField()

class Webinars(models.Model):
    webinar_id = models.AutoField(primary_key=True)
    webinar_title = models.CharField(max_length=100)
    webinar_description = models.TextField()
    webinar_date = models.DateField()
    webinar_registration_link = models.URLField()

class Awards(models.Model):
    award_id = models.AutoField(primary_key=True)
    award_title = models.CharField(max_length=100)
    award_description = models.TextField()

class OurCoreValues(models.Model):
    core_values_id = models.AutoField(primary_key=True)
    core_values_text = models.TextField()

class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    banner_image_url = models.URLField()

