import os

LOG_DIR = '/var/log/graphite'
if os.getenv("CARBONLINK_HOSTS"):
    CARBONLINK_HOSTS = os.getenv("CARBONLINK_HOSTS").split(',')

if os.getenv("CLUSTER_SERVERS"):
    CLUSTER_SERVERS = os.getenv("CLUSTER_SERVERS").split(',')

if os.getenv("MEMCACHE_HOSTS"):
    MEMCACHE_HOSTS = os.getenv("MEMCACHE_HOSTS").split(',')

if os.getenv("WHISPER_DIR"):
    WHISPER_DIR = os.getenv("WHISPER_DIR")

if os.getenv("SECRET_KEY"):
    SECRET_KEY = os.getenv("SECRET_KEY")
else:
    SECRET_KEY = "secret_key"
