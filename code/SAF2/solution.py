import pandas as pd
import string
from langdetect import detect 
import re
import sys
import nltk
import emoji
import enchant
from googletrans import Translator
import validators
from textblob import TextBlob
from indic_transliteration import sanscript 
from indic_transliteration.sanscript import transliterate
from gingerit.gingerit import GingerIt
from googletrans import Translator
from inltk.inltk import identify_language
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator
from nltk.corpus import indian

#from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

translator = Translator()
d = enchant.Dict("en_US")
parser = GingerIt()
# nltk.download('indian')

cList = {"ain't": 'is not',
 "aren't": 'are not',
 "can't": 'cannot',
 "can't've": 'cannot have',
 "'cause": 'because',
 "could've": 'could have',
 "couldn't": 'could not',
 "couldn't've": 'could not have',
 "didn't": 'did not',
 "doesn't": 'does not',
 "don't": 'do not',
 "hadn't": 'had not',
 "hadn't've": 'had not have',
 "hasn't": 'has not',
 "haven't": 'have not',
 "he'd": 'he would',
 "he'd've": 'he would have',
 "he'll": 'he will',
 "he'll've": 'he will have',
 "he's": 'he is',
 "how'd": 'how would',
 "how'd'y": 'how do you',
 "how'll": 'how will',
 "how's": 'how is',
 "I'd": 'I would',
 "I'd've": 'I would have',
 "I'll": 'I will',
 "I'll've": 'I will have',
 "I'm": 'I am',
 "I've": 'I have',
 "isn't": 'is not',
 "it'd": 'it would',
 "it'd've": 'it would have',
 "it'll": 'it will',
 "it'll've": 'it will have',
 "it's": 'it is',
 "let's": 'let us',
 "ma'am": 'madam',
 "mayn't": 'may not',
 "might've": 'might have',
 "mightn't": 'might not',
 "mightn't've": 'might not have',
 "must've": 'must have',
 "mustn't": 'must not',
 "mustn't've": 'must not have',
 "needn't": 'need not',
 "needn't've": 'need not have',
 "o'clock": 'of the clock',
 "oughtn't": 'ought not',
 "oughtn't've": 'ought not have',
 "shan't": 'shall not',
 "sha'n't": 'shall not',
 "shan't've": 'shall not have',
 "she'd": 'she would',
 "she'd've": 'she would have',
 "she'll": 'she will',
 "she'll've": 'she will have',
 "she's": 'she is',
 "should've": 'should have',
 "shouldn't": 'should not',
 "shouldn't've": 'should not have',
 "so've": 'so have',
 "so's": 'so is',
 "that'd": 'that would',
 "that'd've": 'that would have',
 "that's": 'that is',
 "there'd": 'there would',
 "there'd've": 'there would have',
 "there's": 'there is',
 "they'd": 'they would',
 "they'd've": 'they would have',
 "they'll": 'they will',
 "they'll've": 'they will have',
 "they're": 'they are',
 "they've": 'they have',
 "to've": 'to have',
 "wasn't": 'was not',
 "we'd": 'we would',
 "we'd've": 'we would have',
 "we'll": 'we will',
 "we'll've": 'we will have',
 "we're": 'we are',
 "we've": 'we have',
 "weren't": 'were not',
 "what'll": 'what will',
 "what'll've": 'what will have',
 "what're": 'what are',
 "what's": 'what is',
 "what've": 'what have',
 "when's": 'when is',
 "when've": 'when have',
 "where'd": 'where did',
 "where's": 'where is',
 "where've": 'where have',
 "who'll": 'who will',
 "who'll've": 'who will have',
 "who's": 'who is',
 "who've": 'who have',
 "why's": 'why is',
 "why've": 'why have',
 "will've": 'will have',
 "won't": 'will not',
 "won't've": 'will not have',
 "would've": 'would have',
 "wouldn't": 'would not',
 "wouldn't've": 'would not have',
 "y'all": 'you all',
 "y'alls": 'you alls',
 "y'all'd": 'you all would',
 "y'all'd've": 'you all would have',
 "y'all're": 'you all are',
 "y'all've": 'you all have',
 "you'd": 'you would',
 "you'd've": 'you would have',
 "you'll": 'you will',
 "you'll've": 'you you will have',
 "you're": 'you are',
 "you've": 'you have',
 "amn't": 'am not',
 "daren't": 'dare not',
 "daresn't": 'dare not',
 "dasn't": 'dare not',
 "e'er": 'ever',
 'em': 'them',
 "everyone's": 'everyone is',
 'finna': 'fixing to',
 'gimme': 'give me',
 'gonna': 'going to',
 "gon't": 'go not',
 'gotta': 'got to',
 "he've": 'he have',
 "how're": 'how are',
 "I'm'a": 'I am about to',
 "I'm'o": 'I am going to',
 'kinda': 'kind of',
 "may've": 'may have',
 "ne'er": 'never',
 "o'": 'of',
 "o'er": 'over',
 "ol'": 'old',
 "shalln't": 'shall not',
 "somebody's": 'somebody is',
 "someone's": 'someone is',
 "something's": 'something is',
 "that'll": 'that will',
 "that're": 'that are',
 "there'll": 'there will',
 "there're": 'there are',
 "these're": 'these are',
 "this's": 'this is',
 "those're": 'those are',
 "'tis": 'it is',
 "'twas": 'it was',
 'wanna': 'want to',
 "what'd": 'what did',
 "where're": 'where are',
 "which's": 'which is',
 "who'd": 'who would',
 "who'd've": 'who would have',
 "who're": 'who are',
 "why'd": 'why did',
 "why're": 'why are',
 'Whatcha': 'What are you',
 'luv': 'love',
 'sux': 'sucks',
 'wudnt': 'would not',
 'cudnt': 'could not'
 }

