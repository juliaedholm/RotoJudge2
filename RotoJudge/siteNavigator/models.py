from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class ScrapeInputDraft(models.Model):
    class Meta:
        db_table = u'scrape_input_draft'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # Other fields here
    leage_creation_url = models.CharField(max_length=75)
    league_ID = models.IntegerField()
    owner_ID = models.IntegerField()
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'



class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)
    class Meta:
        db_table = u'auth_group'
        
class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = u'auth_permission'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'


class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class FootballLeagues(models.Model):
    rj_league_id = models.IntegerField(primary_key=True)
    league_host = models.CharField(max_length=200, blank=True)
    host_league_id = models.CharField(max_length=50, blank=True)
    league_name = models.CharField(max_length=250, blank=True)
    league_url = models.CharField(max_length=1000, blank=True)
    league_photo_url = models.CharField(max_length=1000, blank=True)
    league_init_email = models.CharField(max_length=200, blank=True)
    date_add = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'football_leagues'
        #options.managed = False

class FootballTeams(models.Model):
    rj_team_id = models.IntegerField(primary_key=True)
    rj_league_id = models.IntegerField(null=True, blank=True)
    team_url = models.CharField(max_length=1000, blank=True)
    team_name = models.CharField(max_length=500, blank=True)
    owner_name = models.CharField(max_length=250, blank=True)
    date_add = models.DateTimeField(null=True, blank=True)
    team_photo_url = models.CharField(max_length=1000, blank=True)
    class Meta:
        db_table = u'football_teams'
        #options.managed = False


class FootballViewWeeklyStats(models.Model):
    player_name = models.CharField(max_length=250, blank=True,primary_key=True)
    player_position = models.CharField(max_length=50, blank=True)
    player_rank_season = models.IntegerField(null=True, blank=True)
    pick_number_position = models.IntegerField(null=True, blank=True, )
    pick_value = models.IntegerField( blank=True)
    team_name = models.CharField(max_length=500, blank=True)
    rj_team_id = models.IntegerField(null=True, blank=True)
    rj_league_id = models.IntegerField(null=True, blank=True)
    player_pts_season = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    week_num = models.IntegerField(null=True, blank=True)
    owner_name = models.CharField(max_length=250, blank=True)
    class Meta:
        db_table = u'football_view_weekly_stats'
        #options.managed = False

class FootballMainWeeklyMatchResults(models.Model):
    rowid = models.IntegerField(primary_key=True)
    home_rj_team_id = models.IntegerField(null=True, blank=True)
    home_score = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    away_rj_team_id = models.IntegerField(null=True, blank=True)
    away_score = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    week_num = models.IntegerField(null=True, blank=True)
    date_add = models.DateTimeField(null=True, blank=True)
    match_winner = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'football_main_weekly_match_results'
        #options.managed = False

class FootballViewStartResults(models.Model):
    team_name = models.CharField(max_length=500, blank=True, primary_key=True)
    player_name = models.CharField(max_length=250, blank=True)
    player_position = models.CharField(max_length=50, blank=True)
    team_position = models.CharField(max_length=50, blank=True)
    pts_scored = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    pts_projected = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    week_num = models.IntegerField(null=True, blank=True)
    player_id = models.IntegerField(null=True, blank=True)
    rj_team_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'football_view_start_results'
        #options.managed = False
        
class FootballViewStartOptimal(models.Model):
    team_name = models.CharField(max_length=500, primary_key=True)
    player_name = models.CharField(max_length=250, blank=True)
    player_position = models.CharField(max_length=50, blank=True)
    team_position = models.CharField(max_length=50, blank=True)
    pts_scored = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    pts_projected = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    week_num = models.IntegerField(null=True, blank=True)
    player_id = models.IntegerField(null=True, blank=True)
    rj_team_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'football_view_start_optimal'
        #options.managed = False

class FootballViewOptimalPercentages(models.Model):
    rj_league_id = models.IntegerField(blank=True, primary_key=True)
    rj_team_id = models.IntegerField(null=True, blank=True)
    team_name = models.CharField(max_length=500, blank=True)
    week_num = models.IntegerField(null=True, blank=True)
    count_optimal = models.BigIntegerField(null=True, blank=True)
    max_optimal = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    percent_optimal = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    class Meta:
        db_table = u'football_view_optimal_percentages'
        #options.managed = False
        
class FootballViewOptimalPercentagesSeason(models.Model):
    rj_league_id = models.IntegerField(primary_key=True, blank=True)
    rj_team_id = models.IntegerField(null=True, blank=True)
    team_name = models.CharField(max_length=500, blank=True)
    season_avg = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    class Meta:
        db_table = u'football_view_optimal_percentages_season'
        #options.managed = False

class FootballViewPickValuesTeam(models.Model):
    rj_league_id = models.IntegerField(primary_key=True, blank=True)
    rj_team_id = models.IntegerField(null=True, blank=True)
    team_name = models.CharField(max_length=500, blank=True)
    week_num = models.IntegerField(null=True, blank=True)
    total_team_pick_value = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'football_view_pick_values_team'
        #options.managed = False
        
class FootballViewCompStartOptimal(models.Model):
    player_id = models.IntegerField(null=True, blank=True)
    player_name = models.CharField(max_length=250, blank=True)
    player_position = models.CharField(max_length=50, blank=True)
    rj_team_id = models.IntegerField(null=True, blank=True)
    result_position = models.CharField(max_length=50, blank=True)
    optimal_position = models.CharField(max_length=50, blank=True)
    week_num = models.IntegerField(null=True, blank=True)
    good_start = models.TextField(blank=True)
    team_name = models.CharField(max_length=500, blank=True)
    class Meta:
        db_table = u'football_view_comp_start_optimal'
        #options.managed = False
        
class FootballViewWeeklyMatchResults(models.Model):
    home_rj_team_id = models.IntegerField(primary_key=True, blank=True)
    home_team = models.CharField(max_length=500, blank=True)
    away_rj_team_id = models.IntegerField(null=True, blank=True)
    home_team_score = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    home_team_optimal = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    away_team = models.CharField(max_length=500, blank=True)
    away_team_score = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    away_score_optimal = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    rj_league_id = models.IntegerField(null=True, blank=True)
    week_num = models.IntegerField(null=True, blank=True)
    match_winner = models.CharField(max_length=500, blank=True)
    class Meta:
        db_table = u'football_view_weekly_match_results'
        #options.managed = False