#Team Gucci Swag -- Nicholas Ng, Sebastian Cain
#IntroCS2 pd1
#Hw35 -- Put Your Plan Into Action
#2015-04-26
import random

'''
Approach:
1. Define lists of each type of word
2. Set local variables equal to those lists
3. Find each instance of <WORDTYPE> and replace it with an actual word
4, Return the story with the new words inserted

'''

nounlist=['pen','ball','dog','cat','truck']
adverblist=['quickly','slowly','stupidly','easily']
verblist=['ran','jumped','slept','power-walked','jay-walked','moonwalked']
adjectivelist=['smelly','dirty','tired','stupid','useless','friendly']

sen1 = "<HERO> was walking around on a <ADJECTIVE> day when he spotted a <NOUN>, who was about to be run over by a <NOUN>. "
sen2 = "<HERO> attempted tp save the poor thing, but then a <VILLIAN> stepped out of the shadows and shot bullets at <HERO>. "
sen3 = "<HERO> dodged the bullets, but it slowed him down. "
sen4 = "<HERO> attempted to catch <VILLIAN>, but he was distracted by the car pileup and <VILLIAN> slipped into the shadows. "
story = sen1 + sen2 + sen3 + sen4

def fillblanks(story):
    nouns=nounlist
    adjectives=adjectivelist
    verbs=verblist
    adverbs=adverblist
    while story.count("<NOUN>") > 0:
        story=story.replace("<NOUN>" , nouns.pop(random.randrange(len(nouns))), 1)
    while story.count("<ADVERB>") > 0:
        story=story.replace("<ADVERB>" , adverbs.pop(random.randrange(len(adverbs))), 1)
    while story.count("<VERB>") > 0:
        story=story.replace("<VERB>" , verbs.pop(random.randrange(len(verbs))), 1)
    while story.count("<ADJECTIVE>") > 0:
        story=story.replace("<ADJECTIVE>" , adjectives.pop(random.randrange(len(adjectives))), 1)
    return story
print fillblanks(story)        

def test():
    return "foo" in "fooey"

print test()
