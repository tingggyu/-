# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accent(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'accent'
        app_label = 'website'


class AccentLexeme(models.Model):
    general_id = models.AutoField(primary_key=True)
    accent = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'accent_lexeme'
        app_label = 'website'


class Administrator(models.Model):
    acount = models.CharField(max_length=45, blank=True, null=True)
    pwd = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45)
    time = models.DateTimeField()
    identity = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'administrator'
        app_label = 'website'


class AdministratorOperateLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Administrator, models.DO_NOTHING)
    account = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    time = models.DateTimeField()
    operate = models.CharField(max_length=45)
    ip = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'administrator_operate_log'
        app_label = 'website'


class Appendices(models.Model):
    name = models.CharField(max_length=45)
    text = models.TextField()
    pdffile = models.CharField(max_length=45, blank=True, null=True)
    xlsfile = models.CharField(max_length=45, blank=True, null=True)
    odsfile = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appendices'
        app_label = 'website'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
        app_label = 'website'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
        app_label = 'website'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
        app_label = 'website'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
        app_label = 'website'
        


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
        app_label = 'website'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
        app_label = 'website'


class BodyAppendices(models.Model):
    name = models.CharField(max_length=45)
    text = models.TextField()
    file = models.CharField(max_length=45)
    img = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'body appendices'
        app_label = 'website'
       