sList = {
 '$:': '-5775591050571123167',
 '%)': '6918099099175134859',
 '%-)': '-5616976888366766776',
 '&-:': '-6799196393729225453',
 '&:': '4116373961892278351',
 "( '}{' )": '-4661919095793812594',
 '(%': '-7390119029409238248',
 "('-:": '-1176533548974838378',
 "(':": '-288946784906448632',
 '((-:': '5214705680899336381',
 '(*': '-8314744249570983158',
 '(-%': '890309365337002399',
 '(-*': '-1202349411336727487',
 '(-:': '3876502721093805183',
 '(-:0': '2537770760831139748',
 '(-:<': '-6803905107300160412',
 '(-:o': '7753188501057435134',
 '(-:O': '-4113309204961422809',
 '(-:{': '-179064948072886579',
 '(-:|>*': '7470131352128016149',
 '(-;': '2001934297005394876',
 '(-;|': '-4915549373138970832',
 '(8': '7177768299249075293',
 '(:': '743378658368125008',
 '(:0': '-2404738321742009141',
 '(:<': '8105386229635653707',
 '(:o': '-7207811267207018196',
 '(:O': '-1345037979392832509',
 '(;': '-984917096941257299',
 '(;<': '4334284308147639580',
 '(=': '-8895380311539911283',
 '(?:': '8563628687875202630',
 '(^:': '-5970539796585527259',
 '(^;': '1544639179278464976',
 '(^;0': '-5020831216718506693',
 '(^;o': '4878797894016806333',
 '(o:': '-5046578097284323341',
 ")':": '3259454611516240607',
 ")-':": '4463211358794296053',
 ')-:': '-8467551937256838485',
 ')-:<': '7519616935924852927',
 ')-:{': '1461769094981333636',
 '):': '3868539617958424135',
 '):<': '6309589912682856755',
 '):{': '4160881591478896701',
 ');<': '2150232963623012524',
 '*)': '-6625799109352308366',
 '*-)': '5943503019321702588',
 '*-:': '-4396709499693561466',
 '*-;': '8061483508401435797',
 '*:': '4932169711202057416',
 '*<|:-)': '5578469792040447126',
 '*\\0/*': '-7762374940309818242',
 '*^:': '-8486947289559999349',
 ',-:': '-2414431753304963011',
 "---'-;-{@": '9139464429215720862',
 '--<--<@': '-442282838902803191',
 '.-:': '-3819484938818662957',
 '..###-:': '-7054833406089903803',
 '..###:': '-164368220946660016',
 '/-:': '2296408612211664989',
 '/:': '-2370535516510370902',
 '/:<': '-1055426437623452014',
 '/=': '-9032036766366041157',
 '/^:': '-2760262154251401995',
 '/o:': '-3659758593577707906',
 '0-8': '6370481810758012042',
 '0-|': '2864866436709815512',
 '0:)': '-5749734044486719391',
 '0:-)': '-8122874664896978176',
 '0:-3': '-7307737152335859663',
 '0:03': '5718210482787748185',
 '0;^)': '707375917137069913',
 '0_o': '9137142558475658391',
 '10q': '911821196125802077',
 '1337': '-8228148248459263961',
 '143': '-3370300939096716034',
 '1432': '-4086424340058825942',
 '14aa41': '-3368152922870306430',
 '182': '-8355775648240087015',
 '187': '6833745999811289812',
 '2g2b4g': '-792981096780077893',
 '2g2bt': '8973722032275636407',
 '2qt': '4910390702036743658',
 '3:(': '5704990547191607292',
 '3:)': '1561637202596835807',
 '3:-(': '-3757597297289720435',
 '3:-)': '6312347943596441462',
 '4col': '3532026496278617735',
 '4q': '3520019350717117890',
 '5fs': '4607955172331530262',
 '8)': '1228952373033925709',
 '8-d': '6878018975994420942',
 '8-o': '6722264324731716189',
 '86': '4472871918693317122',
 '8d': '-3582144242487917915',
 ':###..': '-3258211547321284327',
 ':$': '785461035427441037',
 ':&': '-8252856749755793599',
 ":'(": '1195693619053043090',
 ":')": '-3867482580544023249',
 ":'-(": '3669958747253255211',
 ":'-)": '-5423918124269863128',
 ':(': '-5015572601680138442',
 ':)': '-5154156394742669662',
 ':*': '2352227034547678489',
 ':-###..': '9099979459974978445',
 ':-&': '1314728562015409601',
 ':-(': '-2643108474488572821',
 ':-)': '3546769093473591944',
 ':-))': '-4148222505901266170',
 ':-*': '5847485535011068668',
 ':-,': '5283102988719842516',
 ':-.': '3698265510456848908',
 ':-/': '928052564705431898',
 ':-<': '1896169051684261535',
 ':-d': '-1328628065457714026',
 ':-D': '4458220967920300250',
 ':-o': '5232011470057997875',
 ':-p': '6080048536857773381',
 ':-[': '2230696222651950144',
 ':-\\': '-391338957837050003',
 ':-c': '2228390839508028989',
 ':-|': '-3300142479283151392',
 ':-||': '-8152464753758054711',
 ':-Þ': '-7392925058984880586',
 ':/': '4419234734275587838',
 ':3': '-7807054999825966466',
 ':<': '-290783845539888722',
 ':>': '6086885182644460729',
 ':?)': '-5085258050320294236',
 ':?c': '5431331458223242339',
 ':@': '2953410838462239016',
 ':d': '5878944731322267603',
 ':D': '6441043224705639021',
 ':l': '9091273075392143872',
 ':o': '-7532055946997953409',
 ':p': '-1227555050936368495',
 ':s': '-1706191351417667702',
 ':[': '-9038032266058812655',
 ':\\': '3415067713063829157',
 ':]': '-3177540824121549437',
 ':^)': '8086788012268895205',
 ':^*': '-8373842900252907451',
 ':^/': '-2707802922724011494',
 ':^\\': '-9096003570945093936',
 ':^|': '4675968365964735333',
 ':c': '-7111393752992873188',
 ':c)': '-2869411769725137547',
 ':o)': '1478169677255520964',
 ':o/': '5066344742833197114',
 ':o\\': '2134863562757591937',
 ':o|': '-4070819235094493796',
 ':P': '3054554715046417270',
 ':{': '-1738350623090655603',
 ':|': '-1268592028183582772',
 ':}': '3345854531291762065',
 ':Þ': '2306013208514129256',
 ';)': '5024948637342091238',
 ';-)': '7359771336454887525',
 ';-*': '5661525932809894246',
 ';-]': '-6839266093239107260',
 ';d': '-8579047182005159666',
 ';D': '-8821229646837710245',
 ';]': '-5431279597460191298',
 ';^)': '-8573657651877296097',
 '</3': '-1695628300519593630',
 '<3': '3670694106807187215',
 '<:': '7406830923496994498',
 '<:-|': '-4407807377909941716',
 '=)': '2156351037538165587',
 '=-3': '15037074669549593',
 '=-d': '-452252898576231598',
 '=-D': '-5199739144318196705',
 '=/': '4051125358175866930',
 '=3': '-5722786005478138616',
 '=d': '2120827046103283360',
 '=D': '-409714126044029482',
 '=l': '-4191663125014028307',
 '=\\': '-447161594047499972',
 '=]': '-4810922855043883379',
 '=p': '-7248734219003909704',
 '=|': '-5004960976239223956',
 '>-:': '-2124499330747793172',
 '>.<': '-5164781173411724327',
 '>:': '-1430329329873713382',
 '>:(': '8589561710604411407',
 '>:)': '2963460099213039186',
 '>:-(': '-2162053310512040456',
 '>:-)': '1842702239497519087',
 '>:/': '-2666476028271742017',
 '>:o': '1362731526029694998',
 '>:p': '-5269915790270677462',
 '>:[': '6994604641204369234',
 '>:\\': '-7263273829281072463',
 '>;(': '8799342644450022704',
 '>;)': '-5390095804834311458',
 '>_>^': '1685580499122859082',
 '@:': '5553058621153766046',
 '@>-->--': '8235868190629668239',
 "@}-;-'---": '1068371536570783805',
 '{:': '898482849747590558',
 '|-0': '-6301509953187676206',
 '|-:': '7859858874926894081',
 '|-:>': '7084907644758528616',
 '|-o': '-7162295624321718165',
 '|:': '-4745919248815579056',
 '|;-)': '-5378769776850077391',
 '|=': '555563825342298333',
 '|^:': '-1387411534306764247',
 '|o:': '548232956784944241',
 '||-:': '-7240277821133945000',
 '}:': '-3889853025577089463',
 '}:(': '-1377349367487740596',
 '}:)': '2540069643911903722',
 '}:-(': '5782399845606546582',
 '}:-)': '-5851770717823011663'
 }

