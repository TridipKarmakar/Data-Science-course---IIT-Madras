malgudi = '''It was Monday morning. Swaminathan was reluctant to opne his eyes. He considered Monday specially unpleasant in the calendar. After the delicious freedom of Saturday and Sunday, it was difficult to get into the Monday mood of work and discipline. He shuddered at the very thought of school: that dismal yellow building; the fire-eyed Vedanayagam, his class-teacher; and the Head Master with thin long cane...'''

list_malgudi = malgudi.split(" ")
for i in range(len(list_malgudi)) :
    list_malgudi[i] = list_malgudi[i].lower()


for i in range(len(list_malgudi)) :
    if ("." in list_malgudi[i]) or (";" in list_malgudi[i]) :
        list_malgudi[i] = list_malgudi[i][:len(list_malgudi[i])-1]

        
set_malgudi = set(list_malgudi)
#print(len(list_malgudi))
#print(len(set_malgudi))        



list_malgudi
set_malgudi

d  = {}

max = 0
answer_word = ''
for x in set_malgudi :
    d[x] = 0 
for x in list_malgudi :
    d[x] = d[x] +1 
    if d[x] > max:
        max = d[x]
        answer_word = x
#print(d)
#print("The maximum value is :" ,max , "and the word is :", answer_word)
    

another_word = '''Sherlock Holmes, fictional character created by the Scottish writer Arthur Conan Doyle. The prototype for the modern mastermind detective, Holmes first appeared in Conan Doyle’s A Study in Scarlet, published in Beeton’s Christmas Annual of 1887. The first collection of the Holmes’ tales, published as The Adventures of Sherlock Holmes, appeared in 1892. As the world’s first and only “consulting detective,” he pursued criminals throughout Victorian and Edwardian London, the south of England, and continental Europe. Although the fictional detective had been anticipated by Edgar Allan Poe’s C. Auguste Dupin and Émile Gaboriau’s Monsieur Lecoq, Holmes made a singular impact upon the popular imagination and has been the most enduring character of the detective story.Illustration of Sherlock Holmes and Dr. Watson Illustration of Sherlock Holmes and Dr. WatsonSherlock Holmes (right) explaining to Dr. Watson what he has deduced from a pipe left behind by a visitor; illustration by Sidney Paget for Sir Arthur Conan Doyle's “The Adventure of the Yellow Face,” The Strand Magazine, 1893. Conan Doyle modeled Holmes’s methods and mannerisms on those of Dr. Joseph Bell, who had been his professor at the University of Edinburgh Medical School. In particular, Holmes’s uncanny ability to gather evidence based upon his honed skills of observation and deductive reasoning paralleled Bell’s method of diagnosing a patient’s disease. Holmes offered some insight into his method, claiming that “When you have excluded the impossible, whatever remains, however improbable, must be the truth.” His detecting abilities become clear, though no less amazing, when explained by his companion, Dr. John H. Watson, who recounts the criminal cases they jointly pursue. Although Holmes rebuffs praise, declaring his abilities to be “elementary,” the oft-quoted phrase “Elementary, my dear Watson,” never actually appears in Conan Doyle’s writings. (See also Sherlock Holmes: Pioneer in Forensic Science.) Watson’s narrations describe Holmes as a very complex and moody character who, although of strict habit, is considerably untidy. His London abode at 221B, Baker Street, is tended by his housekeeper, Mrs. Hudson. Holmes appears to undergo bouts of mania and depression, the latter of which are accompanied by pipe smoking, violin playing, and cocaine use. Throughout the four novels and 56 short stories featuring Holmes, a number of characters recur, including the bumbling Scotland Yard inspector Lestrade; the group of “street Arabs” known as the Baker Street Irregulars, who are routinely employed by Holmes as informers; his even wiser but less ambitious brother, Mycroft; and, most notably, his formidable opponent, Professor James Moriarty, whom Holmes considers the “Napoleon of crime.”British actor Basil Rathbone, as Detective Sherlock Holmes who he portrayed in several movies based on the detective created by Arthur Conan Doyle. Britannica Quiz Fictional Detectives Quiz Claiming that Holmes distracted him “from better things,” Conan Doyle famously in 1893 (“The Final Problem”) attempted to kill him off; during a violent struggle on Switzerland’s Reichenbach Falls, both Holmes and his nemesis, Professor Moriarty, are plunged over the edge of the precipice. Popular outcry against the demise of Holmes was great; men wore black mourning bands, the British royal family was distraught, and more than 20,000 readers cancelled their subscriptions to the popular Strand Magazine, in which Holmes regularly appeared. By popular demand, Conan Doyle resurrected his detective in the story “The Adventure of the Empty House” (1903) Benedict Cumberbatch and Martin Freeman as Holmes and Watson Benedict Cumberbatch and Martin Freeman as Holmes and WatsonThe popular BBC television series Sherlock (2010–17) starred Benedict Cumberbatch and Martin Freeman as the iconic detective Sherlock Holmes and his companion, Dr. John Watson, respectively. The Adventures of Sherlock Holmes poster The Adventures of Sherlock Holmes posterPromotional poster for The Adventures of Sherlock Holmes (1939), starring Basil Rathbone and Nigel Bruce. Holmes remained a popular figure into the 21st century. Among the most popular stories in which he is featured are “The Adventure of the Blue Carbuncle” (1892), “The Adventure of the Speckled Band” (1892), “The Adventure of the Six Napoleons” (1904), and the novel The Hound of the Baskervilles (1902). Holmes’s character has been translated to other media as well, and he is widely known on both stage and screen. The earliest actor to have essayed the role is William Gillette (a founding member of the New York Holmes society still known as the Baker Street Irregulars), who gave several popular theatrical portrayals at the turn of the 20th century. Those who appeared as Holmes onscreen include Basil Rathbone, Peter Cushing, Jeremy Brett, Robert Downey, Jr., Benedict Cumberbatch, and Jonny Lee Miller. Ironically, two of the emblems of Holmes, his meerschaum pipe and deerstalker hat, are not original to Conan Doyle’s writings. Gillette introduced the curved meerschaum pipe (it is thought to have been easier on the actor’s jaw during a long performance), and Sidney Paget the deerstalker (or “fore-and-aft”) cap—it was de rigueur for country living—in more than one illustration for The Strand of Holmes at work on his investigations in the country. In addition to myriad translations of the Holmes adventures throughout the world, a genre of parodies and pastiches has developed based upon the Sherlock Holmes character. The mystery drama television series House (2004–12), starring Hugh Laurie, Omar Epps, and Robert Sean Leonard, was a medical take on Holmes and Watson. Holmes was even played by a dog in the 1990s children’s television show Wishbone (1995–98). An entire collection of more scholarly “higher criticism” of Conan Doyle’s writings was initiated by Ronald Knox’s “Studies in the Literature of Sherlock Holmes” (1912). Subsequent higher criticism is epitomized by the work appearing in The Baker Street Journal (begun 1946), published by the Baker Street Irregulars. Holmes devotees, known as Sherlockians or Holmesians, frequently gather in societies around the world to pay tribute to the master detective with a cultist fervor. The most established of these societies are the invitation-only Baker Street Irregulars, founded in 1934, and the Sherlock Holmes Society of London, founded in 1951 and open to anyone. The latter, which publishes The Sherlock Holmes Journal, traces its origins to the Sherlock Holmes Society that was formed in London in 1934 and counted among its members the scholar and writer Dorothy L. Sayers; it had ceased its activities by the 1940s. Get Unlimited A'''

