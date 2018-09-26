## Text Analytics API demo

#### An example of how Ipython widgets can be used to showcase a few simple use cases of Microsoft cognitive services, NLTK library or anything else without writing cumbersome UI code....


A demo of how to implement this solution

Link: https://medium.com/kishan19/using-your-jupyter-notebook-for-a-quick-demo-of-named-entity-recognition-c974853577bf 

To get started, run the below with Python and Pip installed. This downloads all the necessary libraries for this demo.


pip install -r requirements.txt


The first snippet calls the Text Analytics API from Microsoft Cognitive Services. Creating one is very easy and can be found on https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/

The second snippet is on the default NER tagger from NLTK, and how to use the interactive Ipython widget to showcase these capabilities for a simple demo.


References:

1. https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python

2. https://stackoverflow.com/questions/31836058/nltk-named-entity-recognition-to-a-python-list

3. https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#Text