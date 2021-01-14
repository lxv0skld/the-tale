
import os
import sys

TESTS_RUNNING = 'test' in sys.argv or 'testserver' in sys.argv

RUNSERVER_RUNNING = 'runserver' in sys.argv

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
HOME_DIR = os.getenv("HOME")

PROJECT_MODULE = os.path.basename(PROJECT_DIR)

################################################################
# typeguard and coulson MUST be initialized before any poject related imports
# and only for tests
################################################################
if TESTS_RUNNING:
    # TODO: commented to test coulson
    # from typeguard.importhook import install_import_hook
    # install_import_hook('the_tale')

    from coulson import tracers, mergers, namespaces

    spaces = [namespaces.Namespace('the_tale_models',
                                   filter=namespaces.Chained([namespaces.ModulePath(PROJECT_DIR),
                                                              namespaces.ModulePathRE(r'models\.py')]),
                                   mergers=[mergers.SkipVariables(['self',

                                                                   # CHECK
                                                                   'state',
                                                                   'comment',
                                                                   'description',
                                                                   'created_at_turn',
                                                                   'data',
                                                                   'uid',
                                                                   'account',
                                                                   'hero',
                                                                   'key',

                                                                   ]),
                                            mergers.TypeDependency()]),

              namespaces.Namespace('the_tale_forms',
                                   filter=namespaces.Chained([namespaces.ModulePath(PROJECT_DIR),
                                                              namespaces.ModulePathRE(r'forms\.py')]),
                                   mergers=[mergers.SkipVariables(['self',
                                                                   'label',
                                                                   'group',

                                                                   # add annotations
                                                                   'PREFERENCE',
                                                                   'WORD_TYPE',
                                                                   'sort_key',

                                                                   # CHECK
                                                                   'value',
                                                                   'key',
                                                                   'description',
                                                                   'name',
                                                                   'text',
                                                                   'archetype',
                                                                   'abilities',

                                                                   # properties
                                                                   'errors_container',

                                                                   # modules
                                                                   'c',

                                                                   # WHAT???
                                                                   '.0',

                                                                   ]),
                                            mergers.TypeDependency()]),

              namespaces.Namespace('the_tale_relations',
                                   filter=namespaces.Chained([namespaces.ModulePath(PROJECT_DIR),
                                                              namespaces.ModulePathRE(r'relations\.py')]),
                                   mergers=[mergers.SkipVariables(['self',

                                                                   # CHECK
                                                                   'male_text',
                                                                   'female_text',
                                                                   'attribute_value',
                                                                   'delta',
                                                                   'attribute',
                                                                   'abilities',
                                                                   'action_points_cost_modifier',
                                                                   'clan_permission',
                                                                   'availability',
                                                                   'power_cost_modifier',
                                                                   'help',
                                                                   'description',
                                                                   'base',
                                                                   'x',
                                                                   'y',
                                                                   'records',
                                                                   'utg_type',
                                                                   'substitutions',
                                                                   'var',

                                                                   # intersections with modules:
                                                                   'linguistics_restrictions',
                                                                   'attributes',

                                                                   # WHAT???
                                                                   '.0']),
                                            mergers.TypeDependency()]),

              namespaces.Namespace('the_tale',
                                   filter=namespaces.ModulePath(PROJECT_DIR),
                                   mergers=[mergers.SkipVariables(['self',

                                                                   # meta
                                                                   'settings',
                                                                   'default_value',
                                                                   'default',
                                                                   'DEFAULT_VALUE',
                                                                   'name',
                                                                   'handler',
                                                                   'properties',
                                                                   'form',
                                                                   'total',  # function & property
                                                                   'text',
                                                                   'permissions',
                                                                   'role',
                                                                   'race',
                                                                   'experience',
                                                                   'religion_type',
                                                                   'hero',  # onetoonefield, foreignkey, etc
                                                                   'length',
                                                                   'order',
                                                                   'apply',
                                                                   'verbose_units',
                                                                   'id',
                                                                   'info',
                                                                   'effects',
                                                                   'record',
                                                                   'deserializer',
                                                                   'serializer',
                                                                   'formatter',
                                                                   'modifier',
                                                                   'MODIFIER',
                                                                   'priority',
                                                                   'probability',
                                                                   'COHERENCE',
                                                                   'all',
                                                                   'level',
                                                                   'group',
                                                                   'base_value',
                                                                   'slug',
                                                                   'money',
                                                                   'habit_multiplier',
                                                                   'rarity_delta',
                                                                   'can_be_freezed',
                                                                   'work_when_dead',
                                                                   'effect',
                                                                   'path',
                                                                   'forms',
                                                                   'nick',
                                                                   'field',
                                                                   'single',
                                                                   'tag_class',
                                                                   'example',
                                                                   'tag',
                                                                   'category',
                                                                   'last_thread',
                                                                   'last_poster',
                                                                   'author',
                                                                   'thread',
                                                                   'Membership',
                                                                   'technical',
                                                                   'ABILITIES',
                                                                   'utg_name_form',
                                                                   'source',
                                                                   'amount',
                                                                   'objects',
                                                                   'achievements',
                                                                   'widget',
                                                                   # 'errors_container',
                                                                   'caption',
                                                                   'renderer',
                                                                   'depends_on',
                                                                   'chronicle',
                                                                   'url',
                                                                   'News',
                                                                   'subcategory',
                                                                   'members_number',
                                                                   'MembershipRequest',
                                                                   'Clan',
                                                                   'items',
                                                                   'artifact_type',
                                                                   'element',
                                                                   'utg_name',
                                                                   'item',
                                                                   'variable',
                                                                   'chronicle_on_accepted',
                                                                   'approved',
                                                                   'Event',
                                                                   'meta_object',
                                                                   'el',
                                                                   'place',
                                                                   'terrain',
                                                                   'health',
                                                                   'Actor',
                                                                   'common',
                                                                   'peacefulness',
                                                                   'STATE',
                                                                   'NAME',
                                                                   'person',
                                                                   'action_id',
                                                                   'action',
                                                                   'is_processed',
                                                                   'quest',
                                                                   'verbose_value',
                                                                   'is_active',
                                                                   'experience_modifier',
                                                                   'max_health',
                                                                   'intellect_level',
                                                                   'communication_verbal',
                                                                   'size',
                                                                   'template',
                                                                   'result',
                                                                   'Person',
                                                                   'persons',
                                                                   'emissary',
                                                                   'safety',
                                                                   'searching_quest',  # bool & property
                                                                   'values',
                                                                   'mob_type',
                                                                   'communication_gestures',
                                                                   'place_1',
                                                                   'place_2',
                                                                   'Building',
                                                                   'Place',
                                                                   'statistics',
                                                                   'cells',
                                                                   'battles_per_turn',
                                                                   'building',
                                                                   'roads',
                                                                   'risk_level',
                                                                   'additional_abilities',
                                                                   'is_eatable',
                                                                   'MobRecord',
                                                                   'special_effect',
                                                                   'preference_rating',
                                                                   'mob',
                                                                   'abbr',
                                                                   'relation',
                                                                   'form_class',
                                                                   'rarity',
                                                                   'CURRENCY',
                                                                   'bill',
                                                                   'places',
                                                                   'ModeratorForm',
                                                                   'UserForm',
                                                                   'actors',
                                                                   'schema',
                                                                   'k',
                                                                   'SocialConnection',
                                                                   'transport',
                                                                   'communication_telepathic',
                                                                   'Hero',
                                                                   'diary',
                                                                   'Road',
                                                                   'map_info',
                                                                   'artifacts',
                                                                   'CreateClan',
                                                                   'Emissary',
                                                                   'ATTRIBUTE',
                                                                   'r',
                                                                   'choices',
                                                                   # 'label',
                                                                   'choices',
                                                                   'base_name',
                                                                   'person_1',
                                                                   'person_2',
                                                                   'resource_from',
                                                                   'resource_from_delta',
                                                                   'resource_to',
                                                                   'resource_to_delta',
                                                                   'declined_by',
                                                                   'forum_thread',
                                                                   'user_form_initials',
                                                                   'owner',
                                                                   'premium_end_at',
                                                                   'cards_receive_mode',
                                                                   'cost',
                                                                   'purchase',
                                                                   'logic',
                                                                   'Post',
                                                                   'body',
                                                                   'friend_1',
                                                                   'friend_2',
                                                                   'HeroPreferences',
                                                                   'ArtifactRecord',
                                                                   'CompanionRecord',
                                                                   'resource_1',
                                                                   'resource_2',
                                                                   'Bill',
                                                                   'days',
                                                                   'news_subscription',
                                                                   'personal_messages_subscription',
                                                                   'application_info',
                                                                   'PERMISSION',
                                                                   'index',
                                                                   'Account',
                                                                   'email',
                                                                   'password',
                                                                   'application_name',
                                                                   'gender',
                                                                   'voter',
                                                                   'forum_subcategory',
                                                                   'points',
                                                                   'barrier',
                                                                   'motto',
                                                                   'orientation',
                                                                   'attribute',
                                                                   'pgf',
                                                                   'linguistics_restrictions',
                                                                   'base',
                                                                   'environment',
                                                                   'movement',
                                                                   'emissaries',
                                                                   'sort_key',

                                                                   # WHAT???
                                                                   '.0',

                                                                   # object & property
                                                                   # a lot of such intersection see in upper names
                                                                   'declined_bill',
                                                                   'new_place',
                                                                   'permanent_purchases',
                                                                   'clan',
                                                                   'item_1',
                                                                   'item_2',
                                                                   'item_3',
                                                                   'full_name',
                                                                   'collection',
                                                                   'kit',
                                                                   'code',
                                                                   'state',
                                                                   'uid',
                                                                   'availability',
                                                                   'kits',
                                                                   'percents',

                                                                   # functions & properties
                                                                   # a lot of such intersection see in upper names
                                                                   'power_required',
                                                                   'spend_amount',
                                                                   'might_pvp_effectiveness_bonus',
                                                                   'move_speed',
                                                                   'number',
                                                                   'is_empty',
                                                                   'message',
                                                                   'can_participate_in_pvp',
                                                                   'linguistics_restrictions_constants',
                                                                   'is_removed',
                                                                   'item_full_type',
                                                                   'is_moderator',
                                                                   'can_vote',

                                                                   # TODO: add annotations
                                                                   'ACTIVATION_TYPE',
                                                                   'TYPE',
                                                                   'AVAILABILITY',
                                                                   'LOGIC_TYPE',
                                                                   '_model_class',
                                                                   'EFFECT_NAME',
                                                                   'EFFECT_TYPE',
                                                                   'METHOD_NAME',
                                                                   'ABILITY',
                                                                   'CHECK_MODIFIER',
                                                                   'EXCEPTION',
                                                                   'SETTINGS_KEY',
                                                                   'restrictions',
                                                                   'TYPE_CAPTION',
                                                                   'DESCRIPTION',
                                                                   'ACTOR',
                                                                   'NORMAL_POWER',
                                                                   'POSITIVE_TARGET_TYPE',
                                                                   'NEGATIVE_TARGET_TYPE',
                                                                   'ACTOR_TYPE',
                                                                   'PROTOTYPE',
                                                                   'TARGET_TYPE',
                                                                   'coherence',
                                                                   'honor',
                                                                   'TEXTGEN_TYPE',
                                                                   'MESSAGES_LOG_LENGTH',
                                                                   'CONTEXT_MANAGER',
                                                                   'CAPTION',
                                                                   'PROPERTY',
                                                                   # 'WORD_TYPE',
                                                                   'RELATION',
                                                                   'VALUE_COLUMN',
                                                                   'expected_defaults',
                                                                   'DIALOG_ERROR_TEMPLATE',
                                                                   'ERROR_TEMPLATE',
                                                                   'choice',
                                                                   'y_value_range',
                                                                   'y2_value_range',

                                                                   # CHECK
                                                                   'summand_right',
                                                                   'summand_left',
                                                                   'multiplier_right',
                                                                   'ordering',
                                                                   'readonly_fields',
                                                                   'kwargs',
                                                                   'args',
                                                                   'html',
                                                                   'fields',
                                                                   'MULTIPLIER',
                                                                   'row_id',
                                                                   'columns',
                                                                   'rows',
                                                                   'rows_values',
                                                                   'rows_items',
                                                                   'columns_values',
                                                                   'classes_list',
                                                                   'start',
                                                                   'best_base',
                                                                   'NAME_REGEX',
                                                                   'PROCESSING',
                                                                   'coerce_method',
                                                                   'iterated_keys',
                                                                   'method',
                                                                   'argument',
                                                                   'title',
                                                                   'methods',
                                                                   'candidates',
                                                                   'CHOICES',
                                                                   'pdf',
                                                                   'data',
                                                                   'description',
                                                                   'x',
                                                                   'y',
                                                                   'records',
                                                                   'key',
                                                                   'value',
                                                                   'id_',
                                                                   'field_id',

                                                                   # sibling classes
                                                                   'application',
                                                                   'reactor',
                                                                   'processor',

                                                                   # module & function/object
                                                                   'json',
                                                                   'connection',
                                                                   'ability',
                                                                   'workers',
                                                                   'time',
                                                                   'max_ability_points_number',
                                                                   'f',
                                                                   'tags',
                                                                   'uuid',
                                                                   'exceptions',
                                                                   'power',
                                                                   'generator',
                                                                   'c',
                                                                   'companions',
                                                                   'container',
                                                                   'collections',
                                                                   'attributes',
                                                                   'func',
                                                                   'storage',

                                                                   # callables: class & function & classmethod
                                                                   'cancel_sell_lot',
                                                                   'pay',
                                                                   'send_mails',
                                                                   'buy',
                                                                   'show_dialog',
                                                                   'change_role',
                                                                   'request_friendship',
                                                                   'edit',
                                                                   'remove',
                                                                   'request_dialog',
                                                                   'new',
                                                                   'other',
                                                                   'delete',
                                                                   'update_settings',
                                                                   'checker',
                                                                   'view',
                                                                   'show',
                                                                   'stop',
                                                                   'get_structure',
                                                                   'form_choices',
                                                                   'modify_attribute',
                                                                   'get_last_threads',
                                                                   'on_before_logout',
                                                                   'deserialize',
                                                                   'update',
                                                                   'create',
                                                                   'live_query',
                                                                   'normalize_email',
                                                                   'recalculate',
                                                                   'feed']),
                                            mergers.TypeDependency()])]
    tracer = tracers.Tracer(spaces)
    tracer.start_tracing()
