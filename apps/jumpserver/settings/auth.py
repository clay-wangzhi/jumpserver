# -*- coding: utf-8 -*-
#
import os
import ldap
from django.utils.translation import ugettext_lazy as _

from ..const import CONFIG, PROJECT_DIR

# OTP settings
OTP_ISSUER_NAME = CONFIG.OTP_ISSUER_NAME
OTP_VALID_WINDOW = CONFIG.OTP_VALID_WINDOW

# Auth LDAP settings
AUTH_LDAP = CONFIG.AUTH_LDAP
AUTH_LDAP_SERVER_URI = CONFIG.AUTH_LDAP_SERVER_URI
AUTH_LDAP_BIND_DN = CONFIG.AUTH_LDAP_BIND_DN
AUTH_LDAP_BIND_PASSWORD = CONFIG.AUTH_LDAP_BIND_PASSWORD
AUTH_LDAP_SEARCH_OU = CONFIG.AUTH_LDAP_SEARCH_OU
AUTH_LDAP_SEARCH_FILTER = CONFIG.AUTH_LDAP_SEARCH_FILTER
AUTH_LDAP_START_TLS = CONFIG.AUTH_LDAP_START_TLS
AUTH_LDAP_USER_ATTR_MAP = CONFIG.AUTH_LDAP_USER_ATTR_MAP
AUTH_LDAP_USER_QUERY_FIELD = 'username'
AUTH_LDAP_GLOBAL_OPTIONS = {
    ldap.OPT_X_TLS_REQUIRE_CERT: ldap.OPT_X_TLS_NEVER,
    ldap.OPT_REFERRALS: CONFIG.AUTH_LDAP_OPTIONS_OPT_REFERRALS
}
LDAP_CERT_FILE = os.path.join(PROJECT_DIR, "data", "certs", "ldap_ca.pem")
if os.path.isfile(LDAP_CERT_FILE):
    AUTH_LDAP_GLOBAL_OPTIONS[ldap.OPT_X_TLS_CACERTFILE] = LDAP_CERT_FILE
# AUTH_LDAP_GROUP_SEARCH_OU = CONFIG.AUTH_LDAP_GROUP_SEARCH_OU
# AUTH_LDAP_GROUP_SEARCH_FILTER = CONFIG.AUTH_LDAP_GROUP_SEARCH_FILTER
# AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
#    AUTH_LDAP_GROUP_SEARCH_OU, ldap.SCOPE_SUBTREE, AUTH_LDAP_GROUP_SEARCH_FILTER
# )
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_TIMEOUT: CONFIG.AUTH_LDAP_CONNECT_TIMEOUT,
    ldap.OPT_NETWORK_TIMEOUT: CONFIG.AUTH_LDAP_CONNECT_TIMEOUT
}
AUTH_LDAP_CACHE_TIMEOUT = 1
AUTH_LDAP_ALWAYS_UPDATE_USER = True

AUTH_LDAP_SEARCH_PAGED_SIZE = CONFIG.AUTH_LDAP_SEARCH_PAGED_SIZE
AUTH_LDAP_SYNC_IS_PERIODIC = CONFIG.AUTH_LDAP_SYNC_IS_PERIODIC
AUTH_LDAP_SYNC_INTERVAL = CONFIG.AUTH_LDAP_SYNC_INTERVAL
AUTH_LDAP_SYNC_CRONTAB = CONFIG.AUTH_LDAP_SYNC_CRONTAB
AUTH_LDAP_USER_LOGIN_ONLY_IN_USERS = CONFIG.AUTH_LDAP_USER_LOGIN_ONLY_IN_USERS


# ==============================================================================
# 认证 OpenID 配置参数
# 参考: https://django-oidc-rp.readthedocs.io/en/stable/settings.html
# ==============================================================================
AUTH_OPENID = CONFIG.AUTH_OPENID
BASE_SITE_URL = CONFIG.BASE_SITE_URL
AUTH_OPENID_CLIENT_ID = CONFIG.AUTH_OPENID_CLIENT_ID
AUTH_OPENID_CLIENT_SECRET = CONFIG.AUTH_OPENID_CLIENT_SECRET
AUTH_OPENID_PROVIDER_ENDPOINT = CONFIG.AUTH_OPENID_PROVIDER_ENDPOINT
AUTH_OPENID_PROVIDER_AUTHORIZATION_ENDPOINT = CONFIG.AUTH_OPENID_PROVIDER_AUTHORIZATION_ENDPOINT
AUTH_OPENID_PROVIDER_TOKEN_ENDPOINT = CONFIG.AUTH_OPENID_PROVIDER_TOKEN_ENDPOINT
AUTH_OPENID_PROVIDER_JWKS_ENDPOINT = CONFIG.AUTH_OPENID_PROVIDER_JWKS_ENDPOINT
AUTH_OPENID_PROVIDER_USERINFO_ENDPOINT = CONFIG.AUTH_OPENID_PROVIDER_USERINFO_ENDPOINT
AUTH_OPENID_PROVIDER_END_SESSION_ENDPOINT = CONFIG.AUTH_OPENID_PROVIDER_END_SESSION_ENDPOINT
AUTH_OPENID_PROVIDER_SIGNATURE_ALG = CONFIG.AUTH_OPENID_PROVIDER_SIGNATURE_ALG
AUTH_OPENID_PROVIDER_SIGNATURE_KEY = CONFIG.AUTH_OPENID_PROVIDER_SIGNATURE_KEY
AUTH_OPENID_SCOPES = CONFIG.AUTH_OPENID_SCOPES
AUTH_OPENID_ID_TOKEN_MAX_AGE = CONFIG.AUTH_OPENID_ID_TOKEN_MAX_AGE
AUTH_OPENID_ID_TOKEN_INCLUDE_CLAIMS = CONFIG.AUTH_OPENID_ID_TOKEN_INCLUDE_CLAIMS
AUTH_OPENID_USE_STATE = CONFIG.AUTH_OPENID_USE_STATE
AUTH_OPENID_USE_NONCE = CONFIG.AUTH_OPENID_USE_NONCE

