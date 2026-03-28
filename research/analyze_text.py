#!/usr/bin/env python3
"""
Text and pattern analysis for haian.de condolence messages
"""

import re
import json
from collections import Counter

# Extracted message data from the HTML
MESSAGES = [
    {"author": "Alex (whiteheatsyd) Craft", "date": "02.11.2011 12:46", "text": "I am sorry to hear such tragic news, my thoughts are with you at this difficult time. He was always a pleasure to talk to and a man of great respect. You should be very proud of the young man he became. RIP"},
    {"author": "Jojo", "date": "31.10.2011 04:27", "text": "Ich werde dich nie vergessen, mein Freund! In den Jahren, die wir zusammen verbracht haben, die viel zu schnell vergangen sind, hast du mein Leben fuer immer bereichert. Dein Humor, dein Lachen und deine positive Ausstrahlung wo immer du warst, wird deiner Familie und deinen Freunden fuer immer in Erinnerung bleiben. Die Welt ist jetzt ein Stueck weniger freundlich. Fuer immer dein Freund Jojo"},
    {"author": "Jenny", "date": "31.10.2011 18:39", "text": "Haian, du warst über Jahre einer meiner besten Freunde. Wir haben so oft gelacht und auch in schweren Zeiten warst du mir ein Fels in der Brandung. Ich habe dir viel zu verdanken. Mit dir haben wir einen tollen Menschen verloren, der viel gegeben hat. Jemand, der sprechen konnte, ohne zu reden. Ich werde nicht einen Tag mit dir vergessen und du bleibst immer in meinem Herzen!"},
    {"author": "Sandra", "date": "31.10.2011 20:08", "text": "Obwohl du nicht mehr da bist, wirst du uns immer in Erinnerung bleiben. Es waren schöne Momente und lustige Augenblicke, die dich in unserem Herzen bewahren werden. Ein besonderer Mensch der uns fehlen wird."},
    {"author": "Marian", "date": "01.11.2011 17:51", "text": "Ich hatte immer großen Respekt vor deiner intelligenten und lieben Art. Könnte ich die Zeit zurück drehen, würde ich mir wünschen das wir noch öfter was zusammen unternommen hätten. Mit dir geht ein unglaublich liebenswerter Mensch viel, viel zu früh. Auch wenn wir alle sehr traurig sind das du nicht mehr da bist, werden wir oft mit Freude an dich denken. Wir vermissen dich."},
    {"author": "Jana", "date": "01.11.2011 20:21", "text": "Noch finde ich keine Worte für das, was passiert ist. Darum entleihe ich sie Mascha Kaléko: Memento Vor meinem eigenen Tod ist mir nicht bang, nur vor dem Tode derer, die mir nah sind. Wie soll ich leben, wenn sie nicht mehr da sind? Allein im Nebel tast ich todentlang Und lass mich willig in das Dunkel treiben. Das Gehen schmerzt nicht halb so wie das Bleiben. Der weiß es wohl, dem Gleiches widerfuhr; - und die es trugen, mögen mir vergeben. Bedenkt: Den eignen Tod, den stirbt man nur; doch mit dem Tod der andern muss man leben."},
    {"author": "Alan Sheffler", "date": "01.11.2011 22:26", "text": "Sorry this happened. He was a nice guy and a good poker player."},
    {"author": "Maren", "date": "02.11.2011 09:24", "text": "Mit dir verlieren wir einen so liebenswerten, intelligenten, ganz besonderen Menschen. Du wirst immer in unserer Erinnerung bleiben."},
    {"author": "Svenja", "date": "02.11.2011 09:58", "text": "Es ist schwer zu verstehen, dass du nicht mehr da bist Haian, dass dein Lächeln für immer verschwunden ist. In useren Gedanken und Herzen wirst du immer ein Teil von uns sein und ewig leben. Ich werde jede Minute mit dir in glücklicher Erinnerung behalten. Du fehlst! Und ich hoffe, wo immer du bist gibt es einen Pockertisch für dich:) Jeg elsker deg."},
    {"author": "Nicholas Syhler", "date": "02.11.2011 10:45", "text": "This is really sad and I'm so very sorry. Haian was my poker coach a few years ago. I knew him as a very friendly person, always up for a good discussion about poker or politics."},
    {"author": "Ihno", "date": "02.11.2011 17:07", "text": "Dir Haian, auch wenn ich deine Leidenschaft für Poker nicht teilte, so waren jedoch die Skat-Abende mit dir umso schöner. Um in den Worten des Spiels zu sprechen. Dein Blatt war so viel besser, als nur bis 24 zu reizen, damit wären auch durchaus 120 drin gewesen. Kurz gesagt ich kann es nicht begreifen und vermisse dich. Mein Mitgefühl gilt all denen du wichtig warst. Rest in peace Ihno"},
    {"author": "Jannik", "date": "02.11.2011 17:39", "text": "Immer und immer wieder ertappe ich mich bei den Gedanken, was dir in den letzten Stunden durch den Kopf gegangen sein mag! Was in deiner Welt passiert ist in den letzten par Jahren... Haian, auch wenn wir uns aus den Augen verloren haben, auch wenn es ein solch unfassbarer Moment ist, der mich wieder zu dir führt, sei gewiss, dass mein Herz bei dir und deiner Familie ist! Du warst immer ein guter Freund und Weggefährte und für diese Zeit, die ich mit dir verbringen durfte, bin ich dir auf ewig dankbar! Du bleibst mit deinem stolzen Lächeln in meinem Gedächtnis und das für immer, mein Freund!"},
    {"author": "Sven", "date": "03.11.2011 12:13", "text": "Seitdem ich vom Vorfall erfahren habe, denke ich viel über die zusammen verbrachte Zeit nach. Es fällt mir unglaublich schwer zu realisieren, das uns allen ein von Grund auf guter und durch Einzigartigkeit glänzenden Menschen aus unserem Leben entrissen worden ist. Ich werde die Zeit mit dir nie vergessen und du wirst mir auf ewig als ein Mensch in Erinnerung bleiben, der 100% er selbst war. Es schmerzt zutiefst realisieren zu müssen, dich nie wieder zu hören und zu sehen, hatten wir alle doch sicherlich noch so viel mit dir vor. Ich vermisse dich und ich werde bei jedem Blick gen Himmel an dich denken. Ruhe in Frieden mein Freund, Sven"},
    {"author": "Cathrin", "date": "03.11.2011 15:11", "text": "Haian, richtige Worte finde ich nicht. Du gehörst zu den Guten!"},
    {"author": "Kristin", "date": "03.11.2011 16:20", "text": "Nach all der Zeit, die wir miteinander gelacht, gescherzt und auch gegrummelt haben, kann ich einfach nicht fassen, dass es keine Chance mehr geben wird, an diese wundervolle Zeit anzuknüpfen. Das du nun nichtmehr bist macht einem bewusst, dass das Leben viel zu kurz ist und man jeden Moment, der einem zur Verfügung steht, mit Freunden und Familie verbringen sollte und sich nie solange aus den Augen verlieren soll. Ich werde dich und die Zeit mit dir nie vergessen. Danke dir dafür! Meine Gedanken sind bei dir und deinen Lieben. Kristin"},
    {"author": "Nicky", "date": "04.11.2011 10:35", "text": "Lieber Haian, auch wenn du jetzt so weit weg zu seien scheinst, einfach nicht mehr da!- Die gemeinsamen Momente und die stets positiven Erinnerungen an dich werden dich nie in Vergessenheit geraten lassen! In unseren Gedanken, in unseren Erinnerungen wirst du immer ein Teil von uns bleiben! Manche Menschen hinterlassen nur Spuren im Sand, aber du hast Spuren in unseren Herzen hinterlassen! Nicky"},
    {"author": "Sanaz", "date": "04.11.2011 22:04", "text": "Du BIST einzigartig...das wurde mir heute wieder klar.In Gedanken versetze ich mich in die Zeit zurück,in der wir uns auf \"unsere\" Weise begrüßten,gegenüber saßen und miteinander redeten.Die Erinnerung daran zaubert mir auch jetzt ein Lächeln ins Gesicht.Eines Tages grüßen wir uns wieder,doch bis dahin halte ich an diese Erinnerungen fest.Danke Haian!"},
    {"author": "Basti", "date": "04.11.2011 23:59", "text": "Mit dir ist ein Stück Hoffnung aus unserem Leben gewichen. Du warst stets zurückhaltend und bescheiden und obwohl du in vielerlei Hinsicht jeden Grund dazu gehabt hättest, hast du in vorbildlicher Weise nie mit irgendetwas geprahlt. Nie werde ich die vielen schönen Stunden vergessen, die wir gemeinsam verbrachten, sei es auf LAN-Parties oder bei gemeinsamen Skat-Runden. Ich wünschte, ich hätte mehr über dich gewusst, wünschte du hättest mehr über dich preisgegeben, aber offenbar gehörtest du zu der Sorte Mensch, die ihre Probleme lieber allein schultern. Hoffend, dass es dir jetzt besser geht oder zumindest dass du deinen häufig indirekt beschriebenen \"Weltschmerz\" jetzt nichtmehr verspüren musst, in tiefer Verbundenheit Basti"},
    {"author": "Thomas", "date": "06.11.2011 12:11", "text": "Der Tod ist wie ein Horizont, dieser ist nichts anderes als die Grenze unserer Wahrnehmung. Wenn wir um einen Menschen trauern, freuen sich andere, ihn hinter der Grenze wieder zu sehen. Hallo Haian, wir haben uns zwar nur kurz gekannt, aber ich kann Deinen Schritt gut nachvollziehen, da ich die Welt mit anderen Augen sehe. Bestell meiner Atze 'nen schönen Gruß von mir. Wir sehen uns in ca. 55 - 60 jahren wieder. CU in Heaven Thomas"},
    {"author": "David", "date": "08.11.2011 16:24", "text": "A very very sad moment :-( You were such a positive person, you won't be forgotten. RIP Haian"},
    {"author": "David", "date": "10.11.2011 10:54", "text": "Du hast mich durch viele Jahre meiner Kindheit als einer meiner besten Freunde begleitet und es schmerzt mich, dass wir nie mehr die Gelegenheit haben werden, zusammen über die guten alten Zeiten zu sinnieren. Ich werde dich immer als meinen Freund in Erinnerung halten. Ruhe in Frieden Fabian, David"},
    {"author": "Bine", "date": "13.11.2011 22:27", "text": "Schade, dass du nicht mehr da bist."},
    {"author": "Christine", "date": "20.11.2011 11:16", "text": "Niemals bin ich Dir begegnet! Aber an Deinen Spuren, die Du bei Deiner Familie und Freunden hinterlassen hast, erkenne ich, wie viel Du jedem Einzelnen gegeben und bedeutet hast. Möge der Frieden, den Du erlangt hast,sich über alle Erinnerungen legen und die Zurückgelassenen trösten. christine"},
    {"author": "Elke", "date": "23.11.2011 21:19", "text": "Fabian, du hast während eines Lebensabschnittes viel Zeit, gute Zeit wie ich meine, mit meinem Sohn verbracht. Ich habe dich nicht wirklich erlebt. Ich empfinde Respekt vor dir und deinem Schicksal.Meine Gedanken sind bei dir und deiner Familie. Ruhe in Frieden, Fabian"},
    {"author": "Mandy", "date": "17.12.2011 14:46", "text": "Als der Regenbogen verblasste, da kam ein Engel und trug dich mit sanften Schwingen weit über die sieben Weltmeere. Er zeigte dir den hellsten Stern am Himmel. Behutsam setzte er dich an den Rand des Lichts. Du bist hineingegangen und fühltest dich geborgen. Du hast uns nicht verlassen, du bist uns nur ein Stück voraus. Fabian, wir haben uns nie kennengelernt, aber ich weiß, dass viele Menschen dich geliebt haben und immer noch lieben und weiter lieben werden. Mein Mitgefühl gilt diesen Menschen."},
    {"author": "Isabella", "date": "24.02.2012 23:34", "text": "Haian...du fehlst mir unheimlich! :( Ich denke an unsere wunderbare Zeit. Ruhe in Frieden <3 Deine Isa"},
    {"author": "Svenja", "date": "28.04.2012 21:30", "text": "Es ist jetzt ein halbes Jahr her, dass wir dich und damit ein Teil von uns zu Grabe tragen mussten. Du hast in dieser Welt ein so tiefes Loch hinterlassen, dass nur mühsam mit den Erinnerungen an dich geflickt werden kann. Lieber Haian, nur wer in Vergessenheit gerät, der ist wirklich tod. Du mein Großer wirst ewig in mir und sicher auch allen anderen weiterleben!!! Dein Verlust ist schwer zu tragen, doch du bist immer da, im Herzen und in Gedanken. Du fehlst hier! :-* In Liebe Svenja"},
]

