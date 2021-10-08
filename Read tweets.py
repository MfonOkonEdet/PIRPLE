import json
#Program That Reads Text File With Various Tweets
tweetsList = []
uniqueWordsList = ["good","mind","car","traffic","happy","boy","girl","man","woman"]
valueCountList = []
counter= 0

for i in range(10):
    if counter <= 9:
        Tweets = input("\nTweets for today:  ")   
        tweetsList.append(Tweets)
    counter += 1
# Creating Tweets file
with open("Tweets.txt","w") as tweetsFile:
    for copy in tweetsList:
        tweetsFile.write(copy+ "\n")
with open("Tweets.txt","r") as tweetsFile:
    tweetText = tweetsFile.read()
#breaking down words in tweetsFile
tweetText = tweetText.lower()
tweetWords = tweetText.split()
tweetWords = [tweetWord.strip(".,!()[]") for tweetWord in tweetWords]
tweetWords = [tweetWord.replace("'s","") for tweetWord in tweetWords]
#Extracting the Unique words
for tweetWord in tweetWords:
    if tweetWord in uniqueWordsList:
        valueCountList.append(tweetWord)
#Sorting Unique Words alphabetically
valueCountList.sort()

#creating a dicionary to get the key:value of valueCountList
uniqueWords_Dictionary = {}
for words in valueCountList:
    if words in uniqueWords_Dictionary:
        uniqueWords_Dictionary[words] += 1
    else:
        uniqueWords_Dictionary[words] = 1


# creating textFile containing uniqueWords:counts
with open("Unique Words.txt","w") as uniqueWords_File:
    json.dump(uniqueWords_Dictionary, uniqueWords_File)
with open("Unique Words.txt","r") as uniqueWords_File:
    print("\nUnique Words with Counts of Repetition:\n"+uniqueWords_File.read())

# median amount of Unique Words File
median = str(len(valueCountList)/2)
with open("Median.txt","w") as medianValue:
    medianValue.write(median)
with open("Median.txt","r") as medianValue:
    print("\nMedian Amount of Unique Words:\n"+medianValue.read())


                