################################################################


import smart_imports

smart_imports.all()


META_CONFIG_FILE = os.path.join(PROJECT_DIR, 'meta_config.json')
META_CONFIG = utils_meta_config.MetaConfig(config_path=META_CONFIG_FILE)

DEBUG = False

SENTRY_RAVEN_CONFIG = None

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'the_tale',
        'USER': 'the_tale',
        'PASSWORD': 'the_tale',
        'HOST': '',
        'PORT': '',
        'CONN_MAX_AGE': 60 * 60  # close connection after an hour
    }
}

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'ru'

CSRF_FAILURE_VIEW = 'the_tale.urls.handlerCSRF'

CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

SITE_ID = 1
SITE_URL = 'local.the-tale'

SOCIAL_VK_GROUP_URL = None
SOCIAL_TWITTER_GROUP_URL = None
SOCIAL_FACEBOOK_GROUP_URL = None

COMMUNITY_PROJECTS = []
SOCIAL_GITHUB_URL = 'https://github.com/the-tale'
SOCIAL_DOCUMENTATION = 'https://docs.the-tale.org'

SOCIAL_DEVELOPER_BLOG = None

CARDS_TUTORIAL = None

X_FRAME_OPTIONS = 'DENY'

ALLOWED_HOSTS = ['localhost',
                 'the-tale.org',
                 '.the-tale.org',
                 'local.the-tale',
                 '.local.the-tale']