tran_en_hi_file1 = open("crowd_transliterations.hi-en.txt", 'r', encoding="utf8")
tran_en_hi_file2 = open("Hindi-WordTransliterationPairs.txt", 'r', encoding="utf8")
lines1 = tran_en_hi_file1.readlines()
lines2 = tran_en_hi_file2.readlines()
en_hi_transliterate = {}
for line in lines1:
    en,hi = line.split()
    en_hi_transliterate[en.lower()] = hi
for line in lines2:
    en,hi = line.split()
    en_hi_transliterate[en.lower()] = hi

srevList = {}
for k in sList:
    srevList[sList[k]] = k

c_re = re.compile('(%s)' % '|'.join(cList.keys()))

def expand_contractions(text, c_re=c_re):
    def replace(match):
        return cList[match.group(0)]
    return c_re.sub(replace, text)


def is_emoji(character):
    return character in emoji.UNICODE_EMOJI


def text_has_emoji(text):
    for character in text:
        if character in emoji.UNICODE_EMOJI:
            return True
    return False

def is_hyperlink(value):
    if(validators.domain(value) or validators.email(value) or validators.iban(value) or validators.ip_address.ipv4(value) 
        or validators.ip_address.ipv6(value) or validators.mac_address(value) or validators.url(value, public=False) or validators.uuid(value)):
       return True
    else:
       return False