class Content(models.Model):
    body_id = models.IntegerField()
    body_name = models.CharField(max_length=45)
    big_class = models.CharField(max_length=45, blank=True, null=True)
    big_text = models.TextField(blank=True, null=True)
    min_class = models.CharField(max_length=45, blank=True, null=True)
    min_text = models.TextField(blank=True, null=True)
    glossary = models.CharField(max_length=45, blank=True, null=True)
    chinese = models.CharField(max_length=45, blank=True, null=True)
    four_county = models.CharField(max_length=45, blank=True, null=True)
    sea_land = models.CharField(max_length=45, blank=True, null=True)
    tai_po = models.CharField(max_length=45, blank=True, null=True)
    zhao_an = models.CharField(max_length=45, blank=True, null=True)
    nansi_county = models.CharField(max_length=45, blank=True, null=True)
    pinyin = models.CharField(max_length=45, blank=True, null=True)
    explaination = models.TextField(blank=True, null=True)
    proverb = models.CharField(max_length=45, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content'
        app_label = 'website'


class Definition(models.Model):
    lexeme_id = models.IntegerField()
    system_number = models.IntegerField()
    pos = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField()
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'definition'
        app_label = 'website'


class DefinitionDeterminer(models.Model):
    det_id = models.IntegerField()
    def_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'definition_determiner'
        app_label = 'website'


class DefinitionIndex(models.Model):
    def_id = models.AutoField(primary_key=True)
    index_id = models.IntegerField(db_column='Index_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'definition_index'
        app_label = 'website'


class DefinitionOpposite(models.Model):
    def_id = models.IntegerField()
    lexeme = models.IntegerField()
    lexeme_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'definition_opposite'
        app_label = 'website'


class DefinitionSentences(models.Model):
    def_id = models.IntegerField()
    text = models.TextField()
    mandarin_text = models.TextField()
    audio_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'definition_sentences'
        app_label = 'website'


class DefinitionSimilar(models.Model):
    def_id = models.IntegerField()
    lexeme = models.IntegerField()
    related_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'definition_similar'
        app_label = 'website'


class Determiner(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'determiner'
        app_label = 'website'


class Dialect(models.Model):
    lexeme_id = models.IntegerField()
    dialect_lexeme = models.CharField(max_length=100)
    dialct_location = models.CharField(max_length=100)
    audio_name = models.CharField(max_length=100)
    tone_pitch = models.CharField(max_length=100)
    tone_category = models.CharField(max_length=100, blank=True, null=True)
    tone_contour = models.CharField(max_length=100, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dialect'
        app_label = 'website'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'
        app_label = 'website'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
        app_label = 'website'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        app_label = 'website'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        app_label = 'website'


class GeneralLexemes(models.Model):
    version_date = models.IntegerField()
    timestamp = models.IntegerField(blank=True, null=True)
    system_general_umber = models.DateTimeField()
    repository = models.IntegerField()
    lexeme = models.CharField(max_length=100)
    daily_word = models.IntegerField()
    remark = models.TextField()

    class Meta:
        managed = False
        db_table = 'general_lexemes'
        app_label = 'website'


class Homograph(models.Model):
    lexeme_id = models.IntegerField()
    system_number = models.IntegerField()
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'homograph'
        app_label = 'website'


class Illustrate(models.Model):
    category = models.CharField(db_column='Category', max_length=45)  # Field name made lowercase.
    subclass = models.CharField(db_column='Subclass', max_length=45)  # Field name made lowercase.
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'illustrate'
        app_label = 'website'


class Images(models.Model):
    lexeme_id = models.IntegerField()
    img_name = models.CharField(max_length=100)
    description = models.TextField()
    provider = models.CharField(max_length=100)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'
        app_label = 'website'


class IndexView(models.Model):
    first_name = models.CharField(max_length=45, blank=True, null=True)
    second_name = models.CharField(max_length=45, blank=True, null=True)
    third_name = models.CharField(max_length=45, blank=True, null=True)
    fourth_name = models.CharField(max_length=45, blank=True, null=True)
    fifth_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_view'
        app_label = 'website'


class Introduction(models.Model):
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'introduction'
        app_label = 'website'


class LexemeIndex(models.Model):
    def_id = models.IntegerField()
    index_id = models.IntegerField(db_column='Index_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lexeme_index'
        app_label = 'website'


class Lexemes(models.Model):
    general_id = models.IntegerField()
    accent_id = models.IntegerField()
    timestamp = models.IntegerField(blank=True, null=True)
    system_number = models.IntegerField()
    old_system_number = models.IntegerField()
    lexeme_number = models.IntegerField()
    manuscript_id = models.IntegerField()
    lexeme = models.CharField(max_length=100)
    accent = models.CharField(max_length=100)
    radical = models.CharField(max_length=100, blank=True, null=True)
    strokes = models.IntegerField(blank=True, null=True)
    outer_strokes = models.IntegerField(blank=True, null=True)
    word_count = models.IntegerField(blank=True, null=True)
    base_name = models.CharField(max_length=250, blank=True, null=True)
    base_site = models.CharField(max_length=250, blank=True, null=True)
    polysemy = models.TextField(blank=True, null=True)
    alt_term_mark = models.CharField(max_length=250, blank=True, null=True)
    reviewer = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexemes'
        app_label = 'website'


class Mandarin(models.Model):
    lexeme_id = models.IntegerField()
    corresponding_mandarin = models.CharField(max_length=100)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mandarin'
        app_label = 'website'


class NameLexemes(models.Model):
    system_number = models.IntegerField()
    lexeme = models.CharField(max_length=100)
    repository = models.IntegerField()
    accent = models.CharField(max_length=100)
    audio_name = models.CharField(max_length=100)
    attribute = models.CharField(max_length=100, blank=True, null=True)
    tone_pitch = models.CharField(max_length=100)
    tone_category = models.CharField(max_length=100, blank=True, null=True)
    tone_contour = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'name_lexemes'
        app_label = 'website'


class Notice(models.Model):
    title = models.CharField(max_length=45)
    category = models.IntegerField()
    time = models.DateField()
    text = models.TextField()
    web = models.TextField()
    address = models.TextField()
    address_name = models.CharField(max_length=45)
    file = models.CharField(max_length=45)
    file_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'notice'
        app_label = 'website'


class Polysemy(models.Model):
    lexeme_id = models.IntegerField()
    polysemy_lexeme = models.CharField(max_length=100)
    polysemy1 = models.CharField(max_length=100, blank=True, null=True)
    polysemy2 = models.CharField(max_length=100, blank=True, null=True)
    polysemy3 = models.CharField(max_length=100, blank=True, null=True)
    polysemy4 = models.CharField(max_length=100, blank=True, null=True)
    polysemy5 = models.CharField(max_length=100, blank=True, null=True)
    polysemy6 = models.CharField(max_length=100, blank=True, null=True)
    polysemy7 = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polysemy'
        app_label = 'website'


class Pronunciation(models.Model):
    audio_name = models.CharField(max_length=100)
    lexeme_id = models.IntegerField()
    main_pron = models.IntegerField()
    attribute = models.CharField(max_length=100, blank=True, null=True)
    tone_pitch = models.CharField(max_length=100)
    tone_category = models.CharField(max_length=100, blank=True, null=True)
    tone_contour = models.CharField(max_length=100, blank=True, null=True)
    pron_order = models.IntegerField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pronunciation'
        app_label = 'website'


class RelatedLexemes(models.Model):
    lexeme_id = models.IntegerField()
    related_lexeme = models.CharField(max_length=100)
    accent = models.CharField(max_length=100)
    audio_name = models.CharField(max_length=100)
    tone_pitch = models.CharField(max_length=100, blank=True, null=True)
    tone_category = models.CharField(max_length=100, blank=True, null=True)
    tone_contour = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'related_lexemes'
        app_label = 'website'


class Resource(models.Model):
    title = models.CharField(max_length=45)
    category = models.CharField(db_column='Category', max_length=45)  # Field name made lowercase.
    subclass = models.CharField(db_column='Subclass', max_length=45, blank=True, null=True)  # Field name made lowercase.
    summary = models.TextField(db_column='Summary')  # Field name made lowercase.
    address = models.CharField(max_length=45, blank=True, null=True)
    file = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource'
        app_label = 'website'


class ResourceCategory(models.Model):
    category = models.CharField(db_column='Category', max_length=45)  # Field name made lowercase.
    subclass = models.CharField(db_column='Subclass', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resource_category'
        app_label = 'website'


class Reviewer(models.Model):
    lexeme_id = models.IntegerField()
    timestamp = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviewer'
        app_label = 'website'
