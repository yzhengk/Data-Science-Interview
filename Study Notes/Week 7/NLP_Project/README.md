# NLP on Legal Case Notes

-------------------------

## Objective

The main goal of this project is to use natrual language processing methodologies such as topic modeling to analyze the legal text data. The dataset contains Australian legal cases from the Federal Court of Australia (FCA). The main documents analyzed include the full text and the catchphrases of all the cases from the FCA.</br>

## Dataset
The dataset includes 3891 xml files. Each file has the following tags: </br>
`<name>`: name of the case. </br>
`<AustLII>`: link to the austlii page from where the document was taken. </br>
`<catchphrases>`: contains a list of `<catchphrase>`elements. </br>
`<catchphrase>`: a catchphrase for the case, with an id attribute.  </br>
`<sentences>`: contains a list of `<sentence>` elements. </br>
`<sentence>`: a sentence with id attribute. </br>

## Methodologies

I mainly used BeautifulSoup package for transforming the xml data to pandas dataframe. The method for processing the text data I used is NLTK package. The model I created include LDA (Latent Dirichlet Allocation). Stopwords, punctuations, non-english words, low-frequency and high-frequency words were also removed during the process of text-processing. Doc2bow was used for converting document into the bag-of-words format. In the end pyLDAvis topic dashboards was created for seeing the topic with relative words frequence. </br>

The files are listed as follows: </br>

+ **Text Preprocess.ipynb**: this file is for loading the data to the Python pandas dataframe. The `sentences` and `name` tags were extracted from all the xml files.

+ **NLP Process.ipynb**: this file is for processing all the text data from sentences. Stop words, puntuations, non-English words, words embedding, words vectorizations and LDA model were implemented in this file. The final topic visualization dashboard also was created for illustrating purpose.

## References
<https://ac.els-cdn.com/S0013935115300128/1-s2.0-S0013935115300128-main.pdf?_tid=2d9a467a-da2c-4cf8-b773-e677072fcb6a&acdnat=1534216671_66f6c798baa8cb67c75f10f9f4f18ee0> </br>
<https://nlpforhackers.io/topic-modeling/> </br>








