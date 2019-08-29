from twittermoto.streamer import Streamer
import config

auth = {
    'consumer_key'        :config.consumer_key,
    'consumer_secret'     :config.consumer_secret,
    'access_token'        :config.access_token,
    'access_token_secret' :config.access_token_secret
}

keywords = ['earthquake', 'terremoto', 'temblor', '地震', 'jishin', 'gempa bumi','aardbeving',
            'lindol', 'Lumilindol', 'lindu', 'zemljotres', 'sismo', 'زلزال', 'زلزلہ']

user_blacklist = ['@Jasmine_Eq00', '@Rewrite_2011', '@RedneckBot']

streamer = Streamer(auth_keys=auth,
                    filename='../tweets.db',
                    keywords=keywords,
                    user_blacklist=user_blacklist)

streamer.stream()
