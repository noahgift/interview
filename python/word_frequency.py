"""
Problem:  Create a word frequency algorithm without using a library

Copyright:  Noah Gift - 08/06/2016

Intentionally don't coverage edge cases like punction in word split for speed.  
Otherwise would use NLTK library"""

SAMPLE = """Brock Lesnar and Jon Jones share something more in common than just their former billing as UFC 200 headliners.

The banned substance Lesnar tested positive for in in-competition and out-of-competition drug tests in relation to his UFC 200 fight with Mark Hunt was hydroxy-clomiphene, a source with knowledge of the test result confirmed with MMA Fighting on Friday. ESPN and the LA Times were the first to report the news earlier this week.

Jones also tested positive for clomiphene, an anti-estrogen agent, as well as Letrozole, an aromatase inhibitor, before what would have been a main event fight with Daniel Cormier at UFC 200. Jones was pulled from the bout three days before the card after his sample taken June 16 came back. Lesnar's sample taken June 28 didn't come back until after the fight.

Both Lesnar and Jones are facing sanctions from USADA, the body that collected the samples, and the Nevada Athletic Commission, because of the sample collections' proximity to UFC 200, which took place in Las Vegas on July 9.

After an adjudication process, the NAC has the power to suspend and fine both Jones and Lesnar. In Lesnar's case, the fine would be a percentage of his disclosed $2.5 million fight purse. USADA can also suspend them as the UFC's anti-doping partner.

The UFC will not be levying fines against anti-doping offenders, leaving fines up to individual state athletic commissions, according to senior vice president of public relations Dave Sholler.

Lesnar, a current WWE star and former UFC heavyweight champion, made far more than $2.5 million in undisclosed pay at UFC 200 for his win over Hunt, according to reports. That money is likely to go untouched. Hunt has asked the UFC to give him at least half of Lesnar's fight purse because Lesnar was allegedly enhanced in the bout, or he wants to be released from the promotion. The fight would be overturned into a no-contest if the NAC sanctions Lesnar, but it's doubtful Hunt will get his financial wish.

Jones is also not facing any kind of fine from the UFC, just a commission fine. In a case like Chad Mendes, who has been suspended two years by USADA due to testing positive for a banned substance, he will not be fined at all. Mendes' sample came from an out-of-competition test not related to a fight and no commission has jurisdiction.

Money from an NAC fine does not go to the commission, but to a Nevada general fund to be used in other areas. If Lesnar decides to just go back to WWE, never fight again and not pay an NAC fine, the commission would have the ability to seek legal means against him.

Clomiphene, the substance found in both Lesnar and Jones' system, stymies the production of estrogen to stimulate natural testosterone production. It is commonly used as post-cycle therapy (PCT) for those coming of anabolic steroids and works somewhat in the same way as testosterone replacement therapy (TRT). Clinically, it is prescribed to stimulate female ovulation and can also help male virility.

Jones has denied knowingly taking any banned substance and is in the process of having supplements he took tested to determine if any were tainted. Lesnar released a statement to the Associated Press earlier this week"""

def word_count(SAMPLE):
	words = sample.split()
	for word in words:
    	if word in freq:
        	freq[word] += 1
    	else:
        	freq[word] = 1

if __name__ == '__main__':
	main()