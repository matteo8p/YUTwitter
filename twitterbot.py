import tweepy
import time, sys
import twitterAnalyzer
import urbandictionary
import json

print("Running YUTwitter Script!")

CONSUMER_KEY = "ADD CONSUMER KEY HERE"
CONSUMER_SECRET = "SECRET KEY"
ACCESS_KEY = "ACCESS KEY"
ACCESS_SECRET = "ACCESS SECRET"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# Create API object
api = tweepy.API(auth)

# Every window is 15 minutes. loopPerWindow cannot be greater than 15
loopPerWindow = 15
pauseTimeinSeconds = 900 / loopPerWindow

# Check if Rate Limit Error will happen
if loopPerWindow > 15 or 900 % loopPerWindow != 0:
    print("ERROR: loopPerWindow greater than 15 OR pauseTimeinSeconds not whole number")
    sys.exit()

#Returns the number of remaining "Followers" API Calls.
def findRemainingAPICalls():
    loadStat = str(api.rate_limit_status("followers"))
    loadStat = loadStat.replace("\'", "\"")
    jsonFile = json.loads(loadStat)

    return jsonFile["resources"]["followers"]["/followers/ids"]["remaining"]

#Initiate
before = api.followers()
#print("Current Followers: {}".format(before))
print("Initiating. Program begins in {} seconds".format(pauseTimeinSeconds))
time.sleep(pauseTimeinSeconds)
print("======================================================================")

#Loop
while(True):
    after = api.followers()
    newFollowers = twitterAnalyzer.findNewFollowers(before, after) #list of 'User' objects
    unFollowers = twitterAnalyzer.findUnfollowers(before, after)   #list of 'User' objects

    print("Number of Calls remaining this window: {}".format(findRemainingAPICalls()))
    print("Current Followers: {}".format(after))

    print("New Followers: {}".format(newFollowers))
    print("People who Unfollowed: {}".format(unFollowers))

    #TODO: create method that tweets the names of the people that had just unfollowed you.

    # if len(unFollowers) > 0:
    #     message = ""
    #
    #     for unFollower in unFollowers:
    #         message += "@" + unFollower.screen_name + " "
    #
    #     message += "Why did you unfollow me?!? That's super rude of you."
    #     api.update_status(message)
    #     print("Status updated. Message: {}".format(message))

    #TODO: create method that tweets the names of the people that had just followed you.

    if len(newFollowers) > 0:

        for newFollower in newFollowers:
            firstName = newFollower.name.split(" ")[0]
            message = "@{} Hello {}, your name means: {}".format(newFollower.screen_name, firstName, urbandictionary.findDefinition(firstName))
            api.update_status(message)
        print("Status updated. Message: {}".format(message))

    #TODO: link to twilio to send a text whenever someone new follows you.



    #reset
    before = after
    for timeCount in range(0, int(pauseTimeinSeconds)):
        if timeCount % 5 == 0:
            print("Next Check in: {} seconds".format(pauseTimeinSeconds - timeCount))
        time.sleep(1)

    print("======================================================================")