AUTH_USER_MODEL = 'accounts.Account'

OWNER = 'Информация о владельце сайта'

PAGE_TITLE = 'Сказка'

API_CLIENT = 'the_tale-%s' % META_CONFIG.version

##############################
# I18N
##############################

USE_I18N = True
USE_L10N = True

SECRET_KEY = 'test secret key, must be replaced'

TT_SECRET = 'test.secret'

GA_CODE = None
MAIL_RU = None

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'


################################
# Mail settings
################################

SERVER_EMAIL = '«Сказка»: системное сообщение <no-reply@example.com>'
ADMINS = ()

EMAIL_NOREPLY = '«Сказка» <no-reply@example.com>'
EMAIL_SUPPORT = '«Сказка» <support@example.com>'
EMAIL_SUPPORT_SHORT = 'support@example.com'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/emails'

################################
# Discord settings
################################

DISCORD_WIDGET_URL = None
DISCORD_INVITE_LINK = None
DISCORD_BIND_COMMAND = 'tt bind'
DISCORD_HELP_COMMAND = 'tt help'
DISCORD_BOT_NAME = 'Смотритель'

################################
# Other settings
################################

APPEND_SLASH = True

TEMPLATES = [{'BACKEND': 'the_tale.common.utils.jinja2.Backend',
              'DIRS': (os.path.join(PROJECT_DIR, 'jinja2'),),
              'APP_DIRS': True,
              'OPTIONS': {
                  'environment': 'the_tale.common.utils.jinja2.create_environment',
                  'autoescape': True,
                  'trim_blocks': True,
                  'auto_reload': DEBUG,
                  'undefined': jinja2.StrictUndefined,
                  'loader': None,
                  'extensions': ['jinja2.ext.loopcontrols'],

                  'context_processors': ('django.contrib.auth.context_processors.auth',
                                         'django.template.context_processors.debug',
                                         'django.template.context_processors.i18n',
                                         'django.template.context_processors.media',
                                         'django.template.context_processors.static',
                                         'the_tale.common.utils.context_processors.common',
                                         'the_tale.portal.context_processors.section',
                                         'the_tale.portal.context_processors.cdn_paths',
                                         'the_tale.game.balance.context_processors.balance',
                                         'the_tale.game.bills.context_processors.bills_context',
                                         'the_tale.linguistics.context_processors.linguistics_context',
                                         'the_tale.guide.context_processors.guide_context',
                                         'the_tale.blogs.context_processors.blogs_context'),
              }},
             {'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'APP_DIRS': True,
              'OPTIONS': {
                  'debug': False,

                  'context_processors': ('django.contrib.auth.context_processors.auth',
                                         'django.template.context_processors.debug',
                                         'django.template.context_processors.i18n',
                                         'django.template.context_processors.media',
                                         'django.template.context_processors.static',
                                         'django.contrib.messages.context_processors.messages')
              }}
             ]


