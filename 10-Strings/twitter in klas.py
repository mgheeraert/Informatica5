tweet = input('geef tweet: ')

i_hashtag = tweet.find('#')

while i_hashtag != -1:
    #tweet afknippen net na #
    tweet = tweet[i_hashtag +1:]
    i_spatie = tweet.find(' ')

    #hashtag uitknippen (en printen)
    print(tweet[:i_spatie])

     # op zoek naar volgende hashtag
    i_hashtag = tweet.find('#')