def all_special_chars(token):
    return all(i in string.punctuation for i in token)

def check_nums(token):
    return bool(re.match('^-?[0-9]\d*(\.\d+)?$', token))

def check_splcharacter(token):
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:,;!?]')
    if(string_check.search(token) == None):
        return False 
    return True

def trim_rep2(token):
    return re.sub("(.)\\1{2,}", "\\1", token)

def detect_lang(token):
    lang = TextBlob(token)  
    return lang.detect_language()

def part_of_en_dict(token):
    d_US = enchant.Dict("en_US")
    d_UK = enchant.Dict("en_UK")
    d_IN = enchant.Dict("en_IN")
    return (d_US.check(token) or d_UK.check(token) or d_IN.check(token))

def reverse_transliterate(token, src_lang):
    #considering words transliterated in english
    if(src_lang == 'en'):
        src_en = sanscript.ITRANS
        src_latin = sanscript.IAST

    dst_hi = sanscript.DEVANAGARI
    dst_kn = sanscript.KANNADA
    dst_tm = sanscript.GUJARATI
    trans_hi_en = transliterate(token, src_en, dst_hi)
    trans_hi_latin = transliterate(token, src_latin, dst_hi)
    if(trans_hi_en in nltk.corpus.indian.words('hindi.pos')):
        return trans_hi_en
    elif(trans_hi_latin in nltk.corpus.indian.words('hindi.pos')):
        return trans_hi_latin
    return trans_hi_en