MIDDLEWARE = ('django.middleware.common.CommonMiddleware',
              'django.contrib.sessions.middleware.SessionMiddleware',
              'django.middleware.csrf.CsrfViewMiddleware',
              'django.contrib.auth.middleware.AuthenticationMiddleware',
              'django.contrib.messages.middleware.MessageMiddleware',
              'django.middleware.clickjacking.XFrameOptionsMiddleware',
              'the_tale.common.settings.middleware.SettingsMiddleware',
              'the_tale.accounts.middleware.RegistrationMiddleware',
              'the_tale.accounts.third_party.middleware.ThirdPartyMiddleware',
              'the_tale.accounts.middleware.FirstTimeVisitMiddleware',
              'the_tale.common.utils.middleware.NoCacheMiddleware')

ROOT_URLCONF = 'the_tale.urls'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',

    'the_tale.common.less',
    'the_tale.common.utils',
    'the_tale.common.settings',
    'the_tale.common.old_views',
    'the_tale.common.amqp_queues',
    'the_tale.common.postponed_tasks',
    'the_tale.common.meta_relations',
    'the_tale.common.bbcode',
    'the_tale.common.utilities',
    'the_tale.common.locks',

    'the_tale.post_service',

    'the_tale.accounts.third_party',  # MUST be before 'the_tale.accounts', since strange bug in Django 1.8, when model AccessToken placed in accounts application instead third_party
    'the_tale.accounts',
    'the_tale.accounts.personal_messages',
    'the_tale.accounts.friends',
    'the_tale.accounts.achievements',

    'the_tale.clans',

    'the_tale.guide',

    'the_tale.portal',

    'the_tale.game.chronicle',  # MUST be before game, since the same bug like with the_tale.accounts.third_party
    'the_tale.game',
    'the_tale.game.jobs',
    'the_tale.game.heroes',
    'the_tale.game.actions',
    'the_tale.game.quests',
    'the_tale.game.map',
    'the_tale.game.roads',
    'the_tale.game.places',
    'the_tale.game.artifacts',
    'the_tale.game.mobs',
    'the_tale.game.companions',
    'the_tale.game.persons',
    'the_tale.game.balance',
    'the_tale.game.bills',
    'the_tale.game.ratings',
    'the_tale.game.pvp',
    'the_tale.game.cards',
    'the_tale.game.politic_power',
    'the_tale.game.emissaries',

    'the_tale.news',

    'the_tale.forum',
    'the_tale.blogs',
    'the_tale.collections',
    'the_tale.linguistics',

    'the_tale.finances.shop',
    'the_tale.finances.bank',
    'the_tale.finances.xsolla',

    'the_tale.statistics']


