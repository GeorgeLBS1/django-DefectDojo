from django.conf.urls import url

from dojo.product import views

urlpatterns = [
    #  product
    url(r'^product$', views.product, name='product'),
    url(r'^product/(?P<pid>\d+)$', views.view_product,
        name='view_product'),
    url(r'^product/(?P<pid>\d+)/components$', views.view_product_components,
        name='view_product_components'),
    url(r'^product/(?P<pid>\d+)/engagements$', views.view_engagements,
        name='view_engagements'),
    url(r'^product/(?P<pid>\d+)/import_scan_results$',
        views.import_scan_results_prod, name='import_scan_results_prod'),
    url(r'^product/(?P<pid>\d+)/metrics$', views.view_product_metrics,
        name='view_product_metrics'),
    url(r'^product/(?P<pid>\d+)/edit$', views.edit_product,
        name='edit_product'),
    url(r'^product/(?P<pid>\d+)/delete$', views.delete_product,
        name='delete_product'),
    url(r'^product/add', views.new_product, name='new_product'),
    url(r'^product/(?P<pid>\d+)/new_engagement$', views.new_eng_for_app,
        name='new_eng_for_prod'),
    url(r'^product/(?P<pid>\d+)/new_technology$', views.new_tech_for_prod,
         name='new_tech_for_prod'),
    url(r'^technology/(?P<tid>\d+)/edit$', views.edit_technology,
        name='edit_technology'),
    url(r'^technology/(?P<tid>\d+)/delete$', views.delete_technology,
        name='delete_technology'),
    url(r'^product/(?P<pid>\d+)/new_engagement/cicd$', views.new_eng_for_app_cicd,
        name='new_eng_for_prod_cicd'),
    url(r'^product/(?P<pid>\d+)/add_meta_data$', views.add_meta_data,
        name='add_meta_data'),
    url(r'^product/(?P<pid>\d+)/edit_notifications$', views.edit_notifications,
        name='edit_notifications'),
    url(r'^product/(?P<pid>\d+)/edit_meta_data$', views.edit_meta_data,
        name='edit_meta_data'),
    url(r'^product/(?P<pid>\d+)/ad_hoc_finding$', views.ad_hoc_finding,
        name='ad_hoc_finding'),
    url(r'^product/(?P<pid>\d+)/engagement_presets$', views.engagement_presets,
        name='engagement_presets'),
    url(r'^product/(?P<pid>\d+)/engagement_presets/(?P<eid>\d+)/edit$', views.edit_engagement_presets,
        name='edit_engagement_presets'),
    url(r'^product/(?P<pid>\d+)/engagement_presets/add$', views.add_engagement_presets,
        name='add_engagement_presets'),
    url(r'^product/(?P<pid>\d+)/engagement_presets/(?P<eid>\d+)/delete$', views.delete_engagement_presets,
        name='delete_engagement_presets'),
    url(r'^product/(?P<pid>\d+)/add_member$', views.add_product_member,
        name='add_product_member'),
    url(r'^product/member/(?P<memberid>\d+)/edit$', views.edit_product_member,
        name='edit_product_member'),
    url(r'^product/member/(?P<memberid>\d+)/delete$', views.delete_product_member,
        name='delete_product_member'),
    url(r'^product/(?P<pid>\d+)/add_sonarqube$', views.add_sonarqube,
        name='add_sonarqube'),
    url(r'^product/(?P<pid>\d+)/view_sonarqube$', views.view_sonarqube,
        name='view_sonarqube'),
    url(r'^product/(?P<pid>\d+)/edit_sonarqube/(?P<sqcid>\d+)$', views.edit_sonarqube,
        name='edit_sonarqube'),
    url(r'^product/(?P<pid>\d+)/delete_sonarqube/(?P<sqcid>\d+)$', views.delete_sonarqube,
        name='delete_sonarqube'),
    url(r'^product/(?P<pid>\d+)/add_cobaltio$', views.add_cobaltio,
        name='add_cobaltio'),
    url(r'^product/(?P<pid>\d+)/view_cobaltio$', views.view_cobaltio,
        name='view_cobaltio'),
    url(r'^product/(?P<pid>\d+)/edit_cobaltio/(?P<cobaltio_cid>\d+)', views.edit_cobaltio,
        name='edit_cobaltio'),
    url(r'^product/(?P<pid>\d+)/delete_cobaltio/(?P<cobaltio_cid>\d+)$', views.delete_cobaltio,
        name='delete_cobaltio'),
    url(r'^product/(?P<pid>\d+)/add_group$', views.add_product_group,
        name='add_product_group'),
    url(r'^product/group/(?P<groupid>\d+)/edit$', views.edit_product_group,
        name='edit_product_group'),
    url(r'^product/group/(?P<groupid>\d+)/delete$', views.delete_product_group,
        name='delete_product_group'),
]