def translate_to_en(token):
    translation = translator.translate(token, dest='en')
    return translation.text

def grammar_correction(text):
    return (parser.parse(text)['result']).split()

def sentiment_scores(sentence): 
    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
    #print("Overall sentiment dictionary is : ", sentiment_dict) 
    #print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    #print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    #print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
    #print("Sentence Overall Rated As", end = " ") 
    if sentiment_dict['compound'] >= 0.05 :
        sentiment_dict['status'] = 1 
        #print("Positive") 
    elif sentiment_dict['compound'] <= - 0.05 :
        sentiment_dict['status'] = -1
        #print("Negative") 
    else : 
        sentiment_dict['status'] = 0
        #print("Neutral")
    return sentiment_dict

text = sys.argv[1]
text = re.sub(r"http\S+", "", text)
#replace smileys with hash val
for sm in sList:
    text = text.replace(sm, " "+sList[sm]+" ")

tokens = nltk.word_tokenize(expand_contractions(text))
final_tokens = []
final_text_tokens = []
code_mixed = False
for token in tokens:
    if(is_hyperlink(token)):
        continue
    elif(is_emoji(token) or check_nums(token) or check_splcharacter(token) or all_special_chars(token)):
        final_tokens.append(token)
    elif(token.isalpha()):
        token = trim_rep2(token)
        src_lang = 'en'
        final_tokens.append('word_placeholder')
        if(part_of_en_dict(token)):
            final_text_tokens.append(token)
        else:
            code_mixed = True
            if(token.lower() in en_hi_transliterate):
                rev_transliterated_word = en_hi_transliterate[token.lower()]
            else:
                rev_transliterated_word = reverse_transliterate(token.lower(), src_lang)
            en_translated_word = translate_to_en(rev_transliterated_word)
            if(token.isupper()):
                en_translated_word = en_translated_word.upper()
            final_text_tokens.append(en_translated_word)
    else:
        #assuming words written in other languages will be spelled correctly
        src_lang = identify_language(token)
        final_tokens.append('word_placeholder')
        en_translated_word = translate_to_en(token)
        final_text_tokens.append(en_translated_word)

if(code_mixed):
    grammar_corrected_text = grammar_correction(" ".join(final_text_tokens))
    code_mixed = False
else:
    grammar_corrected_text = final_text_tokens

text_index = 0
for index in range(len(final_tokens)):
    if(final_tokens[index]=='word_placeholder'):
        final_tokens[index] = final_text_tokens[text_index]
        text_index+=1

text_final = " ".join(final_tokens)
for hsm in srevList:
    text_final = text_final.replace(hsm, srevList[hsm])

#print(text_final)
sent_dict = sentiment_scores(text_final)
# print(sent_dict)
print(sent_dict["status"], round(sent_dict["neg"]*100,2), round(sent_dict["neu"]*100,2), round(sent_dict["pos"]*100,2), round(sent_dict["compound"]*100,2))