if TESTS_RUNNING:
    # argon password hasher print warnings on time of tests running, so replace it with more fast and more stable hasher
    PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
else:
    PASSWORD_HASHERS = ['django.contrib.auth.hashers.Argon2PasswordHasher',
                        'django.contrib.auth.hashers.PBKDF2PasswordHasher']

###############################
# AMQP
###############################

AMQP_BROKER_HOST = 'localhost'
AMQP_BROKER_USER = 'the_tale'
AMQP_BROKER_PASSWORD = 'the_tale'
AMQP_BROKER_VHOST = '/the_tale'

##############################
# tests
##############################

if TESTS_RUNNING:
    INSTALLED_APPS.append('test_without_migrations')


################
# CACHING
################

CACHES = {'default': {'BACKEND': 'django_redis.cache.RedisCache',
                      'LOCATION': 'unix:///var/run/redis/redis.sock',
                      'OPTIONS': {
                          'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                          'SERIALIZER': 'django_redis.serializers.json.JSONSerializer'}}}


MAINTENANCE_FILE = '/var/www/the_tale/maintenance.html'


try:
    from the_tale.settings_local import *  # pylint: disable=W0403,W0401,W0614
except Exception:  # pylint: disable=W0702,W0703
    pass


if SENTRY_RAVEN_CONFIG:
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(SENTRY_RAVEN_CONFIG['dsn'],
                    integrations=[DjangoIntegration()])


if RUNSERVER_RUNNING:
    INSTALLED_APPS.remove('django.contrib.staticfiles')


if TESTS_RUNNING:
    GAME_ENABLE_WORKER_HIGHLEVEL = True


if DEBUG:
    for template in TEMPLATES:
        if 'OPTIONS' in template:
            if 'auto_reload' in template['OPTIONS']:
                template['OPTIONS']['auto_reload'] = True
            if 'debug' in template['OPTIONS']:
                template['OPTIONS']['debug'] = True


AMQP_CONNECTION_URL = 'amqp://%s:%s@%s/%s' % (AMQP_BROKER_USER,
                                              AMQP_BROKER_PASSWORD,
                                              AMQP_BROKER_HOST,
                                              AMQP_BROKER_VHOST)


##############################
# static content settings
##############################

STATICFILES_DIRS = [os.path.join(PROJECT_DIR, 'static')]

STATIC_URL = '/static/%s/' % META_CONFIG.static_data_version

STATIC_ROOT = '/var/www/the_tale/static/%s/' % META_CONFIG.static_data_version

CDN_DOMAIN = globals().get('CDN_DOMAIN', 'static.the-tale.org')

STATIC_CDN = '//%s/static/%s/' % (CDN_DOMAIN, META_CONFIG.static_data_version)

ADMIN_MEDIA_PREFIX = '%sadmin/' % STATIC_URL

LESS_FILES_DIR = os.path.join(PROJECT_DIR, 'less')
LESS_DEST_DIR = os.path.join(PROJECT_DIR, 'static', 'css')

CDNS_ENABLED = globals().get('CDNS_ENABLED', False)

CDNS = (('STATIC_TWITTER_BOOTSTRAP',
         '%sbootstrap/' % STATIC_URL, '%sbootstrap/' % STATIC_CDN,
         'https:%sbootstrap/css/bootstrap.min.css' % STATIC_CDN),

        ('STATIC_CONTENT',
         STATIC_URL, STATIC_CDN,
         lambda: 'https:%simages/rss.png?_=%f' % (STATIC_CDN, time.time())),  # prevent url from caching for cases, when portal closed to 503
        )


############################
# LOGGING
############################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s %(asctime)s %(module)s %(process)d] %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'django.server': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'the_tale': {
            'handlers': ['mail_admins', 'console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': False
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        }
    } if not TESTS_RUNNING else {}
}
