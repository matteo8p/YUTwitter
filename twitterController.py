import tweepy

CONSUMER_KEY = "ghdBH1x1SXFy8gC0jKq4A7blB"
CONSUMER_SECRET = "1QRkHaBhZStusKnUByviFvdPpurvoVVaHi4JNShdhBN37pNJyO"
ACCESS_KEY = "1215694679871610880-nuduRMtClzBXIUz3c2JUFCrkaah5ub"
ACCESS_SECRET = "oTMbPeoJiGapcwIUY4o0iyENxNo5al9MMxwybkKozaGr5"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# Create API object
api = tweepy.API(auth)

followers = api.followers()
follower = followers[0]
print(follower)
print(follower.name.split(" ")[0])