def analyze_first_letters():
    """Extract first letter of each message"""
    print("=" * 60)
    print("FIRST LETTER ANALYSIS (acrostic)")
    print("=" * 60)
    
    first_letters = []
    for msg in MESSAGES:
        text = msg['text'].strip()
        if text:
            first_letters.append(text[0])
    
    result = ''.join(first_letters)
    print(f"First letters: {result}")
    print(f"Length: {len(result)}")
    
    # Check for German/English meaning
    print(f"\nPotential words: {result}")
    
    return result

def analyze_author_first_letters():
    """Extract first letter of each author name"""
    print("\n" + "=" * 60)
    print("AUTHOR FIRST LETTERS")
    print("=" * 60)
    
    letters = []
    for msg in MESSAGES:
        name = msg['author'].strip()
        if name:
            letters.append(name[0])
    
    result = ''.join(letters)
    print(f"Author initials: {result}")
    print(f"Length: {len(result)}")
    
    return result

def extract_numbers():
    """Extract all numbers from messages"""
    print("\n" + "=" * 60)
    print("NUMBER EXTRACTION")
    print("=" * 60)
    
    all_numbers = []
    for msg in MESSAGES:
        numbers = re.findall(r'\d+', msg['text'])
        all_numbers.extend([int(n) for n in numbers])
        if numbers:
            print(f"{msg['author']}: {numbers}")
    
    # Also extract from dates
    dates = []
    for msg in MESSAGES:
        date_nums = re.findall(r'\d+', msg['date'])
        dates.extend([int(n) for n in date_nums])
    
    print(f"\nAll numbers found: {all_numbers}")
    print(f"Date numbers: {dates}")
    
    return all_numbers, dates

