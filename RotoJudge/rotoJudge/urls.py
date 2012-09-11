from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import django.contrib.auth
admin.autodiscover()

urlpatterns = patterns('siteNavigator.views',
    # Examples:
    (r'^football/home', 'home'),
    (r'^football/stats/OptimalStarts', 'OptimalStarts'),
    (r'^football/stats/PlayerValues', 'PlayerValues'),
    (r'^football/stats/StartingPercentages', 'StartingPercentages'),
    (r'^football/LeagueRankings', 'LeagueRankings'),
    (r'^football/CreateAccount', 'CreateAccount'),
    (r'^football/loginComplete/(?P<created_owner_id>\d+)', 'loginComplete'),
    (r'^football/login/$', 'django.contrib.auth.views.login'),
    (r'^football/(?P<league_id>\d+)/TeamOwnerPage/(?P<owner_id>\d+)', 'TeamOwnerPage'),
    (r'^football/(?P<league_id>\d+)/LeagueHome', 'LeagueHomePage'),
    # url(r'^$', 'football.views.home', name='home'),
    # url(r'^football/', include('football.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
      (r'^football/login', 'django.contrib.auth.views.login'),
)