sherlock_holmes = another_word.split(' ')

for i in range(len(sherlock_holmes)) :
    sherlock_holmes[i] = (sherlock_holmes[i].lower())
    if( "." in sherlock_holmes[i]) and (";" in sherlock_holmes[i] ) : 
        sherlock_holmes[i] = sherlock_holmes[i][:-1]


max = 0
final_word = ''

sherlock_holmes_set = set(sherlock_holmes)
d = {}
for i in sherlock_holmes_set :
    d[i] = 0

for j in sherlock_holmes :
    d[j] = d[j] + 1
    if d[j] > max :
        max = d[j]
        final_word = j

#print(f'The maximum repetaitive word is : {(final_word.upper())}, and the repetation is : {max}' )




d = {}
d["Tridip"] = [93,99,95]
d["Ajit"] = [90,87,90]
d["Supriya"] = [80,98,61]

d = {}

d["Tridip"] = [93,99,95,"tridip97@gmail.com"]
d["Ajit"] = [90,87,90,"ajit76@gmail.com"]
d["Supriya"] = [80,98,61,"supriya67@gmail.com"]
d["Supriya","tridip","Supriya"] = 0 


# print(list(d.items()))


#shorting the value from minimum to maximum 

l = [98,90,1,23,4,5,6,7,8,6]

def sorted_list(l) :
    sorted_list = []
    while(len(l) > 0):
        min = l[0]
        
        for i in l :
            if min > i :
                min = i
        sorted_list.append(min)
        l.remove(min)
    return(sorted_list)


#sorted_list = sorted_list(l)
#print(sorted_list)
l = [98,90,1,23,4,5,6,7,8,6]

def min_element(l) :
    min = l[0]
    for i in l :
        if min > i :
            min = i
    return(min)

def sorted_list(l) :
    sorted_list = []
    while(len(l) > 0 ) :
        min_value = min_element(l)
        sorted_list.append(min_value)
        l.remove(min_value)
    return(sorted_list)

#sorted_list = sorted_list(l)
#print("The sorted list is :",sorted_list)




  