def analyze_poker_references():
    """Analyze poker-related messages"""
    print("\n" + "=" * 60)
    print("POKER/SKAT REFERENCES")
    print("=" * 60)
    
    poker_keywords = ['poker', 'skat', 'blatt', 'reizen', 'tisch', 'coach', 'lan']
    
    for msg in MESSAGES:
        text_lower = msg['text'].lower()
        found = [kw for kw in poker_keywords if kw in text_lower]
        if found:
            print(f"\n{msg['author']} ({msg['date']}):")
            print(f"  Keywords: {found}")
            print(f"  Text: {msg['text'][:150]}...")

def check_encoding_patterns():
    """Check for potential encoded data in messages"""
    print("\n" + "=" * 60)
    print("ENCODING PATTERN CHECKS")
    print("=" * 60)
    
    all_text = ' '.join([m['text'] for m in MESSAGES])
    
    # Check for base64-like patterns
    base64_pattern = r'[A-Za-z0-9+/]{20,}={0,2}'
    matches = re.findall(base64_pattern, all_text)
    if matches:
        print(f"Potential base64 strings: {matches[:10]}")
    else:
        print("No obvious base64 patterns found")
    
    # Check for hex patterns
    hex_pattern = r'[0-9a-fA-F]{8,}'
    hex_matches = re.findall(hex_pattern, all_text)
    if hex_matches:
        print(f"Potential hex strings: {hex_matches[:10]}")
    else:
        print("No obvious hex patterns found")
    
    # Check for unusual character sequences
    print("\nChecking for special characters...")
    special_chars = set()
    for msg in MESSAGES:
        for char in msg['text']:
            if ord(char) > 127:  # Non-ASCII
                special_chars.add((char, ord(char), msg['author']))
    
    if special_chars:
        print("Special characters found:")
        for char, code, author in special_chars:
            print(f"  '{char}' (U+{code:04X}) in {author}")

def analyze_message_lengths():
    """Analyze message lengths for patterns"""
    print("\n" + "=" * 60)
    print("MESSAGE LENGTH ANALYSIS")
    print("=" * 60)
    
    lengths = [len(m['text']) for m in MESSAGES]
    print(f"Message lengths: {lengths}")
    print(f"Min: {min(lengths)}, Max: {max(lengths)}")
    print(f"Sum: {sum(lengths)}")
    
    # Check if lengths map to ASCII
    ascii_chars = [chr(l) if 32 <= l <= 126 else '?' for l in lengths]
    print(f"Lengths as ASCII: {''.join(ascii_chars)}")

def check_whitespace_patterns():
    """Check for unusual whitespace that might encode data"""
    print("\n" + "=" * 60)
    print("WHITESPACE ANALYSIS")
    print("=" * 60)
    
    for msg in MESSAGES:
        text = msg['text']
        # Count different types of whitespace
        spaces = text.count(' ')
        newlines = text.count('\n')
        tabs = text.count('\t')
        
        if tabs > 0 or newlines > 5:
            print(f"{msg['author']}: {spaces} spaces, {newlines} newlines, {tabs} tabs")

def analyze_word_frequency():
    """Analyze word frequencies"""
    print("\n" + "=" * 60)
    print("WORD FREQUENCY ANALYSIS")
    print("=" * 60)
    
    all_words = []
    for msg in MESSAGES:
        words = re.findall(r'\b[a-zA-ZäöüÄÖÜß]+\b', msg['text'].lower())
        all_words.extend(words)
    
    word_counts = Counter(all_words)
    print("Most common words:")
    for word, count in word_counts.most_common(20):
        print(f"  {word}: {count}")

def check_date_patterns():
    """Analyze date patterns"""
    print("\n" + "=" * 60)
    print("DATE PATTERN ANALYSIS")
    print("=" * 60)
    
    for msg in MESSAGES:
        date = msg['date']
        # Extract DD.MM.YYYY HH:MM
        match = re.match(r'(\d{2})\.(\d{2})\.(\d{4}) (\d{2}):(\d{2})', date)
        if match:
            day, month, year, hour, minute = match.groups()
            print(f"{msg['author']}: {day}.{month}.{year} {hour}:{minute}")
            
            # Check for patterns in dates
            nums = [int(day), int(month), int(year), int(hour), int(minute)]
            # Sum of digits
            digit_sum = sum([sum(int(d) for d in str(n)) for n in nums])
            print(f"  Digit sum: {digit_sum}")

if __name__ == "__main__":
    print("TEXT AND PATTERN ANALYSIS FOR HAIAN.DE")
    print("=" * 60)
    
    analyze_first_letters()
    analyze_author_first_letters()
    extract_numbers()
    analyze_poker_references()
    check_encoding_patterns()
    analyze_message_lengths()
    check_whitespace_patterns()
    analyze_word_frequency()
    check_date_patterns()
    
    print("\n" + "=" * 60)
    print("Analysis complete")
    print("=" * 60)