AUTH_OPENID_SHARE_SESSION = CONFIG.AUTH_OPENID_SHARE_SESSION
AUTH_OPENID_IGNORE_SSL_VERIFICATION = CONFIG.AUTH_OPENID_IGNORE_SSL_VERIFICATION
AUTH_OPENID_ALWAYS_UPDATE_USER = CONFIG.AUTH_OPENID_ALWAYS_UPDATE_USER
AUTH_OPENID_AUTH_LOGIN_URL_NAME = 'authentication:openid:login'
AUTH_OPENID_AUTH_LOGIN_CALLBACK_URL_NAME = 'authentication:openid:login-callback'
AUTH_OPENID_AUTH_LOGOUT_URL_NAME = 'authentication:openid:logout'
# ==============================================================================

# Radius Auth
AUTH_RADIUS = CONFIG.AUTH_RADIUS
AUTH_RADIUS_BACKEND = 'authentication.backends.radius.RadiusBackend'
RADIUS_SERVER = CONFIG.RADIUS_SERVER
RADIUS_PORT = CONFIG.RADIUS_PORT
RADIUS_SECRET = CONFIG.RADIUS_SECRET

# CAS Auth
AUTH_CAS = CONFIG.AUTH_CAS
CAS_SERVER_URL = CONFIG.CAS_SERVER_URL
CAS_VERIFY_SSL_CERTIFICATE = False
CAS_LOGIN_URL_NAME = "authentication:cas:cas-login"
CAS_LOGOUT_URL_NAME = "authentication:cas:cas-logout"
CAS_LOGIN_MSG = None
CAS_LOGGED_MSG = None
CAS_IGNORE_REFERER = True
CAS_LOGOUT_COMPLETELY = CONFIG.CAS_LOGOUT_COMPLETELY
CAS_VERSION = CONFIG.CAS_VERSION
CAS_ROOT_PROXIED_AS = CONFIG.CAS_ROOT_PROXIED_AS
CAS_CHECK_NEXT = lambda _next_page: True

# SSO Auth
AUTH_SSO = CONFIG.AUTH_SSO
AUTH_SSO_AUTHKEY_TTL = CONFIG.AUTH_SSO_AUTHKEY_TTL

AUTH_WECOM = CONFIG.AUTH_WECOM
WECOM_CORPID = ''
WECOM_AGENTID = ''
WECOM_CORPSECRET = ''


AUTH_DINGTALK = CONFIG.AUTH_DINGTALK
DINGTALK_AGENTID = ''
DINGTALK_APPKEY = ''
DINGTALK_APPSECRET = ''


# Other setting
TOKEN_EXPIRATION = CONFIG.TOKEN_EXPIRATION
LOGIN_CONFIRM_ENABLE = CONFIG.LOGIN_CONFIRM_ENABLE
OTP_IN_RADIUS = CONFIG.OTP_IN_RADIUS


AUTH_BACKEND_MODEL = 'django.contrib.auth.backends.ModelBackend'
AUTH_BACKEND_PUBKEY = 'authentication.backends.pubkey.PublicKeyAuthBackend'
AUTH_BACKEND_LDAP = 'authentication.backends.ldap.LDAPAuthorizationBackend'
AUTH_BACKEND_OIDC_PASSWORD = 'jms_oidc_rp.backends.OIDCAuthPasswordBackend'
AUTH_BACKEND_OIDC_CODE = 'jms_oidc_rp.backends.OIDCAuthCodeBackend'
AUTH_BACKEND_RADIUS = 'authentication.backends.radius.RadiusBackend'
AUTH_BACKEND_CAS = 'authentication.backends.cas.CASBackend'
AUTH_BACKEND_SSO = 'authentication.backends.api.SSOAuthentication'
AUTH_BACKEND_WECOM = 'authentication.backends.api.WeComAuthentication'
AUTH_BACKEND_DINGTALK = 'authentication.backends.api.DingTalkAuthentication'


AUTHENTICATION_BACKENDS = [AUTH_BACKEND_MODEL, AUTH_BACKEND_PUBKEY]

if AUTH_CAS:
    AUTHENTICATION_BACKENDS.insert(0, AUTH_BACKEND_CAS)
if AUTH_OPENID:
    AUTHENTICATION_BACKENDS.insert(0, AUTH_BACKEND_OIDC_PASSWORD)
    AUTHENTICATION_BACKENDS.insert(0, AUTH_BACKEND_OIDC_CODE)
if AUTH_RADIUS:
    AUTHENTICATION_BACKENDS.insert(0, AUTH_BACKEND_RADIUS)
if AUTH_SSO:
    AUTHENTICATION_BACKENDS.append(AUTH_BACKEND_SSO)
if AUTH_WECOM:
    AUTHENTICATION_BACKENDS.append(AUTH_BACKEND_WECOM)
if AUTH_DINGTALK:
    AUTHENTICATION_BACKENDS.append(AUTH_BACKEND_DINGTALK)


ONLY_ALLOW_EXIST_USER_AUTH = CONFIG.ONLY_ALLOW_EXIST_USER_AUTH
ONLY_ALLOW_AUTH_FROM_SOURCE = CONFIG.ONLY_ALLOW_AUTH_FROM_SOURCE
