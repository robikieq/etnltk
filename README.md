# Ethiopian Language Toolkit (etltk)

- The Ethiopian Natural Language Toolkit (ETLTK) project aimed to develop a suite of open source Natural Language Processing modules for the Ethiopian language.

- Under construction! Not ready for use yet! Currently experimenting :-)

## Installation

### pip

- **etltk** supports Python 3.6 or later. We recommend that you install etltk via `pip`, the Python package manager. To install, simply run:

  ```python
    pip install etltk
  ```

### From Source

- Alternatively, you can also install from source via ethiopian_language_toolkit’s git repository, which will give you more flexibility in developing on top of etltk. For this option, run

  ```python
    git clone https://github.com/robikieq/ethiopian_language_toolkit.git
    
    cd ethiopian_language_toolkit
    
    pip install -e .
  ```

## Usage

1. Text Annotating with AmharicDocument

- Annotating amharic text is very simple: you can simply pass the text to the `AmharicDocument` and access all annotations from the returned AmharicDocument object:
  - Within AmharicDocument, annotations are further stored in `Sentences`, `Tokens`, `Words`.
  
  ```python
    from etltk import AmharicDocument

    # Annotating a Document
    sample_text = """
    ሚያዝያ 14፣ 2014 ዓ.ም በአገር ደረጃ የሰው ሰራሽ አስተውሎት /Artificial Intelligence/ አሁን ካለበት ዝቅተኛ ደረጃ ወደ ላቀ ደረጃ ለማድረስ፣ ሃገርኛ ቋንቋዎችን ለዓለም ተደራሽ ለማድረግ፣ አገራዊ አቅምን ለማሳደግ እና ተጠቃሚ ለመሆን በጋራ አብሮ መስራቱ እጅግ ጠቃሚ ነው፡፡

    በማሽን ዓስተምሮ (Machine Learning) አማካኝነት የጽሁፍ ናሙናዎች በአርቲፊሻል ኢንተለጀንስ ሥርዓት ለማሰልጠን፣ የጽሁፍ ዳታን መሰብሰብ እና ማደራጀት፤ የናቹራል ላንጉዌጅ ፕሮሰሲንግ ቱሎችን /Natural Language Processing Tools/ በመጠቀም የጽሁፍ ዳታን ፕሮሰስ ማድረግ ተቀዳሚ እና መሰረታዊ ጉዳይ ነው።

    የማሽን ለርኒንግ ስልተ-ቀመሮች በመጠቀም ቋንቋዎችን መለየት እና መረዳት፣ የጽሁፍ ይዘቶችን መለየት፣ የቋንቋን መዋቅር መተንተን የሚያስችሉ የሃገሪኛ ናቹራል ላንጉዌጅ ፕሮሰሲንግ ቱሎች፣ ስልተ-ቀመሮች እና ሞዴሎችን ማዘጋጀት ተገቢ ነው። በዚህም መሰረት አማርኛ፣ አፋን ኦሮሞ፣ ሶማሊኛ እና ትግርኛ ቋንቋዎችን ለማሽን የማስተማር ሂደትን ቀላልና የተቀላተፍ እንዲሆን ያስችላል፡፡

    የትርጉም አገልግሎት፣ ቻትቦት (የውይይት መለዋወጫ ሮቦት) ፡ የፅሁፍ ሰነዶች ልየታ፣ የቃላት ትክክለኛነትን ማረጋገጥ፣ በቋንቋን መዋቅር ትንተና መሠረት ጽሁፎችን ለማዋቀር እና ለመመስረት፣ ረጅም ጽሁፎችን ማሳጠር፣ አንኳር ጉዳዮችን መለየት ወይም ጥቅል ሃሳብ ማውጣት፣ ንግግርን ወደ ጽሁፍ የሚቀይሩ አገልግሎቶችን የሚሰጡ መተግበሪያ ማልማት አስረላጊ ነው።

    የአርቲፊሻል ኢንተለጀንስ ቴክኖሎጂ ዘርፍ በጥናት፣ ምርምና ልማት እንዲመራ ማስቻል፣ አስፈላጊ የዲጂታል መሠረተ ልማቶች ማሙሏት መሰረታዊ ለውጥ ለማምጣት፣ እና የአርቲፊሻል ኢንተለጀንስ ውጤቶችን በተግባር በስፋት ጥቅም ላይ እንዲዉሉ ይረዳል። 🤔
    """

    doc = AmharicDocument(sample_text)

    # The following example shows how to print the `clean` text:
    print(doc)
    
    # output: AmharicDocument("ሚያዝያ ዓመተ ምህረት በአገር ደረጃ የሰው ሰራሽ አስተውሎት አሁን ካለበት ዝቅተኛ ደረጃ ወደ ላቀ ደረጃ ለማድረስ ሀገርኛ ቋንቋዎችን ለአለም ተደራሽ ለማድረግ አገራዊ አቅምን ለማሳደግ እና ተጠቃሚ ለመሆን በጋራ አብሮ መስራቱ እጅግ ጠቃሚ ነው በማሽን አስተምሮ አማካኝነት የፅሁፍ ናሙናዎች በአርቲፊሻል ኢንተለጀንስ ስርአት ለማሰልጠን የፅሁፍ ዳታን መሰብሰብ እና ማደራጀት የናቹራል ላንጉዌጅ ፕሮሰሲንግ ቱሎችን በመጠቀም የፅሁፍ ዳታን ፕሮሰስ ማድረግ ተቀዳሚ እና መሰረታዊ ጉዳይ ነው የማሽን ለርኒንግ ስልተቀመሮች በመጠቀም ቋንቋዎችን መለየትና መረዳት የፅሁፍ ይዘቶችን መለየት የቋንቋን መዋቅር መተንተን የሚያስችሉ የናቹራል ላንጉዌጅ ፕሮሰሲንግ ቱሎች ስልተቀመሮች እና ሞዴሎችን ማዘጋጀት አስፈላጊ ነው የትርጉም አገልግሎት ቻትቦት የውይይት መለዋወጫ ሮቦት የፅሁፍ ሰነዶች ልየታ የቃላት ትክክለኛነትን ማረጋገጥ በቋንቋን መዋቅር ትንተና መሰረት ፅሁፎችን ለማዋቀር እና ለመመስረት ረጅም ፅሁፎችን ማሳጠር አንኳር ጉዳዮችን መለየት ወይም ጥቅል ሀሳብ ማውጣት ንግግርን ወደ ፅሁፍ የሚቀይሩ አገልግሎቶችን የሚሰጡ መተግበሪያ ማልማት አስረላጊ ነው የአርቲፊሻል ኢንተለጀንስ ቴክኖሎጂ ዘርፍ በጥናት ምርምና ልማት እንዲመራ ማስቻል አስፈላጊ የዲጂታል መሰረተ ልማቶች ማሙሏት መሰረታዊ ለውጥ ለማምጣት እና የአርቲፊሻል ኢንተለጀንስ ውጤቶችን በተግባር በስፋት ጥቅም ላይ እንዲዉሉ ይረዳል")
  ```

  - Here is a simple example of performing text cleaning on a piece of plaintext using `clean_amharic` function:

  ```python
  from etltk.lang.am import clean_amharic

  # Annotating a Document
  clean = clean_amharic("NLP የናቹራል ላንጉዌጅ ፕሮሰሲንግ ቱሎች My email is john.doe@email.com. ማዘጋጀት amharic 125 <html><h1>አስፈላጊ</h1></html> 456 ነው الرسائل  漢字; simplified Chinese: 汉字; 🤗⭕🤓🤔")

  # The following example shows how to print all sentences in a document:
  print(clean)
  # output: 'የናቹራል ላንጉዌጅ ፕሮሰሲንግ ቱሎች ማዘጋጀት አስፈላጊ ነው'

2. Tokenization - Sentence
    - Here is a simple example of performing sentence tokenization on a piece of plaintext using AmharicDocument:
    
    ```python
    from etltk import AmharicDocument

    # Annotating a Document
    doc = AmharicDocument(sample_text)

    # The following example shows how to print all sentences in a document:
    print(doc.sentences)
    # output: [Sentence("ሚያዝያ ዓመተ ምህረት በአገር ደረጃ የሰው ሰራሽ አስተውሎት አሁን ካለበት ዝቅተኛ ደረጃ ወደ ላቀ ደረጃ ለማድረስ ሀገርኛ ቋንቋዎችን ለአለም ተደራሽ ለማድረግ አገራዊ አቅምን ለማሳደግ እና ተጠቃሚ ለመሆን በጋራ አብሮ መስራቱ እጅግ ጠቃሚ ነው"),
    # Sentence("በማሽን አስተምሮ አማካኝነት የፅሁፍ ናሙናዎች በአርቲፊሻል ኢንተለጀንስ ስርአት ለማሰልጠን የፅሁፍ ዳታን መሰብሰብ እና ማደራጀት"),
    # Sentence("የናቹራል ላንጉዌጅ ፕሮሰሲንግ ቱሎችን በመጠቀም የፅሁፍ ዳታን ፕሮሰስ ማድረግ ተቀዳሚ እና መሰረታዊ ጉዳይ ነው"),
    # Sentence("የማሽን ለርኒንግ ስልተቀመሮች በመጠቀም ቋንቋዎችን መለየትና መረዳት የፅሁፍ ይዘቶችን መለየት የቋንቋን መዋቅር መተንተን የሚያስችሉ የናቹራል ላንጉዌጅ ፕሮሰሲንግ ቱሎች ስልተቀመሮች እና ሞዴሎችን ማዘጋጀት አስፈላጊ ነው"),
    # Sentence("የትርጉም አገልግሎት ቻትቦት የውይይት መለዋወጫ ሮቦት የፅሁፍ ሰነዶች ልየታ የቃላት ትክክለኛነትን ማረጋገጥ በቋንቋን መዋቅር ትንተና መሰረት ፅሁፎችን ለማዋቀር እና ለመመስረት ረጅም ፅሁፎችን ማሳጠር አንኳር ጉዳዮችን መለየት ወይም ጥቅል ሀሳብ ማውጣት ንግግርን ወደ ፅሁፍ የሚቀይሩ አገልግሎቶችን የሚሰጡ መተግበሪያ ማልማት አስረላጊ ነው"),
    # Sentence("የአርቲፊሻል ኢንተለጀንስ ቴክኖሎጂ ዘርፍ በጥናት ምርምና ልማት እንዲመራ ማስቻል አስፈላጊ የዲጂታል መሰረተ ልማቶች ማሙሏት መሰረታዊ ለውጥ ለማምጣት እና የአርቲፊሻል ኢንተለጀንስ ውጤቶችን በተግባር በስፋት ጥቅም ላይ እንዲዉሉ ይረዳል")]
    ```

    - Here is a simple example of performing sentence tokenization on a piece of plaintext using `sentence_tokenize` function:

    ```python
    from etltk.tokenize.am import sent_tokenize

    # Annotating a Document
    sentences = sent_tokenize("የሃገሪኛ ቋንቋዎችን መለየት እና ለመረዳት፣ የጽሁፍ ይዘቶችን መለየት፣ የቋንቋዎቹን ህግጋት መተንተን የሚያስችሉ የሃገሪኛ ተፈጥሯዊ ቋንቋ ፕሮሰሲንግ ቱሎች (NLP Tools)፣ ስልተ-ቀመሮች /Algorithms/ እና ሞዴሎችን /ML models/ በማዘጋጀት ተደራሽ ማድረግ ተገቢ ነው። በዚህም መሰረት አማርኛ፣ አፋን ኦሮሞ፣ ሶማሊኛ እና ትግርኛ ቋንቋዎችን ለማሽን የማስተማር ሂደትን ቀላልና የተቀላተፍ እንዲሆን ያስችላል፡፡")

    # The following example shows how to print all sentences in a document:
    print(sentences)
    # output: ['የሀገሪኛ ቋንቋዎችን መለየት እና ለመረዳት የፅሁፍ ይዘቶችን መለየት የቋንቋዎቹን ህግጋት መተንተን የሚያስችሉ የሀገሪኛ ተፈጥሯዊ ቋንቋ ፕሮሰሲንግ ቱሎች ስልተቀመሮች እና ሞዴሎችን በማዘጋጀት ተደራሽ ማድረግ ተገቢ ነው', 'በዚህም መሰረት አማርኛ አፋን ኦሮሞ ሶማሊኛ እና ትግርኛ ቋንቋዎችን ለማሽን የማስተማር ሂደትን ቀላልና የተቀላተፍ እንዲሆን ያስችላል']

