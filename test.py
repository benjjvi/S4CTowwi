from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator

positive_headlines = [
    "Babi Iawn yn Caerdydd: Croeso i'r Byd i Blentyn Newydd",
    "Prosiect Ynni Gwynt newydd yn Sir Benfro yn creu 500 o swyddi newydd",
    "Eisteddfod Genedlaethol yn Dwyn Llawenydd i Gymunedau Lleol",
    "Cymru yn Ennill Pencampwriaeth Rygbi'r Byd",
    "Achos Mawr o Arloesi Technoleg yn Aberystwyth"
]

negative_headlines = [
    "Llygredd Dŵr yn Achos Perygl i Boblogaeth y Dyffryn",
    "Damwain Car Angheuol ar yr A470: Tri Person Wedi Marw",
    "Tân Mawr yn Dinistrio Siopau Canol y Dref",
    "Lladdfa yn Ysbyty Llanelli: Dau Gleifion yn Marw",
    "Cynnydd Mawr yn Ffigyrau Troseddu yng Nghaerdydd"
]

neutral_headlines = [
    "Seren Yng Nghymru yn Rhoi Cyfweliad Arbennig i'r Papur Lleol",
    "Gŵyl Fwyd Abertawe yn Denu Miloedd o Ymwelwyr",
    "Ffermwr yn Casglu Taro Enfawr gyda’r Cynhaeaf Eleni",
    "Prosiect Adnewyddu’r Promenâd yn Aberystwyth yn Dechrau",
    "Dyfodol Clwb Pêl-droed Wrecsam yn Sefydlog ar ôl Ymgyrch Ariannu Llwyddiannus"
]

for item in positive_headlines:
    # Initialize translator
    translator = Translator()

    # Translate title from Welsh to English
    translated_title = translator.translate(item, src='cy', dest='en').text

    sentiment = SentimentIntensityAnalyzer()
    sent_1 = sentiment.polarity_scores(translated_title)
    print("===")
    print("Original Text:", item)
    print("Translated Text:", translated_title)
    print("Sentiment of POSITIVE:", sent_1)


for item in negative_headlines:
    # Initialize translator
    translator = Translator()

    # Translate title from Welsh to English
    translated_title = translator.translate(item, src='cy', dest='en').text

    sentiment = SentimentIntensityAnalyzer()
    sent_1 = sentiment.polarity_scores(translated_title)
    print("===")
    print("Original Text:", item)
    print("Translated Text:", translated_title)
    print("Sentiment of NEGATIVE:", sent_1)

for item in neutral_headlines:
    # Initialize translator
    translator = Translator()

    # Translate title from Welsh to English
    translated_title = translator.translate(item, src='cy', dest='en').text

    sentiment = SentimentIntensityAnalyzer()
    sent_1 = sentiment.polarity_scores(translated_title)
    print("===")
    print("Original Text:", item)
    print("Translated Text:", translated_title)
    print("Sentiment of NEUTRAL:", sent_1)
