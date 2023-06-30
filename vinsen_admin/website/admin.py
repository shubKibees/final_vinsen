from django.contrib import admin
from .models import (
    User,
    AuthorizedTrainingPartner,
    Footer,
    MainContent,
    Header,
    Domain,
    Brand,
    IndividualTraining,
    GroupPrivateTraining,
    CorporateTraining,
    GovernmentTraining,
    Course,
    Enrollments,
    DeliveryFormat,
    Training,
    WhatIsNew,
    VinsysPortfolio,
    WhyChooseVinsys,
    Products,
    Services,
    SubCategory,
    SubSubCategory,
    ForeignLanguageServices,
    Industries,
    ServiceCategory,
    SubCategoryCategory,
    ProductCategory,
    Quotes,
    Enquiries,
    PressReleases,
    Whitepapers,
    CaseStudies,
    WebinarRegistrations,
    Webinars,
    Awards,
    OurCoreValues,
    Banner,
)
class UserAdmin(admin.ModelAdmin):
    list_display = ( "username","email","first_name","last_name")
class AuthorizedTrainingPartnerAdmin(admin.ModelAdmin):
    list_display = ("partner_name","partner_description")
class FooterAdmin(admin.ModelAdmin):
    list_display = ("social_media_icons",)
class MainContentAdmin(admin.ModelAdmin):
    list_display = ("why_choose_vinsys","news_title",)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("join_us_link",)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("header_logo",)
class DomainAdmin(admin.ModelAdmin):
    list_display = ("domain_name",)

class BrandAdmin(admin.ModelAdmin):
    list_display = ("brand_name",)

class IndividualTrainingAdmin(admin.ModelAdmin):
    list_display = ("introduction_content",)

class GroupPrivateTrainingAdmin(admin.ModelAdmin):
    list_display = ("introduction_content",)

class CorporateTrainingAdmin(admin.ModelAdmin):
    list_display = ("introduction_content",)

class GovernmentTrainingAdmin(admin.ModelAdmin):
    list_display = ("introduction_content",)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name",)

class EnrollmentsAdmin(admin.ModelAdmin):
    list_display = ("user_id", "course_id", "enrollment_date")

class DeliveryFormatAdmin(admin.ModelAdmin):
    list_display = ("delivery_format_name",)

class TrainingAdmin(admin.ModelAdmin):
    list_display = ("training_name",)

class WhatIsNewAdmin(admin.ModelAdmin):
    list_display = ("news_title", "news_content", "news_date")

class VinsysPortfolioAdmin(admin.ModelAdmin):
    list_display = ("portfolio_item",)

class WhyChooseVinsysAdmin(admin.ModelAdmin):
    list_display = ("choose_title", "choose_description")

class ProductsAdmin(admin.ModelAdmin):
    list_display = ("product_name",)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ("service_name",)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("subcategory_name",)

class SubSubCategoryAdmin(admin.ModelAdmin):
    list_display = ("subsubcategory_name",)

class ForeignLanguageServicesAdmin(admin.ModelAdmin):
    list_display = ("service_name",)

class IndustriesAdmin(admin.ModelAdmin):
    list_display = ("industry_name",)

class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("service_id", "subcategory_id")

class SubCategoryCategoryAdmin(admin.ModelAdmin):
    list_display = ("subcategory_id", "subsubcategory_id")

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("product_id", "subcategory_id")

class QuotesAdmin(admin.ModelAdmin):
    list_display = ("document", "pricing", "user_id")

class EnquiriesAdmin(admin.ModelAdmin):
    list_display = ("message", "user_id")

class PressReleasesAdmin(admin.ModelAdmin):
    list_display = ("press_release_title", "press_release_date", "press_release_content")

class WhitepapersAdmin(admin.ModelAdmin):
    list_display = ("whitepaper_title", "whitepaper_description", "whitepaper_url")

class CaseStudiesAdmin(admin.ModelAdmin):
    list_display = ("case_study_title", "case_study_description", "case_study_url")

class WebinarRegistrationsAdmin(admin.ModelAdmin):
    list_display = ("webinar_id", "client_name", "client_email", "registration_date")

class WebinarsAdmin(admin.ModelAdmin):
    list_display = ("webinar_title", "webinar_description", "webinar_date", "webinar_registration_link")

class AwardsAdmin(admin.ModelAdmin):
    list_display = ("award_title", "award_description")

class OurCoreValuesAdmin(admin.ModelAdmin):
    list_display = ("core_values_text",)

class BannerAdmin(admin.ModelAdmin):
    list_display = ("banner_image_url",)

# Register the models with the customized admin classes

admin.site.register(User, UserAdmin)
admin.site.register(AuthorizedTrainingPartner, AuthorizedTrainingPartnerAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(IndividualTraining, IndividualTrainingAdmin)
admin.site.register(GroupPrivateTraining, GroupPrivateTrainingAdmin)
admin.site.register(CorporateTraining, CorporateTrainingAdmin)
admin.site.register(GovernmentTraining, GovernmentTrainingAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollments, EnrollmentsAdmin)
admin.site.register(DeliveryFormat, DeliveryFormatAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(WhatIsNew, WhatIsNewAdmin)
admin.site.register(VinsysPortfolio, VinsysPortfolioAdmin)
admin.site.register(WhyChooseVinsys, WhyChooseVinsysAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(SubSubCategory, SubSubCategoryAdmin)
admin.site.register(ForeignLanguageServices, ForeignLanguageServicesAdmin)
admin.site.register(Industries, IndustriesAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(SubCategoryCategory, SubCategoryCategoryAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Quotes, QuotesAdmin)
admin.site.register(Enquiries, EnquiriesAdmin)
admin.site.register(PressReleases, PressReleasesAdmin)
admin.site.register(Whitepapers, WhitepapersAdmin)
admin.site.register(CaseStudies, CaseStudiesAdmin)
admin.site.register(WebinarRegistrations, WebinarRegistrationsAdmin)
admin.site.register(Webinars, WebinarsAdmin)
admin.site.register(Awards, AwardsAdmin)
admin.site.register(OurCoreValues, OurCoreValuesAdmin)
admin.site.register(Banner, BannerAdmin)



admin.site.site_header = "Vinsys Admin"
admin.site.index_title ="welcome to Vinsys Admin"