3. Tokenization - Word
    - Here is a simple example of performing word tokenization on a piece of plaintext using AmharicDocument:
    
    ```python
    from etltk import AmharicDocument

    # Annotating a Document
    doc = AmharicDocument(sample_text)

    # The following example shows how to print all sentences in a document:
    print(doc.words)
    # output: WordList(['ሚያዝያ', 'ዓመተ', 'ምህረት', 'በአገር', 'ደረጃ', 'የሰው', 'ሰራሽ', 'አስተውሎት', 'አሁን', 'ካለበት', 'ዝቅተኛ', 'ደረጃ', 'ወደ', 'ላቀ', 'ደረጃ', 'ለማድረስ', 'ሀገርኛ', 'ቋንቋዎችን', 'ለአለም', 'ተደራሽ', 'ለማድረግ', 'አገራዊ', 'አቅምን', 'ለማሳደግ', 'እና', 'ተጠቃሚ', 'ለመሆን', 'በጋራ', 'አብሮ', 'መስራቱ', 'እጅግ', 'ጠቃሚ', 'ነው፡፡', 'በማሽን', 'አስተምሮ', 'አማካኝነት', 'የፅሁፍ', 'ናሙናዎች', 'በአርቲፊሻል', 'ኢንተለጀንስ', 'ስርአት', 'ለማሰልጠን', 'የፅሁፍ', 'ዳታን', 'መሰብሰብ', 'እና', 'ማደራጀት', 'የናቹራል', 'ላንጉዌጅ', 'ፕሮሰሲንግ', 'ቱሎችን', 'በመጠቀም', 'የፅሁፍ', 'ዳታን', 'ፕሮሰስ', 'ማድረግ', 'ተቀዳሚ', 'እና', 'መሰረታዊ', 'ጉዳይ', 'ነው', 'የማሽን', 'ለርኒንግ', 'ስልተ', 'ቀመሮች', 'በመጠቀም', 'ቋንቋዎችን', 'መለየትና', 'መረዳት', 'የፅሁፍ', 'ይዘቶችን', 'መለየት', 'የቋንቋን', 'መዋቅር', 'መተንተን', 'የሚያስችሉ', 'የናቹራል', 'ላንጉዌጅ', 'ፕሮሰሲንግ', 'ቱሎች', 'ስልተ', 'ቀመሮች', 'እና', 'ሞዴሎችን', 'ማዘጋጀት', 'አስፈላጊ', 'ነው', 'የትርጉም', 'አገልግሎት', 'ቻትቦት', 'የውይይት', 'መለዋወጫ', 'ሮቦት', 'የፅሁፍ', 'ሰነዶች', 'ልየታ', 'የቃላት', 'ትክክለኛነትን', 'ማረጋገጥ', 'በቋንቋን', 'መዋቅር', 'ትንተና', 'መሰረት', 'ፅሁፎችን', 'ለማዋቀር', 'እና', 'ለመመስረት', 'ረጅም', 'ፅሁፎችን', 'ማሳጠር', 'አንኳር', 'ጉዳዮችን', 'መለየት', 'ወይም', 'ጥቅል', 'ሀሳብ', 'ማውጣት', 'ንግግርን', 'ወደ', 'ፅሁፍ', 'የሚቀይሩ', 'አገልግሎቶችን', 'የሚሰጡ', 'መተግበሪያ', 'ማልማት', 'አስረላጊ', 'ነው', 'የአርቲፊሻል', 'ኢንተለጀንስ', 'ቴክኖሎጂ', 'ዘርፍ', 'በጥናት', 'ምርምና', 'ልማት', 'እንዲመራ', 'ማስቻል', 'አስፈላጊ', 'የዲጂታል', 'መሰረተ', 'ልማቶች', 'ማሙሏት', 'መሰረታዊ', 'ለውጥ', 'ለማምጣት', 'እና', 'የአርቲፊሻል', 'ኢንተለጀንስ', 'ውጤቶችን', 'በተግባር', 'በስፋት', 'ጥቅም', 'ላይ', 'እንዲዉሉ', 'ይረዳል'])
    ```

    - Here is a simple example of performing sentence tokenization on a piece of plaintext using `word_tokenize` function:
    
    ```python
    from etltk.tokenize.am import word_tokenize
      
    # Annotating a Document
    words = word_tokenize("የሃገሪኛ ቋንቋዎችን መለየት እና ለመረዳት፣ የጽሁፍ ይዘቶችን መለየት፣ የቋንቋዎቹን ህግጋት መተንተን የሚያስችሉ የሃገሪኛ ተፈጥሯዊ ቋንቋ ፕሮሰሲንግ ቱሎች (NLP Tools)፣ ስልተ-ቀመሮች /Algorithms/ እና ሞዴሎችን /ML models/ በማዘጋጀት ተደራሽ ማድረግ ተገቢ ነው። በዚህም መሰረት አማርኛ፣ አፋን ኦሮሞ፣ ሶማሊኛ እና ትግርኛ ቋንቋዎችን ለማሽን የማስተማር ሂደትን ቀላልና የተቀላተፍ እንዲሆን ያስችላል፡፡")

    # The following example shows how to print all sentences in a document:
    print(words)
    # output: ['የሀገሪኛ', 'ቋንቋዎችን', 'መለየት', 'እና', 'ለመረዳት', 'የፅሁፍ', 'ይዘቶችን', 'መለየት', 'የቋንቋዎቹን', 'ህግጋት', 'መተንተን', 'የሚያስችሉ', 'የሀገሪኛ', 'ተፈጥሯዊ', 'ቋንቋ', 'ፕሮሰሲንግ', 'ቱሎች', 'ስልተ', 'ቀመሮች', 'እና', 'ሞዴሎችን', 'በማዘጋጀት', 'ተደራሽ', 'ማድረግ', 'ተገቢ', 'ነው', 'በዚህም', 'መሰረት', 'አማርኛ', 'አፋን', 'ኦሮሞ', 'ሶማሊኛ', 'እና', 'ትግርኛ', 'ቋንቋዎችን', 'ለማሽን', 'የማስተማር', 'ሂደትን', 'ቀላልና', 'የተቀላተፍ', 'እንዲሆን', 'ያስችላል']

4. Normalization
    1. Character Level Normalization such as "`ጸ`ሀይ" and "`ፀ`ሐይ"
    2. Labialized Character Normalzation such as "ሞል`ቱዋ`ል" to "ሞል`ቷ`ል"
    3. Short Form Expansion such as "`አ.አ`" to "`አዲስ አበባ`"
    4. Punctuation Normalization such as `::` to `።`

    - Here is a simple example of performing normalization on a piece of plaintext using AmharicDocument:

    ```python
    from etltk.lang.am import normalize

    # normalizing a Document
    normalized = normalize("DHL የዕለቱ My email is john.doe@email.com. እናቀርባለን። amharic 125 <html><h1>Title</h1^X^X></html> 456 processor 18 الرسائل  漢字; simplified Chinese: 汉字; 🤗⭕🤓🤔")

    # The following example shows how to print all normalized in a document:
    print(normalized)
    # output: የዕለቱ     እናቀርባለን
    ```

    - Here is a simple example of performing normalization on a piece of plaintext using `normalize_char`, `normalize_punct`, `normalize_labialized`, `normalize_shortened` function:
    
    ```python
    from etltk.lang.am.normalizer import (
      normalize_char, 
      normalize_labialized, 
      normalize_punct, 
      normalize_shortened)

    # normalization
    char_norm = normalize_char(")

    # The following example shows how to print all sentences in a document:
    print(char_norm)
    # output: